#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Estrattore integrale dei testi del sito generato.

A differenza di estrai_copy.py, che guarda solo i blocchi redazionali
principali, questo tira fuori ogni stringa che un essere umano può leggere o
sentire leggere da uno screen reader: titolo della scheda, descrizione per i
motori di ricerca, voci di navigazione, titoli, paragrafi, elenchi, dati
chiave, pulsanti, collegamenti, etichette dei moduli, testi di aiuto, alt
delle immagini, aria-label, didascalie e piè di pagina.

Serve alla revisione a mano: nessuna regola automatica sostituisce il fatto
di rileggere tutto.

    python3 build/estrai_tutto.py > /tmp/tutto.txt
"""
import re, sys, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "site"
TAG = re.compile(r"<[^>]+>")


def testo(x):
    return re.sub(r"\s+", " ", html.unescape(TAG.sub(" ", x))).strip()


def trova(pat, s, flags=re.S | re.I):
    return [testo(m) for m in re.findall(pat, s, flags)]


# Ordine di lettura: prima ciò che si vede nella scheda del browser e nei
# risultati di ricerca, poi la pagina dall'alto in basso.
CAMPI = [
    ("TITOLO SCHEDA",  r"<title>(.*?)</title>"),
    ("DESCRIZIONE",    r'<meta name="description" content="([^"]*)"'),
    ("OG TITOLO",      r'<meta property="og:title" content="([^"]*)"'),
    ("OG DESCRIZIONE", r'<meta property="og:description" content="([^"]*)"'),
]

DENTRO = [
    ("H1",        r"<h1[^>]*>(.*?)</h1>"),
    ("H2",        r"<h2[^>]*>(.*?)</h2>"),
    ("H3",        r"<h3[^>]*>(.*?)</h3>"),
    ("H4",        r"<h4[^>]*>(.*?)</h4>"),
    ("OCCHIELLO", r'<span class="eyebrow[^"]*"[^>]*>(.*?)</span>'),
    ("PARAGRAFO", r"<p[^>]*>(.*?)</p>"),
    ("ELENCO",    r"<li[^>]*>(.*?)</li>"),
    ("DIDASCALIA", r"<figcaption[^>]*>(.*?)</figcaption>"),
    ("SCHEDA FOTO", r'data-shot="([^"]*)"'),
    ("RIASSUNTO", r"<summary[^>]*>(.*?)</summary>"),
    ("PULSANTE",  r"<button[^>]*>(.*?)</button>"),
    ("LINK",      r"<a\s[^>]*>(.*?)</a>"),
    ("ETICHETTA", r"<label[^>]*>(.*?)</label>"),
    ("SEGNAPOSTO", r'placeholder="([^"]*)"'),
    ("ALT",       r'\salt="([^"]*)"'),
    ("ARIA",      r'aria-label="([^"]*)"'),
    ("TITLE",     r'\stitle="([^"]*)"'),
    ("DATO",      r'<span class="kf__v"[^>]*>(.*?)</span>'),
]

solo = sys.argv[1] if len(sys.argv) > 1 else None
visti_globali = set()

for f in sorted(ROOT.rglob("*.html")):
    rp = f.relative_to(ROOT).as_posix()
    if solo and solo not in rp:
        continue
    s = f.read_text(encoding="utf-8")
    print("\n" + "=" * 78)
    print(rp)
    print("=" * 78)
    for nome, pat in CAMPI:
        for t in trova(pat, s):
            print(f"[{nome:<14}] {t}")

    testa = s[:s.index("<main")] if "<main" in s else ""
    corpo = s[s.index("<main"):] if "<main" in s else s
    pie = corpo[corpo.rindex("<footer"):] if "<footer" in corpo else ""
    corpo = corpo[:corpo.rindex("<footer")] if "<footer" in corpo else corpo

    for etichetta, sorgente in (("TESTATA", testa), ("CORPO", corpo), ("PIEDE", pie)):
        if not sorgente.strip():
            continue
        righe = []
        visti = set()
        for nome, pat in DENTRO:
            for t in trova(pat, sorgente):
                if len(t) < 2 or t in visti:
                    continue
                visti.add(t)
                # Testata e piè di pagina sono identici su tutte le pagine:
                # li stampo per esteso una volta sola.
                if etichetta in ("TESTATA", "PIEDE"):
                    if t in visti_globali:
                        continue
                    visti_globali.add(t)
                righe.append(f"[{nome:<14}] {t}")
        if righe:
            print(f"\n--- {etichetta} " + "-" * (60 - len(etichetta)))
            print("\n".join(righe))
