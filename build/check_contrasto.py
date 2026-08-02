"""Misura il contrasto reale di ogni testo renderizzato, non quello teorico."""
import glob, sys
from playwright.sync_api import sync_playwright
CH = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

JS = r"""(() => {
  const lum = c => { const [r,g,b] = c; const f = v => { v/=255; return v<=.03928? v/12.92 : Math.pow((v+.055)/1.055,2.4); };
    return .2126*f(r)+.7152*f(g)+.0722*f(b); };
  const parse = s => { const m = s.match(/[\d.]+/g); return m ? m.slice(0,4).map(Number) : null; };
  const bgOf = el => {
    let n = el;
    while (n && n !== document.documentElement) {
      const s = getComputedStyle(n); const c = parse(s.backgroundColor);
      if (c && (c[3] === undefined || c[3] > .55)) return c.slice(0,3);
      n = n.parentElement;
    }
    return [255,255,255];
  };
  const out = [];
  const heroScuro = document.body.classList.contains('hero-scuro');
  document.querySelectorAll('body *').forEach(el => {
    if (heroScuro && el.closest('.header')) return;
    if (!el.childNodes.length) return;
    const testo = Array.from(el.childNodes).filter(n=>n.nodeType===3).map(n=>n.textContent.trim()).join(' ').trim();
    if (testo.length < 3) return;
    const s = getComputedStyle(el);
    if (s.visibility === 'hidden' || s.display === 'none' || +s.opacity < .3) return;
    const r = el.getBoundingClientRect(); if (!r.width || !r.height) return;
    const fg = parse(s.color).slice(0,3), bg = bgOf(el);
    const l1 = lum(fg), l2 = lum(bg);
    const cr = (Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);
    const px = parseFloat(s.fontSize), grande = px >= 24 || (px >= 18.66 && +s.fontWeight >= 700);
    const soglia = grande ? 3 : 4.5;
    if (cr < soglia) out.push({sel: el.tagName.toLowerCase()+'.'+(typeof el.className==='string'?el.className.split(' ').filter(Boolean).slice(0,2).join('.'):''),
      testo: testo.slice(0,48), cr: +cr.toFixed(2), soglia, px: +px.toFixed(0), fg: s.color, bg: 'rgb('+bg.join(',')+')'});
  });
  return out;
})()"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CH)
    tot = {}
    for f in sorted(glob.glob("site/**/*.html", recursive=True)):
        u = f.replace("site/", "")
        pg = b.new_page(viewport={"width": 1440, "height": 900})
        pg.goto(f"http://localhost:8899/{u}", wait_until="networkidle")
        pg.evaluate("document.querySelectorAll('[data-reveal]').forEach(e=>e.classList.add('is-in'))")
        pg.wait_for_timeout(250)
        for r in pg.evaluate(JS):
            k = (r["sel"], r["cr"], r["fg"], r["bg"])
            tot.setdefault(k, []).append((u, r["testo"], r["px"], r["soglia"]))
        pg.close()
    b.close()

if not tot:
    print("Nessun testo sotto la soglia WCAG AA.")
else:
    print(f"{len(tot)} combinazioni sotto soglia\n")
    for (sel, cr, fg, bg), occ in sorted(tot.items(), key=lambda x: x[0][1]):
        u, testo, px, soglia = occ[0]
        print(f"  {cr:5.2f} (serve {soglia})  {sel:34s} {px:>3}px  {fg} su {bg}")
        print(f"         «{testo}»  in {u}  ({len(occ)} occorrenze)")
