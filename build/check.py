#!/usr/bin/env python3
"""Controllo qualità: link interni, asset, ancore, immagini senza alt, heading."""
import re, sys
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent.parent / "site"
pagine = sorted(ROOT.rglob("*.html"))
errori, avvisi = [], []

# raccogli tutti gli id presenti per pagina
ids = {}
for f in pagine:
    t = f.read_text(encoding="utf-8")
    ids[f.relative_to(ROOT).as_posix()] = set(re.findall(r'\sid="([^"]+)"', t))

for f in pagine:
    rp = f.relative_to(ROOT).as_posix()
    t = f.read_text(encoding="utf-8")

    # link e risorse
    for attr, val in re.findall(r'(href|src)="([^"]+)"', t):
        if val.startswith(("http", "mailto:", "tel:", "data:", "#", "//")):
            if val.startswith("#") and val[1:] and val[1:] not in ids[rp]:
                errori.append(f"{rp}: ancora inesistente {val}")
            continue
        base, _, anc = val.partition("#")
        target = (f.parent / base).resolve()
        if not target.exists():
            errori.append(f"{rp}: risorsa mancante -> {val}")
        elif anc:
            k = target.relative_to(ROOT).as_posix()
            if k in ids and anc not in ids[k]:
                errori.append(f"{rp}: ancora {anc} inesistente in {k}")

    # immagini senza alt
    for tag in re.findall(r'<img\b[^>]*>', t):
        if 'alt=' not in tag:
            errori.append(f"{rp}: <img> senza alt -> {tag[:70]}")

    # un solo h1
    n_h1 = len(re.findall(r'<h1\b', t))
    if n_h1 != 1:
        errori.append(f"{rp}: {n_h1} elementi h1 (atteso 1)")

    # lang, title, description, canonical
    for chiave, patt in [("lang", r'<html lang="it">'), ("title", r'<title>[^<]{15,}</title>'),
                         ("description", r'name="description" content="[^"]{50,}"'),
                         ("canonical", r'rel="canonical"'), ("og:image", r'property="og:image"')]:
        if not re.search(patt, t):
            errori.append(f"{rp}: manca/insufficiente {chiave}")

    # bottoni icona senza etichetta accessibile
    for tag in re.findall(r'<button\b([^>]*)>(?:\s*<svg.*?</svg>\s*)</button>', t, re.S):
        if 'aria-label' not in tag:
            errori.append(f"{rp}: bottone con sola icona e senza aria-label")

    # segnaposto media da produrre
    n_slot = len(re.findall(r'class="media-slot[ "]', t))
    if n_slot:
        avvisi.append(f"{rp}: {n_slot} segnaposto media da produrre")

print(f"Pagine analizzate: {len(pagine)}\n")
if errori:
    print(f"ERRORI ({len(errori)})")
    for e in errori: print("  ✗", e)
else:
    print("Nessun errore di link, asset, alt, heading o meta.")
print()
if avvisi:
    print(f"Note ({len(avvisi)})")
    for a in avvisi: print("  ·", a)
sys.exit(1 if errori else 0)
