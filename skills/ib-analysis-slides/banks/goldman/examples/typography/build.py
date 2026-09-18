#!/usr/bin/env python3
# [INPUT]: 本文件中的原创虚构数据；Python标准库。
# [OUTPUT]: 四页离线、可编辑HTML；同目录index.html。
# [POS]: typography整页案例的确定性构建器；不读取机构报告。
# [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
from pathlib import Path
from html import escape
D='#00355F'; L='#6E93BE'; T='#23C7BA'; G='#7F7F7F'

def txt(x,y,s,size=10,color=D,weight='normal',style='',anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" {style}>{escape(s)}</text>'

def lines(x,y,ss,**kw):
    return ''.join(txt(x,y+i*12,s,**kw) for i,s in enumerate(ss))

def bracket(x,y,w,label,gap):
    a=x+w/2-gap/2;b=x+w/2+gap/2
    return f'<path d="M{x},{y+17}V{y}H{a}M{b},{y}H{x+w}V{y+17}" fill="none" stroke="{T}" stroke-width=".5"/>'+txt(x+w/2,y+3,label,10,style='letter-spacing="2"',anchor='middle')

def status(x,y,done):
    c=T if done else '#F6CF88'
    p=f'<circle cx="{x}" cy="{y}" r="9.5" fill="white" stroke="{c}" stroke-width="1"/>'
    return p+(f'<path d="M{x-4},{y}l3,3 5,-8" fill="none" stroke="{c}"/>' if done else txt(x,y+4,'~',14,c,'bold',anchor='middle'))

def page(n,title,content):
    titles=title if isinstance(title,list) else [title]
    return f'<article class="slide" id="T{n}"><svg viewBox="0 0 720 405" role="img" aria-label="{escape(" ".join(titles))}">'+''.join(txt(33,38+i*20,t,19,weight='bold') for i,t in enumerate(titles))+content+txt(33,393,'Illustrative only • fictional Meridian Instruments • see sources.md',6,G)+txt(700,393,str(n),6,G,anchor='end')+'</svg></article>'

# -- 客户角色：状态与对象颜色共同编码，圆环不编码份额 --
a=bracket(33,93,237,'LABORATORIES',124)+bracket(459,93,237,'MANUFACTURERS',143)
left=[['Installed workflows across 120 labs'],['Application library: 24 validated methods'],['Remote diagnosis available to all sites'],['Expand certified partner coverage'],['Pilot shared sample-preparation service']]
right=[['Qualified supply for 18 production sites'],['Process recipes supported in three regions'],['Field teams linked to design engineers'],['Extend predictive maintenance trials'],['Build a second calibration hub']]
for i,(ls,rs) in enumerate(zip(left,right)):
    y=142+i*43
    a+=status(43,y-3,i<3)+lines(62,y,ls,size=9.96)
    a+=status(469,y-3,i<3)+lines(487,y,rs,size=9.96,color=L)
a+='<path d="M359,155 A79,79 0 0 0 359,313" fill="none" stroke="'+D+'" stroke-width="44"/>'
a+='<path d="M359,155 A79,79 0 0 1 359,313" fill="none" stroke="'+L+'" stroke-width="44"/>'
a+='<path d="M350,126l14,29-14,31M369,282l-14,31 14,28" fill="none" stroke="white" stroke-width="15"/>'
a+=lines(359,227,['Shared','measurement','platform'],size=11,color=G,weight='bold',anchor='middle')
a+=txt(360,371,'✓ Established capability     ~ Planned action; timing not committed',7,G,anchor='middle')
pages=[page(1,['One Measurement Platform Serves Two Distinct','Customer Workflows'],a)]
# -- 能力与证据：直接小标题+灰斜体限定，不强加括线 --
b=''
blocks=[(115,'Installed workflows support repeat use',['Validated methods reduce the need to reconfigure routine tests.'],['120 laboratory sites; 24 methods in the internal library.']),(209,'Service expands faster than equipment sales',['Remote diagnostics add a recurring touchpoint after installation.'],['Service revenue rose 40%; equipment revenue rose 6.7%.']),(303,'Deployment capacity remains the constraint',['A second hub is planned; capacity and opening date are undisclosed.'],['Target is operational coverage, not a quantified revenue forecast.'])]
for y,head,body,qual in blocks:
    b+=txt(33,y,head,12,weight='bold')+lines(33,y+20,body,size=10)+lines(33,y+39,qual,size=10.56,color=G,style='font-style="italic"')
b+=txt(482,108,'Revenue by business',11,weight='bold')+txt(482,122,'USD millions; fiscal years',8,G,style='font-style="italic"')
for x,year,eq,sv in [(494,2024,150,50),(579,2025,160,70)]:
    for val,bottom,c in [(eq,326,D),(sv,326-eq*.65,L)]:
        h=val*.65;b+=f'<rect x="{x}" y="{bottom-h}" width="49" height="{h}" fill="{c}"/>'+txt(x+24.5,bottom-h/2+3,str(val),10,'white',anchor='middle')
    b+=txt(x+24.5,326-(eq+sv)*.65-7,str(eq+sv),11,G,'bold',anchor='middle')+txt(x+24.5,342,str(year),9,anchor='middle')
b+='<path d="M482,326H647" stroke="#444" stroke-width=".6"/>'+txt(482,364,'Equipment',8,D)+txt(570,364,'Service',8,L)
pages.append(page(2,'Installed Workflows Support a Growing Service Business',b))
# -- 不等长类别列表：类别/金额/条目文字角色分离 --
c=bracket(33,93,230,'DELIVERY CAPABILITIES',184)+bracket(292,93,404,'PRODUCT AND SERVICE BREADTH',251)
for i,ss in enumerate([['24 validated methods spanning','material and environmental tests'],['Remote support available across','three operating regions'],['18 qualified production sites','with process-specific recipes'],['120 laboratory sites on the','shared measurement platform']]):
    y=151+i*57;c+=status(43,y-4,True)+lines(62,y,ss,size=10)
cols=[('Instruments','$100m',['Spectrometry','Optical inspection','Thermal analysis','Sensor arrays'],D),('Modules','$60m',['Sample handling','Power controls','Data acquisition'],L),('Service','$70m',['Calibration','Remote diagnostics','Field maintenance','Training','Workflow support'],'#20657C')]
for i,(label,val,items,col) in enumerate(cols):
    x=292+i*137;c+=f'<rect x="{x}" y="125" width="130" height="37" fill="{col}"/>'+txt(x+65,140,label,9,'white',anchor='middle')+txt(x+65,153,val,9,'white','bold',anchor='middle')
    for j,item in enumerate(items):
        y=167+j*26;c+=f'<rect x="{x}" y="{y}" width="130" height="23" fill="{col}" opacity=".53"/>'+txt(x+65,y+15,item,8.04,'white',anchor='middle')
c+=txt(292,326,'FY2025 revenue; instruments and modules form equipment.',8,G,style='font-style="italic"')+txt(292,342,'Lists describe breadth; rows do not imply equivalent offerings.',8,G,style='font-style="italic"')
pages.append(page(3,'Capabilities Translate into Different Product and Service Roles',c))
# -- 财务：单位、当前金额、解释层级与表格行角色 --
rows=[('Equipment revenue','160','150','6.7%',''),('Service revenue','70','50','40.0%',''),('Net revenue','230','200','15.0%','key'),('Cost of revenue','(140)','(120)','16.7%',''),('Gross profit','90','80','12.5%','subtotal'),('Operating expenses','(52)','(45)','15.6%',''),('Operating profit','38','35','8.6%','key'),('Net interest expense','(4)','(5)','(20.0)%',''),('Pre-tax profit','34','30','13.3%','subtotal'),('Income tax','(7)','(6)','16.7%',''),('Net profit','27','24','12.5%','key'),('Gross margin','39.1%','40.0%','(0.9)pp',''),('Operating margin','16.5%','17.5%','(1.0)pp','')]
assert 160+70==230 and 230-140-52==38 and 38-4-7==27
trs=''.join(f'<tr class="{cl}"><th scope="row">{label}</th><td class="current">{v}</td><td>{p}</td><td>{chg}</td></tr>' for label,v,p,chg,cl in rows)
f=f'''<article class="slide financial" id="T4"><h1>Financial Overview</h1><div class="financial-body"><section class="results"><h2>Financial Results</h2><table><caption>USD millions, except ratios; changes calculated from unrounded inputs</caption><thead><tr><th scope="col"></th><th scope="col">FY2025</th><th scope="col">FY2024</th><th scope="col">vs. FY2024</th></tr></thead><tbody>{trs}</tbody></table></section><section class="highlights"><h2>Financial Overview Highlights</h2><h3>FY2025 revenue and gross profit</h3><ul><li>Net revenue increased 15.0% to $230 million.<ul><li>Equipment contributed $10 million of the $30 million increase; service contributed $20 million.</li><li>Service mix rose to 30.4%, from 25.0% in FY2024.</li></ul></li><li>Gross profit rose 12.5% to $90 million.<ul><li>Cost of revenue increased faster than sales, reducing gross margin by 0.9 percentage points.</li><li>Costs are not disclosed by business; revenue contribution cannot establish segment profitability.</li></ul></li></ul><div class="divider"></div><h3>FY2025 profitability</h3><ul><li>Operating profit increased 8.6% to $38 million.<ul><li>Operating expenses increased by $7 million, absorbing most of the $10 million gross-profit increase.</li></ul></li><li>Net profit increased 12.5% to $27 million.<ul><li>Net interest expense fell by $1 million; tax expense increased by $1 million.</li><li>Operating margin declined by 1.0 percentage point to 16.5%.</li></ul></li></ul><p class="qualifier">Annual results only. Quarterly drivers and per-share data are not provided.</p></section></div><footer>Illustrative only • fictional Meridian Instruments • see sources.md<span>4</span></footer></article>'''
pages.append(f)
css='''*{box-sizing:border-box}body{margin:0;background:#ccc;font-family:Arial,sans-serif}.slide{width:960px;height:540px;background:white;margin:20px auto;position:relative}.slide>svg{display:block;width:960px;height:540px;font-family:Arial,sans-serif}.financial{color:#20396D}.financial h1{height:72px;margin:0;padding:29px 30px 0;color:#748CAB;font-size:19.44px}.financial-body{height:445px;background:#E4E5E7;display:grid;grid-template-columns:480px 480px;padding-top:9px}.financial section{padding:0 14px}.financial .highlights{border-left:1px solid #aaa;padding:0 21px 0 27px}.financial h2{font-size:14.16px;text-align:center;margin:0 0 14px}.financial table{width:100%;border-collapse:collapse;font-size:10px;table-layout:fixed}.financial caption{font-size:6.96px;font-style:italic;text-align:left;padding:0 0 5px}.financial th:first-child{width:43%}.financial th{font-weight:normal;text-align:right}.financial thead th{font-weight:bold;border-bottom:1px solid #748CAB;height:24px}.financial td{text-align:right;height:25px;padding:4px 6px;background:#E3EBF4}.financial tbody th{padding:4px 7px 4px 0}.financial tr:nth-child(odd) td{background:#C7D6E8}.financial .current{font-weight:bold}.financial .key>*{border-top:2px solid #20396D;border-bottom:2px solid #20396D;font-weight:bold}.financial .key>*:first-child{border-left:2px solid #20396D}.financial .key>*:last-child{border-right:2px solid #20396D}.financial .subtotal>*{border-top:1px solid #20396D;font-weight:bold}.financial h3{font-size:10px;margin:0 0 8px}.financial ul{font-size:9.72px;margin:0;padding-left:13px;list-style-type:square;line-height:1.25}.financial li{padding-left:0;margin-bottom:6px}.financial ul ul{list-style-type:'—  ';margin-top:6px}.financial ul ul li{margin-bottom:5px}.financial .divider{border-top:2px solid #20396D;margin:15px 0}.financial .qualifier{font-size:8px;font-style:italic;line-height:1.3;margin-top:9px}.financial footer{height:23px;background:#E4E5E7;padding:4px 20px;font-size:7px;color:#666}.financial footer span{float:right}@media print{body{background:white}.slide{margin:0;break-after:page}}'''
html='<!DOCTYPE html><!-- [INPUT]: build.py中的原创虚构证据与主题角色；[OUTPUT]: 四页离线可编辑HTML；[POS]: typography整页示例；[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md --><html lang="en"><head><meta charset="utf-8"><title>Meridian Instruments — roles in complete pages</title><style>'+css+'</style></head><body>'+''.join(pages)+'</body></html>'
Path(__file__).with_name('index.html').write_text(html)
