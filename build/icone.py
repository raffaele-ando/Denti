#!/usr/bin/env python3
"""Rasterizza marchio e immagine di condivisione usando i font reali del sito."""
import sys, os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site/assets/img"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

MARK = '''<svg viewBox="0 0 32 32" style="width:100%;height:100%">
 <path d="M11.6 0h8.8v11.6H32v8.8H20.4V32h-8.8V20.4H0v-8.8h11.6z" fill="#C4342E"/>
 <path d="M16 8.4c-2.35 0-4 1.45-4 3.75 0 1.45.43 2.65.69 4.1.26 1.36.17 2.73.43 4.1.17.94.51 1.88 1.2 1.88.69 0 .86-.94 1.03-1.96.17-.85.26-1.79.65-1.79s.48.94.65 1.79c.17 1.02.34 1.96 1.03 1.96.69 0 1.03-.94 1.2-1.88.26-1.37.17-2.74.43-4.1.26-1.45.69-2.65.69-4.1 0-2.3-1.65-3.75-4-3.75z" fill="#FBFAF7"/>
</svg>'''

BASE = os.environ.get("BASE", "http://localhost:8899")
FONTS = f'''<style>
@font-face{{font-family:Fraunces;src:url('{BASE}/assets/fonts/fraunces-latin.woff2') format('woff2');font-weight:300 700;font-display:block}}
@font-face{{font-family:Manrope;src:url('{BASE}/assets/fonts/manrope-latin.woff2') format('woff2');font-weight:400 800;font-display:block}}
*{{margin:0;box-sizing:border-box}}
</style>'''

ICON = FONTS + '''<body style="width:180px;height:180px;background:#FBFAF7;display:grid;place-items:center">
<div style="width:120px;height:120px">''' + MARK + '''</div></body>'''

OG = FONTS + '''<body style="width:1200px;height:630px;background:#08243C;position:relative;overflow:hidden;font-family:Manrope">
<div style="position:absolute;width:760px;height:760px;border-radius:50%;background:radial-gradient(circle,#134B7A,transparent 68%);top:-330px;right:-180px"></div>
<div style="position:absolute;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(42,124,191,.5),transparent 68%);bottom:-260px;left:-130px"></div>
<div style="position:relative;padding:64px 80px;height:100%;display:flex;flex-direction:column;justify-content:space-between">
  <div style="display:flex;align-items:center;gap:14px">
    <div style="width:44px;height:44px">''' + MARK.replace('#FBFAF7', '#08243C') + '''</div>
    <div style="line-height:1">
      <div style="font-family:Fraunces;font-size:32px;color:#FFFDF9;font-weight:500">Piccardo</div>
      <div style="font-size:10px;letter-spacing:.22em;color:#7E96A8;font-weight:700;margin-top:5px">STUDIO ODONTOIATRICO · GENOVA</div>
    </div>
  </div>
  <div>
    <div style="font-family:Fraunces;font-size:70px;line-height:1.02;color:#FFFDF9;letter-spacing:-.03em;font-weight:400">
      Sai quanto spendi<br>e <span style="font-style:italic;color:#B4D3EC">non senti niente</span>.
    </div>
    <div style="font-size:22px;color:var(--su-scuro-2);margin-top:26px">Implantologia · Invisalign · Sedazione cosciente</div>
  </div>
  <div style="border-top:1px solid rgba(255,255,255,.14);padding-top:22px;display:flex;justify-content:space-between;align-items:center">
    <div style="font-size:19px;color:#F2AC5E;font-weight:700">★★★★★&nbsp;&nbsp;5,0 su 310 recensioni Google</div>
    <div style="font-size:16px;color:#7E96A8">Via Maragliano 5, Genova · 010 5959492</div>
  </div>
</div></body>'''

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    for nome, html, w, h, scala in [("brand/icon-180", ICON, 180, 180, 1),
                                    ("brand/icon-512", ICON, 180, 180, 2.85),
                                    ("og-default", OG, 1200, 630, 1)]:
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=scala)
        pg.goto(BASE + "/404.html")          # stessa origine dei font
        pg.set_content(html)
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(900)
        f = OUT / f"{nome}.png"
        f.parent.mkdir(parents=True, exist_ok=True)
        pg.screenshot(path=str(f))
        print(" ", f.relative_to(ROOT), f.stat().st_size // 1024, "KB")
        pg.close()
    b.close()
