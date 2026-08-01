# Piccardo — redesign dello studio odontoiatrico

Ridisegno completo di [dentista-genova-dottpiccardo.it](https://www.dentista-genova-dottpiccardo.it) —
Ambulatorio Dentistico Dr. Piccardo U. S.r.l., Via Maragliano 5, Genova.

Da **62 pagine organizzate per organigramma** a **19 pagine organizzate per intenzione del paziente**,
con un'identità visiva nuova, un design system completo e un sito statico funzionante.

---

## In sintesi

Lo studio possiede il capitale di fiducia più forte della categoria a Genova — **5,0 su 310 recensioni
Google**, sei master universitari, oltre 4.000 impianti, un tariffario pubblico completo — e il sito
precedente non ne usava quasi nulla. Il redesign non inventa un posizionamento: lo estrae dalle
recensioni dei pazienti e lo rende visibile in cinque secondi.

> **Il dentista a Genova dove sai quanto spendi e non senti niente.**

Tre pilastri, ciascuno con la sua prova pubblicabile: **non fa male** (master in sedazione, ipnosi
clinica, sedazione endovenosa) · **sai quanto spendi** (37 prezzi online, tasso 0, 19 convenzioni) ·
**lo facciamo qui** (TAC 3D e laboratorio odontotecnico interni).

---

## I documenti

| | |
|---|---|
| [`docs/01-audit-ux.md`](docs/01-audit-ux.md) | Audit euristico del sito esistente: inventario di ciò che vale, 24 criticità con severità, cosa tenere e cosa eliminare |
| [`docs/02-strategia-ia-wireframe.md`](docs/02-strategia-ia-wireframe.md) | Segmenti e jobs-to-be-done ricavati dalle recensioni, posizionamento, tono di voce, nuova architettura, 60 redirect, wireframe |
| [`docs/03-photo-brief.md`](docs/03-photo-brief.md) | Verdetto su tutti i 102 asset esistenti, direzione artistica, 15 scatti e 4 video da produrre, protocollo per i prima/dopo |
| [`docs/04-design-system.md`](docs/04-design-system.md) | Marchio, colore, tipografia, movimento, 42 icone, 10 diagrammi, componenti, accessibilità |
| [`docs/05-roadmap-e-misurazione.md`](docs/05-roadmap-e-misurazione.md) | Dati da confermare, cosa collegare prima di pubblicare, piano di misurazione, priorità successive |

---

## Il sito

19 pagine HTML statiche, nessuna dipendenza runtime.

```
index · trattamenti (hub) · 10 pagine trattamento · studio · team
prezzi · recensioni · contatti · note-legali · 404
```

**Cosa c'è dentro:** mega-menu accessibile, drawer mobile, barra sticky a tre azioni, selettore per
intenzione, slider prima/dopo trascinabile e navigabile da tastiera, contatori animati, tariffario
filtrabile e ricercabile, calcolatore di rata, pannello laterale con i CV, scrollspy, FAQ marcate
`FAQPage`, moduli con validazione, 10 diagrammi vettoriali animati, 42 icone originali,
dati strutturati `Dentist` + `Person` + `BreadcrumbList`, sitemap, robots, 60 redirect 301.

**Cosa manca ed è dichiarato a schermo:** 22 segnaposto media, ciascuno con la specifica di scatto
(`data-shot`), più i dati legali elencati in `docs/05`.

---

## Come si usa

```bash
python3 build/make.py              # genera site/
python3 build/check.py             # link, asset, alt, heading, meta
python3 build/test_interazioni.py  # 67 test funzionali (richiede Playwright)

python3 -m http.server 8899 --directory site   # anteprima locale
```

Per pubblicare basta caricare il contenuto di `site/` su un hosting statico o Apache.
Non serve Node, non serve un CMS, non serve un database.

Per modificare un prezzo, un orario o un contenuto: `build/content.py` e `build/trattamenti.py`,
poi `make.py`. Il dato si aggiorna in tutte le pagine in cui compare.

---

## Struttura

```
docs/                    i cinque documenti di progetto
build/
  content.py             dati d'impresa, tariffario, recensioni, team
  trattamenti.py         contenuti delle 10 pagine trattamento
  ui.py                  icone SVG e diagrammi animati
  shell.py               head, header, footer, componenti condivisi
  componenti.py          blocchi riusabili (prima/dopo, recensioni, mappa, form)
  pagine_home.py         homepage
  pagine_interne.py      tutte le altre pagine
  make.py                generatore
  check.py               controllo qualità
  test_interazioni.py    test funzionali
  prep_images.py         lavorazione delle foto ereditate dal vecchio sito
  icone.py               favicon e immagine di condivisione
site/                    il sito generato
```

---

## Note sui contenuti

Tutti i dati clinici, i prezzi, i curricula e le recensioni provengono dall'export del sito esistente
e dalla scheda Google dello studio. **Nulla è stato inventato**: dove un'informazione mancava è
segnalata come da confermare in `docs/05-roadmap-e-misurazione.md`.

I casi clinici pubblicati sono due, recuperati dall'archivio esistente, con la nota di conformità
prevista dall'art. 9 della L. 24/2017 e dalle linee guida FNOMCeO.
