# Audit UX: dentista-genova-dottpiccardo.it

**Oggetto:** Ambulatorio Dentistico Dr. Piccardo U. SRL. Via Maragliano 5, Genova
**Base dell'analisi:** export completo del sito (62 pagine, 102 asset immagine, 36 video, 5 mappe) + 310 recensioni Google.
**Data:** agosto 2026

---

## 0. Sintesi in una pagina

Il sito attuale non è un sito debole: è un **archivio ricchissimo con un'interfaccia del 2008**. Il problema non è la mancanza di contenuti, ce ne sono più che nel 90% degli studi odontoiatrici italiani, è che **nessuno di quei contenuti è organizzato per far compiere un'azione a una persona spaventata che sta scegliendo un dentista**.

Tre numeri che riassumono tutto:

| | |
|---|---|
| **62** | pagine pubblicate |
| **1** | call-to-action reale e ripetuta (un numero di telefono, in testo) |
| **0** | pagine che rispondono alla domanda che il paziente si fa davvero: *"mi farà male? quanto mi costa? di chi mi sto fidando?"* |

E soprattutto: lo studio possiede **il più forte capitale di fiducia della categoria a Genova**, 5,0/5 su 310 recensioni, 4,9 su 200+ Facebook, e **non lo usa**. Nella homepage è un'immagine JPG di un badge, larga 345 px, senza una sola parola di paziente citata.

> **La tesi del redesign:** non serve inventare nulla. Serve prendere ciò che lo studio è già, indolore, trasparente sui prezzi, tecnologicamente avanti, tutto sotto lo stesso tetto, e renderlo *visibile in 5 secondi* invece che *deducibile in 40 minuti di lettura*.

---

## 1. Inventario di ciò che esiste (e che vale)

Prima di criticare: questo è l'attivo. È molto.

### 1.1 Asset di credibilità clinica

| Elemento | Dettaglio | Valore |
|---|---|---|
| Direttore Sanitario | Dott. Uberto Piccardo, laurea 1997, **6 master universitari di II livello** (Implantoprotesi GE, Sedazione PD, Chirurgia Orale PI, Management Sanitario LUM, Implantologia Digitale PD) | ★★★★★ |
| Casistica implantare | **oltre 4.000 impianti** osteointegrati dal 1999, successo dichiarato **99,8%** | ★★★★★ |
| Pubblicazioni | 2 pubblicazioni Piccardo (Implant Journal 2004, Academy of Osseointegration 2004) + **4 pubblicazioni peer-reviewed** del Dott. De Giovanni (J Clin Med, J Pers Med, Materials, J Prosthodont Res) | ★★★★★ |
| Team | 8 clinici specializzati + segreteria + assistenti. Ortodonzista **specialista** (70/70 Milano) + perfezionamento Invisalign | ★★★★★ |
| Sedazione | Master Padova + sedazione endovenosa diretta + protossido + **diploma di Ipnologo CIICS** | ★★★★★ unico |
| Autorizzazione | Presidio Sanitario, Autorizzazione Comune di Genova 830/2017 | ★★★★ |

### 1.2 Asset di struttura

300 mq al piano terra con accesso diretto dalla strada · 3 poltrone operative · **TAC Cone Beam 3D + ortopantomografo + teleradiografo digitali** (−80% dose radiante) · sala sterilizzazione separata con 2 autoclavi classe B, protocolli ISO 9001, pareti certificate HACCP UNI 11021-2002 · **laboratorio odontotecnico interno** iscritto al Ministero della Salute, CAD-CAM zirconia · barriere architettoniche eliminate (D.M. 236/89), bagno disabili con fasciatoio · area gioco bimbi · **UPS con 3 ore di autonomia** sulle 3 zone operative · **DAE + carrello emergenze + 14 farmaci** e personale formato BLSD con esercitazione mensile · **3 posti auto gratuiti** prenotabili.

### 1.3 Asset commerciali

- **Tariffario pubblico completo** (37 voci con prezzo). Rarissimo nel settore. È un differenziante enorme, oggi sepolto in una pagina di terzo livello.
- Finanziamento **tasso 0 fino a 5.000 €**, tasso agevolato oltre.
- **Invisalign a 125 €/mese** per 36 mesi.
- **20 convenzioni** (FASI, FASDAC, FASIE, FISDE, FASCHIM, CASPIE, Pronto Care, CRAL RINA…).
- Prenotazione online già attiva via MioDottore.
- WhatsApp attivo (+39 347 426 8916).
- Apertura **lun–sab 8:00–20:30**: orario che nessun concorrente regge.
- Servizio a domicilio.

### 1.4 Asset sociali

**5,0 / 5 su 310 recensioni Google.** Su un campione di 310 recensioni, un 5,0 pieno è statisticamente notevole. Temi ricorrenti etichettati da Google: *avanguardia* (18), *ambiente* (13), *prezzi* (13), *competenza* (12), *cordiale* (9), *pulizia* (7), *igiene* (7), *onesto* (6), *invisalign* (5).

Canali social attivi: YouTube (canale con ~36 video, incluse **interviste ai clinici**), Instagram, Facebook, LinkedIn, X.

---

## 2. Audit euristico

Metodo: 10 euristiche di Nielsen + criteri di conversione (Fogg Behavior Model: motivazione × abilità × trigger) + E-E-A-T di Google + WCAG 2.2 AA.
**Severità:** ⬤ critico (blocca la conversione) · ◐ alto · ○ medio.

### 2.1 Architettura dell'informazione

**⬤ Frammentazione patologica.** 62 pagine per uno studio con 3 poltrone. Esistono pagine autonome per: *la sala d'attesa*, *gli uffici e la zona spogliatoi*, *il bagno per disabili*, *il posteggio auto*, *la sala macchine e l'UPS*, *il gruppo di continuità*. Ogni "stanza" è una pagina con 8 immagini. Questa è architettura fatta per il crawler del 2010, non per una persona.
→ *Effetto:* il paziente che cerca "quanto costa un impianto" attraversa 4 livelli di navigazione. Il costo cognitivo (Hick-Hyman) è fuori scala.

**⬤ Nessuna gerarchia di valore.** *Implantologia* (trattamento da 770–2.500 €) e *Bagno disabili* hanno esattamente lo stesso peso nella navigazione. Il menu non distingue ciò che genera fatturato da ciò che è arredamento informativo.

**◐ Duplicazioni.** `preventivo.html` e `richiedi-un-preventivo-on-line.html` sono la stessa pagina (538 parole identiche). `igienista.html` / `igienista2.html`. `caricoimmediato.html` / `caricoimmediato2.html`. `contattaci.html` / `contatti.html`. `tariffe.html` / `tariffario.html`. `sedazione.html` / `protossido.html`. → cannibalizzazione SEO e disorientamento.

**◐ Etichette burocratiche.** "Ambulatorio", "Presidio Sanitario di Assistenza Specialistica Odontoiatrica", "Zone operative", "Direzione Sanitaria". È il lessico dell'ASL, non quello del paziente. Nessuno cerca "zone operative".

**○ Pagine orfane.** `policy.html` (9 parole), `contenziosi-e-risarcimenti.html` (103), `polizza-assicurativa-rc-professionale.html` (57) sono pagine vuote indicizzate.

### 2.2 Conversione

**⬤ Il percorso di prenotazione non esiste come percorso.** Ci sono tre modi di contattare (telefono, WhatsApp, form) rappresentati da **tre icone JPG da 57–90 px**, non etichettate, ripetute in ogni pagina senza gerarchia. Nessuna delle tre spiega *cosa succede dopo*. Il modello di Fogg è violato su tutti e tre gli assi: motivazione bassa (nessuna promessa), abilità bassa (non si capisce dove cliccare), trigger assente (nessun bottone).

**⬤ Zero attrito ridotto sull'ansia.** Il paziente odontofobico, che le recensioni dimostrano essere **il segmento emotivamente più forte dello studio**, non trova in homepage una sola parola su dolore, paura o sedazione. La pagina `protossido.html` che risolve il problema è al terzo livello, sotto "LO STUDIO".

**⬤ Il prezzo è un'occasione sprecata.** Il tariffario pubblico è l'arma competitiva più affilata che questo studio possiede, le recensioni parlano di *prezzi* 13 volte e di *onestà* 6 volte, ed è presentato come un **elenco di testo non formattato di 37 righe**, senza contesto, senza "cosa è incluso", senza finanziamento affiancato, senza confronto. Un prezzo senza contesto è solo un numero grande.

**◐ Nessuna prova sociale utilizzabile.** 310 recensioni a 5,0 ridotte a due immagini-badge da 345×146 px. Nessuna citazione, nessun nome, nessun caso. La prova sociale (Cialdini) funziona per **specificità**: "310 recensioni" convince meno di *"58 primavere e prima estrazione del dente del giudizio: non ho sentito niente"*.

**◐ Nessuna scala di impegno.** L'unica offerta è "prima visita 110 €" o "chiamaci". Manca il gradino a basso attrito (preventivo online gratuito) che è **già un servizio dello studio** ma non è posizionato come porta d'ingresso.

**○ Form legacy.** Campi obbligatori tra cui "ripeti EMAIL", allegato **max 100 KB** (una panoramica dentale ne pesa 2–8 MB: il campo è di fatto inutilizzabile), informativa privacy citata come **D.lgs. 196/2003**: superato dal GDPR dal 2018.

### 2.3 Contenuto e copy

**◐ Scritto dal medico, per il medico.** «*L'implantologia è quella branca dell'odontoiatria che si avvale dell'ausilio degli impianti dentali endoossei osteointegrati*». Il paziente ha chiesto: *"mi rimetteranno il dente?"*.

**◐ Il contenuto forte è nascosto sotto quello debole.** La pagina implantologia dedica **due paragrafi alla mancata osteointegrazione e al fallimento dell'impianto** prima ancora di aver detto cosa si ottiene. È onestà, che è un valore dello studio, ma è ordinata al contrario: la trasparenza sui rischi convince *dopo* che il beneficio è chiaro, non prima.

**◐ Keyword stuffing visibile.** Il footer di ogni pagina contiene un paragrafo di ~1.200 caratteri con la frase "dentisti genova / implantologia / protesi" ripetuta **tre volte identica**. La homepage chiude con un blocco di **~90 keyword** in chiaro ("dentista alito cattivo Genova", "dentista bravissimo a Genova"). Nel 2026 questo è un segnale di spam per Google e un segnale di dilettantismo per l'utente.

**○ Refusi in pagina.** "oggiornate", "coscente", "sucessivo", "compiuter", "prorocolli", "tafiffe", "cute dentistiche". Su un sito medico erodono la percezione di precisione: che è esattamente ciò che le recensioni lodano ("maniacale").

### 2.4 Fiducia (E-E-A-T)

Paradosso centrale: **lo studio ha tutti gli ingredienti dell'autorevolezza e nessuna delle sue forme.**

| Ingrediente posseduto | Come è presentato oggi |
|---|---|
| 6 master universitari | elenco puntato in testo, in una pagina di CV |
| 4.000 impianti / 99,8% | una riga a metà homepage |
| 4 pubblicazioni indicizzate PubMed | in fondo a un CV di terzo livello |
| Diplomi e attestati | 12 foto di **pergamene fotografate storte** |
| Foto del team | **ottime**, ma usate come miniature da 400 px |

I diplomi fotografati sono un anti-pattern: comunicano "provo a convincerti" invece di "sono". Le stesse informazioni, tipografate come dati, comunicano autorità.

### 2.5 Design visivo

**⬤ Nessun sistema.** Non esiste una scala tipografica, una griglia, una palette. I colori compaiono per accidente (il rosso del logo, il ciano dei link di default, il giallo-arancio dei banner "TASSO ZERO" in stile clip-art anni '90, il fucsia sottolineato di "ORTODONZIA INVISIBILE").

**⬤ Testo puro dove serve dimostrazione.** Pagine come `sterilizzazione.html` (887 parole) o `emergenze.html` (508) descrivono **a parole** protocolli che sono per natura visivi e sequenziali. È esattamente il contrario di *show, don't tell*: il protocollo di sterilizzazione in 6 passaggi è un diagramma, non un paragrafo.

**◐ Qualità fotografica disomogenea.** Convivono due mondi: una **serie di 14 ritratti B/N in alta chiave, professionali e coerenti** (ottimi) e un archivio di **snapshot amatoriali di stanze**, sottoesposti, con prospettive storte, montati in collage 2×2 dentro un'unica immagine. Vedi `docs/03-photo-brief.md`.

**◐ Elementi visivi datati.** Clip-art "FINANZIAMENTI TASSO ZERO" con effetto bevel, l'omino 3D del "%" nella pagina convenzioni, banner "Il Tuo Dentista Costa Troppo? Risparmia fino al 70%" con banconote e salvadanaio: comunicano *discount*, mentre il posizionamento reale è *qualità a prezzo onesto*. Sono in conflitto diretto con il resto.

### 2.6 Mobile, performance, accessibilità

**⬤ Immagini-collage.** Molte "immagini" sono in realtà griglie 2×2 di foto diverse incollate in un unico file. Su mobile diventano quattro francobolli illeggibili. Sono anche impossibili da rendere responsive, da ritagliare e da descrivere in `alt`.

**◐ Testo dentro le immagini.** "PRIMA / DOPO", "CONVENZIONI per SOCI", "FINANZIAMENTI TASSO ZERO", il tariffario stesso: testo rasterizzato, non selezionabile, non traducibile, non leggibile da screen reader, non indicizzabile.

**◐ `alt` scritti per Google, non per le persone.** `alt="dentista genova"`, `alt="Il dentista migliore a Genova"`. Uno screen reader legge una keyword al posto di una descrizione.

**◐ Video in autoplay+loop.** 36 embed YouTube con `autoplay=1;loop=1`. Consumo di banda, layout shift, e su alcune pagine più di un video parte insieme.

**○ Contrasto.** Testo grigio su fondo chiaro e link non sottolineati in più punti: sotto il 4,5:1 richiesto da WCAG AA.

---

## 3. Il divario, in una frase

> Lo studio Piccardo **è** uno studio di alto livello che costa il giusto e non fa male.
> Il sito **dice** di essere un ambulatorio autorizzato con molte stanze.

Tutto il redesign nasce da qui.

---

## 4. Cosa tenere (assolutamente)

1. **La trasparenza sui prezzi.** È l'asset differenziante n.1. Va amplificata, non ridotta.
2. **La profondità clinica dei contenuti.** Va riscritta e ristrutturata, non buttata: è ciò che rende il sito autorevole per Google e rassicurante per il paziente informato.
3. **I 14 ritratti B/N.** Sono di livello editoriale e definiscono da soli il linguaggio visivo del nuovo brand.
4. **L'onestà sui rischi** (mancata osteointegrazione, percentuali di successo reali 95%/99%). Va spostata *dopo* il beneficio e trasformata in un segnale di serietà.
5. **L'orario lun–sab 8:00–20:30**, i 3 posti auto, il laboratorio interno, la sedazione. Sono vantaggi concreti, oggi sottovalutati.

## 5. Cosa eliminare

1. Le 90 keyword in chiaro e i footer di keyword stuffing.
2. Le pagine-stanza autonome (12 pagine → 1 tour).
3. Le clip-art "tasso zero" / "risparmia il 70%" / omino del percento.
4. Le foto di diplomi e pergamene (sostituite da dati tipografati).
5. Le immagini-collage 2×2 e il testo rasterizzato.
6. I duplicati (6 coppie di pagine).
7. L'autoplay dei video.
8. Il riferimento al D.lgs. 196/2003 nell'informativa.
