# Design system

Tutto quanto segue è implementato in `site/assets/css/base.css` (token e fondamenta) e
`site/assets/css/components.css` (componenti). I nomi dei token qui riportati sono i nomi reali
delle variabili CSS: il documento e il codice non possono divergere.

---

## 1. I principi

> Uno studio dentistico è un luogo dove le persone hanno paura, e dove quasi tutti
> stanno confrontando due o tre preventivi. Il design deve fare due cose insieme:
> **abbassare l'attivazione emotiva** e **rendere immediatamente leggibile ogni numero**.

Quattro conseguenze operative, che spiegano ogni scelta successiva.

1. **Un blu della fiducia, con un complementare che fa da richiamo.** La letteratura sul
   colore in ambito sanitario e finanziario è concorde nell'associare il blu a competenza,
   affidabilità e calma. Il rischio è che un impianto tutto blu risulti freddo e piatto, così il
   sistema affianca al blu un **ambra caldo**, che sta quasi all'opposto sulla ruota cromatica.
   L'ambra non decora niente: marca solo i punti in cui vogliamo un'azione o uno sguardo.
2. **Distribuzione 60-30-10.** Il 60 per cento della superficie è carta calda, il 30 è blu, il 10
   è ambra. Superata quella soglia il richiamo smette di richiamare, perché l'occhio si abitua.
3. **Il dato ha la stessa dignità del titolo.** Nel sistema tipografico esiste una voce dedicata
   ai numeri (`.stat-n`). «Avanguardia» non è un contenuto, «4.000 impianti» sì.
4. **Show, don't tell.** Dove il sito precedente descriveva un processo a parole, qui c'è un
   diagramma o un'illustrazione. Nessuna pagina è di solo testo, e nessun buco fotografico resta
   un rettangolo grigio.

---

## 2. Marchio

**Nome:** `Piccardo`, con sottotitolo `STUDIO ODONTOIATRICO`.
La ragione sociale completa (*Ambulatorio Dentistico Dr. Piccardo U. S.r.l.*) resta nel footer,
nelle note legali e nei dati strutturati.

**Simbolo.** La croce di San Giorgio, la croce rossa di Genova già presente nel logo storico
dello studio, ricostruita su griglia geometrica: quattro bracci uguali su una matrice 32×32, con
la sagoma di un dente ritagliata in negativo al centro.

```
 ┌──────────────┐   croce  : #C4342E  (rosso Genova)
 │      ██      │   dente  : colore della carta, in negativo
 │   ███░░███   │   griglia: 32 × 32, bracci da 8,8 unità
 │   ███░░███   │
 │      ██      │
 └──────────────┘
```

Funziona per tre ragioni. È **locale**, perché identifica Genova senza doverlo scrivere. È **già
dello studio**, quindi mantiene continuità con quindici anni di insegna. Ed è **geometrico**, per
cui regge alla stessa maniera a 16 pixel e su una vetrina. In più non somiglia a nessun altro
logo dentistico, visto che sono quasi tutti un dente stilizzato azzurro.

Il rosso resta confinato al marchio. Non compare mai su bottoni, campiture o grafici vicino a
immagini cliniche: in odontoiatria il rosso in campo ampio richiama il sangue.

---

## 3. Colore

### 3.1 La struttura

| Ruolo | Quota | Token | Dove |
|---|---|---|---|
| **Base** | 60% | `--paper` `#FAF8F5` | Fondo di quasi tutte le sezioni. È una carta calda, non un bianco: raffredda meno del bianco puro e riduce l'affaticamento in lettura |
| **Primaria** | 30% | `--brand-700` `#134B7A` | Titoli di sezione scure, link, bordi, dati, footer, illustrazioni |
| **Richiamo** | 10% | `--accent-500` `#E4913B` | Bottone primario, parola in corsivo nei titoli, occhielli, prezzi, barra mobile |

### 3.2 La scala completa

| Token | Valore | Uso |
|---|---|---|
| `--ink` | `#0B1A28` | Titoli. Un nero-blu: nel sistema non esiste un grigio neutro |
| `--ink-2` | `#1B2F42` | Testo corrente |
| `--muted` | `#5A6B7A` | Testo secondario e occhielli di paragrafo |
| `--muted-2` | `#74838F` | Didascalie e metadati |
| `--paper` / `--paper-2` / `--paper-3` | `#FAF8F5` `#F3F0EA` `#EAE5DC` | Fondi in tre gradazioni, per dare ritmo alle sezioni |
| `--brand-900` | `#08243C` | Sezioni scure, footer, blocco emotivo, CTA finale |
| `--brand-700` | `#134B7A` | Primaria |
| `--brand-500` | `#2A7CBF` | Accento vivo nelle illustrazioni e nei grafici |
| `--brand-200` / `--brand-100` / `--brand-050` | `#B4D3EC` `#DBEAF7` `#EEF6FC` | Superfici tenui, cornici dei ritratti, fondi delle icone |
| `--accent-500` | `#E4913B` | Riempimento dei richiami |
| `--accent-700` | `#96560F` | Testo ambra su fondo chiaro, dove serve il contrasto |
| `--accent-400` | `#F2AC5E` | Richiami sulle sezioni scure |
| `--red` | `#C4342E` | Solo marchio, più la curva «senza sedazione» nel diagramma dell'ansia |
| `--gold` | `#E0A93B` | Stelle delle recensioni |

### 3.3 Contrasti verificati

Tutte le combinazioni di testo del sistema superano il 4,5:1 richiesto da WCAG 2.2 AA, misurate
con la formula di luminanza relativa WCAG:

| Combinazione | Rapporto |
|---|---|
| `--ink` su `--paper` | 16,6 : 1 |
| `--ink-2` su `--paper` | 12,9 : 1 |
| `--muted` su `--paper` | 5,2 : 1 |
| `--brand-700` su `--paper` | 8,6 : 1 |
| bianco su `--brand-700` | 9,1 : 1 |
| bianco su `--brand-900` | 15,8 : 1 |
| **`--ink` su `--accent-500`** (bottone primario) | **7,1 : 1** |
| `--accent-700` su `--paper` | 5,5 : 1 |

Il bottone primario è ambra con testo blu-nero, invece che bianco su ambra: il bianco su questo
arancio arriverebbe a 2,5:1 e sarebbe illeggibile. La combinazione scelta passa perfino il
livello AAA, e in più è visivamente più distintiva del solito bottone pieno con testo bianco.

### 3.4 Gerarchia dei bottoni

| Livello | Aspetto | Quando |
|---|---|---|
| Primario | Ambra pieno, testo blu-nero | Prenotare, chiamare, inviare. Uno per schermata |
| Secondario | Blu pieno, testo bianco (`.btn--brand`) | Azioni importanti che non sono la principale |
| Terziario | Contorno blu su trasparente (`.btn--ghost`) | Approfondire, navigare |
| Testuale | Freccia animata (`.link-arrow`) | Rimandi dentro le card |

## 4. Tipografia

**Fraunces** (display, variabile) + **Manrope** (testo, variabile). Entrambi **self-hosted** in `site/assets/fonts/` come woff2 con `unicode-range` latin e latin-ext: nessuna richiesta a Google, nessun problema GDPR, nessun rendering bloccante.

- **Fraunces** è una serif a contrasto medio-alto con assi `SOFT` e `WONK`. Il sistema la usa con `SOFT 20` nei titoli (morbida ma seria) e con `SOFT 60 / WONK 1` nel corsivo d'accento. Il suo corsivo è **la voce del brand**: compare una sola volta per titolo, sulla parola che porta il significato, *non senti niente*, *dimostrare*, *differenza*.
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

Tre livelli di ombra soltanto (`--sh-1/2/3`), tutti con una componente blu nel nero (`rgba(11,26,40,…)`), più un'ombra ambra dedicata al bottone primario. Nessuna ombra grigia neutra.

---

## 6. Movimento

Una sola curva per tutto il sistema: `cubic-bezier(.22, 1, .36, 1)`: partenza rapida, arrivo lungo. È la curva che si percepisce come "sicura di sé" senza risultare lenta.

| Comportamento | Durata | Note |
|---|---|---|
| Micro-interazione (hover, focus) | 180 ms | `--t-fast` |
| Transizione standard | 320 ms | `--t` |
| Ingresso allo scroll | 800 ms | `[data-reveal]`, IntersectionObserver, `unobserve` al primo ingresso |
| Scaglionamento di gruppo | 60–90 ms per elemento | `[data-stagger]`, calcolato in JS |
| Conteggio numerico | 1500 ms | easing cubico in uscita |
| Tracciato dei diagrammi | 1600 ms | `stroke-dashoffset` |

Il bottone primario ha un riempimento che sale dal basso (`::after` con `translateY`): un dettaglio piccolo, ma è ciò che distingue un bottone progettato da un rettangolo colorato.

**`prefers-reduced-motion: reduce` disattiva tutto**, reveal, contatori, marquee, tracciati, senza che nulla scompaia. Nessun contenuto dipende dall'animazione per essere leggibile.

---

## 7. Iconografia

**51 icone disegnate per questo progetto** (`build/ui.py`), su griglia 24, tratto 1,6, terminali e giunzioni arrotondate. Nessuna libreria di terze parti: le icone di un brand sanitario devono avere la stessa mano del logo.

Alcune sono specifiche del dominio e non esistono nelle librerie generiche: `impianto` (vite endossea), `mascherina` (allineatore), `corona`, `calma` (piuma: «mano delicata», la parola che ricorre nelle recensioni), `pronto` (tracciato ECG), `accessibile`, `scan`.

---

## 8. Diagrammi

Dieci illustrazioni vettoriali originali, generate da codice e animate all'ingresso in viewport. Sono la traduzione operativa di *show, don't tell*.

| Diagramma | Sostituisce | Cosa mostra |
|---|---|---|
| `impianto` | 3 paragrafi | Quattro fasi: dente mancante → inserimento → osteointegrazione → corona. Con osso trabecolato, gengiva e radici |
| `allineatori` | 2 paragrafi | Un'arcata che si ordina progressivamente, mascherina dopo mascherina |
| `ansia` | l'intera pagina sedazione | **Due curve sovrapposte**: l'ansia con e senza sedazione lungo la seduta. È il pezzo più persuasivo del sito |
| `carie` | 2 paragrafi | Quattro stadi, ciascuno con il costo reale a fianco |
| `prevenzione` |, | Istogramma: 200 € l'anno di igiene contro 1.540 € di impianto |
| `sterilizzazione` | 887 parole | I sei passaggi del protocollo su una linea temporale |
| `protesi` | 2 paragrafi | Scansione → CAD → CAM → prova |
| `chirurgia` | 2 paragrafi | TAC con il nervo evidenziato → anestesia → sutura → controllo |
| `sorriso` | 3 paragrafi | L'ordine corretto: salute → posizione → colore → forma |
| `bimbo` | 3 paragrafi | La prima visita in quattro momenti |

---

## 8-bis. Illustrazioni

Tredici scene vettoriali originali (`build/illustrazioni.py`), disegnate per stare dove una
fotografia manca ancora e dove, in diversi casi, direbbe comunque meno di un disegno: una
sezione, un movimento o una sequenza sono cose che l'obiettivo non inquadra.

Linguaggio comune: campiture piatte su tre valori di blu, **un solo richiamo ambra per scena**,
contorni a 1,8, nessuna ombra e nessun gradiente. Ogni scena entra animata quando raggiunge il
viewport, con elementi che salgono, compaiono o scattano in sequenza scaglionata.

`poltrona` · `maschera` · `laboratorio` · `radiologia` · `sterilizzazione` · `ingresso` ·
`parcheggio` · `bimbi` · `equipe` · `mascherine` · `faccetta` · `video` · `prima-dopo`

Sono usate dentro il componente `media-slot`, che al posto del vecchio rettangolo grigio mostra
l'illustrazione del soggetto e conserva, sotto, la specifica di scatto. La pagina resta piacevole
già prima dello shooting, e nessun buco può passare inosservato: `data-shot` li rende cercabili
tutti con un `grep`.

---

## 8-ter. Come si scrive su questo sito

Regole di redazione applicate a ogni titolo e a ogni paragrafo del sito.

**Un titolo deve portare un'informazione.** «Il laboratorio odontotecnico è dentro» dice al
lettore qualcosa che aveva già capito dal contesto. «Avere l'odontotecnico nella stanza accanto
accorcia i tempi e migliora il risultato» dice perché dovrebbe interessargli. Ogni titolo del
sito supera questa prova.

**Vietata la formula «non è X, è Y».** È una costruzione che sembra profonda e non spiega niente,
e ripetuta due volte in una pagina diventa un tic riconoscibile. Al suo posto: una frase che
dichiara direttamente la cosa, con la spiegazione subito dopo.

**Niente frasi mozze come titolo.** «Scritto prima.» «Nessuna sorpresa. Mai.» «Tre posti auto.
Gratuiti.» Sono formule da manifesto pubblicitario che in un sito medico suonano vuote. I titoli
sono frasi complete, anche lunghe.

**Nessun trattino lungo.** Al suo posto due punti, virgole o punto fermo, scelti in base a cosa
la frase sta facendo davvero.

**Il paragrafo può essere lungo.** La brevità a tutti i costi produce testi che non dicono niente.
Dove c'è qualcosa da spiegare, si spiega: il paziente che sta scegliendo un impianto da
millecinquecento euro legge volentieri sei righe in più.

**Varietà sintattica.** Frasi di lunghezza diversa, subordinate vere, e mai due paragrafi vicini
costruiti allo stesso modo.

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
