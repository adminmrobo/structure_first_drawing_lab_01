# 실전 연습장 미션 판정 점검 (로컬 서버 8765번 필요)
import asyncio
from playwright.async_api import async_playwright
async def setr(page,sc,name,v):
    await page.evaluate("([sc,n,v])=>{const e=document.querySelector('#'+sc+' [name='+n+']');if(e.type==='checkbox'){e.checked=v;}else e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));}",[sc,name,v])
async def done(page,sc): return await page.evaluate("sc=>[...document.querySelectorAll('#'+sc+' .missions li')].map(l=>l.classList.contains('done'))",sc)
async def board(page,sc): return await page.evaluate("sc=>[...document.querySelectorAll('#'+sc+' .board div')].map(d=>d.textContent).join(' | ')",sc)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        page=await b.new_page();await page.route('**/fonts.g*/**',lambda r: r.abort())
        await page.goto("http://localhost:8765/practice/index.html#fitting");await page.wait_for_timeout(800)
        print('fitting before',await done(page,'fitting'))
        await setr(page,'fitting','cloth',112);await setr(page,'fitting','vol',8);await setr(page,'fitting','pose','up')
        await setr(page,'fitting','mat','coat');await setr(page,'fitting','pose','stand')
        print('fitting after',await done(page,'fitting'),await board(page,'fitting'))
        await page.click('.tabs button[data-t=fabric]')
        print('fabric before',await done(page,'fabric'))
        await setr(page,'fabric','wt',90);await page.wait_for_timeout(6000);print(await board(page,'fabric'))
        await setr(page,'fabric','stiff',80);await page.wait_for_timeout(6000);print(await board(page,'fabric'))
        await setr(page,'fabric','stiff',10);await setr(page,'fabric','gather',True);await page.wait_for_timeout(6000);print(await board(page,'fabric'))
        print('fabric after',await done(page,'fabric'))
        await page.click('.tabs button[data-t=workshop]')
        for n,v in [('gar','tee'),('fit','loose'),('mat','jersey'),('act','up'),('light','ul'),('neg',True)]: await setr(page,'workshop',n,v)
        await setr(page,'workshop','gar','coat');await setr(page,'workshop','mat','wool')
        print('workshop after',await done(page,'workshop'))
        await page.click('.tabs button[data-t=desk]')
        SYM=['잔주름 선 수십','실크처럼','오버핏 티셔츠','숄더백 끈','빛 쪽 비탈','프릴 선','양쪽 뒷면','머리 번과 얼굴']
        CA=['정보량 과다','소재 뒤바뀜','핏(여유) 무시','접점 무시(소품)','그림자 방향 반대','흐름 무시(프릴)','접힘 방향 무시','가림 영역 과다']
        for _ in range(60):
            sym=await page.text_content('#desk .sym');k=[i for i,s in enumerate(SYM) if s in sym][0]
            await page.click(f"#desk .deskopts button:text-is('{CA[k]}')");await page.wait_for_timeout(560)
        print('desk after',await done(page,'desk'))
        await b.close()
asyncio.run(main())
