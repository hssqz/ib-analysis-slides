/**
 * [INPUT]: 离线HTML、输出目录；已安装Playwright/Chromium。
 * [OUTPUT]: 隐藏页外导航的截图、SVG文字诊断与原文件哈希；不修改成品。
 * [POS]: 逐页截图与SVG文字诊断，隔离页外导航的潜在截图干扰；不替代内容/视觉判断。
 * [PROTOCOL]: 变更时更新此头部，然后检查 CLAUDE.md
 */
const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const {createHash}=require('node:crypto');
const {chromium}=require('playwright');
const assert=require('node:assert/strict');

async function prepare(page) {
  await page.evaluate(()=>document.fonts.ready);
  await page.addStyleTag({content:'body > nav{visibility:hidden!important}'});
}

function inspectSVG() {
  return [...document.querySelectorAll('article.slide')].map(slide=>{
    const texts=[...slide.querySelectorAll('svg text')].filter(t=>t.getBoundingClientRect().width>0);
    const outside=texts.filter(t=>{
      const b=t.getBoundingClientRect(),s=t.closest('svg').getBoundingClientRect();
      return b.left<s.left-1||b.right>s.right+1||b.top<s.top-1||b.bottom>s.bottom+1;
    }).map(t=>t.textContent);
    // ponytail: O(n²)文字候选框扫描；大规模地图文字时改空间索引。重叠只作为目视候选。
    const overlaps=[];
    for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){
      const a=texts[i].getBoundingClientRect(),b=texts[j].getBoundingClientRect();
      if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>2&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>2)
        overlaps.push([texts[i].textContent,texts[j].textContent]);
    }
    return {id:slide.id,svgTexts:texts.length,outside,overlapCandidates:overlaps};
  });
}

async function selfTest(page) {
  await page.setContent('<nav style="position:sticky;top:0">UI ONLY</nav><article class="slide" style="height:100px"><svg width="100" height="100"><text x="10" y="20">A</text><text x="10" y="20">B</text><text x="99" y="50">Outside</text></svg></article>');
  await prepare(page);
  assert.equal(await page.locator('nav').evaluate(e=>getComputedStyle(e).visibility),'hidden');
  const [row]=await page.evaluate(inspectSVG);
  assert.deepEqual(row.outside,['Outside']);
  assert.equal(row.overlapCandidates.length,1);
  assert.equal(await page.locator('article').evaluate(e=>getComputedStyle(e).visibility),'visible');
  console.log('PASS: navigation isolated; visible slide; SVG outside and overlap detected');
}

async function capture(page,input,output) {
  if(fs.existsSync(output))throw Error('输出目录已存在，请另存检查批次');
  const errors=[];
  await page.route('**/*',route=>{
    if(/^https?:/.test(route.request().url())){errors.push(route.request().url());return route.abort();}
    return route.continue();
  });
  await page.goto(pathToFileURL(path.resolve(input)).href);
  await prepare(page);
  const rows=await page.evaluate(inspectSVG);
  if(!rows.length)throw Error('没有article.slide');
  fs.mkdirSync(output,{recursive:true});
  for(let i=0;i<rows.length;i++){
    const group='pages-'+String(Math.floor(i/6)+1).padStart(2,'0');
    const dir=path.join(output,group);fs.mkdirSync(dir,{recursive:true});
    const target=path.join(group,String(i+1).padStart(2,'0')+'.png');
    await page.locator('article.slide').nth(i).screenshot({path:path.join(output,target)});
    rows[i].screenshot=target;
  }
  const hash=createHash('sha256').update(fs.readFileSync(input)).digest('hex');
  fs.writeFileSync(path.join(output,'report.json'),JSON.stringify({input:path.relative(output,input),sha256:hash,rows,blockedExternalRequests:errors,visualReview:'待逐页目视；文本候选框重叠不自动代表视觉错误'},null,2));
  console.log(JSON.stringify({pages:rows.length,outside:rows.flatMap(r=>r.outside),overlapCandidates:rows.reduce((n,r)=>n+r.overlapCandidates.length,0),blockedExternalRequests:errors,output}));
}

async function main() {
  const args=process.argv.slice(2);
  if(args[0]!=='--self-test'&&args.length!==2)throw Error('用法: capture_pages.cjs input.html new-output-dir | --self-test');
  const browser=await chromium.launch({headless:true,...(process.env.BROWSER_EXECUTABLE_PATH?{executablePath:process.env.BROWSER_EXECUTABLE_PATH}:{})});
  try {
    const page=await browser.newPage({viewport:{width:1100,height:850},deviceScaleFactor:1});
    if(args[0]==='--self-test')await selfTest(page);else await capture(page,args[0],args[1]);
  } finally {await browser.close();}
}
main().catch(e=>{console.error(e.message);process.exitCode=1});
