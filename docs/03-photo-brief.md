# Verdetto sugli asset esistenti + brief fotografico

Ogni immagine del sito attuale è stata aperta e valutata. Criteri: risoluzione utile, esposizione, coerenza cromatica, composizione, attualità, idoneità all'uso commerciale.

**Esito complessivo: 15 file su 102 sono utilizzabili.** Il problema non è la quantità ma la **coerenza**: convivono una serie fotografica professionale e un archivio di scatti da telefono.

---

## 1. Da usare — così com'è o con ritaglio

### ★★★★★ La serie di ritratti in bianco e nero (14 file)

`20180228_212244` · `p_015` · `p_040` · `p_056` · `p_059` · `carmela-pilitano` · `ceciliapirone` · `de-giovanni-emenuele` · `dott-grasso-2` · `tuo-ludovica` · `staff2020` (griglia sorgente)

Alta chiave, fondo bianco, sguardo in camera, illuminazione morbida e frontale. **È materiale di livello editoriale** ed è l'unico asset che da solo può reggere l'identità visiva del sito.

**Lavorazione applicata** (`build/prep_images.py`): ritaglio 4:5 coerente, conversione in scala di grigi, normalizzazione del punto di bianco per fondere il fondo con la carta della pagina, +4% di contrasto. Risultato: 10 ritratti perfettamente allineati fra loro.

> ⚠️ **Unica incoerenza:** tre membri (Pulitanò, De Giovanni, Grasso) indossano una polo scura, gli altri una polo bianca. In B/N stona poco, ma al prossimo shooting va uniformata la divisa.
> ⚠️ **Attenzione ai nomi file:** `ceciliapirone.webp` ritrae in realtà **Erika Carbone, Assistente** (leggibile dal ricamo sulla polo). Rinominato correttamente.

### ★★★☆☆ `al-lavoro-3` — intervento in corso

Due clinici con occhialini ingranditori e mascherina, in azione. È l'unica foto documentaristica vera dell'archivio. Bassa risoluzione (557×372) → usabile solo come banda editoriale, convertita in B/N per coerenza. **Da rifare in alta risoluzione: è lo scatto più prezioso del set.**

### ★★☆☆☆ Casi clinici prima/dopo — 2 coppie recuperabili su ~20

| Caso | Sorgente | Nota |
|---|---|---|
| Riabilitazione protesica | `protesi3` quadranti in basso | Stesso paziente, prima/dopo credibile. Recuperato con bilanciamento esposizione e desaturazione del rosso gengivale. |
| Ortodonzia | `ortodonziacasi` riga superiore | Frontale prima/dopo leggibile. Gengiva arrossata nel "dopo" (post-debonding): accettabile ma non ideale. |

Tutto il resto (`protesi1`, `protesi2`, `otturazioni1–3`, `lumineers2`, `caricoimmediato1–3`, `exgiudizio`) è **da scartare**: flash diretto, bilanciamento del bianco variabile fra prima e dopo, inquadrature diverse fra le due fasi, retrattori assenti, immagini montate in collage.

---

## 2. Da scartare (e perché)

| Gruppo | File | Motivo |
|---|---|---|
| **Stanze e ambienti** | `sala-attesa`, `zoneoperativedentista1–4`, `ufficidentista1–3`, `salamacchine`, `bagnodisabili1–2`, `posteggio`, `direzionesanitaria1–2`, `segretariadentista`, `la-zona-sterilizzazione`, `laboratorioodontotecnico1–3`, `tac-dentale`, `serviziodomicilio` | Scatti da telefono, luce mista tungsteno/neon, verticali cadenti, ambienti disordinati, **montati in collage 2×2 dentro un unico file** (impossibili da rendere responsive). Alcuni mostrano arredi datati. |
| **Diplomi e pergamene** | `master-*` (4), `perfezionamento*` (3), `attestato-*` (3), `claude-bernard-jep`, `diploma-ipnologo`, `specialita-ortodonzia`, `MADIMAS-1`, `ATTESTATO-CARLOTTA` | Fotografie storte di fogli. Comunicano insicurezza. **Le stesse informazioni tipografate come dati comunicano autorità.** |
| **Clip-art commerciale** | `finanziamentitassozero` (×2), `finanziamentitassoagevolato`, `convenzioni`, `tariffario`, `contattaci`, `dentista_preventivi_on_line` | Estetica anni '90 (bevel, ombre dure, omino 3D, banconote e salvadanaio, «Risparmia fino al 70%»). In conflitto diretto con il posizionamento "qualità a prezzo onesto". |
| **Icone di contatto** | `CHIAMA2` (57×57), `whatsapp-dentista-genova` (90×81), `Prenota-online-*` (80×80 e 150×150) | Sostituite da componenti vettoriali e bottoni testuali. |
| **Badge recensioni** | `recensioni-goolge-compressed`, `recensioni-facebbok2-compressed` | Testo rasterizzato a 345×146. Sostituiti da un componente HTML con dati veri e stelle SVG. |
| **Foto di gruppo informali** | `dentista3`, `dentista4`, `dentista5`, `dentistabimbigenova`, `dentisti-genova`, `dentista-genova` | Foto di squadra simpatiche ma con mascherine, pupazzi, sfondi disordinati e (in un caso) **il volto di un bambino con gli occhi coperti da una barra nera** — soluzione da non pubblicare mai. |
| **Illustrazioni cliniche** | `innestiosso1–3`, `caricoimmediato`, `exgiudizio` | Illustrazioni stock di terzi, stile eterogeneo, probabile diritto d'uso non verificato. **Sostituite da diagrammi vettoriali originali** disegnati per il sito. |
| **Foto esterni** | `dovesiamo1–3`, `comeraggiungerci` | Notturne, mosse, insegna sovraesposta; la mappa è uno screenshot raster. Sostituite da mappa interattiva + foto vetrina da rifare. |
| **Interne varie** | `filse2024`, `filse-copertina` | Documento amministrativo del bando FILSE. Va in una nota a piè di pagina, non tra le immagini. |

---

## 3. Brief fotografico — cosa produrre

Sul sito, ogni buco è marcato con un **segnaposto progettato** che riporta a schermo il tipo di media, il formato e la nota di scatto. Sono componenti `.media-slot` con attributo `data-shot`: cercabili nel codice, impossibili da dimenticare in pubblicazione.

### Direzione artistica unica

Un solo linguaggio per tutto il nuovo materiale:

- **Luce:** naturale o finestra simulata, morbida, direzionale da sinistra. Mai flash diretto. Mai luce mista.
- **Colore:** temperatura 5.200–5.600 K costante. Ambiente desaturato, un solo accento caldo per scatto.
- **Composizione:** aria intorno al soggetto, orizzonti dritti, verticali corrette. Formati nativi 3:2 e 4:5.
- **Persone:** sempre in azione o in relazione, mai in posa frontale sorridente (tranne i ritratti). Mani, sguardi, dettagli.
- **Post:** profilo unico. Neri leggermente alzati, contrasto morbido, nessuna vignettatura, nessun filtro.

### Lista scatti — priorità 1 (indispensabili al lancio)

| # | Soggetto | Formato | Uso | Nota |
|---|---|---|---|---|
| 1 | **Dott. Piccardo in studio**, in azione, mezza figura | 3:2 orizz. | Hero home, alternativa al ritratto | Luce di finestra, sfondo studio sfocato |
| 2 | **Ingresso e vetrina** di Via Maragliano 5, ora blu | 3:2 | Contatti, Studio | Insegna leggibile ma non bruciata |
| 3 | **Sala d'attesa** riordinata, grandangolo moderato | 3:2 | Studio | Riordinare prima: niente carte, niente sedie fuori asse |
| 4 | **Zona operativa** con riunito, senza persone | 3:2 | Studio | Piani sgombri, luce spenta sul riunito, ambiente in ombra |
| 5 | **TAC Cone Beam** e scanner intraorale, dettaglio | 4:5 | Studio, Implantologia | Ravvicinato, tagliato, non "foto del macchinario" |
| 6 | **Sterilizzazione**: mani guantate che imbustano lo strumentario | 3:2 | Studio | Dettaglio, non panoramica della stanza |
| 7 | **Laboratorio interno**: mani dell'odontotecnico su una zirconia | 4:5 | Studio, Protesi | È un differenziante forte: merita uno scatto vero |
| 8 | **Maschera per sedazione cosciente** appoggiata, still life | 4:5 | Paura del dentista | Deve risultare rassicurante, non medicale |
| 9 | **Area bimbi** con un bambino di spalle o solo mani | 3:2 | Bambini | Liberatoria genitori obbligatoria. Mai barre nere sugli occhi |
| 10 | **Posto auto interno** con auto parcheggiata, di giorno | 3:2 | Contatti | Risolve un'obiezione reale a Genova centro |

### Lista scatti — priorità 2

11. Ritratto d'équipe al completo, in studio, divisa uniforme, B/N (sostituisce `staff2020`)
12. Rifacimento dei ritratti dei tre membri in polo scura, per uniformare la serie
13. Dettaglio delle mascherine Invisalign in mano
14. Reception con Carlotta al telefono (scatto naturale, non in posa)
15. Serie *behind the scenes*: riunione mensile di formazione sulle emergenze — è una prova concreta e nessun concorrente ce l'ha

### Video

| # | Contenuto | Durata | Uso |
|---|---|---|---|
| V1 | **«Non ho sentito niente»** — un paziente racconta, montato con il Dott. Piccardo che spiega la sedazione | 60–75″ | Blocco paura in home + pillar |
| V2 | **Tour dello studio** in movimento continuo, senza voce, musica sotto | 45″ | Hero della pagina Studio |
| V3 | **Prima visita: cosa succede davvero** — punto di vista del paziente, dall'ingresso al preventivo | 90″ | Prezzi + pagine trattamento |
| V4 | 8 clip verticali 15″, una per clinico: «la domanda che mi fanno più spesso» | 15″ | Team + social |

I 36 video YouTube esistenti (incluse le interviste ai clinici) restano validi come **archivio di approfondimento**: vanno però tolti dall'autoplay e raccolti in una sezione dedicata con anteprima e titolo, non incorporati alla rinfusa.

### Protocollo per i prima/dopo (da adottare subito)

Perché i prossimi casi siano pubblicabili, ogni paziente va fotografato con:

1. **Stessa fotocamera, stessa focale, stessa distanza** (idealmente 100 mm macro o telefono con lente tele, sempre la stessa).
2. **Flash anulare o doppio flash laterale** — mai flash integrato.
3. **Retrattori labiali** e specchi intraorali per le viste occlusali.
4. **Bilanciamento del bianco fissato** su cartoncino grigio, identico nelle due sessioni.
5. **Serie standard:** frontale a denti uniti · frontale sorriso · laterale dx · laterale sx · occlusale sup. · occlusale inf.
6. **Consenso informato scritto** alla pubblicazione, archiviato.
7. **Nessun ritocco** oltre il bilanciamento colore. Il fotoritocco su un prima/dopo medico è un rischio deontologico.

**Conformità:** i prima/dopo in odontoiatria sono ammessi come informazione sanitaria (art. 9 L. 24/2017 e linee guida FNOMCeO) purché veritieri, non promozionali e non ingannevoli. Ogni galleria del sito riporta in modo permanente: *«Casi reali trattati nello studio. I risultati variano da paziente a paziente e non sono garantiti.»*
