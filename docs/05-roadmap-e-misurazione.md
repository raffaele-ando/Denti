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
