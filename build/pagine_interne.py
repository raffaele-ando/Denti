# -*- coding: utf-8 -*-
"""Pagine interne: trattamenti, hub, studio, team, prezzi, recensioni, contatti."""

from content import (STUDIO as S, TARIFFARIO, CONVENZIONI, TEAM, TEAM_BY_SLUG,
                     RECENSIONI, TEMI_RECENSIONI)
from trattamenti import TRATTAMENTI, TRATT_BY_SLUG
from ui import ico, diagramma, stelle
from shell import (head, header, footer, cta_finale, media_slot, breadcrumb,
                   rel, wa_link, orari_lista, rating_badge)
from componenti import (blocco_recensioni, blocco_convenzioni, mappa,
                        form_preventivo, scheda_membro, drawer_persona,
                        prima_dopo)


# ══════════════════════════════════════════════════ PAGINA TRATTAMENTO
def trattamento(t):
    d = 1
    r = rel(d)
    slug = t["slug"]

    faq_schema = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer",
                                           "text": a.replace("<b>", "").replace("</b>", "")}}
                       for q, a in t["faq"]],
    }
    bc_schema = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": S["sito"] + "/"},
            {"@type": "ListItem", "position": 2, "name": "Trattamenti", "item": S["sito"] + "/trattamenti.html"},
            {"@type": "ListItem", "position": 3, "name": t["nav"]},
        ],
    }

    out = head(d, t["meta_title"], t["meta_desc"], f"trattamenti/{slug}.html",
               [faq_schema, bc_schema], tema_scuro=(t["gruppo"] == "Ho paura"))
    out += header(d, "trattamenti")
    out += '<main id="main">'

    # ── hero
    media = ""
    if t.get("hero_media"):
        hm = t["hero_media"]
        media = f'<div data-reveal="scale" style="--d:180ms">{media_slot("Foto", hm["testo"], hm["nota"], ar=hm["ar"], scena=hm.get("scena", "poltrona"))}</div>'
    colonne = "hero__grid" if media else ""
    variante = {"Ho paura": "paura", "Voglio un sorriso migliore": "valore",
                "Mi manca un dente": "valore"}.get(t["gruppo"], "cura")
    out += f'''
<section class="pagehero pagehero--{variante}">
  <span class="pagehero__mark">{ico(t['icona'])}</span>
  <div class="wrap {colonne}">
    <div{'' if media else ' style="max-width:52rem"'}>
      {breadcrumb(d, [("Trattamenti", "trattamenti.html"), (t["nav"], None)])}
      <span class="famiglia" data-reveal><span class="ico">{ico(t['icona'])}</span>{t['gruppo']}</span>
      <h1 class="mt-6" data-reveal style="--d:60ms">{t['h1']}</h1>
      <p class="lead mt-6" data-reveal style="--d:120ms">{t['lead']}</p>
      <div class="hero__cta" data-reveal style="--d:180ms">
        <a class="btn btn--lg" href="{S['booking']}" target="_blank" rel="noopener">{ico('calendario')} Prenota una valutazione</a>
        <a class="btn btn--lg btn--ghost" href="#prezzo">Vedi il prezzo</a>
      </div>
    </div>
    {media}
  </div>
</section>'''

    # ── dati chiave
    kf = "".join(
        f'<div class="keyfact"><dt>{a}</dt><dd>{b}{f"<small>{c}</small>" if c else ""}</dd></div>'
        for a, b, c in t["keyfacts"]
    )
    out += f'<section class="section-sm"><div class="wrap"><dl class="keyfacts" data-reveal>{kf}</dl></div></section>'

    # ── testo introduttivo
    blocchi = "".join(f'<h3>{tit}</h3><p>{txt}</p>' for tit, txt in t["intro"])
    out += f'''
<section class="section-sm">
  <div class="wrap">
    <div class="prose" data-reveal style="max-width:46rem">{blocchi}</div>
  </div>
</section>'''

    # ── diagramma
    if t.get("diagramma"):
        passi = "".join(f'<div class="step"><div><h4>{a}</h4><p>{b}</p></div></div>' for a, b in t["steps"])
        out += f'''
<section class="section sec--1 bg-paper2">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow has-n"><span class="eyebrow__n">1</span>Come funziona</span>
      <h2 class="mt-4">{t['diagramma_titolo']}</h2>
      <p class="lead">{t['diagramma_sub']}</p>
    </div>
    <div data-reveal class="mb-8" style="background:var(--paper);border:1px solid var(--line-soft);border-radius:var(--r-lg);padding:clamp(1rem,3vw,2rem)">
      {diagramma(t['diagramma'])}
    </div>
    <div class="steps steps--row" data-reveal>{passi}</div>
  </div>
</section>'''
    elif t["steps"]:
        passi = "".join(f'<div class="step"><div><h4>{a}</h4><p>{b}</p></div></div>' for a, b in t["steps"])
        out += f'<section class="section bg-paper2"><div class="wrap"><div class="steps steps--row" data-reveal>{passi}</div></div></section>'

    # ── fa per te?
    si = "".join(f'<li>{x}</li>' for x in t["fit_yes"])
    no = "".join(f'<li>{x}</li>' for x in t["fit_no"])
    out += f'''
<section class="section">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow has-n"><span class="eyebrow__n">2</span>Onestamente</span>
      <h2 class="mt-4">{t['fit_titolo']}</h2>
    </div>
    <div class="fit" data-reveal>
      <div class="fit__col fit__col--yes"><h4>{ico('check')}{t['fit_yes_t']}</h4><ul>{si}</ul></div>
      <div class="fit__col fit__col--no"><h4>{ico('info')}{t['fit_no_t']}</h4><ul>{no}</ul></div>
    </div>
  </div>
</section>'''

    # ── caso clinico
    if t.get("caso"):
        out += prima_dopo(d, caso=t["caso"])

    # ── prove
    prove = "".join(
        f'''<article class="card" data-reveal>
        <div class="icon-box {'icon-box--accent' if i==0 else ''}">{ico(ic)}</div>
        <h3 class="mt-6">{tit}</h3><p class="mt-2">{txt}</p></article>'''
        for i, (ic, tit, txt) in enumerate(t["proofs"])
    )
    out += f'''
<section class="section bg-tint">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow has-n"><span class="eyebrow__n">3</span>Le prove</span>
      <h2 class="mt-4">Perché conviene farlo <span class="accent-i">qui</span></h2>
    </div>
    <div class="grid g3" data-stagger="90">{prove}</div>
  </div>
</section>'''

    # ── il clinico
    m = TEAM_BY_SLUG[t["clinico"]]
    cv = "".join(f'<div class="cv-item"><time>{a}</time><span>{b}</span></div>' for a, b in m["cv"][:6])
    out += f'''
<section class="section">
  <div class="wrap split">
    <div data-reveal="left" style="max-width:26rem">
      <div class="portrait-card__frame" style="border-radius:var(--r-lg)">
        <img src="{r}assets/img/team/{m['slug']}.webp" width="720" height="900" loading="lazy"
             alt="Ritratto di {m['nome']}" style="mix-blend-mode:multiply">
      </div>
    </div>
    <div data-reveal="right">
      <span class="eyebrow has-n"><span class="eyebrow__n">4</span>Chi se ne occupa</span>
      <h2 class="mt-4">{m['nome']}</h2>
      <p class="small muted mt-2">{m['ruolo']}</p>
      <p class="lead mt-6">{m['sintesi']}</p>
      {f'<div class="cv-list mt-8">{cv}</div>' if cv else ''}
      <div class="mt-8"><a class="link-arrow" href="{r}team.html">Tutto il team {ico('freccia')}</a></div>
    </div>
  </div>
</section>'''

    # ── prezzo
    righe = "".join(
        f'<div class="tariff-row"><span class="tariff-row__n">{n}</span><span class="tariff-row__p">{p} €</span></div>'
        for n, p in t["prezzi"]
    )
    nota = f'<div class="ribbon mt-6">{ico("euro")}<span>{t["prezzo_nota"]}</span></div>' if t.get("prezzo_nota") else ""
    out += f'''
<section class="section bg-paper2" id="prezzo">
  <div class="wrap split">
    <div data-reveal="left">
      <span class="eyebrow has-n"><span class="eyebrow__n">5</span>Prezzo</span>
      <h2 class="mt-4">Quanto <span class="accent-i">costa</span></h2>
      <p class="lead mt-6">Dopo la prima visita ricevi un preventivo scritto con le lavorazioni una
      per una e il totale. Quella cifra vale fino alla fine della cura, anche se il lavoro dovesse
      rivelarsi più lungo del previsto.</p>
      {nota}
      <div class="mt-8 row gap-3">
        <a class="btn" href="{r}prezzi.html">Tariffario completo</a>
        <a class="btn btn--ghost" href="{r}prezzi.html#finanziamenti">Calcola la rata</a>
      </div>
    </div>
    <div data-reveal="right"><div class="tariff-table">{righe}</div>
      <p class="xs muted mt-4">IVA esente ai sensi dell'art. 10 DPR 633/72. Detraibile al 19% nella dichiarazione dei redditi.</p>
    </div>
  </div>
</section>'''

    # ── faq
    faq = "".join(f'''<div class="acc__item">
  <button class="acc__btn" aria-expanded="false">{q}<span class="acc__ico"></span></button>
  <div class="acc__panel"><div><p>{a}</p></div></div>
</div>''' for q, a in t["faq"])
    out += f'''
<section class="section">
  <div class="wrap" style="max-width:56rem">
    <div class="section-head" data-reveal>
      <span class="eyebrow has-n"><span class="eyebrow__n">6</span>Domande frequenti</span>
      <h2 class="mt-4">Le domande che ci fanno <span class="accent-i">più spesso</span></h2>
    </div>
    <div class="acc" data-single data-reveal>{faq}</div>
  </div>
</section>'''

    # ── correlati
    corr = "".join(f'''<a class="tcard" href="{c}.html" data-reveal>
  <div class="tcard__top"><div class="icon-box">{ico(TRATT_BY_SLUG[c]['icona'])}</div></div>
  <h3>{TRATT_BY_SLUG[c]['nav']}</h3>
  <p>{TRATT_BY_SLUG[c]['breve']}</p>
</a>''' for c in t["correlati"])
    out += f'''
<section class="sec--3">
  <div class="wrap">
    <h3 class="mb-6" data-reveal>Se stai valutando questo, spesso serve anche</h3>
    <div class="grid g3" data-stagger="80">{corr}</div>
  </div>
</section>'''

    out += cta_finale(d)
    out += '</main>' + footer(d)
    return out


# ═════════════════════════════════════════════════════════ HUB TRATTAMENTI
def hub_trattamenti():
    d = 0
    gruppi = {}
    for t in TRATTAMENTI:
        gruppi.setdefault(t["gruppo"], []).append(t)

    sezioni = ""
    for g, lista in gruppi.items():
        cards = "".join(f'''<a class="tcard" href="trattamenti/{t['slug']}.html" data-reveal>
  <div class="tcard__top"><div class="icon-box{' icon-box--accent' if t.get('premium') else ''}">{ico(t['icona'])}</div>
  {'<span class="pill pill--accent">Alta specializzazione</span>' if t.get('premium') else ''}</div>
  <h3>{t['nav']}</h3>
  <p>{t['breve']}</p>
  <div class="tcard__price"><span>{t['prezzi'][0][0]}</span><b>{t['prezzi'][0][1].replace(',00','')}{'' if '/' in t['prezzi'][0][1] or '€' in t['prezzi'][0][1] else ' €'}</b></div>
</a>''' for t in lista)
        sezioni += f'''<div class="mt-16">
  <h2 class="mb-6" data-reveal>{g}</h2>
  <div class="grid g3" data-stagger="80">{cards}</div>
</div>'''

    out = head(d, "Trattamenti odontoiatrici a Genova | Studio Piccardo",
               "Tutti i trattamenti dello studio: implantologia, Invisalign, estetica, protesi, conservativa, chirurgia orale, igiene, pedodonzia, urgenze e sedazione cosciente.",
               "trattamenti.html")
    out += header(d, "trattamenti")
    out += f'''<main id="main">
<section class="pagehero pagehero--cura">
  <span class="pagehero__mark">{ico("dente")}</span>
  <div class="wrap" style="max-width:54rem">
    {breadcrumb(d, [("Trattamenti", None)])}
    <span class="eyebrow" data-reveal>Trattamenti</span>
    <h1 class="mt-4" data-reveal style="--d:60ms">Non sai come si chiama <span class="accent-i">quello che hai</span>? Va bene lo stesso</h1>
    <p class="lead mt-6" data-reveal style="--d:120ms">Quanto dura, chi la esegue e quanto costa
    stanno scritti dentro ogni cura. E in diversi casi la risposta giusta è una cura più
    semplice di quella che immagini, oppure nessuna.</p>
  </div>
</section>
<section class="section" style="padding-top:0"><div class="wrap">{sezioni}</div></section>'''
    out += blocco_convenzioni(d)
    out += cta_finale(d)
    out += '</main>' + footer(d)
    return out


# ══════════════════════════════════════════════════════════════ LO STUDIO
STUDIO_SEZIONI = [
    dict(id="tecnologia", occhiello="Diagnosi", titolo="La TAC per l'impianto la fai <span class='accent-i'>nella stessa visita</span>",
         testo="""<p>Sala raggi interna con <b>TAC Cone Beam 3D</b>, ortopantomografo con braccio tele e teleradiografo, tutti digitali.
         Consente radiografie tridimensionali delle ossa facciali, panoramiche e teleradiografie del cranio per l'ortodonzia.</p>
         <p>Tutti i sistemi radiografici sono digitali, con un <b>abbattimento superiore all'80% della dose</b> rispetto alla pellicola tradizionale.
         Non ti mandiamo in un centro esterno e non aspetti giorni: la diagnosi si completa nella stessa seduta.</p>""",
         dati=[("TAC 3D", "Cone Beam, ossa facciali"), ("−80%", "dose radiante"), ("Scanner", "niente paste da impronta")],
         media=("Foto", "TAC Cone Beam e scanner intraorale, dettaglio ravvicinato",
                "Ravvicinato e tagliato, non «foto del macchinario». Vedi photo brief #5.", "4/3", "radiologia")),
    dict(id="sterilizzazione", occhiello="Sicurezza biologica", titolo="Niente ti arriva in bocca <span class='accent-i'>dopo essere stato</span> in quella di un altro",
         testo="""<p>Sala di sterilizzazione separata, con pareti in smalto lavabile e disinfettabile
         certificate <b>HACCP UNI 11021:2002</b>. Due autoclavi di classe B, protocolli ISO 9001, e ogni kit
         imbustato ed etichettato con tracciabilità individuale.</p>
         <p>A ogni cambio paziente si sostituiscono le pellicole protettive su maniglie, lampada e tastiere,
         si disinfettano le superfici e le componenti idriche del riunito. Il monouso: tovaglioli, aspirasaliva,
         guanti, puntali: esce dallo studio con il paziente.</p>""",
         dati=[("2", "autoclavi classe B"), ("135 °C", "2 atm · 15 min"), ("ISO 9001", "tracciabilità")],
         diagramma="sterilizzazione",
         media=("Foto", "Mani guantate che imbustano lo strumentario",
                "Dettaglio, non panoramica della stanza. Vedi photo brief #6.", "4/3", "sterilizzazione")),
    dict(id="laboratorio", occhiello="Protesi", titolo="Se la protesi non ti convince, <span class='accent-i'>si aggiusta mentre aspetti</span>",
         testo="""<p>Laboratorio odontotecnico interno <b>iscritto al Ministero della Salute</b>, dove si realizzano
         protesi mobili, riparazioni immediate e tutte le protesi fisse in zirconia o composito con tecnologia CAD-CAM.</p>
         <p>In pratica: le prove si fanno mentre sei sulla poltrona, i ritocchi cromatici si eseguono sul momento
         e una protesi rotta si ripara <b>in giornata</b>, senza spedizioni e senza attese.</p>""",
         dati=[("CAD-CAM", "zirconia e composito"), ("Stesso giorno", "riparazioni"), ("Min. Salute", "lab. iscritto")],
         media=("Foto", "Mani dell'odontotecnico su una corona in zirconia",
                "È un differenziante forte e merita uno scatto vero. Vedi photo brief #7.", "4/3", "laboratorio")),
    dict(id="sicurezza", occhiello="Emergenze mediche", titolo="Cosa succede se durante una seduta <span class='accent-i'>ti senti male</span>",
         testo="""<p>Defibrillatore semiautomatico, ossigeno, pallone ambu e cannule orofaringee, pulsossimetro,
         misuratori di pressione da braccio e da polso, misuratore digitale della glicemia e dell'INR.</p>
         <p>Quattordici farmaci d'emergenza organizzati in scatole dedicate, una per ciascun quadro clinico:
         arresto cardiaco e respiratorio, lipotimia, angina, aritmie, infarto, crisi ipertensiva, edema polmonare,
         crisi asmatica, shock anafilattico, crisi epilettica, ictus, crisi ipoglicemica, emorragie da anticoagulanti.</p>
         <p><b>Tutto il personale è formato BLSD</b> e ogni mese si tiene una riunione con esercitazione pratica
         su manichino e defibrillatore trainer, perché una manovra si ricorda con le mani.</p>""",
         dati=[("DAE", "defibrillatore in sede"), ("14", "farmaci d'emergenza"), ("Ogni mese", "esercitazione")],
         media=None),
    dict(id="continuita", occhiello="Continuità", titolo="Se va via la corrente, <span class='accent-i'>l'intervento non si ferma</span>",
         testo="""<p>Un gruppo di continuità UPS garantisce alle tre zone operative <b>tre ore di autonomia</b>
         in caso di black-out. Significa che un intervento chirurgico iniziato non si interrompe mai a metà.</p>
         <p>Lo studio dispone inoltre di un piano antincendio a norma.</p>""",
         dati=[("3 ore", "di autonomia elettrica"), ("3", "zone operative protette")],
         media=None),
    dict(id="accessibilita", occhiello="Accesso", titolo="Dalla strada alla poltrona non c'è un <span class='accent-i'>solo gradino</span>",
         testo="""<p>Circa 300 mq al piano terra con accesso diretto dalla strada. L'intera struttura è stata
         progettata e realizzata ai fini del superamento e dell'eliminazione delle barriere architettoniche,
         nel rispetto del <b>D.M. 236/89</b>.</p>
         <p>Bagno attrezzato per persone con disabilità, dotato anche di <b>fasciatoio</b>. In sala d'attesa
         un'area gioco dedicata ai bambini. Per chi non può muoversi da casa è attivo il
         <b>servizio a domicilio</b>, con attrezzatura portatile, anche presso case di cura.</p>""",
         dati=[("300 mq", "al piano terra"), ("236/89", "nessuna barriera"), ("A domicilio", "su richiesta")],
         media=("Foto", "Ingresso dalla strada e sala d'attesa riordinata",
                "Riordinare prima dello scatto. Grandangolo moderato, verticali corrette. Vedi photo brief #2 e #3.", "3/2", "ingresso")),
    dict(id="parcheggio", occhiello="Parcheggio", titolo="Parcheggi dentro, e <span class='accent-i'>non paghi</span>",
         testo="""<p>Nel cortile interno attiguo allo studio sono disponibili <b>tre posti auto riservati ai pazienti,
         gratuiti e prenotabili</b> chiamando la segreteria. A Genova centro non è un dettaglio.</p>
         <p>In alternativa: Piazza della Vittoria a cinque minuti a piedi, Stazione Brignole a cinque minuti,
         e una ventina di linee bus con fermata in Via XX Settembre o Via Macaggi.</p>""",
         dati=[("3", "posti auto gratuiti"), ("5 min", "da Brignole"), ("20+", "linee bus")],
         media=("Foto", "Posto auto interno con auto parcheggiata, di giorno",
                "Risolve un'obiezione reale. Luce diurna, niente notturne mosse. Vedi photo brief #10.", "3/2", "parcheggio")),
]


def studio():
    d = 0
    nav = "".join(f'<a href="#{s["id"]}">{s["occhiello"]}</a>' for s in STUDIO_SEZIONI)

    sezioni = ""
    for s in STUDIO_SEZIONI:
        dati = "".join(f'<div class="keyfact"><dt>{b}</dt><dd>{a}</dd></div>' for a, b in s["dati"])
        media = ""
        if s["media"]:
            k, txt, nota, ar, scena = s["media"]
            media = f'<div data-reveal="right">{media_slot(k, txt, nota, ar=ar, scena=scena)}</div>'
        dia = ""
        if s.get("diagramma"):
            dia = f'''<div class="mt-8" data-reveal style="background:var(--paper);border:1px solid var(--line-soft);border-radius:var(--r-lg);padding:clamp(1rem,3vw,2rem);grid-column:1/-1">
              {diagramma(s['diagramma'])}</div>'''
        sezioni += f'''<section class="studio-section" id="{s['id']}">
  <div class="split" style="align-items:start">
    <div data-reveal="left">
      <span class="eyebrow">{s['occhiello']}</span>
      <h2 class="mt-4">{s['titolo']}</h2>
      <div class="prose mt-6">{s['testo']}</div>
      <dl class="keyfacts mt-8" style="grid-template-columns:repeat({len(s['dati'])},1fr)">{dati}</dl>
    </div>
    {media}
    {dia}
  </div>
</section>'''

    out = head(d, "Lo studio: tecnologia, sterilizzazione e sicurezza | Piccardo",
               "300 mq in Genova centro: TAC Cone Beam 3D, laboratorio odontotecnico interno, sterilizzazione ISO 9001, defibrillatore, UPS 3 ore, nessuna barriera architettonica, 3 posti auto.",
               "studio.html")
    out += header(d, "studio")
    out += f'''<main id="main">
<section class="pagehero pagehero--cura">
  <span class="pagehero__mark">{ico("scan")}</span>
  <div class="wrap" style="max-width:54rem">
    {breadcrumb(d, [("Lo studio", None)])}
    <span class="eyebrow" data-reveal>Lo studio</span>
    <h1 class="mt-4" data-reveal style="--d:60ms">Entri una volta sola, e dentro <span class="accent-i">c'è già tutto</span></h1>
    <p class="lead mt-6" data-reveal style="--d:120ms">Di solito la TAC si prenota in un centro
    radiologico, la protesi parte per un laboratorio esterno e l'ortodonzista riceve da un'altra
    parte: fra un passaggio e l'altro se ne vanno settimane, e a portare le buste sei tu. Qui la
    sala raggi, il laboratorio e gli otto clinici stanno dietro la stessa porta.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(2rem,4vw,3rem)">
  <div class="wrap">
    <div class="split" style="grid-template-columns:minmax(0,14rem) minmax(0,1fr);gap:clamp(2rem,4vw,4rem);align-items:start">
      <nav class="anchor-nav" aria-label="Sezioni della pagina">{nav}</nav>
      <div>{sezioni}
        <section class="studio-section" id="tour">
          <span class="eyebrow">Tour virtuale</span>
          <h2 class="mt-4">Guarda dove ti siederai, <span class="accent-i">prima di venire</span></h2>
          <p class="lead mt-6" style="max-width:40rem">Sala d'attesa, reception, zone operative,
          sala raggi, sterilizzazione e laboratorio sono tutti su Google Street View. Se l'ansia
          è il tuo problema, arrivare in un posto che hai già visto ne toglie una buona metà.</p>
          <div class="map-embed mt-8" data-reveal>
            <iframe src="https://www.google.com/maps/embed?pb=!4v1523268454645!6m8!1m7!1sCAoSLEFGMVFpcFBqTUlxaDktbERtaUItU0lQUGx6SktwZHRzV2haN2ZSb2FKVjdk!2m2!1d44.40396939!2d8.9403753!3f218.3372179200444!4f-3.67608424969697!5f0.7820865974627469"
                    title="Tour virtuale della sala d'attesa" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe>
          </div>
          <div class="mt-8">{media_slot("Video · 45″", "Tour dello studio in movimento continuo, senza voce",
                    "Sostituirà il tour statico come apertura di questa pagina. Vedi docs/03-photo-brief.md, scheda V2.", ar="16/9", scena="video")}</div>
        </section>
      </div>
    </div>
  </div>
</section>'''
    out += mappa(d)
    out += cta_finale(d, "Vieni a vederlo, senza fare niente",
                      "Puoi fissare un appuntamento in cui non si cura nulla: entri, guardi, parli con qualcuno e te ne vai. Diversi nostri pazienti hanno cominciato esattamente così, e la volta dopo si sono seduti.")
    out += '</main>' + footer(d)
    return out


# ══════════════════════════════════════════════════════════════════ TEAM
def team():
    d = 0
    clinici = [m for m in TEAM if m["cv"] or m["sintesi"]]
    staff = [m for m in TEAM if not (m["cv"] or m["sintesi"])]
    g1 = "".join(scheda_membro(m, d) for m in clinici)
    g2 = "".join(scheda_membro(m, d) for m in staff)

    persone_schema = [{
        "@context": "https://schema.org", "@type": "Person",
        "name": m["nome"], "jobTitle": m["ruolo"],
        "worksFor": {"@type": "Dentist", "name": S["ragione_sociale"]},
        "image": f"{S['sito']}/assets/img/team/{m['slug']}.webp",
    } for m in clinici]

    out = head(d, "Il team: otto specialisti a Genova | Studio Piccardo",
               "L'équipe dello studio: chirurgo orale e implantologo, ortodonzista specialista Invisalign, parodontologo con 4 pubblicazioni, pedodonzista, due igienisti dentali laureati.",
               "team.html", persone_schema, tema_scuro=True)
    out += header(d, "team")
    out += f'''<main id="main">
<section class="pagehero pagehero--paura">
  <span class="pagehero__mark">{ico("gruppo")}</span>
  <div class="wrap" style="max-width:54rem">
    {breadcrumb(d, [("Il team", None)])}
    <span class="eyebrow" data-reveal>L'équipe</span>
    <h1 class="mt-4" data-reveal style="--d:60ms">Chi ti visita la prima volta è chi ti <span class="accent-i">seguirà fino alla fine</span></h1>
    <p class="lead mt-6" data-reveal style="--d:120ms">Otto clinici specializzati in discipline
    diverse, più la segreteria e le assistenti alla poltrona. Nessuno passa il tuo caso a un
    collega di un'altra sede: quando servono più competenze si mettono d'accordo fra loro, e tu
    continui a parlare con la stessa persona.</p>
  </div>
</section>

<section class="section" style="padding-top:clamp(1rem,3vw,2rem)">
  <div class="wrap">
    <div class="team-grid" data-stagger="60">{g1}</div>
    <h3 class="mt-16 mb-6" data-reveal>Segreteria e assistenza</h3>
    <div class="team-grid" data-stagger="60">{g2}</div>
  </div>
</section>

<section class="section bg-dark">
  <div class="wrap split">
    <div data-reveal="left">
      <span class="eyebrow">Formazione</span>
      <h2 class="mt-4">Dove hanno studiato, e <span class="accent-i">cosa hanno pubblicato</span></h2>
      <p class="lead mt-6">Le pubblicazioni del Dott. De Giovanni sono indicizzate su PubMed:
      l'identificativo accanto a ciascuna porta al testo originale, senza passare da noi.</p>
      <ul class="ticks mt-8">
        <li>{ico('check')}<span>Master II livello in <b style="color:#FFFDF9">Implantoprotesi</b>. Università di Genova, 110/110</span></li>
        <li>{ico('check')}<span>Master II livello in <b style="color:#FFFDF9">Sedazione ed emergenze</b>. Università di Padova</span></li>
        <li>{ico('check')}<span>Master II livello in <b style="color:#FFFDF9">Chirurgia orale e d'urgenza</b>. Università di Pisa</span></li>
        <li>{ico('check')}<span>Master II livello in <b style="color:#FFFDF9">Implantologia digitale</b>. Università di Padova</span></li>
        <li>{ico('check')}<span>Master II livello in <b style="color:#FFFDF9">Direzione e Management delle Aziende Sanitarie</b>. LUM Jean Monnet</span></li>
        <li>{ico('check')}<span>Specializzazione in <b style="color:#FFFDF9">Ortognatodonzia</b>. Università di Milano, 70/70</span></li>
        <li>{ico('check')}<span><b style="color:#FFFDF9">Quattro pubblicazioni</b> indicizzate del Dott. De Giovanni (J Clin Med, J Pers Med, Materials, J Prosthodont Res)</span></li>
      </ul>
    </div>
    <div data-reveal="right">
      {media_slot("Foto", "Ritratto d'équipe al completo, in studio, divisa uniforme, bianco e nero",
                  "Sostituisce la griglia esistente. Uniformare le divise: oggi tre membri hanno la polo scura. Vedi photo brief #11 e #12.",
                  ar="4/5", dark=True, scena="equipe")}
    </div>
  </div>
</section>

<section class="section" id="interviste">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Video</span>
      <h2 class="mt-4">Senti come parlano, <span class="accent-i">prima di incontrarli</span></h2>
      <p class="lead">Un minuto a testa, sulla domanda che si sentono fare più spesso.</p>
    </div>
    <div class="grid g3" data-stagger="80">
      {media_slot("Video · 15″", "«La domanda che mi fanno più spesso». Dott. Piccardo", "Formato verticale, riusabile sui social. Vedi la scheda V4 del photo brief.", ar="4/3", scena="video")}
      {media_slot("Video · 15″", "«La domanda che mi fanno più spesso». Dott.ssa Gibelli", "Una clip per ciascun clinico dell'équipe.", ar="4/3", scena="video")}
      {media_slot("Video · 15″", "«La domanda che mi fanno più spesso». Dott. De Giovanni", "Stessa inquadratura e stesso fondo per tutte e otto.", ar="4/3", scena="video")}
    </div>
    <div class="mt-8 center">
      <a class="btn btn--ghost" href="{S['social']['youtube']}" target="_blank" rel="noopener">{ico('youtube')} Il canale YouTube dello studio</a>
    </div>
  </div>
</section>'''
    out += cta_finale(d, "Vuoi parlare con uno di loro?",
                      "Alla prima visita incontri il clinico che seguirà il tuo caso. Se servono più competenze si mettono d'accordo fra loro, e a te arriva un piano solo.")
    out += '</main>'
    out += drawer_persona()
    out += footer(d)
    return out


# ════════════════════════════════════════════════════════════════ PREZZI
def prezzi():
    d = 0
    cat_slug = lambda c: c.lower().replace(" ", "-").replace("'", "")
    chips = '<button class="pill" data-tariff-cat="tutte" aria-pressed="true">Tutte</button>' + "".join(
        f'<button class="pill" data-tariff-cat="{cat_slug(c)}" aria-pressed="false">{c}</button>'
        for c, _ in TARIFFARIO
    )
    tabella = ""
    for cat, voci in TARIFFARIO:
        cs = cat_slug(cat)
        tabella += f'<div class="tariff-cat" data-cat="{cs}">{cat}</div>'
        for nome, sotto, prezzo in voci:
            sub = f'<small>{sotto}</small>' if sotto else ""
            tabella += (f'<div class="tariff-row" data-cat="{cs}" data-nome="{nome} {sotto}">'
                        f'<span class="tariff-row__n">{nome}{sub}</span>'
                        f'<span class="tariff-row__p">{prezzo} €</span></div>')

    conv = "".join(f'<span class="pill">{c}</span>' for c in CONVENZIONI)

    out = head(d, "Prezzi e tariffario: studio dentistico Genova | Piccardo",
               "Il tariffario completo del nostro studio: 37 prestazioni con il prezzo pubblicato. Prima visita 110 €, impianto 770 €, igiene 100 €. Finanziamento a tasso 0 fino a 5.000 €.",
               "prezzi.html")
    out += header(d, "prezzi")
    out += f'''<main id="main">
<section class="pagehero pagehero--valore">
  <span class="pagehero__mark">{ico("euro")}</span>
  <div class="wrap" style="max-width:54rem">
    {breadcrumb(d, [("Prezzi", None)])}
    <span class="eyebrow" data-reveal>Prezzi</span>
    <h1 class="mt-4" data-reveal style="--d:60ms">Il preventivo che firmi è la cifra che <span class="accent-i">pagherai alla fine</span></h1>
    <p class="lead mt-6" data-reveal style="--d:120ms">Nessun ritocco in corso d'opera, nessuna
    voce che spunta a metà cura. Se il lavoro si rivela più lungo del previsto, la differenza
    resta a carico nostro.</p>
    <div class="hero__cta" data-reveal style="--d:180ms">
      <a class="btn btn--lg" href="#preventivo">Preventivo online gratuito</a>
      <a class="btn btn--lg btn--ghost" href="{S['booking']}" target="_blank" rel="noopener">Prenota la prima visita</a>
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="wrap">
    <div class="grid g3" data-stagger="80">
      <article class="card" data-reveal><div class="icon-box">{ico('documento')}</div>
        <h3 class="mt-6">Un preventivo scritto, voce per voce</h3>
        <p class="mt-2">Al termine della prima visita ti consegniamo un piano di cura su carta, con
        ogni lavorazione elencata singolarmente, il tempo previsto, le alternative possibili e il
        totale. Nel documento non compare mai la dicitura «da definire»: se una cifra dipende da un
        esame che ancora manca, te lo scriviamo e ti diciamo quando la sapremo.</p></article>
      <article class="card" data-reveal><div class="icon-box icon-box--accent">{ico('euro')}</div>
        <h3 class="mt-6">Fino a 5.000 euro puoi rateizzare a tasso zero</h3>
        <p class="mt-2">Il finanziamento arriva a trentasei rate senza interessi. Sopra i cinquemila
        euro passa a tasso agevolato, con condizioni che dipendono dall'istituto convenzionato. La
        pratica si apre in segreteria e la risposta arriva in genere in giornata.</p></article>
      <article class="card" data-reveal><div class="icon-box">{ico('scudo')}</div>
        <h3 class="mt-6">Il 19 per cento torna con la dichiarazione</h3>
        <p class="mt-2">Le spese odontoiatriche rientrano fra gli oneri detraibili, quindi una parte
        di quanto spendi la recuperi l'anno successivo. La ricevuta fiscale viene emessa sempre e
        per l'importo effettivamente pagato, anche quando nessuno la chiede.</p></article>
    </div>
  </div>
</section>

<section class="section" id="finanziamenti">
  <div class="wrap">
    <div class="calc" id="calc" data-reveal>
      <div class="calc__grid">
        <div>
          <span class="eyebrow is-bare" style="color:var(--brand-200)">Calcola la rata</span>
          <h2 class="mt-4" style="color:#FFFDF9">Quanto ti verrebbe <span class="accent-i">al mese</span></h2>
          <div class="mt-8">
            <label for="calc-importo">Importo del piano di cura</label>
            <div class="calc__amount" id="calc-importo-val">3.500 €</div>
            <input type="range" id="calc-importo" min="500" max="12000" step="100" value="3500"
                   aria-label="Importo del piano di cura in euro">
            <div class="between xs" style="color:var(--su-scuro-3)"><span>500 €</span><span>12.000 €</span></div>
          </div>
          <div class="mt-8">
            <label>Durata</label>
            <div class="seg">
              {"".join(f'<button data-mesi="{m}" aria-pressed="{"true" if m==36 else "false"}">{m} mesi</button>' for m in [12,18,24,30,36])}
            </div>
          </div>
        </div>
        <div class="calc__out">
          <div class="xs" style="color:var(--su-scuro-2);letter-spacing:.1em;text-transform:uppercase;font-weight:700">Rata mensile</div>
          <div class="calc__rate mt-4"><span id="calc-rata">97</span> €</div>
          <p class="xs mt-6" id="calc-nota" style="color:var(--su-scuro-2)">Tasso 0. TAN 0%, importo fino a 5.000 €</p>
        </div>
      </div>
      <p class="xs mt-8" style="color:var(--su-scuro-3);border-top:1px solid rgba(255,255,255,.1);padding-top:1rem">
        Simulazione indicativa a scopo informativo, non costituisce offerta contrattuale ai sensi del
        D.lgs. 385/1993. Il tasso 0 si applica a importi fino a 5.000 €; oltre tale soglia il calcolo qui
        mostrato è una stima prudenziale su TAN 4,9%. Condizioni, TAEG e fattibilità sono determinati
        dall'istituto finanziario convenzionato. Chiedi il piano esatto in segreteria.
      </p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0" id="tariffario-sez">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Tariffario</span>
      <h2 class="mt-4">Ogni prestazione, con il <span class="accent-i">suo prezzo</span></h2>
      <p class="lead">Quello che non trovi in elenco esiste comunque: chiedilo in segreteria.</p>
    </div>
    <div class="tariff-toolbar" data-reveal>
      <div class="tariff-search">{ico('cerca')}
        <input type="search" id="tariff-q" placeholder="Cerca una prestazione…" aria-label="Cerca nel tariffario">
      </div>
    </div>
    <div class="tariff-toolbar" data-reveal style="margin-bottom:1.5rem">{chips}</div>
    <div class="tariff-table" id="tariffario" data-reveal>{tabella}</div>
    <p id="tariff-empty" class="center muted mt-8" hidden>Nessuna prestazione corrisponde alla ricerca.
    Per le voci non elencate rivolgiti alla segreteria: <a href="tel:{S['tel']}" style="color:var(--brand-700);font-weight:650">{S['tel_display']}</a>.</p>
    <p class="xs muted mt-6">Prezzi in euro, IVA esente ai sensi dell'art. 10 DPR 633/72. Per le prestazioni non
    elencate rivolgersi alla segreteria. I prezzi possono variare in funzione della complessità del caso:
    l'importo definitivo è quello indicato nel preventivo scritto consegnato dopo la prima visita.</p>
  </div>
</section>

<section class="section bg-paper2" id="convenzioni">
  <div class="wrap">
    <div class="section-head is-center" data-reveal>
      <span class="eyebrow is-bare">Convenzioni</span>
      <h2 class="mt-4">Se hai un fondo sanitario, <span class="accent-i">probabilmente è qui</span></h2>
      <p class="lead">Portane gli estremi quando prenoti: alla pratica e ai documenti pensiamo noi,
      e in molti casi la quota coperta viene già scalata dal preventivo.</p>
    </div>
    <div class="row gap-2 center-x" style="justify-content:center;max-width:56rem;margin-inline:auto" data-reveal>{conv}</div>
  </div>
</section>

<section class="section" id="preventivo">
  <div class="wrap">{form_preventivo(d)}</div>
</section>'''
    out += cta_finale(d)
    out += '</main>' + footer(d)
    return out


# ═══════════════════════════════════════════════════════════ RECENSIONI
def recensioni():
    d = 0
    out = head(d, "Recensioni: 5,0 su 310 valutazioni Google | Studio Piccardo",
               "Le recensioni dei pazienti dello studio dentistico Piccardo di Genova: 5,0 su 310 recensioni Google e 4,9 su oltre 200 valutazioni Facebook.",
               "recensioni.html")
    out += header(d, "recensioni")
    out += f'''<main id="main">
<section class="pagehero pagehero--valore">
  <span class="pagehero__mark">{ico("stella")}</span>
  <div class="wrap" style="max-width:54rem">
    {breadcrumb(d, [("Recensioni", None)])}
    <span class="eyebrow" data-reveal>Recensioni</span>
    <h1 class="mt-4" data-reveal style="--d:60ms">Com'è andata, raccontata da <span class="accent-i">chi c'è passato</span></h1>
    <p class="lead mt-6" data-reveal style="--d:120ms">Alcuni avevano paura da vent'anni, altri
    cercavano solo un secondo preventivo. Qui sono riportate parola per parola dalla scheda
    Google, dove restano pubbliche.</p>
  </div>
</section>'''
    out += blocco_recensioni(d, limite=99, titolo="La parola ai pazienti", occhiello="Google · Facebook")
    schede_temi = "".join(
        '<div class="card" style="padding:1.25rem">'
        f'<div class="stat-n" style="font-size:2.4rem">{c}</div>'
        f'<p class="small muted mt-2">{n.lower()}</p></div>'
        for n, c in TEMI_RECENSIONI[:6]
    )
    out += f'''
<section class="section">
  <div class="wrap split">
    <div data-reveal="left">
      <span class="eyebrow">Cosa scrivono</span>
      <h2 class="mt-4">Se cerchi un motivo preciso, <span class="accent-i">probabilmente è uno di questi</span></h2>
      <p class="lead mt-6">Le etichette le genera Google contando le parole che tornano più spesso.
      Non le scegliamo noi.</p>
      <a class="btn mt-8" href="{S['recensioni_url']}" target="_blank" rel="noopener">{ico('stella')} Leggile tutte su Google</a>
    </div>
    <div data-reveal="right">
      <div class="grid g2" style="gap:1rem">{schede_temi}</div>
    </div>
  </div>
</section>'''
    out += cta_finale(d, "La prossima potrebbe essere la tua",
                      "Si comincia con la prima visita: 110 euro, con esame completo, diagnosi e piano di cura consegnato per iscritto.")
    out += '</main>' + footer(d)
    return out


# ═══════════════════════════════════════════════════════════════ CONTATTI
def contatti():
    d = 0
    out = head(d, "Contatti. Via Maragliano 5, Genova | Studio Piccardo",
               "Studio dentistico in Via Maragliano 5, Genova centro. Telefono 010 5959492, WhatsApp, prenotazione online. Aperti lunedì-sabato 8:00-20:30. Tre posti auto gratuiti.",
               "contatti.html")
    out += header(d, "contatti")
    out += f'''<main id="main">
<section class="pagehero pagehero--cura">
  <span class="pagehero__mark">{ico("pin")}</span>
  <div class="wrap" style="max-width:54rem">
    {breadcrumb(d, [("Contatti", None)])}
    <span class="eyebrow" data-reveal>Contatti</span>
    <h1 class="mt-4" data-reveal style="--d:60ms">Rispondiamo dal lunedì al sabato, <span class="accent-i">fino alle otto e mezza</span></h1>
    <p class="lead mt-6" data-reveal style="--d:120ms">Al telefono trovi Carlotta. Su WhatsApp
    puoi scrivere anche di sera e ti richiamiamo alla prima apertura. Dal calendario online
    prenoti da solo, a qualunque ora.</p>
  </div>
</section>

<section class="section-sm">
  <div class="wrap">
    <div class="contact-cards" data-stagger="80">
      <a class="ccard" href="tel:{S['tel']}" data-reveal>
        <div class="icon-box">{ico('telefono')}</div>
        <div class="ccard__val mt-4">{S['tel_display']}<small>Dal lunedì al sabato, 8:00-20:30. Risponde la segreteria dello studio.</small></div>
        <span class="link-arrow mt-4">Chiama adesso {ico('freccia')}</span>
      </a>
      <a class="ccard" href="{wa_link()}" target="_blank" rel="noopener" data-reveal>
        <div class="icon-box">{ico('whatsapp')}</div>
        <div class="ccard__val mt-4">{S['whatsapp_display']}<small>Scrivici quando vuoi, anche di sera. Ti rispondiamo alla prima apertura utile.</small></div>
        <span class="link-arrow mt-4">Apri WhatsApp {ico('freccia')}</span>
      </a>
      <a class="ccard" href="{S['booking']}" target="_blank" rel="noopener" data-reveal>
        <div class="icon-box icon-box--accent">{ico('calendario')}</div>
        <div class="ccard__val mt-4">Prenota online<small>Scegli tu il giorno e l'orario, ventiquattro ore su ventiquattro.</small></div>
        <span class="link-arrow mt-4">Vai al calendario {ico('freccia')}</span>
      </a>
    </div>
    <div class="ribbon mt-8" data-reveal>{ico('pronto')}<span>
      <b>Hai male adesso?</b> Chiama subito il <a href="tel:{S['tel']}" style="color:inherit;text-decoration:underline">{S['tel_display']}</a>:
      cerchiamo sempre uno spazio in giornata. <a href="trattamenti/urgenze.html" style="color:inherit;text-decoration:underline">Cosa fare nell'attesa</a>.
    </span></div>
  </div>
</section>'''
    out += mappa(d)
    out += f'''
<section class="section">
  <div class="wrap">{form_preventivo(d, id_form="contatti-form")}</div>
</section>'''
    out += cta_finale(d)
    out += '</main>' + footer(d)
    return out


# ═════════════════════════════════════════════════════════════ NOTE LEGALI
def note_legali():
    d = 0
    out = head(d, "Note legali, privacy e cookie | Studio Piccardo",
               "Informativa privacy ai sensi del Regolamento UE 2016/679, note legali, polizza RC professionale e informativa cookie dell'Ambulatorio Dentistico Dr. Piccardo U. S.r.l.",
               "note-legali.html")
    out += header(d)
    out += f'''<main id="main">
<section class="subhero">
  <div class="wrap" style="max-width:48rem">
    {breadcrumb(d, [("Note legali", None)])}
    <h1 class="mt-4">Note legali, privacy e cookie</h1>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap prose" style="max-width:44rem">
    <h3 id="titolare">Titolare</h3>
    <p>{S['ragione_sociale']}, {S['via']}, {S['cap']} {S['citta']} (IT).<br>
    Telefono {S['tel_display']}.<br>
    {S['autorizzazione']}.<br>
    Direttore Sanitario: {S['dir_san']}.</p>
    <p><b>Partita IVA, numero REA, PEC e indirizzo email:</b> da inserire prima della pubblicazione.</p>

    <h3 id="privacy">Informativa privacy</h3>
    <p>I dati personali conferiti tramite i moduli presenti su questo sito sono trattati dal Titolare
    ai sensi del <b>Regolamento UE 2016/679 (GDPR)</b> e del D.lgs. 196/2003 come modificato dal D.lgs. 101/2018.</p>
    <p><b>Finalità.</b> Rispondere alle richieste di informazioni, di preventivo e di appuntamento.
    Base giuridica: esecuzione di misure precontrattuali su richiesta dell'interessato (art. 6.1.b GDPR).
    Gli eventuali dati relativi alla salute, comprese le radiografie allegate, sono <b>categorie particolari
    di dati</b> ai sensi dell'art. 9 GDPR e vengono trattati sulla base del consenso esplicito
    dell'interessato (art. 9.2.a) e per finalità di medicina preventiva e diagnosi (art. 9.2.h).</p>
    <p><b>Conservazione.</b> I dati di contatto sono conservati per il tempo necessario a dare riscontro
    alla richiesta e comunque non oltre 24 mesi. I dati sanitari relativi a pazienti in cura seguono
    i termini di conservazione della documentazione sanitaria previsti dalla normativa vigente.</p>
    <p><b>Destinatari.</b> I dati non sono diffusi. Possono essere trattati da fornitori di servizi
    informatici nominati responsabili del trattamento ai sensi dell'art. 28 GDPR.</p>
    <p><b>Diritti.</b> L'interessato può esercitare i diritti di accesso, rettifica, cancellazione,
    limitazione, portabilità e opposizione (artt. 15–22 GDPR) scrivendo al Titolare, e proporre reclamo
    al Garante per la protezione dei dati personali.</p>

    <h3 id="cookie">Cookie</h3>
    <p>Questo sito non utilizza cookie di profilazione propri. L'utilizzo di cookie tecnici e di
    strumenti di misurazione, nonché l'eventuale presenza di pixel di terze parti, va dichiarato
    qui e gestito con un banner di consenso conforme alle Linee guida del Garante del 10 giugno 2021
    <b>prima della messa online</b>.</p>
    <p>Le mappe e i tour virtuali incorporati sono forniti da Google Maps: la loro visualizzazione
    comporta un collegamento ai server di Google. Si consiglia di caricarli previo consenso.</p>

    <h3 id="rc">Polizza RC professionale e contenziosi</h3>
    <p>Ai sensi dell'art. 10, comma 4, della <b>Legge 24/2017</b> (Legge Gelli-Bianco), la struttura sanitaria
    è tenuta a pubblicare sul proprio sito gli estremi della polizza assicurativa per la responsabilità
    civile verso terzi e verso i prestatori d'opera, con l'indicazione della compagnia, della classe
    di rischio e dei massimali. <b>Dati da inserire.</b></p>
    <p>La medesima norma richiede la pubblicazione dei dati relativi ai risarcimenti erogati nell'ultimo
    quinquennio. <b>Dati da inserire.</b></p>

    <h3 id="informazione">Natura delle informazioni pubblicate</h3>
    <p>I contenuti di questo sito hanno finalità di informazione sanitaria ai sensi dell'art. 9 della
    Legge 24/2017 e delle linee guida della FNOMCeO. Non costituiscono in alcun caso diagnosi,
    prescrizione o sostituto della visita medica. Le immagini di casi clinici si riferiscono a pazienti
    realmente trattati presso la struttura, pubblicate previo consenso informato scritto; i risultati
    variano da paziente a paziente e non sono garantiti.</p>
  </div>
</section>'''
    out += '</main>' + footer(d)
    return out


# ═══════════════════════════════════════════════════════════════════ 404
def pagina404():
    d = 0
    out = head(d, "Pagina non trovata | Studio Piccardo",
               "La pagina che cerchi non esiste più: il sito è stato riorganizzato e molti contenuti sono confluiti in pagine più complete. Torna alla home o chiamaci allo 010 5959492.",
               "404.html")
    out += header(d)
    out += f'''<main id="main">
<section class="section center" style="padding-top:calc(var(--header-h) + 6rem)">
  <div class="wrap" style="max-width:38rem">
    <div class="stat-n" style="font-size:6rem">404</div>
    <h1 class="mt-6">Questa pagina non c'è <span class="accent-i">più</span>.</h1>
    <p class="lead mt-6">Quello che cercavi si è spostato altrove. Riparti da qui, oppure
    chiamaci e in trenta secondi ti diciamo noi dov'è finito.</p>
    <div class="hero__cta" style="justify-content:center">
      <a class="btn btn--lg" href="index.html">Torna alla home</a>
      <a class="btn btn--lg btn--ghost" href="trattamenti.html">Tutti i trattamenti</a>
      <a class="btn btn--lg btn--ghost" href="tel:{S['tel']}">{ico('telefono')} {S['tel_display']}</a>
    </div>
  </div>
</section>'''
    out += '</main>' + footer(d)
    return out
