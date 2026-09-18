#!/usr/bin/env python3
"""[INPUT]: 本地PPTX；Python标准库。
[OUTPUT]: 包/原生对象/边界检查；可选生成带规范页切换的新PPTX。
[POS]: 独立于生成后端的最终检查；不证明视觉或Office播放等价。
[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
"""
import argparse
import hashlib
import json
import posixpath
import re
import zipfile
from pathlib import Path
from xml.dom import minidom
from xml.etree import ElementTree as ET

NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'c': 'http://schemas.openxmlformats.org/drawingml/2006/chart'}
P = '{' + NS['p'] + '}'
SLIDE = re.compile(r'ppt/slides/slide(\d+)\.xml$')


def load(path):
    with zipfile.ZipFile(path) as z:
        if sum(i.file_size for i in z.infolist()) > 256 * 1024 * 1024:
            raise ValueError('Package exceeds 256 MiB uncompressed inspection limit')
        if len(z.namelist()) != len(set(z.namelist())):
            raise ValueError('Duplicate ZIP entries')
        if z.testzip():
            raise ValueError('ZIP integrity failure')
        return {n: z.read(n) for n in z.namelist()}


def relationship_errors(files):
    errors = []
    for name, raw in files.items():
        if not name.endswith('.rels'):
            continue
        base = '' if name == '_rels/.rels' else name.rsplit('/_rels/', 1)[0]
        for rel in ET.fromstring(raw):
            if rel.get('TargetMode') == 'External':
                continue
            target = rel.get('Target', '').split('#')[0]
            resolved = posixpath.normpath(posixpath.join(base, target)).lstrip('/')
            if resolved not in files:
                errors.append(f'{name}: missing target {target}')
    return errors


def transition_errors(root, mode):
    nodes = root.findall('p:transition', NS)
    if len(root.findall('.//p:transition', NS)) != len(nodes):
        return ['transition nested inside slide content']
    if mode == 'none':
        return ['unexpected transition'] if nodes else []
    if mode != 'fade':
        return []
    if len(nodes) != 1 or len(nodes[0]) != 1 or nodes[0][0].tag != P+'fade':
        return ['expected exactly one root-level fade transition']
    tags = [n.tag for n in root]
    index = tags.index(P+'transition')
    valid = [P+'cSld', P+'clrMapOvr']
    if not tags or tags[0] != P+'cSld' or any(t not in valid for t in tags[:index]):
        return ['invalid transition order']
    if any(t not in [P+'timing', P+'extLst'] for t in tags[index+1:]):
        return ['invalid trailing slide element order']
    return []


def outside_objects(root, width, height):
    outside = []
    tree = root.find('p:cSld/p:spTree', NS)
    for obj in tree if tree is not None else []:
        xfrm = obj.find('p:spPr/a:xfrm', NS)
        if xfrm is None:
            xfrm = obj.find('p:xfrm', NS)
        if xfrm is None or xfrm.get('rot'):
            continue  # Rotated/group bounds require actual rendering.
        off, ext = xfrm.find('a:off', NS), xfrm.find('a:ext', NS)
        if off is None or ext is None:
            continue
        x, y, w, h = [int(v) for v in (off.get('x'), off.get('y'), ext.get('cx'), ext.get('cy'))]
        if min(x,y,w,h) < 0 or x+w > width+127 or y+h > height+127:
            outside.append({'tag': obj.tag.split('}')[-1], 'emu': [x,y,w,h]})
    return outside


def inspect(files, expected=None, mode='any'):
    errors = relationship_errors(files)
    for name, raw in files.items():
        if name.endswith(('.xml', '.rels')):
            ET.fromstring(raw)
    presentation = ET.fromstring(files['ppt/presentation.xml'])
    size = presentation.find('p:sldSz', NS)
    width, height = int(size.get('cx')), int(size.get('cy'))
    names = sorted((n for n in files if SLIDE.fullmatch(n)), key=lambda n:int(SLIDE.fullmatch(n)[1]))
    if not names or len(presentation.findall('p:sldIdLst/p:sldId', NS)) != len(names):
        errors.append('Slide manifest/count mismatch')
    if expected is not None and len(names) != expected:
        errors.append(f'Expected {expected} slides; got {len(names)}')
    pages = []
    for name in names:
        root = ET.fromstring(files[name])
        errors += [name+': '+e for e in transition_errors(root, mode)]
        outside = outside_objects(root, width, height)
        if outside:
            errors.append(name+': top-level objects outside slide')
        pages.append({'part':name, 'text_runs':len(root.findall('.//a:t', NS)),
                      'shapes':len(root.findall('.//p:sp', NS)), 'tables':len(root.findall('.//a:tbl', NS)),
                      'charts':len(root.findall('.//c:chart', NS)), 'pictures':len(root.findall('.//p:pic', NS)),
                      'outside':outside})
    return {'slides':pages, 'embedded_workbooks':len([n for n in files if n.endswith('.xlsx')]),
            'errors':errors, 'scope':'ZIP/XML/relationships/top-level bounds; visual review still required'}


def patch_transition(raw, mode):
    # DOM保留命名空间前缀及mc属性；不通过正则拼接OOXML。
    doc = minidom.parseString(raw)
    root = doc.documentElement
    for node in list(root.childNodes):
        if node.nodeType == node.ELEMENT_NODE and node.namespaceURI == NS['p'] and node.localName == 'transition':
            root.removeChild(node)
    if mode == 'fade':
        prefix = root.prefix + ':' if root.prefix else ''
        transition = doc.createElementNS(NS['p'], prefix+'transition')
        transition.appendChild(doc.createElementNS(NS['p'], prefix+'fade'))
        before = next((n for n in root.childNodes if n.nodeType == n.ELEMENT_NODE and n.localName in ('timing','extLst')), None)
        root.insertBefore(transition, before)
    return doc.toxml(encoding='UTF-8')


def finalize(source, target, mode):
    if source.resolve() == target.resolve() or target.exists():
        raise ValueError('Output must be a new path; original is preserved')
    files = load(source)
    report = inspect(files)
    if report['errors']:
        raise ValueError(report['errors'])
    for name in files:
        if SLIDE.fullmatch(name):
            files[name] = patch_transition(files[name], mode)
    report = inspect(files, mode=mode)
    if report['errors']:
        raise ValueError(report['errors'])
    # 排他创建，失败只清理本次创建的输出。
    handle = target.open('xb')
    try:
        with handle, zipfile.ZipFile(handle, 'w', zipfile.ZIP_DEFLATED) as z:
            for name, raw in files.items():
                z.writestr(name, raw)
    except Exception:
        target.unlink(missing_ok=True)
        raise
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    f = sub.add_parser('finalize');f.add_argument('source',type=Path);f.add_argument('target',type=Path)
    f.add_argument('--transition',choices=['fade','none'],default='fade')
    c = sub.add_parser('check');c.add_argument('source',type=Path)
    c.add_argument('--expect-slides',type=int);c.add_argument('--transition',choices=['any','fade','none'],default='any')
    args = parser.parse_args()
    if args.command == 'finalize':
        report = finalize(args.source,args.target,args.transition); path=args.target
    else:
        report = inspect(load(args.source),args.expect_slides,args.transition);path=args.source
    report['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    print(json.dumps(report,indent=2))
    if report['errors']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
