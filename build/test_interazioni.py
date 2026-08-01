#!/usr/bin/env python3
"""Test funzionali dell'interfaccia (Playwright)."""
import sys
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8899"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
ok, ko = [], []


def check(nome, cond, extra=""):
    (ok if cond else ko).append(f"{nome} {extra}".strip())


with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)

    # ── desktop ────────────────────────────────────────────────
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto(f"{BASE}/index.html", wait_until="networkidle")

    pg.hover(".nav__item.has-mega")
    pg.wait_for_timeout(400)
    check("mega menu si apre al passaggio", pg.locator(".mega").first.is_visible())
    check("mega menu elenca i 10 trattamenti", pg.locator(".mega__link").count() == 10,
          f"({pg.locator('.mega__link').count()})")

    pg.mouse.move(200, 860); pg.wait_for_timeout(600)
    check("mega menu si chiude", not pg.locator(".mega").first.is_visible())

    # tab per intenzione
    pg.locator('[role="tab"]').nth(2).click(); pg.wait_for_timeout(300)
    check("tab 3 selezionato", pg.locator('[role="tab"]').nth(2).get_attribute("aria-selected") == "true")
    check("pannello 3 visibile", pg.locator('#pan-2').is_visible())
    check("pannello 1 nascosto", not pg.locator('#pan-0').is_visible())
    pg.locator('[role="tab"]').nth(2).press("ArrowRight"); pg.wait_for_timeout(200)
    check("frecce da tastiera sui tab", pg.locator('[role="tab"]').nth(3).get_attribute("aria-selected") == "true")

    # slider prima/dopo
    ba = pg.locator(".ba").first
    ba.scroll_into_view_if_needed(); pg.wait_for_timeout(700)
    box = ba.bounding_box()
    pg.mouse.move(box["x"] + box["width"] * .8, box["y"] + box["height"] / 2)
    pg.wait_for_timeout(250)
    pos = pg.evaluate("getComputedStyle(document.querySelector('.ba')).getPropertyValue('--pos')")
    check("slider prima/dopo risponde", pos.strip() not in ("50%", ""), f"(--pos={pos.strip()})")
    ba.press("ArrowLeft"); pg.wait_for_timeout(150)
    check("slider accessibile da tastiera", ba.get_attribute("aria-valuenow") is not None)

    # contatori
    pg.locator(".stat-bar").scroll_into_view_if_needed(); pg.wait_for_timeout(2200)
    testi = pg.locator(".stat-bar .stat-n").all_inner_texts()
    check("contatore impianti", "4.000" in testi[0], f"({testi[0]!r})")
    check("contatore successo", "99,8" in testi[1], f"({testi[1]!r})")
    check("anno senza separatore", testi[2].strip() == "1997", f"({testi[2]!r})")

    # header sticky
    pg.mouse.wheel(0, 300); pg.wait_for_timeout(400)
    check("header diventa opaco allo scroll", "is-stuck" in (pg.locator(".header").get_attribute("class") or ""))
    pg.close()

    # ── prezzi ─────────────────────────────────────────────────
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto(f"{BASE}/prezzi.html", wait_until="networkidle")

    tot = pg.locator(".tariff-row").count()
    pg.fill("#tariff-q", "impianto"); pg.wait_for_timeout(300)
    vis = pg.locator(".tariff-row:not(.is-hidden)").count()
    check("ricerca nel tariffario filtra", 0 < vis < tot, f"({vis}/{tot})")
    pg.fill("#tariff-q", ""); pg.wait_for_timeout(200)
    pg.locator('[data-tariff-cat="implantologia"]').click(); pg.wait_for_timeout(300)
    check("filtro per categoria", pg.locator(".tariff-row:not(.is-hidden)").count() == 4,
          f"({pg.locator('.tariff-row:not(.is-hidden)').count()})")

    # calcolatore
    pg.locator("#calc").scroll_into_view_if_needed()
    check("rata iniziale 3.500/36 a tasso 0", pg.inner_text("#calc-rata") == "97", f"({pg.inner_text('#calc-rata')})")
    pg.locator('[data-mesi="12"]').click(); pg.wait_for_timeout(200)
    check("rata a 12 mesi", pg.inner_text("#calc-rata") == "292", f"({pg.inner_text('#calc-rata')})")
    pg.eval_on_selector("#calc-importo", "e=>{e.value=8000;e.dispatchEvent(new Event('input'))}")
    pg.wait_for_timeout(200)
    check("oltre 5.000 € passa a tasso agevolato", "agevolato" in pg.inner_text("#calc-nota"))

    # form
    pg.locator("#form-preventivo").scroll_into_view_if_needed()
    pg.locator("#form-preventivo button[type=submit]").click(); pg.wait_for_timeout(300)
    check("il form blocca l'invio a vuoto", pg.locator(".field--error").count() >= 4,
          f"({pg.locator('.field--error').count()} campi in errore)")
    pg.fill("#form-preventivo [name=nome]", "Mario Rossi")
    pg.fill("#form-preventivo [name=tel]", "0105959492")
    pg.fill("#form-preventivo [name=email]", "non-valida")
    pg.check("#form-preventivo [name=privacy]")
    pg.locator("#form-preventivo button[type=submit]").click(); pg.wait_for_timeout(300)
    check("email non valida intercettata", pg.locator(".field--error").count() == 1)
    pg.fill("#form-preventivo [name=email]", "mario@esempio.it")
    pg.locator("#form-preventivo button[type=submit]").click(); pg.wait_for_timeout(1400)
    check("conferma di invio mostrata", pg.locator(".form-success.is-on").count() == 1)
    pg.close()

    # ── team ───────────────────────────────────────────────────
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto(f"{BASE}/team.html", wait_until="networkidle")
    pg.locator("[data-person]").first.click(); pg.wait_for_timeout(600)
    check("drawer del professionista si apre", pg.locator("#person-drawer.is-open").count() == 1)
    check("drawer contiene il CV", "Master universitario" in pg.inner_text(".person-drawer__body"))
    pg.keyboard.press("Escape"); pg.wait_for_timeout(500)
    check("drawer si chiude con Escape", pg.locator("#person-drawer.is-open").count() == 0)
    pg.close()

    # ── mobile ─────────────────────────────────────────────────
    pg = b.new_page(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
    pg.goto(f"{BASE}/index.html", wait_until="networkidle")
    pg.mouse.wheel(0, 400); pg.wait_for_timeout(500)
    check("barra sticky mobile compare", "is-in" in (pg.locator(".mobile-bar").get_attribute("class") or ""))
    check("barra ha 3 azioni", pg.locator(".mobile-bar a").count() == 3)
    pg.locator(".burger").click(); pg.wait_for_timeout(500)
    check("drawer mobile si apre", pg.locator(".drawer.is-open").count() == 1)
    pg.locator(".drawer__group").nth(1).locator(".drawer__head").click(); pg.wait_for_timeout(500)
    check("accordion del drawer si espande", pg.locator(".drawer__group.is-open").count() == 1)
    larg = pg.evaluate("document.documentElement.scrollWidth")
    check("nessuno scroll orizzontale", larg <= 390, f"(scrollWidth={larg})")
    pg.close()

    # ── accessibilità di base su tutte le pagine ───────────────
    import glob, os
    for f in sorted(glob.glob("site/**/*.html", recursive=True)):
        u = f.replace("site/", "")
        pg = b.new_page(viewport={"width": 1280, "height": 800})
        pg.goto(f"{BASE}/{u}", wait_until="domcontentloaded")
        w = pg.evaluate("document.documentElement.scrollWidth")
        check(f"{u}: nessun overflow orizzontale", w <= 1280, f"({w})")
        err = pg.evaluate("""(()=>{const out=[];
          document.querySelectorAll('a[href]').forEach(a=>{
            if(!a.textContent.trim() && !a.getAttribute('aria-label') && !a.querySelector('.sr-only')) out.push(a.outerHTML.slice(0,60));});
          return out;})()""")
        check(f"{u}: nessun link senza nome accessibile", not err, str(err[:2]))
        pg.close()

    b.close()

print(f"PASSATI: {len(ok)}")
if ko:
    print(f"\nFALLITI: {len(ko)}")
    for k in ko:
        print("  ✗", k)
    sys.exit(1)
print("Tutti i test funzionali sono passati.")
