#!/usr/bin/env python3
# [INPUT]: 本文件原创虚构数据；Python标准库，无私人报告依赖。
# [OUTPUT]: 五主题七页HTML、计算检查；同目录index.html。
# [POS]: Blackstone风格阶段二整页实例；按证据关系绘制，不是PDF转图器。
# [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
from pathlib import Path
from html import escape
from math import pi, sin, cos

GREEN, DARK, SAND, RUST, GREY = '#4b9f8a','#1b5e5c','#c39d78','#a95228','#c9ced6'
CYAN, TEAL, LIME, MAGENTA = '#0097c3','#006778','#c8dd03','#b8005c'


from drawing import text, lines, rect, line, overview


def shell(id_,theme,tag,title,body):
    strategy=theme=='strategy';day=theme=='day'; height=540; family='Trebuchet MS' if day else 'Arial'
    base=text(36,29,tag,11,family=family,weight='bold')+line(36,39,684,39,'#000',5.5)
    base+=lines(36,73,title,22,24,family='Georgia',weight='bold')
    if strategy:
        base=text(23,19,'Illustrative Investment Strategy',8,'#777','Georgia')+text(696,19,'Fictional scenario • not a forecast',8,'#777','Georgia',anchor='end')
        base+=text(23,49,tag,18,weight='bold')+line(23,56,697,56,'#000',1.5)
        base+=lines(23,79,title,18,22,family='Georgia')+line(23,95,697,95,'#000',5.5)
    base+=body+line(36,491,684,491,'#111',.6)
    base+=text(36,510,'Source: original fictional inputs in build.py; see sources.md. Illustrative only.',7)
    base+=text(684,525,id_,8,anchor='end')
    return f'<article class="slide {theme}" id="{id_}"><svg viewBox="0 0 720 {height}" role="img" aria-label="{escape(tag)}">{base}</svg></article>'


# -- B1：V2专属13pt正文/14pt短标签；行高由真实文字行数确定 --
rows=[(['Platform'],GREEN,[['$8.0bn committed across three credit strategies.'],['Origination teams operate in four regions.'],['Committed capital is distinct from portfolio NAV.']]),(['Experience'],DARK,[['Core team has invested together since 2012.'],['The committee reviews every new commitment.'],['Operating partners support borrowers after closing.']]),(['Portfolio'],SAND,[['$2.4bn portfolio across 120 borrowers at year-end.'],['92% first lien; recovery rates are not inferred.'],['Largest borrower: 2.0% of portfolio fair value.']]),(['Alignment'],GREY,[['Three-year incentive lookback.'],['Fee basis and waivers remain contract-specific.'],['No fee savings assumed without comparisons.']])]
pages=[overview('B1','NORTHFIELD CREDIT — INVESTMENT OVERVIEW',
    ['A diversified lending platform pairs scale','with disciplined portfolio construction'],rows,
    'Source: original fictional inputs in build.py; see sources.md. Illustrative only.',
    'Northfield Credit — illustrative analysis')]

# -- B2：季度、LTM与时点不同表头；金额、每股值与百分比独立 --
financial=[('Operating results','','','','','section green'),('Net investment income','42','45','158','174',''),('Net income','39','41','144','153',''),('Net investment income per share','0.70','0.75','2.63','2.90',''),('Net income per share','0.65','0.68','2.40','2.55',''),('Regular dividends per share','0.62','0.64','2.40','2.50',''),('Portfolio activity','','','','','section blue'),('New commitments','220','250','810','930',''),('Investment fundings','190','205','740','820',''),('Investments sold and repaid','(150)','(180)','(590)','(680)',''),('','','','31 Mar 2024','31 Mar 2025','period'),('Balance sheet','','','','','section sand'),('Investments at fair value','','','2,100','2,400',''),('Debt principal','','','1,040','1,200',''),('Net asset value','','','1,100','1,200',''),('NAV per share','','','18.33','20.00',''),('Debt-to-equity','','','0.95x','1.00x',''),('First-lien exposure','','','90%','92%',''),('Number of borrowers','','','108','120','')]
assert 45/60==.75 and 174/60==2.9 and 1200/60==20
trs=''
for row_index,(label,a,c,d,e,role) in enumerate(financial):
    trs+=f'<tr class="{role}"><th scope="row">{escape(label)}</th>'+''.join(f'<td class="{"current" if i==3 or (i==1 and row_index<10) else ""}">{escape(v)}</td>' for i,v in enumerate([a,c,d,e]))+'</tr>'
pages.append(f'''<article class="slide earnings" id="B2"><h1>FIRST QUARTER 2025 SELECTED FINANCIAL HIGHLIGHTS</h1><p class="units">$ in millions, except per-share amounts, ratios and borrower counts</p><table><colgroup><col style="width:44%"><col><col><col><col></colgroup><thead><tr><th scope="col"></th><th scope="col">1Q’24</th><th scope="col">1Q’25</th><th scope="col">1Q’24 LTM</th><th scope="col">1Q’25 LTM</th></tr></thead><tbody>{trs}</tbody></table><div class="notes">Quarterly and LTM income measures are flows; balance-sheet measures are dated stocks.<br>60 million shares assumed throughout. Ratios are calculated from unrounded fictional inputs.<br>Source: original fictional Northfield Credit data in build.py. Illustrative only.</div><footer>Northfield Credit — illustrative analysis<span>B2</span></footer></article>''')

# -- B3：并列机制汇合；条件性判断与关键词角色同时保留 --
b=text(36,135,'Potential effects of a lower base rate:',14,family='Georgia')
mechanisms=[(['Asset yields','decline'],['Floating-rate assets reprice','as base rates move lower.','Liability costs may also fall.']),(['Deployment','may rise'],['Lower borrowing costs can','support new transactions.','Demand is not guaranteed.']),(['Coverage may','improve'],['Lower interest expense can','support borrower cash flow.','Operating risks remain.'])]
for i,(claim,copy) in enumerate(mechanisms):
    x=36+i*228;color=[GREEN,DARK,SAND][i]
    b+=rect(x,164,192,139,'white',f'stroke="{color}" stroke-width="1.2"')
    b+=f'<circle cx="{x+12}" cy="164" r="12" fill="{color}"/>'+text(x+12,169,i+1,15,'white',family='Georgia',anchor='middle')
    b+=lines(x+96,195,claim,16,20,color=RUST,family='Georgia',weight='bold',anchor='middle')+lines(x+99,241,copy,13,21,anchor='middle')
    b+=f'<path d="M{x+99} 307V335H360V354" fill="none" stroke="{GREEN}" stroke-width="1.4"/>'
b+=f'<path d="M353 349L360 361L367 349Z" fill="{GREEN}"/>'+text(360,381,'Conditional outcome',14,family='Georgia',anchor='middle')
b+=rect(36,394,648,65,'white',f'stroke="#006492" stroke-width="1.5"')
b+='<text x="360" y="421" font-family="Arial" font-size="14" text-anchor="middle"><tspan font-family="Georgia" font-weight="bold" fill="#a95228">Deployment and borrower coverage</tspan> may offset <tspan font-family="Georgia" font-weight="bold" fill="#a95228">lower asset yields.</tspan></text>'+text(360,445,'The net effect depends on repricing, leverage and credit performance.',12,anchor='middle')
pages.append(shell('B3','credit','CREDIT IN A LOWER-RATE ENVIRONMENT',['Lower rates affect income, deployment','and borrower coverage through different channels'],b))

# -- B4：分组标题断口与生命周期层级，普通标题不滥用括线 --
b=text(132,157,'Investment Office',18,family='Georgia',weight='bold')+text(132,181,'A shared review process connects three distinct stages.',13,family='Trebuchet MS')
label='Committee review supports decisions across the investment lifecycle'
# ponytail: 此静态案例按已验收标签保留固定净空；改标签后用实际浏览器文字框重算断口。
b+=line(36,211,684,211,DARK,2.25)+rect(106,198,508,26,'white')+text(360,218,label,12.3,family='Georgia',weight='bold',anchor='middle')
stages=[('Underwriting',['Sector research','Borrower diligence','Downside scenarios','Credit approval']),('Execution',['Capital formation','Documentation','Security perfection','Closing review']),('Portfolio Management',['Covenant monitoring','Operating support','Watchlist review','Exit planning'])]
for i,(name,items) in enumerate(stages):
    x=36+i*216;b+=text(x,248,name,15.5,family='Georgia',weight='bold')+line(x,263,x+207,263,[GREEN,DARK,SAND][i],1.5)
    for j,item in enumerate(items):
        xx=x+9+(j%2)*104; yy=298+(j//2)*83
        b+=rect(xx,yy,87,35,'white',f'stroke="{[GREEN,DARK,SAND][i]}" stroke-width="1"')+text(xx+43.5,yy+22,''.join(w[0] for w in item.split()).upper(),13,[GREEN,DARK,SAND][i],family='Georgia',anchor='middle')
        b+=text(xx+43.5,yy+51,item,9.2,family='Trebuchet MS',anchor='middle')
pages.append(shell('B4','day','INVESTMENT OFFICE — LIFECYCLE RESPONSIBILITIES',['A shared investment office coordinates','specialist responsibilities across the lifecycle'],b))

# -- B5：两个分类各自闭合；外引标签与组内图例，不把分类相加 --
def donut(cx,cy,values,colors):
    assert sum(values)==100
    out='';start=0;r=40
    for value,color in zip(values,colors):
        length=2*pi*r*value/100
        out+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="23" stroke-dasharray="{length} {2*pi*r-length}" stroke-dashoffset="{-start}" transform="rotate(-90 {cx} {cy})"/>'
        start+=length
    return out+text(cx,cy+4,'100%',11,family='Trebuchet MS',anchor='middle')

b=line(346,131,346,466,'#888',.5)+text(184,143,'By seniority',15,family='Georgia',weight='bold',anchor='middle')+text(522,143,'By rate structure',15,family='Georgia',weight='bold',anchor='middle')
for cx,cy,vals,colors,period in [(184,223,[90,10],[GREEN,SAND],'FY2024'),(184,371,[92,8],[GREEN,SAND],'FY2025'),(522,223,[84,16],[DARK,GREY],'FY2024'),(522,371,[88,12],[DARK,GREY],'FY2025')]:
    b+=donut(cx,cy,vals,colors)+text(cx,cy-65,period,10,family='Trebuchet MS',anchor='middle')
    b+=text(cx+74,cy+33,str(vals[0])+'%',11,colors[0],weight='bold')+line(cx+45,cy+25,cx+68,cy+29,colors[0])
    angle=(vals[0]+vals[1]/2)*2*pi/100-pi/2
    label_color='#606873' if colors[1]==GREY else RUST
    b+=text(cx-65,cy-47,str(vals[1])+'%',11,label_color,weight='bold',anchor='end')+line(cx+52*cos(angle),cy+52*sin(angle),cx-60,cy-50,label_color)
for x,label,color in [(62,'First lien',GREEN),(203,'Other',SAND),(407,'Floating rate',DARK),(560,'Fixed rate',GREY)]:
    b+=rect(x,452,8,8,color)+text(x+13,460,label,10,family='Trebuchet MS')
b+=text(36,481,'Each classification describes the same portfolio at fair value; the two totals are not additive.',8,family='Trebuchet MS')
pages.append(shell('B5','day','PORTFOLIO CONSTRUCTION',['Seniority and rate structure provide','two separate views of the same portfolio'],b))

# -- B6：正负分项各自堆叠，净额线按代数和，预测区间从真实边界起 --
flows={'Bank A':[80,120,100,-30,-60,40,100,80],'Bank B':[40,60,-20,-50,20,30,40,50],'Bank C':[-20,-30,-40,20,30,50,60,70]}
periods=['23Q1','23Q2','23Q3','23Q4','24Q1','24Q2','24Q3F','24Q4F']; colors=[CYAN,TEAL,LIME]
net=[sum(v[i] for v in flows.values()) for i in range(8)]; assert net==[100,150,40,-60,-10,120,200,200]
b=lines(187,125,['Central-bank balance-sheet changes','Quarterly change, illustrative $bn'],12,16,anchor='middle')
b+=rect(268,158,69,272,'#eee')+text(302,170,'Forecast',8,anchor='middle')
for v in [-100,0,100,200]:
    y=354-v*.82;b+=line(63,y,337,y,'#ccc',.5)+text(56,y+3,v,9,anchor='end')
points=[]
for i,period in enumerate(periods):
    x=75+i*35;pos=neg=0
    for vals,col in zip(flows.values(),colors):
        v=vals[i]; bottom=pos if v>=0 else neg;top=bottom+v
        b+=rect(x-10,354-max(bottom,top)*.82,20,abs(v)*.82,col)
        if v>=0:pos=top
        else:neg=top
    points.append(f'{x},{354-net[i]*.82}');b+=text(x,458,period,7.5,anchor='middle')
b+='<polyline points="'+' '.join(points)+'" fill="none" stroke="#222" stroke-width="1.7"/>'
for i,(label,col) in enumerate(zip(flows,colors)):
    x=68+i*77;b+=rect(x,472,8,5,col)+text(x+12,478,label,8)
b+=text(302,478,'— Net',8,anchor='middle')
b+=text(527,126,'Average policy rate',12,weight='bold',anchor='middle')+text(527,142,'Illustrative annual %, separate unit',9,anchor='middle')
rates=[2.8,3.4,3.8,3.3];pts=[]
for i,v in enumerate(rates):
    x=410+i*76;y=266-(v-2)*45;pts.append(f'{x},{y}');b+=text(x,284,2021+i,9,anchor='middle')+text(x,y-8,f'{v:.1f}%',10,anchor='middle')
b+='<polyline points="'+' '.join(pts)+f'" fill="none" stroke="{CYAN}" stroke-width="2"/>'+line(399,270,660,270,'#444')
b+=lines(527,324,['Latest policy move across 20 banks','Share of banks, illustrative %'],12,16,anchor='middle')
for x,v,label in [(438,75,'Easing'),(580,25,'Tightening')]:
    b+=rect(x,450-v,45,v,CYAN)+text(x+22.5,443-v,f'{v}%',11,anchor='middle')+text(x+22.5,470,label,9,anchor='middle')
pages.append(shell('B6','strategy','Policy Measures Give Complementary Signals',['Balance-sheet flows and policy rates answer different questions'],b))

# -- B7：透明的虚构敏感性公式；不冒用源报告未恢复的DDM模型 --
# 约定 payout=40%, perpetual g=2%, discount=treasury+5%; 所有输入显式。
eps=[8,9,10,11,12,13];yields=[2,2.5,3,3.5,4,4.5,5]
values=[[e*.4/(y/100+.05-.02) for y in yields] for e in eps]
assert abs(values[2][2]-66.6666666667)<1e-7
trs=''
for e,row in zip(eps,values):
    trs+=f'<tr><th scope="row">{e:.2f}</th>'
    for value in row:
        t=(value-40)/64;t=max(0,min(1,t));rgb=(round(245-120*t),round(170+40*t),round(160+15*t))
        trs+=f'<td style="background:rgb{rgb}">{value:.1f}</td>'
    trs+='</tr>'
body=text(360,131,'Treasury yield (%)',14,weight='bold',anchor='middle')+text(36,450,'Illustrative perpetual model: value = EPS × 40% ÷ (Treasury yield + 5% − 2%).',10)+text(36,469,'Constant payout and growth; no transition period. This is not the source report’s DDM formula.',9)
page=shell('B7','strategy','Valuation Sensitivity',['Two explicit assumptions determine the scenario value'],body)
table='<table class="sensitivity"><thead><tr><th scope="col">EPS ($)</th>'+''.join(f'<th scope="col">{v:.2f}%</th>' for v in yields)+'</tr></thead><tbody>'+trs+'</tbody></table>'
pages.append(page.replace('</article>',table+'</article>'))
CSS='''*{box-sizing:border-box}body{margin:0;background:#d4d4d4;color:#111;font-family:Arial,sans-serif}.slide{position:relative;width:960px;height:720px;background:white;margin:24px auto}.slide>svg{display:block;width:100%;height:100%}.earnings{width:960px;height:742px;padding:37px 48px}.earnings h1{margin:0;border-bottom:7px solid #000;padding-bottom:14px;font-size:15px;letter-spacing:.1px}.earnings .units{font-size:10px;font-style:italic;margin:14px 0 10px}.earnings table{width:100%;border-collapse:collapse;font-size:10px;table-layout:fixed}.earnings th,.earnings td{height:22px;padding:3px 7px;font-weight:normal;text-align:right}.earnings th:first-child{text-align:left}.earnings thead{color:white;background:#000}.earnings thead th{text-align:center}.earnings tr:nth-child(even){background:#f0f1f1}.earnings .current{border-left:1px solid #a95228;border-right:1px solid #a95228}.earnings thead th:nth-child(3),.earnings thead th:nth-child(5){border:1px solid #a95228}.earnings tbody tr:nth-child(10) .current,.earnings tbody tr:last-child .current{border-bottom:1px solid #a95228}.earnings .section th{padding-left:2px}.earnings .green>*{background:#b4d9d0}.earnings .blue>*{background:#c5d8ec}.earnings .sand>*{background:#c39d78}.earnings .period>*{color:white;background:#000;text-align:center}.earnings .notes{position:absolute;left:48px;right:48px;bottom:58px;font-size:9px;line-height:1.5;border-top:1px solid;padding-top:7px}.earnings footer{position:absolute;bottom:25px;left:48px;right:48px;font-size:9px}.earnings footer span{float:right}.sensitivity{position:absolute;left:48px;top:204px;width:864px;height:337px;table-layout:fixed;border-collapse:collapse;font-size:16px}.sensitivity td,.sensitivity th{text-align:center;padding:8px;border:1px solid white}.sensitivity thead th{font-size:12px}.sensitivity tbody th{font-size:14px}@media print{body{background:white}.slide{margin:0;break-after:page}}'''
html='<!DOCTYPE html><!-- [INPUT]: build.py原创虚构输入；[OUTPUT]: 七页离线可编辑HTML；[POS]: Blackstone五主题案例；[PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md --><html lang="en"><head><meta charset="utf-8"><title>Five Blackstone-inspired themes — original examples</title><style>'+CSS+'</style></head><body>'+''.join(pages)+'</body></html>'
assert len(pages)==7
Path(__file__).with_name('index.html').write_text(html)
print('PASS: seven original pages; periods, per-share values, ring totals, signed net flows and sensitivity formula.')
