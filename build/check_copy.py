#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controllo editoriale automatico.

Cerca nel sito generato le forme che corrispondono ai cinque difetti descritti
in docs/06-metodo-editoriale.md. Segnala sospetti, non emette sentenze: la
decisione resta di chi scrive, ma nulla passa senza essere stato guardato.

    python3 build/check_copy.py
"""
import re, sys, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "site"
TAG = re.compile(r"<[^>]+>")


def testo(x):
    return re.sub(r"\s+", " ", html.unescape(TAG.sub("", x))).strip()


# I blocchi redazionali che vanno giudicati. Il testo legale e le FAQ restano
# fuori: lì la precisione conta più della forma.
BLOCCHI = [
    ("titolo",     r"<h1[^>]*>(.*?)</h1>"),
    ("titolo",     r"<h2[^>]*>(.*?)</h2>"),
    ("sottotitolo", r"<h3[^>]*>(.*?)</h3>"),
    ("apertura",   r'<p class="lead[^"]*"[^>]*>(.*?)</p>'),
]

REGOLE = [
    # F1. la pagina parla di sé stessa
    ("F1 meta-testo", re.compile(
        r"\b(qui sotto trovate|qui sotto trovi|in questa pagina|nelle pagine che seguono|"
        r"le sezioni che seguono|la ragione per cui|abbiamo scelto|le abbiamo scelte|"
        r"abbiamo preferito|vanno raccolte|il redesign|questo sito|in questo elenco trovi|"
        r"sono tutte verificabili|come vedrai|come puoi vedere)\b", re.I)),
    # F2. istruzioni invece di affordance
    ("F2 istruzioni", re.compile(
        r"\b(trascina|clicca|scorri fino|muovi il cursore|scrivi il nome|premi il|"
        r"seleziona la|usa il filtro|apri il menu)\b", re.I)),
    # F3. descrive ciò che è già visibile
    ("F3 didascalia ovvia", re.compile(
        r"\b(qui sotto|qui accanto|nell'immagine|nella foto|come mostrato)\b", re.I)),
    # F4. costruzioni vietate
    ("F4 formula vietata", re.compile(
        r"(non è (un|una|il|la|solo)[^.,;:]{2,40}[,:] è\b|"
        r"non si tratta di[^.,;:]{2,40}[,:] (ma|bensì)\b)", re.I)),
    # F5. numerali in lettere nei titoli, il tic del contare
    ("F5 numerale scritto", re.compile(
        r"\b(due|tre|quattro|cinque|sei|sette|otto|nove|dieci|trecento|trentasei|"
        r"trecentodieci|duecento|centodieci)\b", re.I)),
    # F6. titolo costruito su una negazione. Una frase negativa lascia
    # impresso il concetto che nega, anche quando serve a smentirlo: il
    # lettore ricorda «fa male» e dimentica il «non». Vale doppio nei
    # titoli, che sono la parte che si legge davvero.
    ("F6 titolo in negativo", re.compile(
        r"\b(non|niente|nessun\w*|mai|senza)\b", re.I)),
]

# L'unica negazione ammessa in un titolo. «Non ho sentito niente» è la frase
# che i pazienti scrivono da soli nelle recensioni: qui la negazione cancella
# una paura che il lettore porta con sé, non aggiunge un difetto al mittente.
# Ogni altra eccezione va discussa, non aggiunta di nascosto a questa riga.
DEROGHE_F6 = re.compile(r"non senti niente", re.I)

# Frasi in cui il numerale è la notizia e quindi resta legittimo.
DEROGHE = re.compile(r"(tasso zero|5\.000|rate|master|impianti|recensioni|specialisti)", re.I)

problemi = []
strutture = {}

for f in sorted(ROOT.rglob("*.html")):
    rp = f.relative_to(ROOT).as_posix()
    if rp in ("note-legali.html", "404.html"):
        continue
    s = f.read_text(encoding="utf-8")
    corpo = s[s.index("<main"):] if "<main" in s else s
    for tipo, pat in BLOCCHI:
        for m in re.findall(pat, corpo, re.S):
            t = testo(m)
            if len(t) < 8:
                continue
            for nome, rx in REGOLE:
                hit = rx.search(t)
                if not hit:
                    continue
                if nome.startswith("F5"):
                    if tipo != "titolo" or DEROGHE.search(t):
                        continue
                if nome.startswith("F6"):
                    if tipo not in ("titolo", "sottotitolo") or DEROGHE_F6.search(t):
                        continue
                problemi.append((rp, tipo, nome, hit.group(0), t[:96]))
            # F6. due titoli vicini con la stessa costruzione
            if tipo == "titolo":
                impronta = " ".join(t.lower().split()[:3])
                strutture.setdefault(impronta, []).append((rp, t[:70]))

    # Le costruzioni vietate e le istruzioni all'utente non valgono solo nei
    # titoli: vanno cercate in ogni paragrafo, comprese le schede riassuntive
    # che non hanno una classe propria.
    for m in re.findall(r"<p[^>]*>(.*?)</p>", corpo, re.S):
        t = testo(m)
        # L'etichetta dell'area di caricamento file è l'unica istruzione
        # ammessa: su desktop non esiste altro modo per segnalare che il
        # riquadro accetta un trascinamento.
        if "Trascina qui il file" in t:
            t = t.replace("Trascina qui il file", "")
        for nome in ("F2 istruzioni", "F4 formula vietata"):
            rx = dict(REGOLE)[nome]
            hit = rx.search(t)
            if hit and not any(p[0] == rp and p[3] == hit.group(0) for p in problemi):
                problemi.append((rp, "paragrafo", nome, hit.group(0), t[:96]))

ripetuti = {k: v for k, v in strutture.items() if len(v) > 2}

print(f"Blocchi redazionali analizzati in {len(list(ROOT.rglob('*.html'))) - 2} pagine\n")
if problemi:
    print(f"SOSPETTI ({len(problemi)})\n")
    for rp, tipo, nome, frammento, t in problemi:
        print(f"  [{nome}] {rp} · {tipo}")
        print(f"     «{frammento}» in: {t}…\n")
else:
    print("Nessun difetto editoriale rilevato dalle regole automatiche.\n")

if ripetuti:
    print(f"APERTURE RIPETUTE ({len(ripetuti)})\n")
    for k, v in ripetuti.items():
        print(f"  «{k}…» compare {len(v)} volte")
        for rp, t in v[:4]:
            print(f"     {rp}: {t}")
    print()

sys.exit(1 if problemi else 0)
