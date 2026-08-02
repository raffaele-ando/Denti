#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inventario integrale e deduplicato di ogni stringa leggibile del sito.

estrai_tutto.py stampa tutto pagina per pagina, e quindi ripete 19 volte il
menu, il piè di pagina e il richiamo finale: 3.773 occorrenze in tutto, che
scoraggiano la lettura completa e la rendono di fatto una scrematura.

Questo invece produce l'elenco che si può davvero leggere fino in fondo:
ogni stringa una volta sola, senza quelle che sono già contenute dentro
un'altra (l'HTML annidato le duplica), raggruppate per la pagina in cui
compaiono la prima volta e con l'indicazione di quante pagine le usano.

    python3 build/inventario.py           tutto
    python3 build/inventario.py prezzi    solo le pagine il cui nome contiene «prezzi»
"""
import re, sys, html, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "site"
TAG = re.compile(r"<[^>]+>")

FONTI = [
    ("TITOLO SCHEDA", r"<title>(.*?)</title>"),
    ("DESCRIZIONE",   r'<meta name="description" content="([^"]*)"'),
    ("H1", r"<h1[^>]*>(.*?)</h1>"),
    ("H2", r"<h2[^>]*>(.*?)</h2>"),
    ("H3", r"<h3[^>]*>(.*?)</h3>"),
    ("H4", r"<h4[^>]*>(.*?)</h4>"),
    ("OCCHIELLO", r'<span class="eyebrow[^"]*"[^>]*>(.*?)</span>'),
    ("APERTURA",   r'<p class="lead[^"]*"[^>]*>(.*?)</p>'),
    ("PARAGRAFO",  r"<p[^>]*>(.*?)</p>"),
    ("ELENCO",     r"<li[^>]*>(.*?)</li>"),
    ("DIDASCALIA", r"<figcaption[^>]*>(.*?)</figcaption>"),
    ("DOMANDA",    r"<summary[^>]*>(.*?)</summary>"),
    ("PULSANTE",   r"<button[^>]*>(.*?)</button>"),
    ("LINK",       r"<a\s[^>]*>(.*?)</a>"),
    ("ETICHETTA",  r"<label[^>]*>(.*?)</label>"),
    ("SEGNAPOSTO", r'placeholder="([^"]*)"'),
    ("ALT",        r'\salt="([^"]*)"'),
    ("ARIA",       r'aria-label="([^"]*)"'),
    ("BRIEF FOTO", r'data-shot="([^"]*)"'),
    ("DATO",       r'<span class="kf__v"[^>]*>(.*?)</span>'),
    ("PREZZO",     r'<span class="tariff-row__n"[^>]*>(.*?)</span>'),
]


def testo(x):
    return re.sub(r"\s+", " ", html.unescape(TAG.sub(" ", x))).strip()


filtro = sys.argv[1] if len(sys.argv) > 1 else None

# stringa -> (tipo, prima pagina in cui compare, numero di pagine)
visto = {}
conteggio = collections.Counter()
ordine = []

for f in sorted(ROOT.rglob("*.html")):
    rp = f.relative_to(ROOT).as_posix()
    if filtro and filtro not in rp:
        continue
    s = f.read_text(encoding="utf-8")
    for tipo, pat in FONTI:
        for m in re.findall(pat, s, re.S | re.I):
            t = testo(m)
            if len(t) < 3 or "@context" in t:
                continue
            conteggio[t] += 1
            if t not in visto:
                visto[t] = (tipo, rp)
                ordine.append(t)

# L'HTML annidato fa sì che il testo di un <a> ricompaia dentro il <p> che lo
# contiene. Tengo solo le stringhe che non sono già dentro un'altra: così si
# legge ogni parola una volta.
lunghe = sorted(ordine, key=len, reverse=True)
sopra = []
for t in lunghe:
    if not any(t in g and t != g for g in sopra):
        sopra.append(t)
tenute = set(sopra)

per_pagina = collections.OrderedDict()
for t in ordine:
    if t not in tenute:
        continue
    tipo, rp = visto[t]
    per_pagina.setdefault(rp, []).append((tipo, t, conteggio[t]))

tot = sum(len(v) for v in per_pagina.values())
parole = sum(len(t.split()) for v in per_pagina.values() for _, t, _ in v)
print(f"{tot} stringhe uniche da leggere · {parole} parole · {len(per_pagina)} pagine\n")

for rp, righe in per_pagina.items():
    print("=" * 78)
    print(f"{rp}   ({len(righe)} stringhe nuove qui)")
    print("=" * 78)
    for tipo, t, n in righe:
        rip = f"  [in {n} pagine]" if n > 1 else ""
        print(f"[{tipo:<13}]{rip} {t}")
    print()
