# Cosa manca, chi lo fa, come si misura

Il sito nel repository è **completo e funzionante**: 19 pagine, navigazione, form, calcolatore,
filtri, animazioni, dati strutturati, redirect. Quello che segue è ciò che serve per portarlo online
e per capire se funziona.

---

## 1. Dati da confermare con lo studio

Sono gli unici punti in cui il sito contiene un segnaposto testuale invece di un dato reale.
Nessuno di questi è stato inventato: dove non conoscevamo il valore, l'abbiamo dichiarato.

| Dove | Cosa manca | Perché serve |
|---|---|---|
| `note-legali.html` | **Partita IVA, REA, PEC, email** | Obbligo di legge |
| `note-legali.html#rc` | **Estremi della polizza RC professionale**: compagnia, classe di rischio, massimali | **Obbligo dell'art. 10 c. 4 L. 24/2017** per le strutture sanitarie |
| `note-legali.html#rc` | **Risarcimenti erogati nell'ultimo quinquennio** | Stesso obbligo |
| `note-legali.html#cookie` | Elenco effettivo di cookie e pixel | Il sito attuale monta un **Meta Pixel** (`id=441213099860271`): va dichiarato e subordinato a consenso |
| `build/content.py` → `email` | Indirizzo email reale | Attualmente `info@dentista.ge`, da verificare |
| Orari | Il sito attuale dichiara sia «8.00–20.00» sia «8.00–20.30» | Abbiamo adottato **8:00–20:30**: da confermare |
| Convenzioni | L'elenco varia fra homepage e pagina convenzioni (`HELP CARD` e `HBM` compaiono solo in una) | Ne abbiamo unificati 19: da validare |
| **Valutazione media Google** | Il sito riporta **5,0** su 310 recensioni, ripreso dall'estratto della scheda fornito a inizio progetto e **mai verificato in autonomia** | La media cambia a ogni nuova recensione. **Va riletta su Google Maps prima di pubblicare** e corretta in `build/content.py` → `voto`. I titoli del sito non poggiano più sulla media ma sul numero di recensioni, che è documentato: se la media fosse 4,9 non cambierebbe una riga di copy |

---

## 1-bis. Promesse operative: cosa il sito può dire, e cosa no

L'export del vecchio sito documenta attrezzature, titoli, prezzi e orari. **Non documenta come lo
studio organizza il lavoro**, e in una prima stesura ci avevo messo delle promesse operative che
nessuna fonte sosteneva. Le ho tolte tutte. Restano qui perché diverse sono probabilmente vere, e
se lo studio le conferma per iscritto si possono rimettere: sono argomenti di vendita forti.

| Promessa rimossa | Perché è stata tolta | Cosa serve per rimetterla |
|---|---|---|
| «Chi ti visita la prima volta è chi ti seguirà fino alla fine» | Nessun riscontro, e il vecchio sito descrive lo staff come «dott. Piccardo e i migliori **dentisti collaboratori odontoiatri specialisti** nelle varie discipline»: un caso multidisciplinare vede per forza più clinici | Conferma dello studio su come vengono assegnati i casi |
| «Il preventivo che firmi è la cifra che pagherai alla fine» e «se il lavoro si rivela più lungo del previsto, la differenza resta a carico nostro» | È un **impegno contrattuale**, e non compare da nessuna parte nell'export. Comparivano in dodici punti del sito | Conferma scritta dello studio. Se la danno, è probabilmente l'argomento più forte che hanno |
| «Cerchiamo sempre uno spazio in giornata» | Il vecchio sito dice solo «per i pazienti dello studio il dentista sarà comunque reperibile anche in urgenza». Diverso, e più debole | Conferma sulla gestione reale dell'agenda urgenze |
| «Ti rispondiamo entro due giorni lavorativi» | Il vecchio modulo preventivi dice «ti risponderà **il prima possibile**». Un tempo di risposta dichiarato è una promessa misurabile | Il tempo medio reale di risposta |
| «La tua storia la racconti una volta sola» | Stessa radice della prima: presuppone un coordinamento interno che non è documentato | Come circolano le informazioni fra i clinici |
| «Otto specialisti» / «otto clinici» | La pagina *Chi siamo* del vecchio sito ne elenca **sette**: Piccardo, Gibelli, Parodi Baiardi, Tuo, De Giovanni, Grasso, Pulitanò. Più segreteria e assistenti | Elenco aggiornato dell'équipe |

**Regola per chi scriverà la prossima riga.** Attrezzature, titoli, prezzi e orari si possono
affermare, perché hanno una fonte. Un comportamento organizzativo, un tempo di risposta o una
garanzia economica **no**, finché lo studio non lo mette per iscritto. La differenza non è
formale: la prima categoria è verificabile da chiunque, la seconda espone lo studio a una
contestazione, e su un sito sanitario anche a qualcosa di peggio.

---

## 1-ter. Verifica integrale delle affermazioni contro l'export

Ogni affermazione fattuale del sito nuovo è stata confrontata con le 61 pagine dell'export del
sito attuale, lette per intero (43.228 parole, 1.702 righe dopo aver tolto il testo che si ripete
su ogni pagina). Esito: **cinque errori miei, due contraddizioni interne alla fonte, due dati che
esistevano e che avevo dichiarato mancanti.**

### Un secondo giro sulle promesse, e perché il primo non era bastato

Il primo audit sulle promesse operative cercava **le frasi che ricordavo**, non la forma. Quattro
inviti erano sopravvissuti proprio per questo. Il secondo giro ha cercato per costruzione, cioè
ogni frase che offre una possibilità al lettore, e li ha trovati tutti.

| Rimosso | Perché |
|---|---|
| «Vuoi parlare con uno di loro? … chiedilo in segreteria» *(richiamo pagina team)* | Zero riscontri. L'unica cosa vicina è `direzionesanitaria.md`: l'ufficio del direttore «è a disposizione dei pazienti per discutere delle loro problematiche terapeutiche», che riguarda chi è già in cura e solo il Dott. Piccardo |
| «Puoi venire solo a guardare. Puoi fissare un appuntamento in cui non si cura nulla» *(richiamo pagina studio)* | Zero riscontri |
| «Diversi nostri pazienti hanno cominciato esattamente così, e la volta dopo si sono seduti» | **Prova inventata.** Non è una promessa esagerata, è una statistica di comportamento dei pazienti che non esiste da nessuna parte |
| «Molti pazienti hanno iniziato così» *(FAQ paura del dentista)* | Stessa cosa |
| «Chiedila subito al telefono: … la riceviamo ogni giorno» | Frequenza inventata |

Le due CTA su misura sono state sostituite con quella standard, verificata. La FAQ «E se ho paura
anche solo di venire in studio?» ora risponde con due cose documentate: la sedazione si concorda
già per la prima seduta (`protossido.md`) e le stanze sono visitabili su Street View
(`virtuale.md`).

**Promesse dello stesso tipo che invece hanno una fonte**, e che restano: la prenotazione dei posti
auto in segreteria (`posteggio.md`), il servizio a domicilio (`domicilio.md`), la sedazione su
richiesta anche per l'igiene (`protossido.md`), l'invio della panoramica per il preventivo
(`preventivo.md`).

**Rete permanente:** `check_copy.py` ha la regola F15, che segnala ogni frase costruita come
un'offerta. Le quattro verificate qui sopra sono in un elenco di deroghe con la pagina che le
documenta. Se ne compare una nuova, o ha una fonte e si aggiunge all'elenco, o esce dal sito.

### Errori corretti

| Affermazione | Fonte | Correzione |
|---|---|---|
| «Sei master universitari di II livello» | `piccardo.md` ne elenca **cinque**: Implantoprotesi Genova 2013/14 (110/110), Sedazione ed emergenze Padova 2014/15, Chirurgia orale e d'urgenza Pisa 2015/16, Direzione e Management LUM 2018/19, Implantologia Digitale Padova 2021/22. In più due perfezionamenti universitari e il corso di Lione, che master non sono | «Cinque master universitari di II livello» |
| «Defibrillatore semiautomatico» | `index.md`: «defibrillatore **automatico**» | «Defibrillatore automatico» |
| Linee bus: 15, 17, 18, 19, 20, 30, 33, 36, 37, 39, 40, 42, 44, 46, 47 | `raggiungerci.md` include anche la **14** | Aggiunta la 14 |
| «1997, l'anno in cui il Dott. Piccardo ha iniziato a esercitare» | Laurea e abilitazione sono del 1997, ma `piccardo.md` dice «inizia la libera professione odontoiatrica **nel 1998**» | «L'anno della laurea in Odontoiatria» |
| Servizio a domicilio senza indicazione di costo | `domicilio.md`: «Il prezzo delle prestazioni sarà gravato esclusivamente per il tempo di spostamento e disponibilità del medico odontoiatra di **150,00 €**» | Il supplemento è ora dichiarato |

### Contraddizioni dentro la fonte, da far sciogliere allo studio

| Dato | Versione A | Versione B |
|---|---|---|
| **Autonomia del gruppo di continuità** | `index.md`: «garantisce alle tre zone operative **tre ore** di autonomia» | `gruppocontinuita.md`: «eroga 10 kWora per **2 ore**… garantisce un'autonomia di 2 ore» |
| **Orario di apertura** | `index.md`: «dalle ore 8.00 alle ore **20.00**» | `contatti.md`, `piccardo.md`, `tariffario.md` e il piè di pagina di tutte le pagine: «dal Lunedì al Sabato **8.00-20.30**» |
| **Chi segue la pedodonzia** | `chisiamo.md` e `pedodonzista.md`: **Dott.ssa Ludovica Tuo** | `pedodonzia.md`: «la **dott.ssa F. Barbato** da sempre si occupa della cura dei denti dei bambini» |
| **Assistenti alla poltrona** | `assistenti.md`: **Cecilia Pirone e Virginia La Paglia** | La scheda del team che ho costruito riporta Erika Carbone e Virginia |
| **Elenco convenzioni** | `convenzioni.md` include **HELP CARD** | `index.md` include **HBM** al suo posto |

Sul sito nuovo ho usato la versione maggioritaria (20:30, Tuo, tre ore), ma **vanno confermate
tutte**, e le assistenti vanno verificate per nome.

### Dati che esistevano e che avevo dichiarato mancanti

Questo è l'errore opposto, e va detto perché mi ha portato a scrivere «da inserire» su una pagina
pubblica quando il dato era già online:

- **Polizza RC professionale**, da `polizza-assicurativa-rc-professionale.md`: polizza
  n. 2024/03/2585668, Reale Mutua Assicurazioni, decorrenza 31/12/2024, scadenza il 31/12 di ogni
  anno, massimale 2.000.000 €. Ora pubblicata. Va riconfermata alla messa online, perché scade
  ogni anno.
- **Risarcimenti dell'ultimo quinquennio**, da `contenziosi-e-risarcimenti.md`: «Negli ultimi
  cinque anni Ambulatorio Dentistico Dr. Piccardo U. Srl non ha avuto contenziosi con i pazienti e
  non ha erogato risarcimenti diretti o indiretti attraverso la compagnia assicurativa.» Ora
  pubblicata: è un obbligo di legge assolto, e anche un argomento di fiducia notevole.

### Fatti verificati che il sito nuovo non usa ancora

Tutti nell'export, tutti concreti, tutti inutilizzati. Sono materiale pronto per la prossima
iterazione:

- **Lumineers garantite 10 anni**, con certificato di conformità e autenticità rilasciato dal
  medico abilitato, e «nel 90% dei casi non viene rimossa nessuna struttura dentaria sensibile»
- **Occhiali video con i cartoni animati** durante le sedute dei bambini
- **Priorità nella prenotazione dei posti auto** ai pazienti con disabilità o con bimbi piccoli
- **Sala d'attesa**: 12 poltroncine, wi-fi con password, area bimbi con tavolini, carrozzina a
  disposizione, e **tutti i diplomi e i master esposti alle pareti**
- **Reception**: pagamento con Pagodil in 12 rate, buoni regalo per igiene e sbiancamento, foglio
  di giustificazione per il lavoro
- **Controindicazioni del protossido** dichiarate esplicitamente: primi tre mesi di gravidanza,
  tossicodipendenze, terapia antidepressiva, infezioni polmonari acute, gravi malattie mentali
- **Il riunito portatile** del servizio a domicilio: doppio aspiratore chirurgico, due trapani,
  lampada UV, ablatore, pistola aria-acqua, con un odontotecnico al seguito

---

## 1-quater. Audit inverso: cosa si era perso nel passaggio

Consolidare 62 pagine in 19 significa tagliare, ed è giusto. Ma tagliare la prosa non deve
significare perdere i fatti. Ho preso 73 argomenti presenti nell'export e li ho cercati uno per uno
nel sito nuovo: **54 c'erano, 19 no**. Tredici erano perdite vere e sono stati recuperati.

**Nessuna URL è rimasta orfana:** tutte e 60 le pagine interne dell'originale hanno il loro
redirect 301, la sessantunesima è la home.

### Recuperati

| Perso | Dove è tornato |
|---|---|
| **Ansiolisi orale con benzodiazepine** | Pagina paura del dentista. Era la terza via di sedazione documentata in `sedazione.md`, e il sito nuovo ne citava solo due |
| **Rialzo del seno mascellare** con piezoelettrico | Chirurgia orale, scheda innesti |
| **Innesto con membrana o griglia in titanio** | Chirurgia orale, scheda innesti |
| **Damon System** e attacchi estetici | Invisalign e ortodonzia, dove si spiega quando l'apparecchio fisso resta la scelta migliore |
| **Radiografie del carpo e dell'articolazione temporo-mandibolare** | Pagina studio, sala raggi: completano il «tutto in sede» |
| **Mappa tattile in Braille** e **sistema di allarme** nel bagno | Pagina studio, accessibilità. Era il dettaglio più forte che avevo perso |
| **Carrozzina a disposizione** in sala d'attesa | Pagina studio, accessibilità |
| **Diplomi, master e specializzazioni appesi in sala d'attesa** | Pagina studio. È la prova fisica di ciò che il sito sostiene, e non la citavo |
| **Wi-fi con password** | Pagina studio |
| **Pagodil, dodici rate dal bancomat** | Pagina prezzi, accanto al finanziamento a tasso zero |
| **Metodi di pagamento**: contanti, bancomat, carta, assegno, convenzione | Nota del tariffario |
| **Buoni regalo** per igiene e sbiancamento | Modulo preventivo |
| **Giustificativo per il datore di lavoro** | Modulo preventivo |

### Tagliati e lasciati fuori, con motivo

- **Uscite di emergenza ed estintori a norma:** obbligo di legge per qualunque locale pubblico,
  non dice niente su questo studio.
- **Dodici poltroncine in sala d'attesa:** dettaglio d'arredo senza conseguenze per chi legge.
- **«Addetta al recupero crediti in caso di morosità»:** informazione interna. Sul sito comunica
  al paziente che è considerato un potenziale insolvente, prima ancora di essere entrato.
- **MioDottore:** non è perso, è riusato. È il sistema di prenotazione online collegato a tutti i
  pulsanti «Prenota». Resta da valutare se citarlo anche come terza fonte di recensioni.

### Una promessa trovata nell'audit, non pubblicata

`segretariadentista.md` dice che la segreteria «organizza gli orari dei medici odontoiatri in modo
che vi sia sempre presente un medico odontoiatra **ogni giorno dell'anno**». È nella fonte, ma
contraddice l'orario pubblicato su ogni pagina, dove la domenica è chiusa. **Da chiarire con lo
studio prima di usarla:** se vale per la reperibilità e non per l'apertura, va detto così.

---

## 2. Da collegare prima della pubblicazione

**1. Endpoint dei moduli.** Oggi i due form validano lato client e mostrano la conferma, ma non inviano nulla (`app.js`, blocco *Form: validazione + invio simulato*). Serve un endpoint. Tre opzioni, in ordine di preferenza:

- uno script PHP sul dominio, se l'hosting è Apache/PHP: nessun terzo, nessun trasferimento di dati sanitari fuori;
- un servizio di form con contratto GDPR e server UE;
- integrazione diretta con il gestionale dello studio.

⚠️ **Il modulo accetta il caricamento di una panoramica: è un dato sanitario ex art. 9 GDPR.** L'endpoint deve essere in HTTPS, i file non devono finire in una cartella pubblica indicizzabile, e va definita una politica di cancellazione. Il vecchio limite di 100 KB è stato portato a 15 MB, che è la dimensione reale di una panoramica.

**2. Cookie banner.** Il Meta Pixel e le mappe Google richiedono un consenso preventivo conforme alle Linee guida del Garante del 10 giugno 2021. Le mappe vanno caricate solo dopo il consenso (click-to-load).

**3. Redirect 301.** `site/.htaccess` contiene già le 60 regole. Se l'hosting non è Apache vanno tradotte per Nginx o per il pannello del provider. **Nessuno dei 62 URL storici deve restituire 404**: alcuni sono indicizzati da oltre quindici anni ed è il patrimonio SEO dello studio.

**4. Google Business Profile.** Allineare NAP (nome, indirizzo, telefono) e orari a quelli del sito, e collegare la nuova URL. È il primo fattore di posizionamento locale.

**5. Search Console.** Inviare `sitemap.xml`, monitorare le 404 nelle prime quattro settimane, chiedere la reindicizzazione delle 17 nuove pagine.

---

## 2-bis. Cosa esisteva già, e cosa è nuovo

Una precisazione utile in fase di presentazione allo studio, per non spacciare
per novità ciò che c'era già.

| Servizio | Nel sito precedente | Nel redesign |
|---|---|---|
| **Valutazione gratuita della panoramica** | **Esisteva.** La pagina `preventivo.html` diceva: «Per avere un preventivo invia tramite posta elettronica la tua richiesta dettagliata. Se hai la possibilità non dimenticarti di inviare come allegato la tua panoramica», e il footer di ogni pagina prometteva «preventivi implantologia protesi gratuiti» | Stesso servizio, reso usabile. Prima era una pagina di terzo livello con un modulo che accettava allegati **fino a 100 KB**, quando una panoramica ne pesa da 2 a 8 MB: di fatto il caricamento non funzionava. Ora il limite è 15 MB, il modulo è in homepage e in due pagine, e dichiara i tempi di risposta |
| Prenotazione online | Esisteva, tramite widget MioDottore | Stesso strumento, promosso a bottone primario |
| Tariffario pubblico | Esisteva | Stesso contenuto, con ricerca, filtri e calcolatore di rata |
| Finanziamento a tasso 0 | Esisteva | Stesso, con simulatore |
| Sedazione cosciente | Esisteva, in due pagine di terzo livello | Promossa a pagina pilastro, perché è il differenziante più forte |
| Tour virtuale Google | Esisteva | Stesso embed, in un contesto che lo spiega |

**Non abbiamo inventato nessun servizio nuovo.** Il redesign riordina, rende
usabile e mette in evidenza ciò che lo studio già offriva: è esattamente il
motivo per cui è proponibile senza chiedere al cliente di cambiare nulla della
propria organizzazione.

---

## 3. Produzione fotografica

Vedi `docs/03-photo-brief.md` per la lista completa. In sintesi: **10 scatti in priorità 1**, 5 in priorità 2, **4 video**. Il sito segnala da solo i 22 punti in cui manca un media, con la specifica di scatto stampata a schermo.

Il contenuto a più alto ritorno è **V1: «Non ho sentito niente»**: la testimonianza di un paziente montata con il Dott. Piccardo che spiega la sedazione. Occupa il blocco più emotivo della homepage e la pagina che regge il posizionamento.

Da adottare **subito**, indipendentemente dal sito: il protocollo fotografico per i casi clinici (§3 del photo brief). Ogni mese in cui non lo si applica è un mese di casi non pubblicabili.

---

## 4. Come si misura

Senza misurazione questo redesign è un'opinione. Con la misurazione è una decisione verificabile.

### Eventi da tracciare

| Evento | Innesco | Perché |
|---|---|---|
| `click_telefono` | `a[href^="tel:"]` | Da segmentare per pagina e per dispositivo |
| `click_whatsapp` | link WhatsApp | |
| `click_prenota` | link a MioDottore | Da distinguere: header, hero, CTA finale, barra mobile |
| `invio_preventivo` | submit del modulo preventivo | Con e senza panoramica allegata |
| `apertura_tariffario` | scroll fino alla tabella prezzi | Il tariffario è il differenziante: va misurato se viene letto |
| `uso_calcolatore` | interazione con lo slider | Segnale forte di intenzione d'acquisto |
| `uso_prima_dopo` | trascinamento dello slider | Misura l'efficacia dei casi clinici |
| `scelta_intenzione` | click sui tab della home | **Dice quale segmento arriva davvero.** È il dato più utile per le decisioni successive |
| `apertura_faq` | apertura di un accordion | Le FAQ più aperte sono le obiezioni reali: vanno promosse più in alto |

Il tracciamento va installato **dopo** il consenso ai cookie, e i click-to-call vanno letti insieme al registro chiamate della segreteria: il sito porta la telefonata, ma è la segreteria che chiude l'appuntamento.

### Baseline da rilevare prima del passaggio

Prima di sostituire il sito, registrare per almeno 30 giorni: sessioni, sorgenti, pagine più viste, chiamate ricevute, appuntamenti prenotati via MioDottore. Senza baseline non si potrà dire se il redesign ha funzionato.

### Obiettivi a 90 giorni

| Indicatore | Come leggerlo |
|---|---|
| Tasso di contatto (chiamate + WhatsApp + form ÷ sessioni) | È **la** metrica. Tutto il resto è diagnostica |
| Contatti da mobile | Il redesign agisce soprattutto qui: barra sticky, click-to-call, form corto |
| Richieste di preventivo con panoramica allegata | Misura il funzionamento del gradino a basso attrito |
| Posizione media su *implantologia Genova*, *invisalign Genova*, *dentista senza dolore Genova* | Attendere 8–12 settimane dopo i redirect |
| Nuove recensioni Google al mese | Il sito può aumentarle: chiedere la recensione dopo la seduta, con QR in reception |

---

## 5. Cosa farei dopo, in ordine

1. **Video V1 e le 10 foto di priorità 1.** Il sito è progettato attorno a quei buchi: riempirli è ciò che lo porta dall'80% al 100%.
2. **Endpoint dei form + cookie banner.** Sono i due blocchi che impediscono la pubblicazione.
3. **Pagina «La tua prima visita».** Un contenuto che il sito attuale non ha e che nessun concorrente genovese ha: cosa succede minuto per minuto, cosa portare, quanto dura, cosa esce dallo studio. Abbassa l'ansia del segmento A e alza la conversione del gradino più costoso.
4. **Casi clinici come contenuto ricorrente.** Con il protocollo fotografico attivo, un caso al mese in due anni diventa una galleria che nessun concorrente può replicare in fretta.
5. **Blog/FAQ estese in ottica SEO.** Le 60 domande delle pagine trattamento sono già scritte e marcate `FAQPage`: da lì si generano contenuti long-tail («quanto costa un impianto a Genova», «invisalign fa male»).
6. **Recensioni video.** Tre pazienti, 30 secondi ciascuno. La prova sociale in video converte più del testo, e lo studio ha 310 persone disposte a farlo.

---

## 6. Struttura del repository

```
docs/          i cinque documenti di progetto: è la parte che si presenta al cliente
build/         sorgenti Python del generatore (contenuti, componenti, icone, diagrammi)
  make.py            genera il sito         → python3 build/make.py
  check.py           controllo qualità      → python3 build/check.py
  test_interazioni.py  71 test funzionali   → python3 build/test_interazioni.py
  prep_images.py     lavorazione delle foto ereditate
  icone.py           rasterizza favicon e immagine di condivisione
site/          il sito generato: HTML statico puro, apribile senza build
```

Il cliente riceve `site/`: file HTML, CSS, JS e immagini, caricabili su qualsiasi hosting.
Non serve Node, non serve un CMS, non serve un database. `build/` serve a chi manterrà il sito:
modificare un prezzo significa cambiare una riga in `build/content.py` e rilanciare `make.py`,
e il prezzo si aggiorna in tutte le pagine in cui compare.
