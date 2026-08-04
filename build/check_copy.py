#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controllo editoriale automatico.

Cerca nel sito generato le forme che corrispondono ai difetti descritti in
docs/06-metodo-editoriale.md e analizzati in docs/07-tassonomia-dei-difetti.md. Segnala sospetti, non emette sentenze: la
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
    # F9. dislocazione con ripresa pronominale: è un tratto del parlato
    # (italiano dell'uso medio, Sabatini 1985), fuori registro in un titolo
    # scritto di una struttura sanitaria. Vedi docs/07, classe C10.
    # Il marcatore affidabile non è il clitico da solo, che in italiano è
    # normalissimo, ma il clitico con il soggetto pronominale posposto
    # enfatico: «te la leggiamo noi», «alla pratica pensiamo noi».
    ("F9 dislocazione parlata", re.compile(
        r"\b(te|ce|glie)\s?(la|lo|li|le)\s+\w+(iamo|ate|ano)\s+noi\b|"
        r"\b(ci\s+)?(pensiamo|facciamo|diciamo|vediamo|scriviamo|troviamo)\s+noi\b|"
        # Clitico di ripresa dopo un sintagma anteposto: «chi ti curerà LO sai»,
        # «la tua storia LA racconti». In italiano scritto il clitico sta prima
        # del verbo solo se qualcosa è stato spostato in testa alla frase.
        r"(?<!^)(?<!\bnon )\b(lo|la|li|le|ne)\s+"
        r"(sai|sa|sanno|sappiamo|racconti|racconta|raccontiamo|cura|curano|curiamo|"
        r"fai|fa|fanno|facciamo|vedi|vede|vedono|trovi|trova|troviamo|paghi|paga|"
        r"scegli|sceglie|scegliamo|porti|porta|portiamo|metti|mette|mettiamo|"
        r"togli|toglie|togliamo|leggi|legge|leggiamo|apri|apre|apriamo)\b", re.I)),
    # F10. autoelogio: enfatizzatori e parole che ogni concorrente può
    # scrivere a costo zero. Vedi docs/07, classe C1.
    ("F10 autoelogio", re.compile(
        r"\b(verificabil\w+|garantit\w+|all'avanguardia|professionalità|eccellenza|"
        r"leader|il migliore|la migliore|di altissimo livello|unico nel suo genere|"
        r"assolutamente)\b", re.I)),
    # F11. comparazione implicita con un concorrente non nominato. Oltre al
    # trasferimento spontaneo di tratti, per una struttura sanitaria italiana
    # c'è un profilo normativo. Vedi docs/07, classe C11.
    ("F11 frecciata al concorrente", re.compile(
        r"\b(invece di (scoprir|sapere|dover)|piuttosto che (scoprir|dover|andare)|"
        r"a differenza di (chi|quelli|altri)|molti (altri )?studi|altri studi|"
        r"come fanno (in )?(molti|altri)|troppo onerosi)\b", re.I)),
    # F12. asserzione ovvia sulla sede. Un titolo che informa il lettore del
    # fatto che le stanze dello studio stanno dentro lo studio non aggiunge
    # niente al senso comune: è la classe C2 di docs/07, ed è la prima cosa
    # che è stata contestata in questo progetto. Ci sono ricascato una volta
    # con «gli specialisti, la sala raggi e il laboratorio sono allo stesso
    # indirizzo», quindi adesso c'è una rete.
    ("F12 ovvietà sulla sede", re.compile(
        r"\b(la sala raggi|il laboratorio|la tac|lo scanner|le radiografie|"
        r"gli specialisti|i clinici|l'ambulatorio)\b[^.]{0,70}?\b(è|sono|si fanno|stanno)\b"
        r"[^.]{0,40}?\b(qui|dentro|in sede|allo stesso indirizzo|nella stessa sede|"
        r"nello stesso posto|intern[oaie])\b", re.I)),
    # F13. elenco dei campi: il testo descrive la struttura del dato che sta
    # sotto invece di dare il dato. «Titolo esatto, ateneo, anno accademico»,
    # «Sotto ci sono i percorsi completi», «Ogni titolo porta l'ateneo che lo
    # ha rilasciato e l'anno»: tre travestimenti della stessa frase, che mi è
    # passata tre volte in tre revisioni diverse.
    ("F13 elenco dei campi", re.compile(
        r"\b(ogni|con)\s+(il |la |lo |i |le |gli )?(titolo|voce|scheda|riga|prestazione)\b[^.]{0,45}?"
        r"\b(porta|riporta|indica|ha accanto|è accompagnat)\b|"
        r"\btitolo esatto\b|\bateneo (che lo ha rilasciato|e l'anno)\b|"
        r"\b(sotto|accanto|di seguito) (ci sono|trovi|trovate)\b|"
        r"\bcon (nome e cognome|l'ateneo e l'anno)\b", re.I)),
    # F14. vanto di un obbligo. La formazione continua è dovuta per legge a
    # ogni professionista sanitario: presentarla come un pregio costa zero e
    # vale zero, esattamente come «professionalità».
    ("F14 vanto di un obbligo", re.compile(
        r"\b(continua a (studiar|formar|aggiornar)|formazione continua|"
        r"sempre aggiornat|costante aggiornamento|in continuo aggiornamento|"
        r"corsi di aggiornamento ogni anno)\w*", re.I)),
    # F15. promessa di servizio. Ogni frase che offre una possibilità al
    # lettore è un impegno che lo studio dovrà mantenere al telefono. Vanno
    # tutte ricondotte a una fonte nell'export, e quelle già verificate stanno
    # nell'elenco qui sotto con la pagina che le documenta. Se ne compare una
    # nuova, o ha una fonte e si aggiunge all'elenco, o si toglie dal sito.
    ("F15 promessa di servizio", re.compile(
        r"\b(si può fissare|puoi fissare|puoi chiedere|basta chieder|chiedilo|chiedila|"
        r"puoi parlare|puoi venire|si può richiedere|su richiesta|è possibile prenotare)\w*", re.I)),
]

# Promesse di servizio già ricondotte a una fonte nell'export.
PROMESSE_VERIFICATE = re.compile(
    r"posti auto|"          # posteggio.md: prenotazione tramite segreteria
    r"a domicilio|"         # domicilio.md
    r"in sedazione|"        # protossido.md: sedazione su richiesta, igiene compresa
    r"sedazione cosciente|"
    r"panoramica|"          # preventivo.md: allegare la panoramica
    r"in visita",           # chiedere chiarimenti in visita: non è un servizio
    re.I)

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
    # Le recensioni sono citazioni testuali e il testo legale è vincolato:
    # su nessuno dei due si può intervenire, quindi non vanno giudicati.
    corpo = re.sub(r"<blockquote.*?</blockquote>", " ", corpo, flags=re.S)
    corpo = re.sub(r'<p class="ba-disclaimer".*?</p>', " ", corpo, flags=re.S)
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
                if nome.startswith("F12") and tipo not in ("titolo", "sottotitolo"):
                    continue
                if nome.startswith("F15") and PROMESSE_VERIFICATE.search(t):
                    continue
                # Il clitico di ripresa si giudica solo nei titoli: in un
                # paragrafo «se la scegli» è un normale pronome oggetto, non
                # una dislocazione, e la differenza non si vede da una regex.
                if nome.startswith("F9") and tipo not in ("titolo", "sottotitolo") \
                        and not re.search(r"\bnoi\b", hit.group(0)):
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
        for nome in ("F2 istruzioni", "F4 formula vietata", "F9 dislocazione parlata",
                     "F10 autoelogio", "F11 frecciata al concorrente",
                     "F15 promessa di servizio"):
            if nome.startswith("F15") and PROMESSE_VERIFICATE.search(t):
                continue
            rx = dict(REGOLE)[nome]
            hit = rx.search(t)
            # Nel corpo il clitico oggetto è italiano scritto normale («se la
            # scegli»): lì si giudica solo la forma enfatica con «noi».
            if hit and nome.startswith("F9") and "noi" not in hit.group(0).lower():
                continue
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
