#!/usr/bin/env python3
# [INPUT]: 本Skill目录，或明确提供的新HTML路径；Python标准库。
# [OUTPUT]: 缺文件/断链接/活动内容/远程依赖等检查失败时非零退出。
# [POS]: 发布包和静态HTML的最小可运行检查；不替代浏览器和语义验收。
# [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class StaticSlides(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides, self.ids, self.english = 0, set(), False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        assert tag not in {'script', 'iframe', 'object', 'embed', 'foreignobject', 'base'}, tag
        assert not any(k.startswith('on') for k in attrs), 'event handler'
        assert not (tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh'), 'refresh'
        for key in ('src', 'href', 'xlink:href', 'action', 'srcset'):
            value = attrs.get(key, '') or ''
            assert not re.search(r'(?i)(https?:|javascript:|file:|^//)', value), (key, value)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, ('duplicate ID', attrs['id'])
            self.ids.add(attrs['id'])
        self.english |= tag == 'html' and attrs.get('lang', '').startswith('en')
        self.slides += tag == 'article' and 'slide' in attrs.get('class', '').split()


def check_html(path):
    text = path.read_text(encoding='utf-8')
    assert not re.search(r'(?i)@import|url\(\s*[\"\x27]?(?:https?:|//|file:)', text), 'remote CSS'
    parser = StaticSlides()
    parser.feed(text)
    assert parser.english and parser.slides, (path, 'English document / article.slide missing')
    return parser.slides


def check_links(root):
    for path in root.rglob('*.md'):
        for raw in re.findall(r'\]\(([^)\n]+)\)', path.read_text()):
            target = raw.strip('<>').split('#')[0]
            if not target or urlsplit(target).scheme:
                continue
            assert (path.parent / unquote(target)).exists(), (path, target)


def self_test():
    valid = '<html lang="en"><article class="slide" id="a"></article></html>'
    parser = StaticSlides()
    parser.feed(valid)
    assert parser.slides == 1 and parser.english
    for bad in ['<script></script>', '<img src="https://example.org/x">',
                '<svg onload="alert(1)">', '<i id="x"></i><i id="x">']:
        try:
            StaticSlides().feed(bad)
        except AssertionError:
            continue
        raise AssertionError('Unsafe example was accepted')


def main():
    self_test()
    if len(sys.argv) > 1:
        targets = [Path(p) for p in sys.argv[1:]]
    else:
        assert (ROOT / 'SKILL.md').read_text().startswith('---\nname: ib-analysis-slides\n')
        for name in ['references/evidence.md', 'references/execution.md', 'banks/goldman/PROFILE.md']:
            assert (ROOT / name).is_file(), name
        check_links(ROOT)
        targets = sorted((ROOT / 'banks/goldman/examples').rglob('*.html'))
        assert len(targets) == 4, 'Expected four public example documents'
    counts = [check_html(path) for path in targets]
    print(f'PASS: {len(targets)} HTML documents, {sum(counts)} slides; static checks and self-test')


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, OSError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
