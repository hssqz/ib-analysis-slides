#!/usr/bin/env python3
"""[INPUT]: 已生成PPTX，LibreOffice和Poppler外部可执行文件。
[OUTPUT]: 新QA目录中的实际PDF/逐页PNG与输入哈希。
[POS]: 可选真实应用渲染；无镜像编辑器、无自动安装。
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
"""
import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path


def render(source, output, office, rasterizer):
    source = source.resolve()
    if not source.is_file() or source.suffix.lower() != '.pptx':
        raise ValueError('Input must be an existing PPTX')
    for exe in (office, rasterizer):
        if not shutil.which(exe):
            raise ValueError(f'Missing {exe}; install LibreOffice and Poppler or use another actual renderer')
    output.mkdir(parents=True, exist_ok=False)
    with tempfile.TemporaryDirectory(prefix='ppt-maker-office-') as profile:
        result = subprocess.run([office, '-env:UserInstallation='+Path(profile).as_uri(), '--headless',
                                 '--convert-to','pdf','--outdir',str(output),str(source)],
                                capture_output=True,text=True,timeout=120,check=True)
    pdf = output/(source.stem+'.pdf')
    if not pdf.is_file():
        raise RuntimeError('LibreOffice produced no PDF: '+result.stdout+result.stderr)
    subprocess.run([rasterizer,'-png','-r','96',str(pdf),str(output/'page')],check=True,timeout=120)
    images = sorted(output.glob('page-*.png'))
    if not images:
        raise RuntimeError('No rendered pages')
    report = {'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
              'renderer':subprocess.check_output([office,'--version'],text=True).strip(),
              'pages':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in images},
              'visual_review':'pending; open every PNG, this script does not approve appearance'}
    (output/'render.json').write_text(json.dumps(report,indent=2)+'\n')
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('source',type=Path);p.add_argument('output',type=Path)
    p.add_argument('--office',default='soffice');p.add_argument('--rasterizer',default='pdftoppm');a=p.parse_args()
    print(json.dumps(render(a.source,a.output.resolve(),a.office,a.rasterizer),indent=2))


if __name__=='__main__':main()
