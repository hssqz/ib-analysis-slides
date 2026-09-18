#!/usr/bin/env node
/*
 * [INPUT]: 本文件内原创虚构数据；PptxGenJS；可选同目录example.png。
 * [OUTPUT]: 新目录中的3页raw.pptx，原生文字/形状/表格/图表及内嵌工作簿。
 * [POS]: 公开后端的可重建示例；前2页承接已发布Meridian HTML T2/T4。
 * [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
 */
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const pptxgen = require('pptxgenjs');
const pptx = new pptxgen();
pptx.defineLayout({ name:'SOURCE', width:10, height:5.625 });
pptx.layout='SOURCE'; pptx.author='IB Analysis Slides'; pptx.subject='Fictional editable examples';
pptx.title='Meridian Instruments — editable handoff'; pptx.lang='en-US';
pptx.theme={headFontFace:'Arial',bodyFontFace:'Arial',lang:'en-US'};
const D='00355F', L='6E93BE', G='7F7F7F', T='23C7BA', F='20396D';

function text(slide, value, x, y, w, h, size=10, extra={}) {
  slide.addText(value,{x:x/72,y:y/72,w:w/72,h:h/72,fontFace:'Arial',fontSize:size,
    color:D,margin:0,breakLine:false,vertAnchor:'top',valign:'top',paraSpaceAfter:0,
    lineSpacingMultiple:1,...extra});
}
function rect(slide,x,y,w,h,color) {
  slide.addShape(pptx.ShapeType.rect,{x:x/72,y:y/72,w:w/72,h:h/72,line:{color,transparency:100},fill:{color}});
}
function line(slide,x,y,w,h,color=T,width=.5) {
  slide.addShape(pptx.ShapeType.line,{x:x/72,y:y/72,w:w/72,h:h/72,line:{color,width}});
}
function footer(slide,n) {
  text(slide,'Illustrative only • fictional Meridian Instruments • see sources.md',33,386,625,10,6,{color:G});
  text(slide,String(n),687,386,15,10,6,{color:G,align:'right'});
}
function analysis() {
  const s=pptx.addSlide();
  text(s,'Installed Workflows Support a Growing Service Business',33,20,663,28,19,{bold:true});
  const blocks=[
    [115,'Installed workflows support repeat use','Validated methods reduce the need to reconfigure routine tests.','120 laboratory sites; 24 methods in the internal library.'],
    [209,'Service expands faster than equipment sales','Remote diagnostics add a recurring touchpoint after installation.','Service revenue rose 40%; equipment revenue rose 6.7%.'],
    [303,'Deployment capacity remains the constraint','A second hub is planned; capacity and opening date are undisclosed.','Target is operational coverage, not a quantified revenue forecast.']
  ];
  for(const [y,head,body,qual] of blocks) {
    text(s,head,33,y-12,438,18,12,{bold:true});
    text(s,body,33,y+10,440,17,10);
    text(s,qual,33,y+29,440,18,10.56,{color:G,italic:true});
  }
  text(s,'Revenue by business',482,97,200,17,11,{bold:true});
  text(s,'USD millions; fiscal years',482,114,200,14,8,{color:G,italic:true});
  for(const [x,year,eq,sv] of [[494,2024,150,50],[579,2025,160,70]]) {
    for(const [val,bottom,col] of [[eq,326,D],[sv,326-eq*.65,L]]) {
      const h=val*.65;rect(s,x,bottom-h,49,h,col);
      text(s,String(val),x,bottom-h/2-6,49,14,10,{color:'FFFFFF',align:'center'});
    }
    text(s,String(eq+sv),x,326-(eq+sv)*.65-18,49,17,11,{color:G,bold:true,align:'center'});
    text(s,String(year),x,333,49,14,9,{align:'center'});
  }
  line(s,482,326,165,0,'444444',.6);
  text(s,'Equipment',482,356,80,14,8);text(s,'Service',570,356,70,14,8,{color:L});footer(s,1);
}
function pxText(s,value,x,y,w,h,size,opts={}) {
  text(s,value,x*.75,y*.75,w*.75,h*.75,size*.75,{color:F,...opts});
}
function financial() {
  const s=pptx.addSlide();
  rect(s,0,54,720,351,'E4E5E7');
  pxText(s,'Financial Overview',30,29,880,29,19.44,{color:'748CAB',bold:true});
  pxText(s,'Financial Results',14,81,452,20,14.16,{bold:true,align:'center'});
  pxText(s,'Financial Overview Highlights',507,81,432,20,14.16,{bold:true,align:'center'});
  line(s,360,60.75,0,320,'AAAAAA',.75);
  pxText(s,'USD millions, except ratios; changes calculated from unrounded inputs',14,112,452,12,6.96,{italic:true});
  const rows=[
    ['Equipment revenue','160','150','6.7%',''],['Service revenue','70','50','40.0%',''],
    ['Net revenue','230','200','15.0%','key'],['Cost of revenue','(140)','(120)','16.7%',''],
    ['Gross profit','90','80','12.5%','subtotal'],['Operating expenses','(52)','(45)','15.6%',''],
    ['Operating profit','38','35','8.6%','key'],['Net interest expense','(4)','(5)','(20.0)%',''],
    ['Pre-tax profit','34','30','13.3%','subtotal'],['Income tax','(7)','(6)','16.7%',''],
    ['Net profit','27','24','12.5%','key'],['Gross margin','39.1%','40.0%','(0.9)pp',''],
    ['Operating margin','16.5%','17.5%','(1.0)pp','']
  ];
  const none={type:'none'};
  const data=[['','FY2025','FY2024','vs. FY2024'].map(v=>({text:v,options:{bold:true,fill:'E4E5E7',border:[none,none,{color:'748CAB',pt:.75},none]}}))];
  rows.forEach((r,i)=>data.push(r.slice(0,4).map((v,j)=>({text:v,options:{
    bold:j===1||Boolean(r[4]),fill:j===0?'E4E5E7':i%2?'E3EBF4':'C7D6E8',
    border:[r[4]?{color:F,pt:r[4]==='key'?1.5:.75}:none,
      r[4]==='key'&&j===3?{color:F,pt:1.5}:none,
      r[4]==='key'?{color:F,pt:1.5}:none,r[4]==='key'&&j===0?{color:F,pt:1.5}:none]
  }}))));
  s.addTable(data,{x:14/96,y:123/96,w:452/96,colW:[194.36,85.88,85.88,85.88].map(v=>v/96),
    rowH:[24,...rows.map(()=>25)].map(v=>v/96),fontFace:'Arial',fontSize:7.5,color:F,
    margin:[3,4.5,3,4.5],align:'right',valign:'mid',autoPage:false,border:none,objectName:'Financial results — native cells'});
  const copy=[
    [508,111,'FY2025 revenue and gross profit',true],
    [521,130,'Net revenue increased 15.0% to $230 million.'],
    [534,148.14,'Equipment contributed $10 million of the $30 million increase; service contributed $20 million.'],
    [534,165.28,'Service mix rose to 30.4%, from 25.0% in FY2024.'],
    [521,183.42,'Gross profit rose 12.5% to $90 million.'],
    [534,201.56,'Cost of revenue increased faster than sales, reducing gross margin by 0.9 percentage points.'],
    [534,218.70,'Costs are not disclosed by business; revenue contribution cannot establish segment profitability.'],
    [508,274.98,'FY2025 profitability',true],
    [521,293.98,'Operating profit increased 8.6% to $38 million.'],
    [534,312.13,'Operating expenses increased by $7 million, absorbing most of the $10 million gross-profit increase.'],
    [521,342.41,'Net profit increased 12.5% to $27 million.'],
    [534,360.55,'Net interest expense fell by $1 million; tax expense increased by $1 million.'],
    [534,377.69,'Operating margin declined by 1.0 percentage point to 16.5%.']
  ];
  for(const [x,y,t,bold] of copy) {
    pxText(s,t,x,y,939-x,28,bold?10:9.72,{bold:!!bold});
    if(!bold)pxText(s,x===521?'▪':'—',x-13,y,12,16,9.72);
  }
  line(s,508*.75,258*.75,431*.75,0,F,1.5);
  pxText(s,'Annual results only. Quarterly drivers and per-share data are not provided.',508,398.83,431,30,8,{italic:true});
  pxText(s,'Illustrative only • fictional Meridian Instruments • see sources.md',20,521,860,12,7,{color:'666666'});
  pxText(s,'2',910,521,30,12,7,{color:'666666',align:'right'});
}
function nativeObjects() {
  const s=pptx.addSlide();
  text(s,'Native Chart Data and Editable Group Labels',33,20,663,28,19,{bold:true});
  for(const [x,label] of [[33,'NATIVE CHART'],[389,'EDITABLE OBJECTS']]) {
    const w=300,gap=190;line(s,x,82,(w-gap)/2,0);line(s,x+(w+gap)/2,82,(w-gap)/2,0);
    line(s,x,82,0,17);line(s,x+w,82,0,17);
    text(s,label,x,74,w,16,10,{align:'center',charSpacing:2});
  }
  s.addChart(pptx.ChartType.bar,[{name:'Scenario delta',labels:['FY2024','FY2025'],values:[-4,7]}],{
    x:33/72,y:115/72,w:300/72,h:225/72,barDir:'col',showLegend:false,
    showValue:true,showTitle:false,showBorder:false,showCatName:false,
    catAxisLabelFontFace:'Arial',catAxisLabelFontSize:9,valAxisLabelFontFace:'Arial',valAxisLabelFontSize:8,
    valAxisMinVal:-5,valAxisMaxVal:10,valAxisMajorUnit:5,chartColors:[D],
    catAxisLineColor:'777777',valAxisLineColor:'777777',showCatName:false,
    showMarker:false,showShadow:false,objectName:'Native chart with embedded workbook'});
  text(s,'Separate capability-test data: −4 and +7',33,346,320,18,9,{italic:true,color:G});
  rect(s,389,117,300,44,L);text(s,'Editable text inside a shape',399,129,280,22,12,{color:'FFFFFF',bold:true});
  text(s,'Grouping labels retain regular weight and tracking.\nThe chart contains an editable data workbook.\nThe swatch below is an original PNG, not a chart.',389,180,300,60,10);
  const png=path.join(__dirname,'example.png');
  s.addImage({path:png,x:389/72,y:261/72,w:80/72,h:40/72,altText:'Original two-color demonstration swatch'});
  text(s,'Raster media stays an image.',481,274,204,24,10,{italic:true,color:G});footer(s,3);
}
async function main() {
  const output=process.argv[2];if(!output)throw new Error('Usage: node build.cjs NEW_OUTPUT_DIRECTORY');
  assert.equal(160+70,230);assert.equal(230-140-52,38);assert.equal(38-4-7,27);
  assert.equal(((70/50-1)*100).toFixed(1),'40.0');
  analysis();financial();nativeObjects();fs.mkdirSync(output,{recursive:false});
  await pptx.writeFile({fileName:path.join(output,'raw.pptx')});
  console.log(path.resolve(output,'raw.pptx'));
}
if(require.main===module)main().catch(e=>{console.error(e.message);process.exitCode=1;});
