# [INPUT]: Explicit labels, evidence lines and source text; Python standard library.
# [OUTPUT]: SVG primitives and the V2-derived overview article used by examples and migration.
# [POS]: Shared overview typography and geometry; other theme roles remain in build.py.
# [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
from html import escape

def text(x,y,value,size=12,color='#111',family='Arial',weight='normal',anchor='start',extra=''):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" {extra}>{escape(str(value))}</text>'


def lines(x,y,values,size=12,step=17,**kw):
    return ''.join(text(x,y+i*step,s,size,**kw) for i,s in enumerate(values))


def rect(x,y,w,h,color,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" {extra}/>'


def line(x,y,x2,y2,color='#999',width=.7,extra=''):
    return f'<path d="M{x},{y}L{x2},{y2}" fill="none" stroke="{color}" stroke-width="{width}" {extra}/>'



def overview(id_,tag,title,rows,source,footer):
    """Content-led V2 overview; explicit line breaks are reviewed at final size."""
    assert 1 <= len(rows) <= 5 and 1 <= len(title) <= 2
    b=text(36,29,tag,11,weight='normal')+line(36,39,684,39,'#000',5.5)
    b+=lines(36,73,title,22,24,family='Georgia',weight='normal')
    # Balance the whole body after calculating text height; do not pack rows at the top.
    heights=[max(65,16+sum(len(item) for item in copy)*17+(len(copy)-1)*3) for _,_,copy in rows]
    spare=464-132-sum(heights)-12*(len(rows)-1)
    assert spare>=0, 'Overview exceeds source area; edit copy or split the page.'
    padding=min(24,spare/len(rows))
    y=132
    for (label,color,copy),minimum in zip(rows,heights):
        assert 1 <= len(label) <= 2 and copy
        height=minimum+padding
        assert y+height <= 479, 'Overview exceeds source area; edit copy or split the page.'
        b+=rect(36,y,132,height,color)
        b+=lines(102,y+height/2+5-(len(label)-1)*8,label,14,16,
                 color='#111' if color=='#c9ced6' else 'white',anchor='middle')
        b+=line(188,y,684,y,'#bbb',.6)
        baseline=y+19+padding/2
        for item in copy:
            b+=rect(193,baseline-5,3,3,'#a95228')+lines(205,baseline,item,13,17)
            baseline+=len(item)*17+3
        y+=height+12
    b+=line(36,491,684,491,'#111',.6)+text(36,507,source,7)
    b+=text(36,525,footer,8)+text(684,525,id_,8,anchor='end')
    return f'<article class="slide investor" id="{id_}"><svg viewBox="0 0 720 540" role="img" aria-label="{escape(tag)}">{b}</svg></article>'
