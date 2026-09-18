#!/usr/bin/env python3
"""[INPUT]: 已安装PptxGenJS及原创3页示例。
[OUTPUT]: 实际导出、原生对象、数据、边界与页切换失败回归。
[POS]: 单一可运行后端检查；视觉验收由render.py和逐页观察承担。
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
"""
import hashlib
import subprocess
import tempfile
from pathlib import Path
from xml.etree import ElementTree as ET
import pptx
ROOT=Path(__file__).resolve().parents[1]


def require_error(call):
    try:
        call()
    except ValueError:
        return
    raise AssertionError('Expected an explicit rejection')


def main():
    with tempfile.TemporaryDirectory(prefix='ppt-maker-test-') as tmp:
        output=Path(tmp)/'output'
        subprocess.run(['node',str(ROOT/'examples/build.cjs'),str(output)],check=True)
        raw=output/'raw.pptx'; original=hashlib.sha256(raw.read_bytes()).hexdigest()
        target=output/'deck.pptx';pptx.finalize(raw,target,'fade')
        files=pptx.load(target); report=pptx.inspect(files,3,'fade')
        assert not report['errors'],report
        assert [p['tables'] for p in report['slides']]==[0,1,0]
        assert [p['charts'] for p in report['slides']]==[0,0,1]
        assert [p['pictures'] for p in report['slides']]==[0,0,1]
        assert report['embedded_workbooks']==1
        table=ET.fromstring(files['ppt/slides/slide2.xml']).find('.//a:tbl',pptx.NS)
        rows=[[n.text for n in r.findall('.//a:t',pptx.NS)] for r in table.findall('a:tr',pptx.NS)]
        assert rows[3]==['Net revenue','230','200','15.0%'],rows
        assert len(rows)==14 and rows[11]==['Net profit','27','24','12.5%']
        chart=ET.fromstring(files['ppt/charts/chart1.xml'])
        assert [n.text for n in chart.findall('.//c:numCache/c:pt/c:v',pptx.NS)]==['-4','7']
        assert hashlib.sha256(raw.read_bytes()).hexdigest()==original
        require_error(lambda:pptx.finalize(raw,target,'fade'))
        assert pptx.inspect(files,4,'fade')['errors']
        none=output/'none.pptx';pptx.finalize(raw,none,'none')
        assert not pptx.inspect(pptx.load(none),3,'none')['errors']
        bad=dict(files);root=ET.fromstring(bad['ppt/slides/slide1.xml'])
        transition=root.find('p:transition',pptx.NS);root.remove(transition)
        root.find('p:cSld',pptx.NS).append(transition)
        bad['ppt/slides/slide1.xml']=ET.tostring(root)
        assert any('nested' in e for e in pptx.inspect(bad,3,'fade')['errors'])
        broken=dict(files);del broken['ppt/charts/chart1.xml']
        assert any('missing target' in e for e in pptx.inspect(broken,3,'fade')['errors'])
        print('PASS: 3 slides, native table/chart/workbook/image, source values, fade/none order, missing relationship and overwrite rejection')


if __name__=='__main__':main()
