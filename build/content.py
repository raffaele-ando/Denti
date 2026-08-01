# -*- coding: utf-8 -*-
"""Contenuti del sito Piccardo.

Tutti i dati clinici, i prezzi, i curricula e le recensioni provengono
dall'export del sito esistente e dalla scheda Google dello studio.
Nessun dato è stato inventato: dove un'informazione manca è marcata TODO.
"""

# ============================================================ dati d'impresa
STUDIO = {
    "brand": "Piccardo",
    "ragione_sociale": "Ambulatorio Dentistico Dr. Piccardo U. S.r.l.",
    "claim": "Studio odontoiatrico · Genova",
    "dir_san": "Dott. Uberto Piccardo",
    "autorizzazione": "Presidio Sanitario di Assistenza Specialistica Odontoiatrica — Autorizzazione Comune di Genova 830/2017",
    "via": "Via Maragliano 5",
    "cap": "16121",
    "citta": "Genova",
    "regione": "Liguria",
    "paese": "IT",
    "lat": 44.404043,
    "lng": 8.940488,
    "tel_display": "010 5959492",
    "tel": "+390105959492",
    "whatsapp": "393474268916",
    "whatsapp_display": "347 426 8916",
    "whatsapp_msg": "Buongiorno, avrei bisogno del vostro aiuto per il seguente motivo:",
    "email": "info@dentista.ge",  # TODO confermare con lo studio
    "orari_testo": "Lunedì – Sabato · 8:00 – 20:30",
    "sito": "https://www.dentista-genova-dottpiccardo.it",
    "booking": "http://www.miodottore.it/strutture/ambulatorio-dentistico-dr-u-piccardo-srl?utm_source=widget-clinic-50939&utm_medium=link&widget=1&fid=50939&saasonly=true",
    "gmaps": "https://www.google.com/maps/place/Dott.+U.+Piccardo+,+Dentista+Implantologia+Genova/@44.404043,8.9382993,17z",
    "recensioni_url": "https://www.google.com/maps/place/Dott.+U.+Piccardo+,+Dentista+Implantologia+Genova/@44.404043,8.9382993,17z/data=!4m7!3m6!1s0x12d343c3d1f9069b:0x930c52f023ce72d9!8m2!3d44.404043!4d8.940488!9m1!1b1",
    "voto": "5,0",
    "n_recensioni": 310,
    "voto_fb": "4,9",
    "social": {
        "instagram": "https://www.instagram.com/studio_dentistico_piccardo/",
        "facebook": "https://www.facebook.com/dentistagenova",
        "youtube": "https://www.youtube.com/@UbertoPiccardodentista",
        "linkedin": "https://www.linkedin.com/in/dentistagenova/",
        "x": "https://x.com/dentista_genova",
    },
}

ORARI = [
    ("Lunedì", "8:00 – 20:30", False),
    ("Martedì", "8:00 – 20:30", False),
    ("Mercoledì", "8:00 – 20:30", False),
    ("Giovedì", "8:00 – 20:30", False),
    ("Venerdì", "8:00 – 20:30", False),
    ("Sabato", "8:00 – 20:30", False),
    ("Domenica", "Chiuso", True),
]

# ================================================================ navigazione
MEGA = [
    ("Ho paura del dentista", [
        ("paura-del-dentista", "Paura del dentista", "Sedazione cosciente e ipnosi clinica"),
        ("urgenze", "Urgenze e dolore", "Ti riceviamo in giornata"),
    ]),
    ("Mi manca un dente", [
        ("implantologia", "Implantologia", "Oltre 4.000 impianti dal 1999"),
        ("protesi-e-corone", "Protesi e corone", "Zirconia CAD-CAM dal laboratorio interno"),
        ("chirurgia-orale", "Chirurgia orale", "Giudizio, estrazioni, parodontologia"),
    ]),
    ("Voglio un sorriso migliore", [
        ("invisalign-ortodonzia", "Invisalign e ortodonzia", "Da 125 €/mese, tasso 0"),
        ("estetica-del-sorriso", "Estetica del sorriso", "Faccette Lumineers e sbiancamento"),
    ]),
    ("Prevenzione e famiglia", [
        ("igiene-e-prevenzione", "Igiene e prevenzione", "Ogni sei mesi, senza fastidio"),
        ("cure-conservative", "Otturazioni e devitalizzazioni", "Conservare il dente, sempre"),
        ("bambini", "Bambini", "Il primo dentista si ricorda per sempre"),
    ]),
]

# ================================================================= tariffario
TARIFFARIO = [
    ("Visite e diagnosi", [
        ("Prima visita e piano di cura", "Visita completa, diagnosi e preventivo scritto", "110,00"),
        ("Visita di controllo", "", "110,00"),
    ]),
    ("Prevenzione ed estetica", [
        ("Igiene orale professionale", "Detartrasi, air-flow e lucidatura", "100,00"),
        ("Sbiancamento dei denti", "", "275,00"),
    ]),
    ("Conservativa", [
        ("Otturazione media", "", "130,00"),
        ("Otturazione estesa", "", "160,00"),
        ("Otturazione estetica su denti anteriori", "", "160,00"),
        ("Ricostruzione preprotesica", "", "220,00"),
    ]),
    ("Endodonzia", [
        ("Devitalizzazione — 1 canale", "", "160,00"),
        ("Devitalizzazione — 2 canali", "", "210,00"),
        ("Devitalizzazione — 3 canali", "", "310,00"),
        ("Ritrattamento canalare", "", "380,00"),
        ("Apicectomia", "", "350,00"),
        ("Perno moncone", "", "270,00"),
    ]),
    ("Chirurgia", [
        ("Estrazione semplice", "", "110,00"),
        ("Estrazione complessa", "", "160,00"),
        ("Estrazione ottavo incluso mucoso", "Dente del giudizio", "270,00"),
        ("Estrazione ottavo incluso osseo", "Dente del giudizio", "400,00"),
        ("Intervento parodontale", "", "350,00"),
        ("Allungamento di corona clinica", "", "250,00"),
        ("Innesto di osso", "In base all'estensione", "500,00 – 1.500,00"),
    ]),
    ("Implantologia", [
        ("Impianto dentale", "", "770,00"),
        ("Impianto post-estrattivo", "", "900,00"),
        ("Perno per impianto", "", "270,00"),
        ("Corona su impianto", "", "770,00"),
    ]),
    ("Protesi fissa", [
        ("Corona in zirconia", "Realizzata nel laboratorio interno", "770,00"),
        ("Corona in ceramica con attacco", "", "1.100,00"),
        ("Corona provvisoria in resina", "", "120,00"),
        ("Corona provvisoria in resina armata", "", "220,00"),
    ]),
    ("Protesi mobile", [
        ("Protesi totale per arcata", "", "1.650,00"),
        ("Protesi parziale con ganci o attacchi", "Per arcata", "1.870,00"),
        ("Scheletrato per arcata", "", "1.870,00"),
        ("Overdenture su impianti", "", "2.200,00"),
        ("Ribasatura per arcata", "", "440,00"),
        ("Riparazione protesi o aggiunta di un dente", "", "160,00"),
    ]),
    ("Altro", [
        ("Bite", "", "330,00"),
    ]),
]

CONVENZIONI = [
    "FASI", "FASI Open", "FASDAC", "FASIE", "FISDE", "FASCHIM", "PrimaDent",
    "Sigma Dental", "Help Card", "Pronto Care", "UniCralBox", "Assirete",
    "Caspie", "Medicina Privata", "Fondo Salute", "Miglior Salute",
    "CoopSalute", "Pubblica Assistenza La Lanterna ONLUS", "CRAL RINA",
]

# ================================================================ recensioni
# Testi pubblici dalla scheda Google dello studio. <b> evidenzia il passaggio
# che porta l'informazione decisiva per il lettore.
RECENSIONI = [
    dict(nome="Fabio Burlando", quando="2 anni fa", tema="paura", guide=True,
         testo="58 primavere sulle spalle e prima estrazione di dente del giudizio: prima anestesia come non sentirla, seconda un leggero fastidio di 5 secondi. <b>Non ho sentito niente!</b>"),
    dict(nome="Antonella Grazia Rodà", quando="1 anno fa", tema="competenza",
         testo="Studio dentistico di altissimo livello. Il dottor Piccardo si distingue per la professionalità e per la <b>capacità di mettere a proprio agio i pazienti</b>, trasmettendo sicurezza e tranquillità. Il trattamento è stato impeccabile, con risultati che hanno superato le mie aspettative."),
    dict(nome="Ciurlo Alessandro", quando="1 anno fa", tema="prezzi", guide=True,
         testo="Mi ha risolto in poco tempo e in modo economico un problema che si trascinava da tempo, dopo aver consultato <b>diversi altri pareri che prevedevano preventivi troppo onerosi</b>, soluzioni invasive e percorsi di cura molto lunghi."),
    dict(nome="Eri V", quando="2 anni fa", tema="estetica",
         testo="Tra capsule e gummy smile il mio sorriso non era dei più belli. La Dott.ssa Gibelli ha allineato i denti con Invisalign, poi il Dott. Leonida la gengivectomia laser. <b>Ora quando sorrido i miei familiari mi dicono che i denti sembrano veri.</b> Sono molto esigente: non mi è mai piaciuto l'effetto dei denti finti."),
    dict(nome="Giancarlo Podda", quando="6 anni fa", tema="sicurezza", guide=True,
         testo="<b>L'igiene è uno dei punti di forza, da fare invidia a molte sale operatorie, direi quasi maniacale.</b> Essendo un soggetto allergico ho guardato alla gestione dell'emergenza: lo studio è dotato di defibrillatore e carrello attrezzatissimo, e posso confermarlo essendo un professionista del settore."),
    dict(nome="Serena Gaggero", quando="8 anni fa", tema="prezzi",
         testo="Ho fatto ortodonzia con Invisalign, un intervento di implantologia e i trattamenti di igiene semestrali. <b>Chiarezza nei preventivi e nessuna sorpresa in corso d'opera.</b> Lo consiglio vivamente."),
    dict(nome="Tina Mamola", quando="8 anni fa", tema="paura",
         testo="Ho un passato, fin da bambina, colmo di sedute dai dentisti, molti dei quali mi hanno lasciato un vero trauma. <b>Oggi vado tranquilla dal Dr. Piccardo e per me questo è già un enorme successo.</b> Sto eseguendo lavori complessi ma non ho mai avvertito né dolore né timore."),
    dict(nome="Marco Penso", quando="7 anni fa", tema="tecnologia",
         testo="Mi è stato fatto un impianto con una tecnologia digitale: <b>scansione tridimensionale della bocca, elaborazione al computer e stampa in pochi minuti.</b> Messo in bocca calzava come un guanto."),
    dict(nome="Mariachiara Allasia", quando="8 anni fa", tema="ambiente", guide=True,
         testo="L'ambiente è ordinato, pulito e soprattutto <b>tranquillizzante — cosa non da poco, per uno studio dentistico</b>. Apprezzabilissima l'attenzione alla salute generale, ad esempio il controllo delle mucose per la prevenzione del cancro orale."),
    dict(nome="Maria Angela Bruzzone", quando="6 anni fa", tema="implantologia",
         testo="Premesso che ho la soglia del dolore molto bassa, <b>ho fatto otto impianti e mi sono trovato benissimo</b>, super coccolato dal dott. Piccardo e da tutto lo staff. Grazie, mi avete cambiato la vita."),
    dict(nome="Renato Dini", quando="14 anni fa", tema="prezzi",
         testo="Consiglio a tutti il dott. Piccardo: <b>onesto — ricevuta fiscale sempre, anche se non richiesta, e del valore effettivo del pagamento</b> — altamente professionale e gentile."),
    dict(nome="Cristina Bazzurro", quando="6 anni fa", tema="bambini",
         testo="Molto bravi e gentili, grande pulizia e soprattutto pazienti. <b>Grazie a loro il mio bimbo vive l'appuntamento dal dentista senza più paura</b> e con grande serenità."),
    dict(nome="Roberta Lungarini", quando="2 anni fa", tema="paura",
         testo="<b>La mia atavica paura del dentista si è ridimensionata</b> grazie alla capacità di mettere totalmente a proprio agio il paziente. Struttura curata nel dettaglio e grande competenza di tutta l'équipe."),
    dict(nome="Andrea Carratù", quando="6 anni fa", tema="tecnologia",
         testo="Prezzi onestissimi ma, cosa più importante, grande professionalità. <b>I raggi si fanno lì, al momento, evitando il fastidio di andare in giro.</b> Anche con i bambini sono straordinari."),
    dict(nome="Alberto Zotti", quando="4 anni fa", tema="disponibilita", guide=True,
         testo="Davvero cortesi e molto professionali: <b>mi hanno ricevuto il sabato mattina con meno di 24 ore di preavviso.</b>"),
    dict(nome="Andrea Lacopo", quando="12 anni fa", tema="competenza", guide=True,
         testo="Professionisti che hanno in dono quel tocco di umanità che accorcia la distanza tra medico e paziente: <b>con l'operatore si instaura un rapporto empatico da cui deriva agio e fiducia.</b>"),
    dict(nome="Danilo Gazza", quando="12 anni fa", tema="ortodonzia",
         testo="Cliente da 10 anni così come tutti i miei familiari. <b>Terapia con Invisalign, risultato eccezionale</b> e interventi non invasivi."),
    dict(nome="Michela Zavaglia", quando="7 anni fa", tema="ortodonzia",
         testo="Mi sono affidata a loro per Invisalign: <b>appena avevo un problema l'hanno subito risolto.</b> Persone gentili, disponibili, affidabili."),
]

TEMI_RECENSIONI = [
    ("Avanguardia", 18), ("Ambiente", 13), ("Prezzi", 13), ("Competenza", 12),
    ("Cordialità", 9), ("Pulizia", 7), ("Igiene", 7), ("Onestà", 6), ("Invisalign", 5),
]

# ====================================================================== team
TEAM = [
    dict(
        slug="uberto-piccardo", nome="Dott. Uberto Piccardo",
        ruolo="Direttore Sanitario · Chirurgo orale, implantologo, protesista, sedazionista",
        albo="Odontoiatra dal 1997",
        sintesi="Fondatore dello studio. Sei master universitari di II livello, oltre 4.000 impianti osteointegrati e la sedazione cosciente come disciplina, non come cortesia.",
        cv=[
            ("1992", "Diploma di <b>Odontotecnico</b>, Istituto P. Gaslini — 60/60"),
            ("1997", "Laurea in <b>Odontoiatria e Protesi Dentaria</b>, Università di Genova — 108/110"),
            ("2002", "Corso di Chirurgia Anatomica applicata all'Implantologia, <b>Université Claude Bernard</b>, Lione"),
            ("2003-04", "Perfezionamento universitario in <b>Implantoprotesi</b>, Università di Genova"),
            ("2013", "Esecutore <b>BLSD</b> — Basic Life Support Defibrillation (rinnovato Padova 2015)"),
            ("2013-14", "Master universitario di II livello in <b>Implantoprotesi</b>, Università di Genova — 110/110"),
            ("2014-15", "Master universitario di II livello in <b>Sedazione ed emergenze in odontoiatria</b>, Università di Padova"),
            ("2015", "Sedazionista presso la <b>Clinica Odontoiatrica Universitaria di Padova</b>"),
            ("2015-16", "Master universitario di II livello in <b>Chirurgia orale e d'urgenza</b>, Università di Pisa"),
            ("2016", "Chirurgo orale presso la <b>Clinica Odontoiatrica di Pisa</b>"),
            ("2017", "Diploma di <b>Ipnologo</b> — Corso di Ipnosi Clinica e Comunicazione Ipnotica, CIICS Torino"),
            ("2018-19", "Master universitario di II livello in <b>Direzione e Management delle Aziende Sanitarie</b>, Università LUM Jean Monnet"),
            ("2021-22", "Master universitario di II livello in <b>Implantologia Digitale</b>, Università di Padova"),
        ],
        pubblicazioni=[
            "U. Piccardo, M. M. Rossini — <i>Carico immediato intraforaminale: tecnica per una realizzazione rapida della protesi provvisoria</i>. Implant Journal 2004; 03, p. 5.",
            "P. Cortella, R. Garrone, U. Piccardo, M. M. Rossini — <i>Teeth in a Day: Placement of Implants with Immediate Load into Fresh Extraction Sites Using Flapless Surgery</i>. Academy of Osseointegration, Program Guide 2004, p. 58.",
        ],
        societa=["A.I.N.O.S. — Anestesia Narcodontostomatologica", "A.I.S.O.D. — Sedazionisti Odontoiatri", "A.I.O. — Associazione Italiana Odontoiatri", "C.I.I.C.S. — Ipnosi Clinica Sperimentale"],
        tratta=["implantologia", "chirurgia-orale", "protesi-e-corone", "paura-del-dentista"],
    ),
    dict(
        slug="francesca-gibelli", nome="Dott.ssa Francesca Gibelli",
        ruolo="Ortodonzista · Specialista in Ortognatodonzia · Perfezionata Invisalign",
        albo="Specialista dal 2010",
        sintesi="Specializzazione in Ortognatodonzia con 70/70 a Milano e perfezionamento universitario in tecnica Invisalign. Dal 2003 si occupa esclusivamente di ortodonzia.",
        cv=[
            ("1998-2003", "Laurea in <b>Odontoiatria e Protesi Dentaria</b>, Università di Genova — 110/110 e lode, tesi sperimentale in ortodonzia"),
            ("2003", "Abilitazione all'esercizio della professione"),
            ("2003-07", "Medico frequentatore presso la <b>U.O. Ortodonzia dell'Ospedale San Martino</b>"),
            ("2003-04", "Corso annuale di Ortognatodonzia generale — Prof. A. Silvestrini Biavati"),
            ("2003-10", "Libera professione a Genova e Milano, <b>esclusivamente ortodonzia</b>"),
            ("2007-10", "Professore a contratto, Corso di Laurea in Odontoiatria: <i>moderne tecniche ortodontiche nei casi clinici complessi</i>"),
            ("2010", "<b>Specializzazione in Ortognatodonzia</b>, Università di Milano — 70/70, Dir. Prof. G. Farronato"),
            ("2014-15", "Perfezionamento universitario in <b>tecnica Invisalign</b>"),
        ],
        pubblicazioni=[], societa=[],
        tratta=["invisalign-ortodonzia", "estetica-del-sorriso"],
    ),
    dict(
        slug="emanuele-degiovanni", nome="Dott. Emanuele De Giovanni",
        ruolo="Parodontologo e chirurgo orale",
        albo="Odontoiatra dal 2020",
        sintesi="Quattro pubblicazioni scientifiche indicizzate, specializzando in Chirurgia bucco-maxillo-facciale, medico frequentatore alla Maxillo-Facciale del Policlinico San Martino.",
        cv=[
            ("2013", "Laurea in <b>Scienze Motorie, Sport e Salute</b>, Università di Genova"),
            ("2020", "Laurea in <b>Odontoiatria e Protesi Dentaria</b>, Università di Genova — 110/110 con lode e dignità di stampa"),
            ("2020", "Abilitazione alla professione — 60/60"),
            ("2021", "Assegnista di ricerca in Malattie Odontostomatologiche, Università di Genova (DISC)"),
            ("2021", "Tutor didattico, tirocinio clinico — Corso di Laurea in Odontoiatria, Università di Genova"),
            ("2023 →", "Medico frequentatore, <b>U.O. Chirurgia Maxillo-Facciale, Policlinico San Martino</b>"),
            ("2023", "Corso di Chirurgia parodontale e mucogengivale — Prof. G. Zucchelli"),
            ("2024 →", "Specializzando in <b>Chirurgia bucco-maxillo-facciale</b>, Università FACOP, San Paolo (Brasile)"),
            ("2024 →", "Chirurgo orale e implantologo presso lo studio"),
        ],
        pubblicazioni=[
            "Pesce P, Menini M, Santori G, <b>De Giovanni E</b>, Bagnasco F, Canullo L. <i>Photo and plasma activation of dental implant titanium surfaces. A systematic review with meta-analysis of pre-clinical studies.</i> J Clin Med. 2020;9(9):2817.",
            "Menini M, <b>De Giovanni E</b>, Bagnasco F, Delucchi F, Pera F, Baldi D, Pesce P. <i>Salivary micro-RNA and oral squamous cell carcinoma: a systematic review.</i> J Pers Med. 2021;11(2):101.",
            "Delucchi F, <b>De Giovanni E</b>, Pesce P, Bagnasco F, Pera F, Baldi D, Menini M. <i>Framework materials for full-arch implant-supported rehabilitations: a systematic review of clinical studies.</i> Materials. 2021;14:3251.",
            "Pesce P, Del Fabbro M, Menini M, <b>De Giovanni E</b>, Annunziata M, Khijmatgar S, Canullo L. <i>Effects of abutment materials on peri-implant soft tissue health and stability: a network meta-analysis.</i> J Prosthodont Res. 2023.",
        ],
        societa=[],
        tratta=["chirurgia-orale", "implantologia"],
    ),
    dict(
        slug="federico-parodi", nome="Dott. Federico Parodi Baiardi",
        ruolo="Conservativa, endodonzia e protesi",
        albo="Odontoiatra", sintesi="Si occupa di ciò che permette di non arrivare mai all'estrazione: otturazioni, devitalizzazioni e riabilitazioni protesiche.",
        cv=[], pubblicazioni=[], societa=[],
        tratta=["cure-conservative", "protesi-e-corone"],
    ),
    dict(
        slug="ludovica-tuo", nome="Dott.ssa Ludovica Tuo",
        ruolo="Pedodonzia e odontoiatria infantile",
        albo="Odontoiatra", sintesi="Segue i bambini dalla comparsa del primo dentino: prevenzione, fluoroprofilassi e intercettazione precoce dei problemi ortodontici.",
        cv=[], pubblicazioni=[], societa=[],
        tratta=["bambini"],
    ),
    dict(
        slug="gianluca-grasso", nome="Dott. Gianluca Grasso",
        ruolo="Igienista dentale", albo="Laurea in Igiene Dentale",
        sintesi="Igiene professionale, mantenimento parodontale e implantare, istruzione alle manovre domiciliari.",
        cv=[], pubblicazioni=[], societa=[], tratta=["igiene-e-prevenzione"],
    ),
    dict(
        slug="carmela-pulitano", nome="Dott.ssa Carmela Pulitanò",
        ruolo="Igienista dentale", albo="Laurea in Igiene Dentale",
        sintesi="Igiene professionale e prevenzione, con particolare attenzione ai pazienti con sensibilità elevata.",
        cv=[], pubblicazioni=[], societa=[], tratta=["igiene-e-prevenzione"],
    ),
    dict(
        slug="carlotta-fabiano", nome="Carlotta Fabiano",
        ruolo="Segreteria e amministrazione", albo="",
        sintesi="La prima voce che senti al telefono. Gestisce appuntamenti, preventivi, convenzioni e pratiche di finanziamento.",
        cv=[], pubblicazioni=[], societa=[], tratta=[],
    ),
    dict(
        slug="erika-carbone", nome="Erika Carbone",
        ruolo="Assistente alla poltrona", albo="", sintesi="",
        cv=[], pubblicazioni=[], societa=[], tratta=[],
    ),
    dict(
        slug="virginia", nome="Virginia",
        ruolo="Assistente alla poltrona", albo="", sintesi="",
        cv=[], pubblicazioni=[], societa=[], tratta=[],
    ),
]

TEAM_BY_SLUG = {m["slug"]: m for m in TEAM}
