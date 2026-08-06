# -*- coding: utf-8 -*-
"""Homepage."""

from content import STUDIO as S, RECENSIONI, TEMI_RECENSIONI, TEAM, CONVENZIONI
from trattamenti import TRATT_BY_SLUG
from ui import ico, stelle
from shell import (head, header, footer, cta_finale, media_slot, rating_badge,
                   rel, wa_link)
from componenti import (blocco_recensioni, striscia_team, prima_dopo,
                        blocco_convenzioni, mappa)


def _pilastro(icona, titolo, testo, link, label, cls="", guida=False):
    g = " card--lead" if guida else ""
    return f'''<article class="card card--pillar card--hover{g}" data-reveal>
  <div class="icon-box {cls}">{ico(icona)}</div>
  <h3>{titolo}</h3>
  <p>{testo}</p>
  <div class="card__foot"><a class="link-arrow" href="{link}">{label} {ico('freccia')}</a></div>
</article>'''


def _tcard(slug, depth=0):
    t = TRATT_BY_SLUG[slug]
    prezzo = t["prezzi"][0] if t.get("prezzi") else None
    riga = ""
    if prezzo:
        riga = f'<div class="tcard__price"><span>{prezzo[0]}</span><b>{prezzo[1].replace(",00","")} €</b></div>' \
            if "€" not in prezzo[1] and "/" not in prezzo[1] else \
            f'<div class="tcard__price"><span>{prezzo[0]}</span><b>{prezzo[1]}</b></div>'
    badge = '<span class="pill pill--accent">Alta specializzazione</span>' if t.get("premium") else ""
    return f'''<article class="tcard" data-reveal>
  <div class="tcard__top"><div class="icon-box">{ico(t['icona'])}</div>{badge}</div>
  <h3>{t['nav']}</h3>
  <p>{t['breve']}</p>
  {riga}
  <a class="tcard__link" href="{rel(depth)}trattamenti/{slug}.html"><span class="sr-only">{t['nav']}</span></a>
</article>'''


INTENZIONI = [
    ("Ho paura", ["paura-del-dentista", "igiene-e-prevenzione", "bambini"]),
    ("Mi manca un dente", ["implantologia", "protesi-e-corone", "chirurgia-orale"]),
    ("Voglio un sorriso migliore", ["invisalign-ortodonzia", "estetica-del-sorriso", "protesi-e-corone"]),
    ("Ho un dolore adesso", ["urgenze", "cure-conservative", "chirurgia-orale"]),
    ("Prevenzione e famiglia", ["igiene-e-prevenzione", "bambini", "cure-conservative"]),
]


def render():
    r = ""
    out = head(
        0,
        "Dentista a Genova centro: implantologia, Invisalign, sedazione | Studio Piccardo",
        "Studio odontoiatrico in Via Maragliano 5, Genova. Implantologia, ortodonzia invisibile e cure con sedazione cosciente. Tariffario pubblico, 310 recensioni Google. Lun–sab 8:00–20:30.",
        "",
    )
    out += header(0, "home")
    out += '<main id="main">'

    # ───────────────────────────────────────────────────────────── HERO
    out += f'''
<section class="hero">
  <div class="aura aura--1"></div><div class="aura aura--2"></div>
  <div class="wrap hero__grid">
    <div>
      <div data-reveal>{rating_badge(0)}</div>
      <h1 class="display hero__title" data-reveal style="--d:80ms">
        Uno studio dentistico<br>a Genova, con il <span class="accent-i">laboratorio</span><br>e la sala raggi in sede.
      </h1>
      <p class="lead mt-6" data-reveal style="--d:160ms">
        Sette clinici, ognuno con la sua disciplina: implantologia, ortodonzia
        invisibile, chirurgia orale, protesi, pedodonzia. Le cure si possono eseguire
        anche in sedazione cosciente, e il tariffario è pubblicato per intero.
      </p>
      <div class="hero__cta" data-reveal style="--d:240ms">
        <a class="btn btn--lg" href="{S['booking']}" target="_blank" rel="noopener">{ico('calendario')} Prenota la prima visita</a>
        <a class="btn btn--lg btn--ghost" href="prezzi.html">Guarda il tariffario</a>
      </div>
      <div class="hero__meta" data-reveal style="--d:320ms">
        <span>{ico('pin')} {S['via']}, {S['citta']} centro</span>
        <span>{ico('orologio')} <span class="badge-live" data-open-now></span></span>
        <span>{ico('auto')} 3 posti auto gratuiti</span>
      </div>
    </div>

    <div class="portrait-card" data-reveal="scale" style="--d:200ms">
      <div class="portrait-card__frame">
        <img src="assets/img/team/uberto-piccardo.webp" width="720" height="901"
             alt="Ritratto del dottor Uberto Piccardo, direttore sanitario dello studio" fetchpriority="high">
        <span class="portrait-card__tag">Dott. Uberto Piccardo · Direttore Sanitario</span>
      </div>
      <div class="price-card">
        <div class="price-card__top">
          <span class="price-card__label">Prima visita<br>e piano di cura</span>
          <span class="price-card__val">110 €</span>
        </div>
        <ul>
          <li>{ico('check')} Visita completa e diagnosi</li>
          <li>{ico('check')} Radiografie in studio, se necessarie</li>
          <li>{ico('check')} Piano di cura e preventivo scritto</li>
          <li>{ico('check')} Tempi e alternative, messe nero su bianco</li>
        </ul>
      </div>
    </div>
  </div>
</section>'''

    # ─────────────────────────────────────────────────────── BARRA NUMERI
    numeri = [
        ("4000", "+", "impianti osteointegrati inseriti dal 1999", False),
        ("99.8", "%", "la percentuale di successo sulla casistica dello studio", False),
        ("1997", "", "l'anno della laurea in Odontoiatria del Dott. Piccardo", True),
        ("7", "", "clinici, ognuno con la sua disciplina", False),
    ]
    celle = "".join(
        '''<div class="stat-bar__item" data-reveal style="--d:{d}ms">
        <div class="stat-n"><span data-count="{n}"{pl}>{n0}</span><span class="stat-suffix">{p}</span></div>
        <p class="stat-bar__lbl">{l}</p></div>'''.format(
            d=i * 70, n=n, p=p, l=l, pl=" data-plain" if plain else "",
            n0=n if plain else "0")
        for i, (n, p, l, plain) in enumerate(numeri)
    )
    out += f'<section class="stat-bar"><div class="wrap"><div class="stat-bar__grid">{celle}</div></div></section>'

    # ───────────────────────────────────────────────────────── I PILASTRI
    pilastri = (
        _pilastro(
            "calma", "Puoi fare qualunque cura in sedazione",
            "Il Dott. Piccardo ha conseguito a Padova un master universitario di secondo livello "
            "in sedazione ed emergenze in odontoiatria, e in quella stessa clinica universitaria "
            "ha poi lavorato come sedazionista. Lo studio pratica la sedazione cosciente "
            "inalatoria, quella endovenosa e la comunicazione ipnotica: tre strumenti diversi, "
            "che si scelgono in base a quanto è forte l&rsquo;ansia e a quanto durerà l&rsquo;intervento.",
            "trattamenti/paura-del-dentista.html", "Come funziona la sedazione", guida=True)
        + _pilastro(
            "euro", "Il tariffario è pubblico, voce per voce",
            "Trentasei prestazioni sono pubblicate online con il loro costo, dalla prima visita "
            "all&rsquo;impianto. Dopo la visita ricevi un piano di cura scritto, con le voci una per "
            "una, i tempi previsti e le alternative possibili. L&rsquo;importo si può rateizzare a "
            "tasso zero fino a cinquemila euro, e diciannove fra fondi e casse sanitarie sono "
            "convenzionati con lo studio.",
            "prezzi.html", "Apri il tariffario completo")
        + _pilastro(
            "scan", "Cominci e finisci nello stesso studio",
            "La sala raggi ospita una TAC Cone Beam tridimensionale e uno scanner intraorale. Il "
            "laboratorio odontotecnico, iscritto al Ministero della Salute, sta due porte più in "
            "là e fresa le corone in zirconia mentre sei ancora in poltrona. Gli esami si fanno "
            "qui e le protesi nascono qui, così le settimane di spedizione e di attesa restano "
            "fuori dal conto.",
            "studio.html", "Guarda com&rsquo;è fatto lo studio")
    )
    out += f'''
<section class="section sec--1">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow has-n"><span class="eyebrow__n">1</span>Perché qui</span>
      <h2 class="mt-4">Come si lavora in questo studio</h2>
      <p class="lead">Tre aspetti che valgono per tutte le cure, dalla seduta di igiene alla riabilitazione su impianti.</p>
    </div>
    <div class="g-feature" data-stagger="90">{pilastri}</div>
  </div>
</section>'''

    # ───────────────────────────────────────────── SELETTORE PER INTENZIONE
    tabs = "".join(
        f'<button class="intent__tab" role="tab" id="tab-{i}" aria-controls="pan-{i}" '
        f'aria-selected="{"true" if i==0 else "false"}">{nome}</button>'
        for i, (nome, _) in enumerate(INTENZIONI)
    )
    pannelli = ""
    for i, (nome, slugs) in enumerate(INTENZIONI):
        cards = "".join(_tcard(s) for s in slugs)
        pannelli += (f'<div class="intent__panel grid g3" role="tabpanel" id="pan-{i}" '
                     f'aria-labelledby="tab-{i}"{"" if i==0 else " hidden"}>{cards}</div>')
    out += f'''
<section class="section bg-paper2">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow has-n"><span class="eyebrow__n">2</span>Trattamenti</span>
      <h2 class="mt-4">Cosa ti porta qui?</h2>
    </div>
    <div class="intent" data-tabs data-reveal>
      <div class="intent__tabs" role="tablist" aria-label="Scegli il motivo della visita">{tabs}</div>
      {pannelli}
    </div>
    <div class="mt-8 center"><a class="btn btn--ghost" href="trattamenti.html">Tutti i trattamenti {ico('freccia')}</a></div>
  </div>
</section>'''

    # ────────────────────────────────────────────────────── BLOCCO PAURA
    out += f'''
<section class="section bg-dark">
  <div class="wrap split">
    <div data-reveal="left">
      {media_slot("Video · 60″", "«Non ho sentito niente»: testimonianza di un paziente montata con il Dott. Piccardo che spiega la sedazione",
                  "Il paziente racconta la sua seduta, il Dott. Piccardo spiega la sedazione. Volto in campo con liberatoria firmata, audio in presa diretta.",
                  ar="4/3", dark=True, scena="video")}
    </div>
    <div data-reveal="right">
      <span class="eyebrow has-n"><span class="eyebrow__n">3</span>Odontofobia</span>
      <h2 class="mt-4">Il livello di sedazione si stabilisce prima della seduta</h2>
      <p class="lead mt-6">La paura del dentista nasce quasi sempre da qualcosa che è successo
      davvero, spesso da bambini, e il corpo la ripropone appena riconosce il rumore del riunito
      o l'odore dello studio. È una reazione automatica, e a una reazione automatica si risponde
      con la farmacologia. Prima della seduta si valuta quanta ansia c'è e si sceglie insieme
      <b style="color:#FFFDF9">quale sedazione usare</b>, fino al grado che preferisci.</p>
      <ul class="ticks mt-8">
        <li>{ico('check')}<span><b style="color:#FFFDF9">Sedazione cosciente inalatoria.</b>
        Una miscela personalizzata di ossigeno e protossido d'azoto, respirata da una mascherina
        appoggiata sul naso. Resti sveglio e rispondi alle domande; alla fine bastano cinque minuti
        di ossigeno puro per tornare a guidare.</span></li>
        <li>{ico('check')}<span><b style="color:#FFFDF9">Sedazione endovenosa.</b>
        Gestita direttamente dal Dott. Piccardo, senza appoggiarsi a un anestesista esterno.
        Serve negli interventi lunghi, o nei pazienti in cui la sola inalatoria non basta.</span></li>
        <li>{ico('check')}<span><b style="color:#FFFDF9">Comunicazione ipnotica.</b>
        Diploma di Ipnologo conseguito al CIICS di Torino nel 2017. In molti casi abbassa l'ansia
        prima ancora che serva somministrare qualcosa.</span></li>
      </ul>
      <div class="mt-8"><a class="btn" href="trattamenti/paura-del-dentista.html">{ico('calma')} Leggi come funziona la sedazione</a></div>
      <figure class="quote-band mt-12">
        <p class="pull pull--i">«Ero terrorizzata al solo pensiero di andare dal dentista.
        Lui mi ha fatto passare completamente la paura, mai sentito dolore.»</p>
        <figcaption class="pull-cite">Chicca Grisaffi, recensione pubblica su Google</figcaption>
      </figure>
    </div>
  </div>
</section>'''

    # ────────────────────────────────────────────────────────── PRIMA/DOPO
    out += prima_dopo(0)

    # ──────────────────────────────────────────────────────── TEAM STRIP
    out += striscia_team(0)

    # ───────────────────────────────────────────────────────── RECENSIONI
    out += blocco_recensioni(
        0, limite=9,
        titolo="310 persone hanno raccontato com'è andata",
        occhiello="La parola ai pazienti")

    # ────────────────────────────────────────────────────── PREZZI ESTRATTO
    voci = [("Prima visita e piano di cura", "110"), ("Igiene orale professionale", "100"),
            ("Otturazione media", "130"), ("Devitalizzazione, 1 canale", "160"),
            ("Impianto dentale", "770"), ("Corona in zirconia", "770")]
    righe = "".join(
        f'<div class="tariff-row"><span class="tariff-row__n">{n}</span><span class="tariff-row__p">{p} €</span></div>'
        for n, p in voci
    )
    out += f'''
<section class="section">
  <div class="wrap split">
    <div data-reveal="left">
      <span class="eyebrow has-n"><span class="eyebrow__n">6</span>Prezzi</span>
      <h2 class="mt-4">Il preventivo che ricevi è quello che paghi</h2>
      <p class="lead mt-6">Dalla seduta di igiene alla riabilitazione su impianti. Dopo la prima
      visita ricevi un preventivo scritto con il totale, e quel totale vale fino alla fine
      della cura.</p>
      <div class="ribbon mt-8">{ico('euro')}<span><b>Finanziamento a tasso 0</b> fino a 5.000 €, fino a 36 rate. Tasso agevolato oltre.</span></div>
      <div class="mt-8 row gap-3">
        <a class="btn" href="prezzi.html">Tariffario completo</a>
        <a class="btn btn--ghost" href="prezzi.html#preventivo">Preventivo online gratuito</a>
      </div>
    </div>
    <div data-reveal="right">
      <div class="tariff-table">
        <div class="tariff-cat">Le voci più richieste</div>
        {righe}
      </div>
      <p class="xs muted mt-4">Prezzi in euro, IVA esente ai sensi dell'art. 10 DPR 633/72. Il preventivo personalizzato viene consegnato in forma scritta dopo la prima visita.</p>
    </div>
  </div>
</section>'''

    # ──────────────────────────────────────────────────────── CONVENZIONI
    out += blocco_convenzioni()

    # ────────────────────────────────────────────────────────── DOVE SIAMO
    out += mappa(0)

    out += cta_finale(0)
    out += '</main>'
    out += footer(0)
    return out
