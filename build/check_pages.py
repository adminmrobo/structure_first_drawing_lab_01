import asyncio, sys
from playwright.async_api import async_playwright
PAGES=["index.html","01_photo_to_drawing.html","02_fit.html","03_material.html","04_motion.html","05_ai_vfx.html","06_failure_lab.html","practice/index.html"]
async def main(shots=False):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        bad=0
        for w in (390,1280):
            pg=await b.new_page(viewport={"width":w,"height":900});await pg.route('**/fonts.g*/**',lambda r: r.abort())
            errs=[];pg.on("pageerror",lambda e: errs.append(str(e)));pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
            for u in PAGES:
                errs.clear();await pg.goto("http://localhost:8765/"+u);await pg.wait_for_timeout(1500)
                ov=await pg.evaluate("document.documentElement.scrollWidth-window.innerWidth")
                fails=await pg.evaluate("[...document.querySelectorAll('[data-panel]')].filter(h=>h.textContent.includes('불러오지 못했')).map(h=>h.dataset.panel)")
                e=[x for x in errs if 'fonts' not in x and 'net::' not in x and 'Failed to load resource' not in x]
                if ov>2 or fails or e: bad+=1
                print(w,u,"overflow",ov,"failpanels",fails,"err",e[:3])
                if shots and w==1280:
                    for i,el_ in enumerate(await pg.query_selector_all(".panel")):
                        if not await el_.is_visible(): continue
                        await el_.screenshot(path=f"/tmp/shot_{u.replace('/','_')}_{i}.png")
        await b.close();print("BAD",bad)
asyncio.run(main(len(sys.argv)>1))
