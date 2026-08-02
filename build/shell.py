# -*- coding: utf-8 -*-
"""Impalcatura comune: head, header, drawer, footer, componenti condivisi."""

import json
from content import STUDIO, MEGA, ORARI, CONVENZIONI
from ui import ico, marchio, stelle

S = STUDIO


def rel(depth, path=""):
    """Percorso relativo alla radice del sito."""
    return ("../" * depth) + path


def wa_link():
    from urllib.parse import quote
    return f"https://api.whatsapp.com/send?phone={S['whatsapp']}&text={quote(S['whatsapp_msg'])}"


# ═══════════════════════════════════════════════════════════════════ HEAD
def head(depth, titolo, descrizione, canonical, schema_extra=None,
         og_img="assets/img/og-default.png", tema_scuro=False):
    r = rel(depth)
    schema = {
        "@context": "https://schema.org",
        "@type": "Dentist",
        "@id": S["sito"] + "/#studio",
        "name": f"{S['brand']}. Studio odontoiatrico",
        "legalName": S["ragione_sociale"],
        "url": S["sito"],
        "telephone": S["tel"],
        "priceRange": "€€",
        "image": S["sito"] + "/assets/img/team/uberto-piccardo.webp",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": S["via"],
            "postalCode": S["cap"],
            "addressLocality": S["citta"],
            "addressRegion": S["regione"],
            "addressCountry": S["paese"],
        },
        "geo": {"@type": "GeoCoordinates", "latitude": S["lat"], "longitude": S["lng"]},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "08:00", "closes": "20:30",
        }],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "5.0",
            "reviewCount": S["n_recensioni"],
            "bestRating": "5",
        },
        "medicalSpecialty": ["Dentistry", "OralSurgery", "Orthodontic"],
        "availableService": [
            {"@type": "MedicalProcedure", "name": n} for n in
            ["Implantologia dentale", "Ortodonzia invisibile Invisalign", "Sedazione cosciente",
             "Chirurgia orale", "Igiene orale professionale", "Protesi dentaria",
             "Estetica dentale", "Odontoiatria infantile"]
        ],
        "sameAs": list(S["social"].values()),
    }
    blocchi = [schema] + (schema_extra or [])
    ld = "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False, separators=(",", ":"))}</script>'
        for b in blocchi
    )
    return f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titolo}</title>
<meta name="description" content="{descrizione}">
<link rel="canonical" href="{S['sito']}/{canonical}">
<meta name="theme-color" content="#FBFAF7" media="(prefers-color-scheme: light)">
<meta name="format-detection" content="telephone=yes">

<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:site_name" content="{S['brand']}. Studio odontoiatrico Genova">
<meta property="og:title" content="{titolo}">
<meta property="og:description" content="{descrizione}">
<meta property="og:url" content="{S['sito']}/{canonical}">
<meta property="og:image" content="{S['sito']}/{og_img}">
<meta name="twitter:card" content="summary_large_image">

<link rel="preload" href="{r}assets/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{r}assets/fonts/manrope-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/css/base.css">
<link rel="stylesheet" href="{r}assets/css/components.css">
<link rel="icon" href="{r}assets/img/brand/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/img/brand/icon-180.png">
{ld}
</head>
<body class="{'hero-scuro' if tema_scuro else ''}">
<a class="skip-link" href="#main">Vai al contenuto</a>'''


# ═════════════════════════════════════════════════════════════════ HEADER
def _mega_menu(depth):
    r = rel(depth)
    cols = ""
    for titolo, voci in MEGA:
        links = "".join(
            f'<a class="mega__link" href="{r}trattamenti/{slug}.html">{nome}<span>{sub}</span></a>'
            for slug, nome, sub in voci
        )
        cols += f'<div class="mega__col"><h5>{titolo}</h5>{links}</div>'
    cols += f'''<div class="mega__promo">
  <div>
    <h5>Prima visita</h5>
    <p class="mt-2">Visita completa, diagnosi e piano di cura scritto. Il preventivo che ricevi è quello che paghi.</p>
    <div class="stat-n mt-4" style="color:#F2E9D8;font-size:2.2rem">110&nbsp;€</div>
  </div>
  <a class="link-arrow" style="color:var(--brand-200)" href="{r}prezzi.html">Tutto il tariffario {ico('freccia')}</a>
</div>'''
    return f'<div class="mega" role="region" aria-label="Tutti i trattamenti">{cols}</div>'


def header(depth, current=""):
    r = rel(depth)
    voci = [("trattamenti", "Trattamenti", True), ("studio", "Lo studio", False),
            ("team", "Il team", False), ("prezzi", "Prezzi", False), ("contatti", "Contatti", False)]
    nav = ""
    for slug, label, mega in voci:
        cur = ' aria-current="page"' if current == slug else ""
        if mega:
            nav += (f'<li class="nav__item has-mega">'
                    f'<a class="nav__link" href="{r}trattamenti.html" aria-expanded="false"{cur}>'
                    f'{label}{ico("chevron", "nav__chev")}</a>{_mega_menu(depth)}</li>')
        else:
            nav += f'<li class="nav__item"><a class="nav__link" href="{r}{slug}.html"{cur}>{label}</a></li>'

    return f'''<header class="header">
<div class="wrap header__inner">
  <a class="brand" href="{r}index.html" aria-label="{S['brand']}: home">
    {marchio()}
    <span class="brand__type">
      <span class="brand__name">{S['brand']}</span>
      <span class="brand__sub">Studio odontoiatrico</span>
    </span>
  </a>
  <nav class="header__nav" aria-label="Principale"><ul class="nav">{nav}</ul></nav>
  <div class="header__actions">
    <a class="tel-link" href="tel:{S['tel']}">{ico('telefono')}<span>{S['tel_display']}</span></a>
    <a class="btn btn--sm hide-mobile" href="{S['booking']}" target="_blank" rel="noopener">Prenota la prima visita</a>
    <button class="burger" aria-label="Apri il menu" aria-expanded="false" aria-controls="drawer"><span></span></button>
  </div>
</div>
</header>
{_drawer(depth)}
{_mobile_bar()}'''


def _drawer(depth):
    r = rel(depth)
    gruppi = ""
    for titolo, voci in MEGA:
        links = "".join(f'<a href="{r}trattamenti/{slug}.html">{nome}</a>' for slug, nome, _ in voci)
        gruppi += f'''<div class="drawer__group">
  <button class="drawer__head" aria-expanded="false">{titolo}{ico('chevron')}</button>
  <div class="drawer__panel"><div>{links}</div></div>
</div>'''
    return f'''<div class="drawer" id="drawer">
<div class="drawer__group"><a class="drawer__head" href="{r}trattamenti.html">Tutti i trattamenti</a></div>
{gruppi}
<div class="drawer__group"><a class="drawer__head" href="{r}studio.html">Lo studio</a></div>
<div class="drawer__group"><a class="drawer__head" href="{r}team.html">Il team</a></div>
<div class="drawer__group"><a class="drawer__head" href="{r}prezzi.html">Prezzi</a></div>
<div class="drawer__group"><a class="drawer__head" href="{r}recensioni.html">Recensioni</a></div>
<div class="drawer__group"><a class="drawer__head" href="{r}contatti.html">Contatti</a></div>
<div class="drawer__cta">
  <a class="btn btn--block" href="{S['booking']}" target="_blank" rel="noopener">{ico('calendario')} Prenota online</a>
  <a class="btn btn--ghost btn--block" href="tel:{S['tel']}">{ico('telefono')} {S['tel_display']}</a>
</div>
</div>'''


def _mobile_bar():
    return f'''<nav class="mobile-bar" aria-label="Azioni rapide">
  <a href="tel:{S['tel']}">{ico('telefono')}Chiama</a>
  <a href="{wa_link()}" target="_blank" rel="noopener">{ico('whatsapp')}WhatsApp</a>
  <a class="is-primary" href="{S['booking']}" target="_blank" rel="noopener">{ico('calendario')}Prenota</a>
</nav>'''


# ═════════════════════════════════════════════════════════════════ FOOTER
def cta_finale(depth, titolo="Il primo passo costa 110 euro e finisce con un foglio in mano",
               testo="Dentro ci sono l'esame completo della bocca, le radiografie se servono, la diagnosi e il piano di cura con i costi già scritti. Esci sapendo cosa ti aspetta e quanto ti aspetta."):
    return f'''<section class="section">
<div class="wrap">
  <div class="cta-final" data-reveal>
    <span class="eyebrow is-bare" style="color:var(--brand-200)">Prenota</span>
    <h2 class="mt-4">{titolo}</h2>
    <p class="lead mt-4">{testo}</p>
    <div class="cta-final__btns">
      <a class="btn btn--lg" href="{S['booking']}" target="_blank" rel="noopener">{ico('calendario')} Prenota online</a>
      <a class="btn btn--lg btn--ghost" href="tel:{S['tel']}">{ico('telefono')} {S['tel_display']}</a>
      <a class="btn btn--lg btn--ghost" href="{wa_link()}" target="_blank" rel="noopener">{ico('whatsapp')} WhatsApp</a>
    </div>
    <p class="xs mt-6" style="color:var(--su-scuro-3)">{S['orari_testo']} · {S['via']}, {S['citta']} · 3 posti auto gratuiti</p>
  </div>
</div>
</section>'''


def footer(depth):
    r = rel(depth)
    tratt_links = ""
    for _, voci in MEGA:
        for slug, nome, _ in voci:
            tratt_links += f'<li><a href="{r}trattamenti/{slug}.html">{nome}</a></li>'
    soc = "".join(
        f'<a href="{u}" target="_blank" rel="noopener" aria-label="{k.capitalize()}">{ico(k)}</a>'
        for k, u in S["social"].items()
    )
    return f'''<footer class="footer">
<div class="wrap">
  <div class="footer__grid">
    <div>
      <a class="brand" href="{r}index.html">{marchio()}
        <span class="brand__type"><span class="brand__name">{S['brand']}</span>
        <span class="brand__sub">Studio odontoiatrico</span></span></a>
      <p class="mt-6">{S['ragione_sociale']}<br>{S['via']} · {S['cap']} {S['citta']}</p>
      <p class="mt-4"><a href="tel:{S['tel']}"><b>{S['tel_display']}</b></a><br>
      WhatsApp {S['whatsapp_display']}</p>
      <p class="mt-4" style="color:var(--su-scuro-3);font-size:var(--fs-xs)">{S['orari_testo']}</p>
      <div class="socials mt-6">{soc}</div>
    </div>
    <div>
      <h5>Trattamenti</h5>
      <ul>{tratt_links}</ul>
    </div>
    <div>
      <h5>Lo studio</h5>
      <ul>
        <li><a href="{r}studio.html">Tecnologia e ambienti</a></li>
        <li><a href="{r}studio.html#sterilizzazione">Sterilizzazione</a></li>
        <li><a href="{r}studio.html#laboratorio">Laboratorio interno</a></li>
        <li><a href="{r}studio.html#sicurezza">Sicurezza e emergenze</a></li>
        <li><a href="{r}studio.html#accessibilita">Accessibilità</a></li>
        <li><a href="{r}team.html">Il team</a></li>
        <li><a href="{r}recensioni.html">Recensioni</a></li>
      </ul>
    </div>
    <div>
      <h5>Prezzi e accesso</h5>
      <ul>
        <li><a href="{r}prezzi.html">Tariffario completo</a></li>
        <li><a href="{r}prezzi.html#finanziamenti">Finanziamenti a tasso 0</a></li>
        <li><a href="{r}prezzi.html#convenzioni">Convenzioni ({len(CONVENZIONI)})</a></li>
        <li><a href="{r}prezzi.html#preventivo">Preventivo online gratuito</a></li>
        <li><a href="{r}contatti.html">Dove siamo e parcheggio</a></li>
        <li><a href="{S['booking']}" target="_blank" rel="noopener">Prenotazione online</a></li>
      </ul>
      <p class="mt-6" style="font-size:var(--fs-xs);color:var(--su-scuro-3)">{S['autorizzazione']}<br>
      Direttore Sanitario: {S['dir_san']}</p>
    </div>
  </div>
  <div class="footer__legal">
    <span>© <span data-year></span> {S['ragione_sociale']} · P. IVA da inserire</span>
    <span><a href="{r}note-legali.html">Note legali e privacy</a> · <a href="{r}note-legali.html#cookie">Cookie</a> · <a href="{r}sitemap.xml">Sitemap</a></span>
  </div>
</div>
</footer>
<script src="{rel(depth)}assets/js/app.js" defer></script>
</body>
</html>'''


# ═══════════════════════════════════════════════════════════ COMPONENTI
# Ogni scena illustrata è stata sostituita da un'icona in filigrana: il
# segnaposto deve leggersi come una scheda di produzione, non come un disegno.
_ICONA_SCENA = {
    "poltrona": "scan", "maschera": "calma", "laboratorio": "corona",
    "radiologia": "scan", "sterilizzazione": "scudo", "ingresso": "pin",
    "parcheggio": "auto", "bimbi": "bimbo", "equipe": "gruppo",
    "mascherine": "mascherina", "faccetta": "scintilla", "video": "play",
    "prima-dopo": "scambio",
}


def media_slot(tipo, testo, nota, ar="3/2", dark=False, scena="poltrona", extra=""):
    """Scheda di scatto: tiene il posto di un media ancora da produrre.

    Non è un'illustrazione né un rettangolo grigio, ma una scheda di
    produzione: crocini di taglio agli angoli, formato dichiarato, soggetto in
    evidenza e nota tecnica per il fotografo. Comunica che quel vuoto è una
    decisione, non una dimenticanza, e resta cercabile con `data-shot`.
    """
    d = " shotcard--dark" if dark else ""
    v = "video" if tipo.lower().startswith("video") else "foto"
    etichetta = "Video da produrre" if v == "video" else "Fotografia da produrre"
    return f'''<figure class="shotcard{d}" data-reveal="fade" data-shot="{testo}" style="--ar:{ar}"{extra}>
  <span class="shotcard__ghost" aria-hidden="true">{ico(_ICONA_SCENA.get(scena, "camera"))}</span>
  <span class="shotcard__kind">{ico("video" if v == "video" else "camera")}{etichetta}</span>
  <span class="shotcard__ratio">{ar.replace("/", ":")}</span>
  <figcaption class="shotcard__body">
    <p class="shotcard__subj">{testo}</p>
    <p class="shotcard__spec">{nota}</p>
  </figcaption>
</figure>'''


def rating_badge(depth=0, dark=False):
    r = rel(depth)
    col = "color:var(--su-scuro)" if dark else ""
    return f'''<a class="rating-inline" style="{col}" href="{r}recensioni.html">
  {stelle()}<b>{S['voto']}</b><span class="sep">·</span><span style="font-weight:500">{S['n_recensioni']} recensioni Google</span>
</a>'''


def breadcrumb(depth, voci):
    """voci: lista di (label, href|None)."""
    r = rel(depth)
    out = f'<li><a href="{r}index.html">Home</a></li>'
    for label, href in voci:
        out += f'<li><a href="{r}{href}">{label}</a></li>' if href else f'<li>{label}</li>'
    return f'<nav aria-label="Percorso"><ol class="breadcrumb">{out}</ol></nav>'


def orari_lista():
    out = ""
    for g, o, chiuso in ORARI:
        c = ' class="is-closed"' if chiuso else ""
        out += f'<li{c}><b>{g}</b><span>{o}</span></li>'
    return f'<ul class="hours">{out}</ul>'
