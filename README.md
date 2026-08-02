# Piccardo, redesign dello studio odontoiatrico

Ridisegno completo di [dentista-genova-dottpiccardo.it](https://www.dentista-genova-dottpiccardo.it) -
Ambulatorio Dentistico Dr. Piccardo U. S.r.l., Via Maragliano 5, Genova.

Da **62 pagine organizzate per organigramma** a **19 pagine organizzate per intenzione del paziente**,
con un'identità visiva nuova, un design system completo e un sito statico funzionante.

---

## In sintesi

Lo studio possiede il capitale di fiducia più forte della categoria a Genova, **310 recensioni Google**, cinque master universitari di II livello, oltre 4.000 impianti, un tariffario pubblico completo: e il sito
precedente non ne usava quasi nulla. Il redesign non inventa un posizionamento: lo estrae dalle
recensioni dei pazienti e lo rende visibile in cinque secondi.

> **Sai quanto spendi prima di sederti, e non senti niente.**

Tre pilastri, ciascuno con la sua prova pubblicabile: **non fa male** (master in sedazione, ipnosi
clinica, sedazione endovenosa) · **sai quanto spendi** (36 prezzi online, tasso 0, 19 convenzioni) ·
**lo facciamo qui** (TAC 3D e laboratorio odontotecnico interni).

---

## I documenti

| | |
|---|---|
| [`docs/01-audit-ux.md`](docs/01-audit-ux.md) | Audit euristico del sito esistente: inventario di ciò che vale, 24 criticità con severità, cosa tenere e cosa eliminare |
| [`docs/02-strategia-ia-wireframe.md`](docs/02-strategia-ia-wireframe.md) | Segmenti e jobs-to-be-done ricavati dalle recensioni, posizionamento, tono di voce, nuova architettura, 60 redirect, wireframe |
| [`docs/03-photo-brief.md`](docs/03-photo-brief.md) | Verdetto su tutti i 102 asset esistenti, direzione artistica, 15 scatti e 4 video da produrre, protocollo per i prima/dopo |
| [`docs/04-design-system.md`](docs/04-design-system.md) | Marchio, colore, tipografia, movimento, 51 icone, 10 diagrammi, componenti, accessibilità |
| [`docs/05-roadmap-e-misurazione.md`](docs/05-roadmap-e-misurazione.md) | Dati da confermare, cosa collegare prima di pubblicare, piano di misurazione, priorità successive |
| [`docs/06-metodo-editoriale.md`](docs/06-metodo-editoriale.md) | Chi legge e in che stato, gli otto difetti di scrittura da evitare, la griglia di valutazione, le decisioni prese sui titoli con le alternative scartate |
| [`docs/07-tassonomia-dei-difetti.md`](docs/07-tassonomia-dei-difetti.md) | Le frasi contestate in revisione classificate una per una: nome accademico del difetto, meccanismo, fonti, e la procedura per individuarlo prima che finisca in pagina |

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
`FAQPage`, moduli con validazione, 10 diagrammi vettoriali animati, 51 icone originali,
dati strutturati `Dentist` + `Person` + `BreadcrumbList`, sitemap, robots, 60 redirect 301.

**Cosa manca ed è dichiarato a schermo:** 22 segnaposto media, ciascuno con la specifica di scatto
(`data-shot`), più i dati legali elencati in `docs/05`.

---

## Come si usa

```bash
python3 build/make.py              # genera site/
python3 build/check.py             # link, asset, alt, heading, meta

python3 -m http.server 8899 --directory site   # anteprima locale, serve ai due controlli sotto

python3 build/check_contrasto.py   # contrasto WCAG misurato sul rendering reale
python3 build/check_copy.py        # controllo editoriale (docs/06)
python3 build/test_interazioni.py  # 71 test funzionali (richiede Playwright)
python3 build/estrai_copy.py       # estratto dei blocchi redazionali
python3 build/estrai_tutto.py      # estratto integrale pagina per pagina
python3 build/inventario.py        # le 511 stringhe uniche del sito, da leggere tutte
```

I quattro controlli vanno eseguiti tutti prima di ogni consegna. `check_contrasto.py` e
`test_interazioni.py` hanno bisogno del server locale già avviato.

Per pubblicare basta caricare il contenuto di `site/` su un hosting statico o Apache.
Non serve Node, non serve un CMS, non serve un database.

### Anteprima su GitHub Pages

Il sito vive in `site/`, non nella radice del repository: senza configurazione GitHub Pages
mostrerebbe il `README.md` al posto della homepage. Sono previste due strade, entrambe già pronte.

**Consigliata: pubblicazione automatica.**
`Settings → Pages → Build and deployment → Source: GitHub Actions`.
Il workflow [`.github/workflows/pages.yml`](.github/workflows/pages.yml) rigenera il sito dai
sorgenti, esegue il controllo qualità e pubblica `site/` sulla radice del dominio Pages.
Da quel momento ogni push aggiorna il sito da solo.
Indirizzo risultante: `https://<utente>.github.io/<repo>/`

**Alternativa: pubblicazione dal branch.**
`Settings → Pages → Source: Deploy from a branch`, branch `claude/dental-studio-redesign-acgd4w`,
cartella `/ (root)`. In questo caso l'`index.html` nella radice reindirizza automaticamente
a `site/index.html`: il sito si apre lo stesso, con un indirizzo un livello più profondo.

Tutti i percorsi interni sono relativi, quindi il sito funziona identico sia sulla radice di un
dominio sia in una sottocartella. Il file `.nojekyll` disattiva l'elaborazione Jekyll di GitHub.

Per modificare un prezzo, un orario o un contenuto: `build/content.py` e `build/trattamenti.py`,
poi `make.py`. Il dato si aggiorna in tutte le pagine in cui compare.

---

## Struttura

```
docs/                    i sette documenti di progetto
build/
  content.py             dati d'impresa, tariffario, recensioni, team
  trattamenti.py         contenuti delle 10 pagine trattamento
  ui.py                  icone SVG e diagrammi animati
  shell.py               head, header, footer, componenti condivisi
  componenti.py          blocchi riusabili (prima/dopo, recensioni, mappa, form)
  pagine_home.py         homepage
  pagine_interne.py      tutte le altre pagine
  make.py                generatore
  check.py               link, asset, alt, heading, meta
  check_contrasto.py     contrasto WCAG misurato sul rendering
  check_copy.py          controllo editoriale
  estrai_copy.py         estratto dei blocchi redazionali
  estrai_tutto.py        estratto integrale, pagina per pagina
  inventario.py          le stringhe uniche del sito, deduplicate
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
