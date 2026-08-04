# Metodo editoriale

Documento di lavoro, non di vendita. Serve a chi scriverà la prossima riga di questo sito
e a me, per non ripetere gli errori che sono stati contestati in revisione.

Qui ci sono le regole e le decisioni. L'analisi dei difetti, con i nomi tecnici che linguisti,
retori, psicologi cognitivi e progettisti di interfaccia usano per identificarli, sta in
[`07-tassonomia-dei-difetti.md`](07-tassonomia-dei-difetti.md).

---

## 1. Chi legge, e in che stato

Prima di qualunque regola di scrittura, la fotografia del lettore. Viene dalle 310 recensioni,
che sono la migliore ricerca utente disponibile su questo studio.

- **Ha paura, o ha vergogna, o entrambe.** Molti hanno rimandato per anni. Non sono lettori
  neutrali: sono persone che stanno già facendo uno sforzo ad aprire la pagina.
- **Sta confrontando.** Nella maggior parte dei casi ha già in mano due o tre preventivi.
- **Legge sul telefono, e scansiona.** La ricerca sulla lettura a schermo (Nielsen Norman Group)
  stima che si legga fra il 20 e il 30 per cento delle parole di una pagina. Quello che viene
  letto davvero sono i titoli, i grassetti e i numeri.
- **Non è un collega, non è un investitore, non è un giurato.** Non gli interessa il nostro
  metodo, non gli interessa come abbiamo scelto le recensioni, non gli interessa perché
  pubblichiamo il tariffario.

Da qui discende la regola che governa tutte le altre:

> **Il titolo dice cosa cambia per chi legge. Il corpo dice perché è vero.
> Mai il contrario, mai una terza cosa.**

---

## 2. I difetti trovati in revisione

Sono difetti reali, presi dalla versione precedente di questo sito. Li elenco con l'esempio
originale perché servano da campione negativo.

### F1. Meta-testo: la pagina parla di sé stessa

Il difetto più grave e il più frequente. La pagina spiega la propria struttura, il proprio
metodo editoriale, le proprie intenzioni.

> ✗ «Qui sotto trovate tre affermazioni precise e, accanto a ognuna, il titolo universitario,
> il numero o il documento che la sostiene. Sono tutte verificabili.»
>
> ✗ «Le abbiamo scelte per coprire situazioni diverse, non per convenienza.»
>
> ✗ «Sui siti degli studi dentistici si vedono spesso fotografie di diplomi incorniciati…
> Li abbiamo scritti: titolo esatto, ateneo, anno accademico.»
>
> ✗ «Lo studio ha già un archivio di interviste video sul canale YouTube. Vanno raccolte qui…»
> *(questa era addirittura una nota di lavoro finita nel sito pubblicato)*

Chi legge non ha chiesto una difesa del progetto. Se le affermazioni sono verificabili si vede
dal fatto che accanto c'è il documento, non perché lo annunciamo. **Il paragrafo che spiega la
credibilità la riduce**: è il meccanismo per cui «fidati di me» produce l'effetto opposto.

**Correzione:** eliminare l'annuncio e lasciare solo la cosa. Se serve la prova, la prova sta
nel corpo, in silenzio.

### F2. Istruzioni per l'uso al posto dell'affordance

Quando l'interfaccia non si spiega da sola, la si riprogetta; non si aggiunge un paragrafo che
insegna a usarla.

> ✗ «Trascina il cursore sull'immagine per confrontare la situazione iniziale con il risultato.»
>
> ✗ «Scegli la situazione che ti somiglia di più. Al posto di un elenco di quaranta prestazioni
> vedrai le tre che riguardano davvero il tuo caso.»
>
> ✗ «Muovi il cursore e scopri quanto pagheresti al mese.»
>
> ✗ «Clicca su una persona per leggerne il percorso completo.»

**Correzione applicata:** il cursore del prima/dopo si muove da solo per un attimo quando entra
nello schermo, e mostra un indicatore di trascinamento che sparisce al primo tocco. Nessuno deve
più leggere che si trascina: lo si vede.

### F3. Didascalia che descrive quello che si vede già

> ✗ «Due casi trattati qui, fotografati prima e dopo», scritto sopra due fotografie di un prima
> e di un dopo.

Se l'immagine mostra denti rotti e poi denti a posto, la didascalia deve dire **quello che
l'immagine non può dire**: che intervento è stato fatto, in quante sedute, in quanto tempo,
quanto è costato.

### F4. Punto di vista sbagliato: lo studio, o peggio l'analista

> ✗ «L'ortodontista, il chirurgo e l'odontotecnico lavorano a dieci metri l'uno dall'altro»
> → è la pianta dello studio. Al paziente interessa che **la sua storia la racconta una volta
> sola**.
>
> ✗ «Nelle 310 recensioni pubbliche tornano sempre le stesse tre cose»
> → è l'osservazione di chi ha analizzato il dataset. Al paziente interessa **leggere qualcuno
> che era nella sua situazione**.
>
> ✗ «Ogni strumento attraversa sei passaggi prima di tornare in bocca a un paziente»
> → è il protocollo visto dall'interno. Al paziente interessa che **ogni strumento gli arriva
> sigillato, con la data sopra**.

**Test:** metti «e quindi?» dopo il titolo. Se la risposta non è immediata e non riguarda il
lettore, il titolo è scritto dal lato sbagliato.

### F5. Il tic del contare

Nella versione precedente comparivano, in poche schermate: *tre motivi, tre strade, le stesse
tre cose, le tre parole, sei passaggi, tre poltrone, tre ore, tre posti auto, trecento metri
quadri, trentasei prestazioni, diciannove fondi, quattro pubblicazioni, sei master.*

Il numero è potente perché è raro. Usato in ogni titolo diventa un vezzo, e per giunta obbliga
la frase a una struttura sempre uguale.

**Regola adottata:** il numero vive nel componente che lo espone (la barra dei dati, i dati
chiave, il tariffario, i contatori), non nel titolo che gli sta sopra. Nel titolo entra solo
quando **è la notizia** («Fino a 5.000 euro puoi rateizzare a tasso zero»).

---

## 3. La griglia di valutazione

Ogni titolo e ogni testo di apertura passano queste otto domande. Basta un no per riscrivere.

| # | Domanda | Se la risposta è no |
|---|---|---|
| 1 | Parla di ciò che accade **al lettore**, non al sito né allo studio? | Riscrivi dal punto di vista di chi legge |
| 2 | Aggiunge qualcosa che **non si vede già** dal contesto? | Elimina o sostituisci con un'informazione |
| 3 | Reggerebbe **da solo**, letto senza il resto della pagina? | Rendilo autosufficiente: si legge solo quello |
| 4 | Evita di **spiegare l'interfaccia**? | Sistema l'interfaccia, non il testo |
| 5 | Evita di **annunciare la propria credibilità**? | Togli l'annuncio, tieni la prova |
| 6 | Ha una **struttura diversa** dai due titoli precedenti? | Cambia la costruzione della frase |
| 7 | È scritto **in positivo**, senza *non, niente, nessuno, mai, senza*? | Dì quello che c'è al posto di quello che manca |
| 8 | Si legge **senza notare chi l'ha scritto**: niente metafore, giochi di parole, frecciate? | Togli l'immagine e lascia il fatto |

---

## 4. Le decisioni, con le alternative scartate

Per i titoli portanti riporto le opzioni realmente valutate. Serve a mostrare il criterio, non
solo l'esito.

### Home, sezione dei tre argomenti

| Opzione | Giudizio |
|---|---|
| «Tre motivi per sceglierci, e la prova di ciascuno» *(versione precedente)* | Scartata. F1 e F5: annuncia una struttura retorica e conta |
| «Quello che ti fa rimandare, di solito, è una di queste tre cose» | Scartata. Buon punto di vista, ma conta ancora |
| «Fa male, costa troppo, ci vuole una vita» | Scelta al secondo passaggio, **poi scartata al terzo**: pianta tre associazioni negative sullo studio e non si spiega da sola. Vedi il punto 6 |
| **«Prima di cominciare sai cosa sentirai, quanto pagherai e quanto ci vorrà»** | **Scelta.** Dice in positivo la stessa cosa, regge da sola e le tre schede sotto rispondono una per una |

### Home, selettore per intenzione

| Opzione | Giudizio |
|---|---|
| «Ogni percorso comincia da un problema diverso» + istruzioni | Scartata. F2 |
| «Perché sei qui?» | Scartata. In italiano suona sbrigativo, quasi ostile |
| **«Cosa ti porta qui?»** | **Scelta.** È la domanda che fa la segretaria al telefono. Le pillole sotto sono la risposta, quindi l'interfaccia si spiega da sola e il testo di servizio sparisce |

### Home, blocco sulla paura

| Opzione | Giudizio |
|---|---|
| «Se rimandi le cure per paura, ci sono tre strade per uscirne» | Scartata. F5 |
| «La paura del dentista si tratta come qualsiasi altra cosa» | Scartata. Vera ma fredda |
| «Non ti chiederemo di farti coraggio» | Scelta al secondo passaggio, **poi scartata al terzo** perché costruita su una negazione |
| **«Puoi decidere tu quanta ansia sentire»** | **Scelta.** Dà al lettore la leva che abbassa davvero l'ansia, cioè il controllo, e la dà in positivo |

### Home, sezione équipe

| Opzione | Giudizio |
|---|---|
| «L'ortodontista, il chirurgo e l'odontotecnico lavorano a dieci metri l'uno dall'altro» | Scartata. F4 |
| «Chi ti visita è chi ti opera» | Scartata. Vera ma già detta nel titolo della pagina team |
| **«Non dovrai raccontare la tua storia tre volte»** | **Scelta.** È il fastidio concreto che il paziente conosce. Il corpo spiega il perché, cioè che sono tutti nella stessa sede |

### Home, prima e dopo

| Opzione | Giudizio |
|---|---|
| «Due casi trattati qui, fotografati prima e dopo» + istruzioni | Scartata. F2 e F3 insieme |
| «Cosa c'è stato in mezzo» | Buona, ma vaga |
| **«Quanto ci è voluto, e quanto è costato»** | **Scelta.** Promette esattamente l'informazione che la fotografia non contiene, ed è la domanda che chiunque si fa guardando un prima e dopo |

### Home, recensioni

| Opzione | Giudizio |
|---|---|
| «Nelle 310 recensioni pubbliche tornano sempre le stesse tre cose» | Scartata. F4 e F5 |
| «Leggi chi aveva paura quanto te» | Scartata. Ottima per un segmento solo |
| **«310 persone hanno raccontato com'è andata»** | **Scelta.** Nessun vanto, nessuna media da difendere, e il verbo *raccontare* invita alla lettura invece di chiudere il discorso |

### Home, prezzi

| Opzione | Giudizio |
|---|---|
| «Trentasei prezzi online, così puoi confrontarci prima di telefonare» | Scartata. F4 e F5: descrive una funzione del sito |
| «I prezzi non te li diciamo in poltrona» | Scartata. Efficace ma costruita in negativo su un sospetto |
| «Puoi farti i conti adesso» | Scelta al secondo passaggio, **poi scartata al terzo**: registro da bar, e il corpo ci aggiungeva una frecciata agli altri studi |
| **«I prezzi sono tutti online»** | **Scelta.** Cinque parole, soggetto e verbo, il fatto e basta |

---

## 5. Secondo passaggio: revisione riga per riga di tutte le pagine

Il primo giro aveva corretto i titoli portanti. Il secondo è stato fatto su un estratto completo
(`build/estrai_copy.py` mette in fila H1, H2, H3, occhielli, testi di apertura, didascalie e
pulsanti di tutte e 19 le pagine: 367 righe). Ogni riga è passata per la griglia del punto 3.
Undici blocchi non l'hanno superata.

| Dove | Prima | Difetto | Dopo |
|---|---|---|---|
| Home, casi clinici | «Sotto ciascuna trovi il trattamento, il numero di sedute e il tempo che è servito: sono le tre cose che una fotografia non può dirti» | F1 + F3: annuncia cosa c'è scritto sotto, e sotto c'è già scritto | «Stessa luce, stessa distanza e stesso obiettivo nelle due sessioni: fra il prima e il dopo cambiano solo i denti» |
| Hub trattamenti | «Trova il tuo problema, non la nostra prestazione» | Costruzione X-non-Y, e descrive l'architettura del sito | «Non sai come si chiama quello che hai? Va bene lo stesso» |
| Hub trattamenti, apertura | «Ogni pagina dice in cosa consiste il trattamento…» | F1: la pagina spiega le pagine | «Quanto dura, chi la esegue e quanto costa stanno scritti dentro ogni cura» |
| Team, formazione | «Titolo esatto, ateneo che lo ha rilasciato, anno accademico» | F3: è l'elenco delle colonne della tabella sotto | «L'identificativo accanto a ciascuna porta al testo originale, senza passare da noi» |
| Recensioni, apertura | «Le recensioni sono sulla scheda Google, dove nessuno può modificarle» | F1: annuncia la propria credibilità | «Qui sono riportate parola per parola dalla scheda Google, dove restano pubbliche» |
| Recensioni, temi | occhiello «Come le leggiamo» | F4: punto di vista di chi analizza | occhiello «Cosa scrivono» |
| Implantologia | «Che cos'è, senza giri di parole» / «I numeri veri, non quelli da brochure» / «Casistica, non promesse» | Tre titoli di fila che annunciano la propria onestà invece di dire la cosa | «Una vite in titanio al posto della radice» / «Quante probabilità ci sono che duri» / «4.000 impianti dal 1999» |
| Invisalign | «Il vantaggio che nessun apparecchio fisso ha» / «Non è l'unica ortodonzia che facciamo» | Il primo annuncia e non dice; il secondo è scritto dal lato dello studio | «Le togli quando mangi, e quando ti pare» / «Quando l'apparecchio fisso resta la scelta migliore» |
| Estetica | «Il criterio che seguiamo» | F4 | «"Non voglio sembrare rifatto"», che è la frase del paziente già citata nel corpo |
| Igiene | «La parte che quasi nessuno racconta» / «Numeri reali, presi dal nostro tariffario» | Annuncio senza contenuto, e rivendicazione di veridicità | «Lo screening del cavo orale è dentro il prezzo» / «La stessa carie costa 130 euro adesso e 1.540 fra qualche anno» |
| Bambini | «Consigli pratici, quelli che servono davvero» / «Lo studio è attrezzato» | Annuncio e genericità | «Si comincia dal primo dentino, con una garza» / «Area gioco, fasciatoio, passeggino ovunque» |

Il controllo automatico è stato poi esteso ai paragrafi, non ai soli titoli, perché due
costruzioni vietate erano sopravvissute nel corpo del testo dove nessuno le cercava:
*«Non è un adempimento: è un allenamento»* (pagina studio) e *«Il vero nemico non è il tempo:
è la peri-implantite»* (FAQ implantologia). Stessa cosa nelle schede dell'elenco trattamenti,
dove c'era *«La paura è un parametro clinico, non una debolezza»*.

L'unica istruzione all'utente rimasta in tutto il sito è l'etichetta dell'area di caricamento
file, *«Trascina qui il file o scegli dal dispositivo»*: su desktop non esiste un altro modo per
segnalare che un riquadro accetta un trascinamento, e il controllo automatico la esclude
esplicitamente.

Due correzioni di forma applicate nello stesso passaggio:

- **I numeri tornano in cifre.** L'apertura dell'igiene diceva *«Duecento euro all'anno… centotrenta
  euro invece di millecinquecento»*. Su schermo si scansiona, e una cifra scritta in lettere perde
  esattamente la proprietà per cui la si usa: essere l'unica cosa che si nota in un paragrafo.
  Ora è *«200 euro all'anno… 130 euro invece di 1.540»*.
- **La pagina 404** non racconta più la riorganizzazione del sito, che è un fatto nostro.

### Il prima/dopo, senza istruzioni

Correzione al difetto F2, questa volta nel codice e non nel testo. Il cursore del confronto ora:

1. fa **una passata sola da solo** quando il componente entra nello schermo, con un'accelerazione
   che imita il gesto della mano;
2. **pulsa tre volte** attorno alla maniglia finché nessuno l'ha toccato;
3. **si ferma al primo contatto** (mouse, dito, tastiera o focus) e non riparte più.

Con `prefers-reduced-motion` non si muove nulla. Il paragrafo che spiegava di trascinare è stato
eliminato, e `build/test_interazioni.py` verifica che non ricompaia.

---

## 6. Terzo passaggio: il framing negativo, e il titolo che non era mai stato giudicato

### F7. La negazione lascia impresso ciò che nega

La ricerca sulla smentita è concorde: ripetere un'affermazione negativa per correggerla la rende
più familiare, e la familiarità viene scambiata per verità (Skurnik, Yoon, Park e Schwarz, 2005;
Schwarz e colleghi, 2007, sull'effetto di ritorno della familiarità). A questo si somma il
peso asimmetrico dell'informazione negativa: una parola sfavorevole pesa più di una favorevole
a parità di contenuto. In pratica, chi legge **«Fa male, costa troppo, ci vuole una vita»**
associa quelle tre cose allo studio, anche quando le tre schede sotto le smentiscono una per una.

Ci si aggiunge un difetto di leggibilità: quel titolo non si spiega da solo. Bisogna leggere
la riga sotto per capire che sono le frasi dei pazienti al telefono, e quindi cade la domanda 3
della griglia.

**Regola adottata:** un titolo dice quello che c'è, non quello che manca. Si scrive in positivo
anche quando la notizia è l'assenza di qualcosa: *«è tutto in piano»* invece di *«non c'è un solo
gradino»*, *«ogni strumento arriva da te sigillato»* invece di *«niente ti arriva in bocca dopo
essere stato in quella di un altro»*. `check_copy.py` segnala ogni titolo che contiene
*non, niente, nessuno, mai, senza*.

**L'unica deroga** è *«non senti niente»*, che è la frase che i pazienti scrivono da soli nelle
recensioni. Lì la negazione cancella una paura che il lettore porta con sé invece di aggiungere
un difetto al mittente, e la distinzione è proprio quella che regge tutto il resto della regola.
La deroga è scritta nel codice del controllo, non nascosta: ogni altra eccezione va discussa.

### Il titolo della homepage

Era rimasto invariato dal primo giorno perché era anche la frase di posizionamento del documento
di strategia, e questo lo aveva sottratto al giudizio. Sbagliato: la frase che vende il progetto
allo studio e la frase che accoglie un paziente impaurito non sono lo stesso testo.

| Opzione | Giudizio |
|---|---|
| «Il dentista a Genova dove sai quanto spendi e non senti niente» *(versione precedente)* | Scartata. Il soggetto è lo studio, i due vantaggi sono attaccati con un «dove» e diventano attributi di una categoria. È la formula SEO parola chiave più differenziatore, cioè esattamente il titolo che scriverebbe chiunque |
| «Entri sapendo quanto spendi. Esci senza aver sentito niente» | Scartata. Il parallelismo è bello ma «senza aver sentito niente» è una costruzione contorta |
| «Sai già come andrà, prima di cominciare» | Buona: la prevedibilità è la leva che abbassa davvero l'ansia. Ma è astratta, e non dice né il prezzo né il dolore |
| **«Sai quanto spendi prima di sederti, e non senti niente»** | **Scelta.** Tre verbi che appartengono a chi legge, i due pilastri in una frase sola, e il secondo è la frase testuale delle recensioni |

Nota SEO, perché la scelta ha un costo: «Genova» esce dall'H1. Resta nel tag `title`, nella
descrizione, nei dati strutturati con l'indirizzo completo, nella riga sotto i pulsanti, nel
titolo della sezione sui trasporti e nel piè di pagina. Il peso dell'H1 sul posizionamento locale
è molto inferiore a quello del `title`, quindi il rischio è contenuto e la scelta è reversibile
in una riga.

### Le altre riscritture di questo passaggio

| Dove | Prima | Dopo |
|---|---|---|
| Home, sezione dei tre argomenti | «Fa male, costa troppo, ci vuole una vita» | «Prima di cominciare sai cosa sentirai, quanto pagherai e quanto ci vorrà» |
| Home, scheda prezzi | «Sai la cifra prima di aprire bocca» | «Il preventivo che firmi vale fino alla fine» |
| Home, scheda sede unica | «Non ti mandiamo da nessun'altra parte» | «Cominci e finisci nello stesso studio» |
| Home, odontofobia | «Non ti chiederemo di farti coraggio» | «Puoi decidere tu quanta ansia sentire» |
| Home, équipe | «Non dovrai raccontare la tua storia tre volte» | «La tua storia la racconti una volta sola» |
| Hub trattamenti | «Non sai come si chiama quello che hai? Va bene lo stesso» | «Basta sapere dove ti fa male, al nome ci pensiamo noi» |
| Studio, sterilizzazione | «Niente ti arriva in bocca dopo essere stato in quella di un altro» | «Ogni strumento arriva da te sigillato e datato» |
| Studio, emergenze | «Cosa succede se durante una seduta ti senti male» | «Attrezzati come un ambulatorio di emergenza» |
| Studio, accesso | «Dalla strada alla poltrona non c'è un solo gradino» | «Dalla strada alla poltrona è tutto in piano» |
| Implantologia | «Perché il titanio non si "rigetta"» | «Il corpo tratta il titanio come osso» |
| Conservativa | «servono a un solo scopo: evitare l'estrazione» | «servono a tenerti il tuo dente» |
| Conservativa | «Otturazioni: perché non usiamo l'amalgama» | «Otturazioni in composito, del colore del dente» |
| Estetica | «Faccette progettate perché nessuno si accorga che li hai fatti» | «Faccette e sbiancamenti che passano per denti tuoi» |
| Estetica | «"Non voglio sembrare rifatto"» | «"Voglio che sembrino i miei"» |
| Bambini | «Alla prima visita non curiamo nulla» | «La prima visita di un bambino è una conta dei denti, e basta» |
| Urgenze | «Orari che nessuno ha» / «Se non puoi muoverti» | «Aperti anche il sabato, tutto il giorno» / «Se resti a casa, veniamo noi» |
| Igiene | «Cosa costa non farla» | «Quanto costa aspettare» |
| 404 | «Questa pagina non c'è più» | «Questa pagina si è spostata» |

Nello stesso giro sono stati sistemati i testi che nessun controllo guardava:

- **Testi alternativi delle immagini.** Erano etichette vuote: *«Situazione prima del trattamento»*
  non dice nulla a chi usa uno screen reader. Ora descrivono la fotografia
  (*«Incisivi superiori scheggiati e di colore disomogeneo»*), e i ritratti portano nome e ruolo
  invece di *«Ritratto di Dott. …»*.
- **Descrizioni per i motori di ricerca.** Quella della 404 raccontava la riorganizzazione del
  sito; quella della home dichiarava il voto 5,0, che resta un dato non verificato in autonomia.
- **`build/estrai_tutto.py`**, nuovo: mette in fila ogni stringa leggibile del sito generato,
  compresi meta, alt, aria-label, etichette dei moduli, voci di menu, testi di aiuto e piè di
  pagina. 1.700 righe. È lo strumento che ha fatto emergere questi difetti, e il motivo per cui
  l'estrattore precedente non bastava: guardava solo titoli e aperture.

---

### Il rischio della sovracorrezione

Un errore commesso mentre correggevo un altro errore, che vale la pena lasciare scritto.

Avevo tolto «La tua storia la racconti una volta sola» perché prometteva un coordinamento interno
che nessuna fonte documentava. Al suo posto ho scritto:

> ✗ «Gli specialisti, la sala raggi e il laboratorio sono allo stesso indirizzo»

Verificatissima, e inutile: uno studio dentistico ha la sala raggi al proprio indirizzo per
definizione. È la classe **C2** della tassonomia, l'asserzione che non aggiorna il *common ground*,
cioè esattamente il difetto che aveva aperto tutta questa revisione con «Le radiografie si fanno
qui» e «Il laboratorio odontotecnico è dentro». E il *dove* riporta l'origo dentro lo studio, che è
la **C3**: la stessa planimetria di «lavorano a dieci metri l'uno dall'altro», riscritta peggio.
Il tutto come titolo di una sezione che mostra dieci facce, e che quindi parlava di immobili sopra
delle persone.

**La regola che mancava:** il rimedio a un'affermazione senza fonte non è dire una cosa vera e
banale. È cercare **il fatto verificato che ha una conseguenza per chi legge**. Sostituire una
promessa inventata con un'ovvietà documentata non è un miglioramento, è un pareggio verso il basso.

Il fatto verificato con conseguenza c'era, e stava nell'export: ogni disciplina ha un clinico che
fa solo quella, e il Dott. Piccardo era odontotecnico prima di essere odontoiatra, quindi le corone
che mette le sa anche costruire. Titolo attuale: **«Per ogni disciplina c'è chi la fa tutti i
giorni»**.

`check_copy.py` ha ora la regola F12, che segnala i titoli in cui una stanza o un'attrezzatura
dello studio viene dichiarata presente nello studio.

---

### Il residuo di una promessa già cancellata

Dopo aver tolto «Chi ti visita la prima volta è chi ti seguirà fino alla fine», perché nessuna
fonte la sosteneva, il titolo della pagina team era diventato:

> ✗ «Chi ti curerà lo sai già adesso»

Tre difetti in cinque parole, più un quarto che è il peggiore.

1. **Dislocazione con clitico di ripresa** (C10): *chi ti curerà **lo** sai*. È il tratto del
   parlato che avevo già bandito e per cui avevo già scritto un rilevatore. Il rilevatore
   catturava solo la forma enfatica con «noi» posposto, quindi è passata.
2. **Metadiscorso** (C1): «lo sai già adesso» significa *questa pagina contiene l'elenco*. È la
   pagina che descrive il proprio contenuto, travestita da beneficio.
3. **Non falsificabile**: qualunque studio con una pagina team può scrivere la stessa riga.
4. **Era il residuo della promessa cancellata.** Alludeva alla continuità di cura senza
   impegnarsi: abbastanza vaga da essere difendibile, abbastanza suggestiva da far credere la
   cosa che avevo appena eliminato perché non vera. Peggio del titolo originale, non meglio.

**Regola aggiunta:** quando si toglie un'affermazione non verificata, si toglie anche la sua
ombra. Un titolo che la evoca senza dirla è più disonesto di quello che la diceva.

Titolo attuale: **«Ognuno di loro ha studiato una cosa, e continua a studiarla»**, con sotto i tre
fatti che lo reggono (Gibelli solo ortodonzia dal 2003, De Giovanni quattro pubblicazioni
indicizzate, Tuo solo bambini).

Il rilevatore F9 ora cerca il clitico di ripresa in tutti i titoli, non solo nella forma con
«noi». Nel corpo resta limitato, perché lì un clitico oggetto è italiano scritto normale e nessuna
espressione regolare sa distinguere *«se la scegli»* da una dislocazione. Applicato subito, ha
trovato altre due dislocazioni scritte da me in giornata: *«le corone che ti mette le sa anche
costruire»* e *«La TAC per l'impianto la fai nella stessa visita»*.

---

### Tre tentativi sullo stesso titolo, e il difetto che si ricicla

La pagina team ha richiesto tre riscritture, e ognuna ha sbagliato in modo diverso. Vale la pena
lasciarle tutte, perché il pattern è più istruttivo del risultato.

| Tentativo | Difetto |
|---|---|
| «Chi ti visita la prima volta è chi ti seguirà fino alla fine» | Promessa operativa non verificata, contraddetta dall'organizzazione dello studio |
| «Chi ti curerà lo sai già adesso» | Dislocazione parlata, metadiscorso, e l'ombra della promessa appena cancellata |
| «Ognuno di loro ha studiato una cosa, e continua a studiarla» | Origo dello studio, vanto di un obbligo di legge, sostantivo vago |
| **«Chi ti curerà?»** | **Scelta.** È la domanda che il lettore si sta facendo, e le dieci facce sotto sono la risposta. Una domanda non può essere ovvia né vantarsi |

**Il vanto di un obbligo** merita un nome suo, ed è la regola **F14**. La formazione continua è
obbligatoria per legge per ogni professionista sanitario italiano: presentarla come un pregio
costa zero e vale zero, esattamente come «professionalità». Il controllo automatico l'ha subito
trovata anche in una scheda di implantologia intitolata «Formazione continua», che era lì da
settimane.

**L'elenco dei campi** è la regola **F13**, e nasce da una frase che mi è passata **tre volte in
tre revisioni diverse**, ogni volta travestita:

> ✗ «Titolo esatto, ateneo che lo ha rilasciato, anno accademico»
> ✗ «Sotto ci sono i percorsi completi, con l'ateneo e l'anno di ogni titolo»
> ✗ «Ogni titolo porta l'ateneo che lo ha rilasciato e l'anno»

Sono la stessa cosa: il testo descrive la **struttura del dato** invece di dare il dato. Quando un
difetto ritorna tre volte con parole diverse, il giudizio non basta e serve una rete.

---

## 7. Il registro: F8, la scrittura che si mette in mostra

Il difetto che restava dopo tutti i passaggi precedenti non era nei contenuti ma nel **tono**.
Le frasi erano corrette, verificate, dal punto di vista giusto, e suonavano comunque sbagliate:

> ✗ «Il primo passo costa 110 euro e finisce con un foglio in mano.»
>
> ✗ «Puoi farti i conti adesso, con la cifra sotto gli occhi, invece di scoprirla da seduto
> con il tovagliolo al collo.»
>
> ✗ «Esci sapendo cosa ti aspetta e quanto ti aspetta.»
>
> ✗ «Con il tariffario completo pubblicato online, prima che tu entri.»

Tre problemi, tutti dello stesso tipo.

**È scrittura sovra-scritta.** Ogni frase cerca un'immagine: il foglio in mano, il tovagliolo al
collo, il gioco di parole su *aspetta*. Una immagine forte in una pagina si nota; una per frase
stanca, e sposta l'attenzione dall'informazione a chi l'ha scritta. La scrittura di marca che
funziona è **sotto-scritta**: dice la cosa e si ferma. «La prima visita costa 110 euro.»

**È intimità recitata.** *Farti i conti*, *aprire bocca*, *il tovagliolo al collo* sono
espressioni da bar messe in bocca a uno studio medico. Il registro colloquiale non si ottiene
scegliendo parole colloquiali: si ottiene con frasi corte e parole comuni. Un'azienda che finge
di darti del tu da amico ottiene l'effetto opposto di quello che cerca.

**Contiene frecciate.** *Invece di scoprirla da seduto con il tovagliolo al collo* è un colpo agli
altri studi travestito da immagine. Chi vende bene non nomina il concorrente, nemmeno per
allusione: espone il proprio dato e lascia fare il confronto a chi legge.

**Regola adottata.** Una frase, un'informazione. Sostantivi concreti e numeri al posto delle
metafore. Nessuna dislocazione parlata (*te la leggiamo noi*, *alla pratica pensiamo noi*),
nessuna coda ammiccante (*e basta*, *non è un dettaglio*, *ne toglie una buona metà*), nessuna
antitesi a effetto (*come disciplina, non come cortesia*). Se una frase si può togliere senza
perdere un'informazione, si toglie.

| Dove | Prima | Dopo |
|---|---|---|
| Richiamo finale, 16 pagine | «Il primo passo costa 110 euro e finisce con un foglio in mano» + «Esci sapendo cosa ti aspetta e quanto ti aspetta» | «La prima visita costa 110 euro» + «Comprende l'esame completo della bocca, le radiografie se servono, la diagnosi e il piano di cura scritto con tutti i costi» |
| Home, prezzi | «Puoi farti i conti adesso» + il tovagliolo al collo | «I prezzi sono tutti online» + «Dalla seduta di igiene alla riabilitazione su impianti. Dopo la prima visita ricevi un preventivo scritto con il totale, e quel totale vale fino alla fine della cura» |
| Home, apertura | «…Con il tariffario completo pubblicato online, prima che tu entri» | «Sedazione cosciente disponibile per ogni seduta, otto specialisti nella stessa sede, tariffario pubblico» |
| Home, prima scheda | «Il dolore lo togliamo prima che arrivi» | «Puoi fare qualunque cura in sedazione» |
| Contatti | «Hai già una panoramica? Te la leggiamo noi» | «Hai già una panoramica? Possiamo leggerla adesso» |
| Contatti | «fino alle otto e mezza» | «fino alle 20:30» |
| Recensioni, richiamo | «La prossima potrebbe essere la tua» | rimosso, usa il richiamo standard |
| Team, Dott. Piccardo | «la sedazione cosciente come disciplina, non come cortesia» | «la sedazione cosciente praticata con una formazione universitaria dedicata» |
| Paura del dentista | «La paura del dentista ha una risposta clinica, e qui la usiamo ogni giorno» | «La paura del dentista si tratta con la sedazione cosciente» |
| Bambini | «L'obiettivo non è curare: è che voglia tornare» | «L'obiettivo è solo che abbia voglia di tornare» |
| Implantologia | «non si può accorciare senza pagarla in affidabilità» | «è l'unica attesa che non si può accorciare» |
| Studio, parcheggio | «A Genova centro non è un dettaglio» | rimosso |
| Studio, tour | «arrivare in un posto che hai già visto ne toglie una buona metà» | «vedere le stanze prima di entrarci cambia molto» |

Il richiamo finale merita una nota a parte: compare in sedici pagine. Un testo che si ripete
sedici volte deve essere neutro. Una battuta letta una volta è una battuta; letta sedici volte
è un tic.

---

## 8. Controllo automatico

`build/check_copy.py` cerca nel sito generato le forme che corrispondono ai difetti elencati sopra:
formule di meta-testo, istruzioni all'utente, la costruzione «non è X, è Y», i numerali scritti
in lettere nei titoli e le ripetizioni della stessa struttura. Va eseguito prima di ogni
consegna, insieme a `check.py` e `check_contrasto.py`.

Il controllo non sostituisce il giudizio: segnala i sospetti, la decisione resta di chi scrive.
