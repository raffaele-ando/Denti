#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Estrae ogni testo redazionale del sito, per poterlo giudicare tutto insieme.

Senza una lista unica non ci si accorge delle ripetizioni, dei tic e dei
paragrafi che spiegano l'interfaccia invece di parlare al lettore.
"""
import re, glob, html, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "site"
TAG = re.compile(r"<[^>]+>")

def testo(x):
    return html.unescape(TAG.sub("", x)).replace("\n", " ").strip()
    
PATTERN = [
    ("H1",       r'<h1[^>]*>(.*?)</h1>'),
    ("H2",       r'<h2[^>]*>(.*?)</h2>'),
    ("H3",       r'<h3[^>]*>(.*?)</h3>'),
    ("OCCHIELLO",r'<span class="eyebrow[^"]*"[^>]*>(.*?)</span>'),
    ("LEAD",     r'<p class="lead[^"]*"[^>]*>(.*?)</p>'),
    ("DIDASC",   r'<p class="shotcard__subj">(.*?)</p>'),
    ("CTA",      r'<a class="btn[^"]*"[^>]*>(.*?)</a>'),
]

pagine = sorted(ROOT.rglob("*.html"))
visti = set()
for f in pagine:
    s = f.read_text(encoding="utf-8")
    body = s[s.index("<main") if "<main" in s else 0:]
    righe = []
    for nome, pat in PATTERN:
        for m in re.findall(pat, body, re.S):
            t = testo(m)
            if len(t) < 3 or t in visti:
                continue
            visti.add(t)
            righe.append((nome, t))
    if righe:
        print(f"\n{'='*78}\n{f.relative_to(ROOT)}\n{'='*78}")
        for nome, t in righe:
            print(f"[{nome:9}] {t}")
