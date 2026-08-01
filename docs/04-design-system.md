# Design system — Piccardo

Tutto quanto segue è implementato in `site/assets/css/base.css` (token e fondamenta) e
`site/assets/css/components.css` (componenti). I nomi dei token qui riportati sono i nomi reali
delle variabili CSS: il documento e il codice non possono divergere.

---

## 1. Il principio

> Uno studio dentistico è un luogo dove le persone hanno paura.
> Il design non deve essere allegro: deve essere **calmo, preciso e chiaro sui numeri**.

Tre conseguenze operative, che spiegano ogni scelta successiva:

1. **Niente ciano.** Il celeste dentale è la scelta di default della categoria e nel contesto medico è associato al freddo clinico. Il sistema è costruito su un **verde profondo** e su una **carta calda**: due colori che abbassano l'attivazione emotiva invece di alzarla.
2. **Ogni affermazione è un numero.** Nel sistema tipografico esiste una voce dedicata al dato (`.stat-n`) che ha la stessa dignità di un titolo. «Avanguardia» non è un contenuto; «4.000 impianti» sì.
3. **Show, don't tell.** Dove il sito precedente descriveva un processo a parole, qui c'è un diagramma vettoriale animato. Nessuna pagina è di solo testo.

---

## 2. Marchio

**Nome:** `Piccardo` · sottotitolo `STUDIO ODONTOIATRICO`.
La ragione sociale completa (*Ambulatorio Dentistico Dr. Piccardo U. S.r.l.*) resta nel footer, nelle note legali e nei dati strutturati.

**Simbolo.** La croce di San Giorgio — la croce rossa di Genova, già presente nel logo storico dello studio — ricostruita su griglia geometrica: quattro bracci uguali su una matrice 32×32. Al centro, in negativo, la sagoma di un dente.

```
 ┌──────────────┐   croce  : #C4342E  (rosso Genova)
 │      ██      │   dente  : colore della carta, in negativo
 │   ███░░███   │   griglia: 32 × 32, bracci da 8,8 unità
 │   ███░░███   │
 │      ██      │
 └──────────────┘
```

Perché funziona: è **locale** (identifica Genova senza scriverlo), è **già dello studio** (continuità con il logo esistente), è **geometrico** (regge a 16 px come a 3 metri) e non assomiglia a nessun altro logo dentistico — che sono quasi tutti un dente stilizzato azzurro.

Il rosso è riservato **al solo marchio**. Non compare mai su bottoni, sfondi o grafici vicino a immagini cliniche: in un contesto odontoiatrico il rosso in campo ampio richiama il sangue.

---

## 3. Colore

| Token | Valore | Uso |
|---|---|---|
| `--ink` | `#0A1714` | Titoli. È un **nero-verde**, non un grigio: nel sistema non esiste un neutro puro |
| `--ink-2` | `#1D302B` | Testo corrente |
| `--muted` | `#5C6C67` | Testo secondario, lead |
| `--muted-2` | `#86928D` | Didascalie, metadati |
| `--paper` | `#FBFAF7` | Fondo principale, carta calda |
| `--paper-2` | `#F4F1EB` | Sezioni alternate |
| `--paper-3` | `#EDE8DF` | Superfici piene, osso nei diagrammi |
| `--line` / `--line-soft` | `#DFDAD1` / `#EBE7E0` | Bordi |
| **`--green-700`** | **`#114C41`** | **Primaria**: bottoni, link, dati |
| `--green-900` | `#08251F` | Sezioni scure, footer, CTA finale |
| `--green-500` | `#1F8069` | Accento vivo, hover, grafici |
| `--green-100/200` | `#E3EFE9` / `#C9E1D7` | Superfici tenui, icone su fondo |
| `--red` | `#C4342E` | **Solo marchio** e curva «senza sedazione» |
| `--brass` | `#A87A33` | Trattamenti ad alto valore (implantologia, estetica) |
| `--gold` | `#E0A93B` | Stelle delle recensioni |

**Contrasto.** Le combinazioni di testo del sistema superano il rapporto 4,5:1 richiesto da WCAG 2.2 AA:
`--ink` su `--paper` ≈ 16,8:1 · `--muted` su `--paper` ≈ 6,3:1 · bianco su `--green-700` ≈ 9,1:1 · `#A5BDB5` su `--green-900` ≈ 7,4:1.

---

## 4. Tipografia

**Fraunces** (display, variabile) + **Manrope** (testo, variabile). Entrambi **self-hosted** in `site/assets/fonts/` come woff2 con `unicode-range` latin e latin-ext: nessuna richiesta a Google, nessun problema GDPR, nessun rendering bloccante.

- **Fraunces** è una serif a contrasto medio-alto con assi `SOFT` e `WONK`. Il sistema la usa con `SOFT 20` nei titoli (morbida ma seria) e con `SOFT 60 / WONK 1` nel corsivo d'accento. Il suo corsivo è **la voce del brand**: compare una sola volta per titolo, sulla parola che porta il significato — *non senti niente*, *dimostrare*, *differenza*.
- **Manrope** è una sans geometrica con terminali leggermente aperti: chiara come Inter ma più calda, e meno vista.

| Ruolo | Token | Scala fluida |
|---|---|---|
| Display (hero) | `.display` | 2,9 → 6,5 rem |
| H1 | `--fs-h1` | 2,4 → 4,4 rem |
| H2 | `--fs-h2` | 1,95 → 3,2 rem |
| Lead | `--fs-lead` | 1,08 → 1,42 rem |
| Corpo | `--fs-body` | 1,0625 rem, interlinea 1,62 |
| Occhiello | `.eyebrow` | 0,75 rem, tracking 0,16 em, maiuscolo, preceduto da un filetto |
| Dato | `.stat-n` | 2,6 → 4,2 rem, Fraunces `opsz 144`, cifre lining |

`text-wrap: balance` sui titoli e `pretty` sui paragrafi: nessuna riga orfana, nessuna vedova.

---

## 5. Spazio, forma, ombra

Ritmo su base 4 px. Le sezioni respirano con `--sp-section` (4,5 → 9 rem) e il contenuto è contenuto in `--maxw` 78 rem, con la colonna di testo limitata a **40 rem** (≈ 68 caratteri: l'intervallo di leggibilità ottimale).

Raggi: `6 / 10 / 16 / 24 / 34 px` più `999px` per le pillole. Le forme sono **morbide ma non gommose**: le card a 24 px leggono come oggetti tattili, i bottoni a pillola invitano al tocco. È una scelta di riduzione dell'ansia: gli angoli vivi in ambito medico leggono come strumenti.

Tre livelli di ombra soltanto (`--sh-1/2/3`), tutti con una componente verde nel nero (`rgba(10,23,20,…)`): nessuna ombra grigia neutra.

---

## 6. Movimento

Una sola curva per tutto il sistema: `cubic-bezier(.22, 1, .36, 1)` — partenza rapida, arrivo lungo. È la curva che si percepisce come "sicura di sé" senza risultare lenta.

| Comportamento | Durata | Note |
|---|---|---|
| Micro-interazione (hover, focus) | 180 ms | `--t-fast` |
| Transizione standard | 320 ms | `--t` |
| Ingresso allo scroll | 800 ms | `[data-reveal]`, IntersectionObserver, `unobserve` al primo ingresso |
| Scaglionamento di gruppo | 60–90 ms per elemento | `[data-stagger]`, calcolato in JS |
| Conteggio numerico | 1500 ms | easing cubico in uscita |
| Tracciato dei diagrammi | 1600 ms | `stroke-dashoffset` |

Il bottone primario ha un riempimento che sale dal basso (`::after` con `translateY`): un dettaglio piccolo, ma è ciò che distingue un bottone progettato da un rettangolo colorato.

**`prefers-reduced-motion: reduce` disattiva tutto** — reveal, contatori, marquee, tracciati — senza che nulla scompaia. Nessun contenuto dipende dall'animazione per essere leggibile.

---

## 7. Iconografia

**42 icone disegnate per questo progetto** (`build/ui.py`), su griglia 24, tratto 1,6, terminali e giunzioni arrotondate. Nessuna libreria di terze parti: le icone di un brand sanitario devono avere la stessa mano del logo.

Alcune sono specifiche del dominio e non esistono nelle librerie generiche: `impianto` (vite endossea), `mascherina` (allineatore), `corona`, `calma` (piuma — «mano delicata», la parola che ricorre nelle recensioni), `pronto` (tracciato ECG), `accessibile`, `scan`.

---

## 8. Diagrammi

Dieci illustrazioni vettoriali originali, generate da codice e animate all'ingresso in viewport. Sono la traduzione operativa di *show, don't tell*.

| Diagramma | Sostituisce | Cosa mostra |
|---|---|---|
| `impianto` | 3 paragrafi | Quattro fasi: dente mancante → inserimento → osteointegrazione → corona. Con osso trabecolato, gengiva e radici |
| `allineatori` | 2 paragrafi | Un'arcata che si ordina progressivamente, mascherina dopo mascherina |
| `ansia` | l'intera pagina sedazione | **Due curve sovrapposte**: l'ansia con e senza sedazione lungo la seduta. È il pezzo più persuasivo del sito |
| `carie` | 2 paragrafi | Quattro stadi, ciascuno con il costo reale a fianco |
| `prevenzione` | — | Istogramma: 200 € l'anno di igiene contro 1.540 € di impianto |
| `sterilizzazione` | 887 parole | I sei passaggi del protocollo su una linea temporale |
| `protesi` | 2 paragrafi | Scansione → CAD → CAM → prova |
| `chirurgia` | 2 paragrafi | TAC con il nervo evidenziato → anestesia → sutura → controllo |
| `sorriso` | 3 paragrafi | L'ordine corretto: salute → posizione → colore → forma |
| `bimbo` | 3 paragrafi | La prima visita in quattro momenti |

---

## 9. Componenti principali

`btn` (4 varianti) · `pill` · `stars` · `header` con mega-menu · `drawer` mobile · `mobile-bar` sticky a 3 azioni · `hero` con `portrait-card` e `price-card` · `stat-bar` con contatori · `card` / `tcard` / `ccard` · **`media-slot`** · `intent` (tab accessibili) · **`ba`** (slider prima/dopo) · `rev` (recensione) · `member` + `person-drawer` · `tariff-table` filtrabile · **`calc`** (calcolatore rata) · `marquee` · `acc` (FAQ) · `steps` · `fit` (sì/no) · `keyfacts` · `anchor-nav` con scrollspy · `field` / `file-drop` / `chip-group` · `cta-final` · `footer`.

### Il componente `media-slot`

È la risposta progettuale al problema fotografico. Dove manca un'immagine buona **non si mette una stock photo**: si mette un segnaposto disegnato che dichiara a schermo il tipo di media, il soggetto e la nota di scatto.

```html
<figure class="media-slot" data-kind="Video · 60″" data-shot="…" style="--ar:4/3">
```

L'attributo `data-shot` rende ogni buco **cercabile nel codice** (`grep -r data-shot site/`) e il controllo automatico ne conta 22 in 10 pagine. È impossibile pubblicare dimenticandone uno.

---

## 10. Accessibilità

- Contrasto **WCAG 2.2 AA** su tutte le combinazioni di testo.
- `:focus-visible` visibile ovunque: contorno verde da 2,5 px con offset di 3 px.
- Tutti i pattern interattivi sono conformi alle WAI-ARIA Authoring Practices: tab con frecce, `aria-selected` e roving tabindex; accordion con `aria-expanded`; drawer con `role="dialog"`, `aria-modal`, chiusura con Escape e ritorno del focus all'elemento che l'ha aperto; slider prima/dopo con `role="slider"`, `aria-valuenow` e controllo da tastiera.
- Skip link, un solo `h1` per pagina, gerarchia dei titoli senza salti.
- `alt` descrittivi e non keyword-stuffed. Le icone decorative sono `aria-hidden`.
- Target di tocco ≥ 44 px sulla barra mobile.
- Zero overflow orizzontale a 320 px (verificato dai test).

## 11. Prestazioni

CSS totale ≈ 42 KB non compresso · JS ≈ 13 KB, vanilla, `defer`, nessuna dipendenza · font self-hosted con `preload` e `unicode-range` · immagini WebP con `width`/`height` dichiarati (nessun layout shift) e `loading="lazy"` sotto la piega · `fetchpriority="high"` sul ritratto dell'hero · animazioni solo su `transform` e `opacity`.
