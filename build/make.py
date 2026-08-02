#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera il sito statico in `site/`.

    python3 build/make.py

Ogni pagina è HTML puro: il cliente riceve file apribili senza build step.
"""
import sys, os, re
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import componenti
from trattamenti import TRATTAMENTI
componenti.TRATT_NAV = {t["slug"]: t["nav"] for t in TRATTAMENTI}

from content import STUDIO as S
import pagine_home, pagine_interne
from ui import marchio

OUT = Path(__file__).resolve().parent.parent / "site"


def scrivi(percorso, contenuto):
    p = OUT / percorso
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(contenuto, encoding="utf-8")
    return len(contenuto)


# ═════════════════════════════════════════════════════════════════ MARCHIO
def favicon():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
            '<rect width="32" height="32" rx="7" fill="#FBFAF7"/>'
            '<g transform="translate(3.2 3.2) scale(0.8)">'
            + marchio("").replace('class=""', '').replace(
                '<svg  viewBox="0 0 32 32" aria-hidden="true">', '').replace('</svg>', '')
            .replace('class="cross"', 'fill="#C4342E"').replace('class="tooth"', 'fill="#FBFAF7"')
            + '</g></svg>')


def og_default():
    """Immagine di condivisione social, generata come SVG (da esportare in PNG)."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#08251F"/>
<circle cx="1010" cy="90" r="360" fill="#114C41" opacity=".45"/>
<circle cx="150" cy="620" r="260" fill="#1F8069" opacity=".18"/>
<g transform="translate(80 78)">
  <g transform="scale(1.5)">
    <path d="M11.6 0h8.8v11.6H32v8.8H20.4V32h-8.8V20.4H0v-8.8h11.6z" fill="#C4342E"/>
    <path d="M16 8.4c-2.35 0-4 1.45-4 3.75 0 1.45.43 2.65.69 4.1.26 1.36.17 2.73.43 4.1.17.94.51 1.88 1.2 1.88.69 0 .86-.94 1.03-1.96.17-.85.26-1.79.65-1.79s.48.94.65 1.79c.17 1.02.34 1.96 1.03 1.96.69 0 1.03-.94 1.2-1.88.26-1.37.17-2.74.43-4.1.26-1.45.69-2.65.69-4.1 0-2.3-1.65-3.75-4-3.75z" fill="#08251F"/>
  </g>
  <text x="66" y="26" font-family="Georgia,serif" font-size="38" fill="#FFFDF9">Piccardo</text>
  <text x="67" y="46" font-family="Helvetica,sans-serif" font-size="12" letter-spacing="4" fill="var(--su-scuro-3)">STUDIO ODONTOIATRICO · GENOVA</text>
</g>
<text x="80" y="300" font-family="Georgia,serif" font-size="62" fill="#FFFDF9">Sai quanto spendi</text>
<text x="80" y="372" font-family="Georgia,serif" font-size="62" fill="#FFFDF9">e <tspan font-style="italic" fill="#C9E1D7">non senti niente</tspan>.</text>
<text x="80" y="452" font-family="Helvetica,sans-serif" font-size="23" fill="var(--su-scuro-2)">Implantologia · Invisalign · Sedazione cosciente</text>
<g transform="translate(80 510)">
  <text x="0" y="20" font-family="Helvetica,sans-serif" font-size="19" fill="#F2E9D8">★★★★★  5,0 su 310 recensioni Google</text>
  <text x="0" y="52" font-family="Helvetica,sans-serif" font-size="17" fill="var(--su-scuro-3)">Via Maragliano 5, Genova · lun–sab 8:00–20:30 · 010 5959492</text>
</g>
</svg>'''


# ═════════════════════════════════════════════════════════════ SEO TECNICO
def sitemap(urls):
    voci = "".join(
        f'  <url><loc>{S["sito"]}/{u}</loc><changefreq>monthly</changefreq>'
        f'<priority>{p}</priority></url>\n' for u, p in urls
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{voci}</urlset>\n'


REDIRECT = {
    "protossido.html": "trattamenti/paura-del-dentista.html",
    "sedazione.html": "trattamenti/paura-del-dentista.html",
    "implantologia.html": "trattamenti/implantologia.html",
    "caricoimmediato.html": "trattamenti/implantologia.html",
    "caricoimmediato2.html": "trattamenti/implantologia.html",
    "innestiosso.html": "trattamenti/implantologia.html",
    "invisalign.html": "trattamenti/invisalign-ortodonzia.html",
    "ortodonzia.html": "trattamenti/invisalign-ortodonzia.html",
    "lumineers.html": "trattamenti/estetica-del-sorriso.html",
    "sbiancamentidenti.html": "trattamenti/estetica-del-sorriso.html",
    "capsule.html": "trattamenti/protesi-e-corone.html",
    "dentiera.html": "trattamenti/protesi-e-corone.html",
    "scheletrato.html": "trattamenti/protesi-e-corone.html",
    "nylon.html": "trattamenti/protesi-e-corone.html",
    "otturazioni.html": "trattamenti/cure-conservative.html",
    "devitalizzazioni.html": "trattamenti/cure-conservative.html",
    "giudizio.html": "trattamenti/chirurgia-orale.html",
    "igiene.html": "trattamenti/igiene-e-prevenzione.html",
    "pedodonzia.html": "trattamenti/bambini.html",
    "bambini.html": "trattamenti/bambini.html",
    "emergenze.html": "trattamenti/urgenze.html",
    "domicilio.html": "trattamenti/urgenze.html",
    "servizi.html": "trattamenti.html",
    "studio.html": "studio.html",
    "salaattesa.html": "studio.html",
    "salaraggi.html": "studio.html#tecnologia",
    "sterilizzazione.html": "studio.html#sterilizzazione",
    "laboratorio.html": "studio.html#laboratorio",
    "uffici.html": "studio.html",
    "zoneoperative.html": "studio.html",
    "bagnodisabili.html": "studio.html#accessibilita",
    "posteggio.html": "studio.html#parcheggio",
    "gruppocontinuita.html": "studio.html#continuita",
    "direzionesanitaria.html": "team.html",
    "reception.html": "team.html",
    "virtuale.html": "studio.html#tour",
    "chisiamo.html": "team.html",
    "piccardo.html": "team.html",
    "gibelli.html": "team.html",
    "parodi.html": "team.html",
    "pedodonzista.html": "team.html",
    "igienista.html": "team.html",
    "igienista2.html": "team.html",
    "parodontologo.html": "team.html",
    "assistenti.html": "team.html",
    "segretariadentista.html": "team.html",
    "interviste.html": "team.html#interviste",
    "tariffe.html": "prezzi.html",
    "tariffario.html": "prezzi.html",
    "finanziamenti.html": "prezzi.html#finanziamenti",
    "convenzioni.html": "prezzi.html#convenzioni",
    "preventivo.html": "prezzi.html#preventivo",
    "richiedi-un-preventivo-on-line.html": "prezzi.html#preventivo",
    "contatti.html": "contatti.html",
    "contattaci.html": "contatti.html",
    "dovesiamo.html": "contatti.html#dove-siamo",
    "raggiungerci.html": "contatti.html#dove-siamo",
    "policy.html": "note-legali.html",
    "contenziosi-e-risarcimenti.html": "note-legali.html#rc",
    "polizza-assicurativa-rc-professionale.html": "note-legali.html#rc",
}


def htaccess():
    righe = "\n".join(f"Redirect 301 /{a} /{b}" for a, b in sorted(REDIRECT.items())
                      if a != b.split("#")[0])
    return f"""# Redirect 301 dal vecchio sito: vedi docs/02-strategia-ia-wireframe.md
# Nessuno dei {len(REDIRECT)} URL storici deve restituire 404.
Options -Indexes
ErrorDocument 404 /404.html
DirectoryIndex index.html

{righe}

# Compressione
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css text/javascript application/javascript image/svg+xml application/json
</IfModule>

# Cache degli asset con hash-free naming: rivedere alla prima release
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp            "access plus 6 months"
  ExpiresByType font/woff2            "access plus 1 year"
  ExpiresByType text/css              "access plus 1 week"
  ExpiresByType application/javascript "access plus 1 week"
  ExpiresByType text/html             "access plus 0 seconds"
</IfModule>

<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
</IfModule>
"""


# ══════════════════════════════════════════════════════════════════ MAIN
def main():
    pagine = []

    pagine.append(("index.html", pagine_home.render(), "1.0"))
    pagine.append(("trattamenti.html", pagine_interne.hub_trattamenti(), "0.9"))
    for t in TRATTAMENTI:
        pagine.append((f"trattamenti/{t['slug']}.html", pagine_interne.trattamento(t), "0.9"))
    pagine.append(("studio.html", pagine_interne.studio(), "0.8"))
    pagine.append(("team.html", pagine_interne.team(), "0.8"))
    pagine.append(("prezzi.html", pagine_interne.prezzi(), "0.9"))
    pagine.append(("recensioni.html", pagine_interne.recensioni(), "0.7"))
    pagine.append(("contatti.html", pagine_interne.contatti(), "0.8"))
    pagine.append(("note-legali.html", pagine_interne.note_legali(), "0.2"))
    pagine.append(("404.html", pagine_interne.pagina404(), "0.1"))

    tot = 0
    for percorso, html, _ in pagine:
        n = scrivi(percorso, html)
        tot += n
        print(f"  {percorso:44s} {n/1024:7.1f} KB")

    scrivi("assets/img/brand/favicon.svg", favicon())
    scrivi("assets/img/og-default.svg", og_default())
    scrivi("sitemap.xml", sitemap([(u, p) for u, _, p in pagine if u != "404.html"]))
    scrivi("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {S['sito']}/sitemap.xml\n")
    scrivi(".htaccess", htaccess())

    print(f"\n  {len(pagine)} pagine · {tot/1024:.0f} KB di HTML · {len(REDIRECT)} redirect 301")


if __name__ == "__main__":
    main()
