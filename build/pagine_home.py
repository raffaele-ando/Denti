# -*- coding: utf-8 -*-
"""Homepage."""

from content import STUDIO as S, RECENSIONI, TEMI_RECENSIONI, TEAM, CONVENZIONI
from trattamenti import TRATT_BY_SLUG
from ui import ico, stelle
from shell import (head, header, footer, cta_finale, media_slot, rating_badge,
                   rel, wa_link)
from componenti import (blocco_recensioni, striscia_team, prima_dopo,
                        blocco_convenzioni, mappa)


def _pilastro(icona, titolo, testo, link, label, cls=""):
    return f'''<article class="card card--pillar card--hover" data-reveal>
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
        "Studio odontoiatrico in Via Maragliano 5, Genova. Implantologia, ortodonzia invisibile e cure con sedazione cosciente. Tariffario pubblico, 5,0 su 310 recensioni. Lun–sab 8:00–20:30.",
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
        Il dentista a Genova<br>dove sai quanto spendi<br>e <span class="accent-i">non senti niente</span>.
      </h1>
      <p class="lead mt-6" data-reveal style="--d:160ms">
        Implantologia, ortodonzia invisibile e chirurgia orale, eseguite con
        sedazione cosciente da un'équipe di otto specialisti. Con il tariffario
        completo pubblicato online, prima che tu entri.
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
        ("1997", "", "l'anno in cui il Dott. Piccardo ha iniziato a esercitare", True),
        ("8", "", "clinici specializzati in discipline diverse", False),
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
            "calma", "Il dolore si controlla con tecniche precise",
            "Il Dott. Piccardo ha conseguito a Padova un master universitario di secondo livello "
            "in sedazione ed emergenze in odontoiatria, e in quella stessa clinica universitaria "
            "ha poi lavorato come sedazionista. Lo studio pratica la sedazione cosciente "
            "inalatoria, quella endovenosa e la comunicazione ipnotica: tre strumenti diversi, "
            "che si scelgono in base a quanto è forte l&rsquo;ansia e a quanto durerà l&rsquo;intervento.",
            "trattamenti/paura-del-dentista.html", "Come funziona la sedazione")
        + _pilastro(
            "euro", "Il prezzo lo conosci prima di sederti",
            "Trentasei prestazioni sono pubblicate online con il loro costo, dalla prima visita "
            "all&rsquo;impianto. Dopo la visita ricevi un piano di cura scritto, con le voci una per "
            "una, i tempi previsti e le alternative possibili. L&rsquo;importo si può rateizzare a "
            "tasso zero fino a cinquemila euro, e diciannove fra fondi e casse sanitarie sono "
            "convenzionati con lo studio.",
            "prezzi.html", "Apri il tariffario completo")
        + _pilastro(
            "scan", "Diagnosi, chirurgia e protesi nello stesso posto",
            "La sala raggi ospita una TAC Cone Beam tridimensionale e uno scanner intraorale. Il "
            "laboratorio odontotecnico, iscritto al Ministero della Salute, sta due porte più in "
            "là e fresa le corone in zirconia mentre sei ancora in poltrona. Nessun esame da fare "
            "altrove, nessuna protesi da spedire e da aspettare per settimane.",
            "studio.html", "Guarda com&rsquo;è fatto lo studio")
    )
    out += f'''
<section class="section">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Perché qui</span>
      <h2 class="mt-4">Tre motivi per sceglierci, e la <span class="accent-i">prova</span> di ciascuno</h2>
      <p class="lead">Qualsiasi studio può scrivere «professionalità» e «tecnologia
      all&rsquo;avanguardia»: sono parole che non costano nulla. Qui sotto trovate tre affermazioni
      precise e, accanto a ognuna, il titolo universitario, il numero o il documento che la
      sostiene. Sono tutte verificabili.</p>
    </div>
    <div class="grid g3" data-stagger="90">{pilastri}</div>
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
      <span class="eyebrow">Trattamenti</span>
      <h2 class="mt-4">Ogni percorso comincia da un <span class="accent-i">problema diverso</span></h2>
      <p class="lead">Scegli la situazione che ti somiglia di più. Al posto di un elenco di
      quaranta prestazioni vedrai le tre che riguardano davvero il tuo caso, ciascuna con il
      costo di partenza e la pagina che la spiega per intero.</p>
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
                  "Il singolo contenuto a più alto impatto dell'intero sito. Priorità di produzione 1. Vedi docs/03-photo-brief.md → V1.",
                  ar="4/3", dark=True, scena="video")}
    </div>
    <div data-reveal="right">
      <span class="eyebrow">Odontofobia</span>
      <h2 class="mt-4">Se rimandi le cure per paura, ci sono <span class="accent-i">tre strade</span> per uscirne</h2>
      <p class="lead mt-6">L'odontofobia si comporta come un riflesso condizionato. Nasce quasi
      sempre da un episodio reale, spesso dell'infanzia, e il corpo la ripropone appena riconosce
      il rumore del riunito o l'odore dello studio. Chiedere a una persona di farsi coraggio
      significa chiederle di controllare una reazione automatica, e infatti quasi mai funziona.
      Qui l'ansia viene valutata prima della seduta e si decide insieme
      <b style="color:#FFFDF9">quale livello di sedazione usare</b>, con la stessa serietà con
      cui si sceglie il tipo di anestesia.</p>
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
      <figure class="mt-12" style="border-left:2px solid var(--brand-500);padding-left:1.25rem">
        <p class="pull pull--i" style="font-size:clamp(1.15rem,1rem+.8vw,1.5rem);line-height:1.35">«58 primavere sulle spalle e prima estrazione di dente del giudizio. Non ho sentito niente.»</p>
        <figcaption class="pull-cite">Fabio Burlando · recensione Google</figcaption>
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
        titolo="Trecentodieci pazienti hanno recensito lo studio, e la media è <span class='accent-i'>cinque su cinque</span>",
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
      <span class="eyebrow">Prezzi</span>
      <h2 class="mt-4">Il tariffario è <span class="accent-i">pubblico</span> e lo trovi per intero</h2>
      <p class="lead mt-6">Trentasei prestazioni con il costo indicato accanto, dalla pulizia dei
      denti alla riabilitazione su impianti. Pubblicarlo ci espone al confronto, e va bene così:
      chi arriva sapendo già quanto spenderà si siede in poltrona molto più tranquillo, e quella
      tranquillità vale più di qualche preventivo in meno.</p>
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
