import sys, os
from playwright.sync_api import sync_playwright
OUT="/tmp/shots"; os.makedirs(OUT, exist_ok=True)
pages = sys.argv[1:] or ["index.html"]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
    for path in pages:
        name = path.replace("/","_").replace(".html","")
        for label, w, h, full in [("desktop",1440,900,True), ("mobile",390,844,True)]:
            pg = b.new_page(viewport={"width":w,"height":h}, device_scale_factor=1)
            pg.goto(f"http://localhost:8899/{path}", wait_until="networkidle")
            pg.wait_for_timeout(500)
            # forza tutte le reveal
            pg.evaluate("document.querySelectorAll('[data-reveal]').forEach(e=>e.classList.add('is-in'))")
            pg.wait_for_timeout(900)
            pg.screenshot(path=f"{OUT}/{name}_{label}.png", full_page=full)
            pg.close()
        print("ok", name)
    b.close()
