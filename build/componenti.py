# -*- coding: utf-8 -*-
"""Blocchi riusabili condivisi fra più pagine."""

from content import (STUDIO as S, RECENSIONI, TEMI_RECENSIONI, TEAM,
                     TEAM_BY_SLUG, CONVENZIONI, ORARI)
from ui import ico, stelle
from shell import rel, media_slot, wa_link, orari_lista


# ═══════════════════════════════════════════════════════════ PRIMA / DOPO
CASI = {
    # La didascalia porta le informazioni che la fotografia non contiene:
    # cosa è stato fatto, in quanto tempo, quante sedute, quanto è costato.
    "riabilitazione": dict(
        titolo="Corone in zirconia sugli incisivi superiori",
        nota="Sei sedute in quattro mesi, e i denti sotto le corone sono i suoi.",
        prima="caso-riabilitazione-prima", dopo="caso-riabilitazione-dopo",
        alt_prima="Incisivi superiori scheggiati e di colore disomogeneo",
        alt_dopo="Gli stessi incisivi con le corone in zirconia, allineati e di colore uniforme",
    ),
    "ortodonzia": dict(
        titolo="Affollamento e morso aperto, corretti con l'ortodonzia",
        nota="Diciotto mesi di trattamento, controlli ogni sei settimane, e tutti i denti al loro posto.",
        prima="caso-ortodonzia-prima", dopo="caso-ortodonzia-dopo",
        alt_prima="Denti anteriori affollati e sovrapposti, con i margini che non combaciano",
        alt_dopo="Gli stessi denti allineati sull'arcata, con i margini che combaciano",
    ),
}


def _slider(caso, depth=0):
    c = CASI[caso]
    r = rel(depth)
    return f'''<figure class="ba-case" data-reveal>
  <div class="ba" style="--pos:50%" data-autohint>
    <img src="{r}assets/img/casi/{c['prima']}.webp" alt="{c['alt_prima']}" loading="lazy" width="900" height="676">
    <img class="ba__after" src="{r}assets/img/casi/{c['dopo']}.webp" alt="{c['alt_dopo']}" loading="lazy" width="900" height="676">
    <span class="ba__lbl ba__lbl--a">Prima</span>
    <span class="ba__lbl ba__lbl--b">Dopo</span>
    <span class="ba__handle"><span class="ba__knob">{ico('scambio')}</span></span>
  </div>
  <figcaption class="ba-case__meta">
    <div><h4>{c['titolo']}</h4><p class="xs muted">{c['nota']}</p></div>
  </figcaption>
</figure>'''


def prima_dopo(depth=0, caso=None, titolo=None):
    """Griglia prima/dopo. Se `caso` è indicato mostra solo quello + slot."""
    if caso:
        corpo = f'<div class="grid g2">{_slider(caso, depth)}' + \
            media_slot("Foto · prima e dopo", "Secondo caso clinico dello stesso trattamento",
                       "Protocollo standardizzato: stessa focale, flash anulare, retrattori e bilanciamento del bianco fissato.",
                       ar="4/3", scena="prima-dopo") + '</div>'
        tit = titolo or "Quanto ci è voluto, in questo caso"
    else:
        slot = media_slot("Foto · prima e dopo", "Caso di implantologia a carico immediato",
                          "Serie standard: frontale, laterale destra e sinistra, occlusale. Consenso scritto archiviato.",
                          ar="4/3", scena="prima-dopo") + media_slot(
            "Foto · prima e dopo", "Caso di estetica con faccette",
            "Stessa illuminazione e stessa distanza nelle due sessioni, nessun ritocco oltre il bilanciamento del colore.",
            ar="4/3", scena="faccetta")
        corpo = f'<div class="grid g2">{_slider("riabilitazione", depth)}{_slider("ortodonzia", depth)}{slot}</div>'
        tit = titolo or "Quanto ci è voluto, e quanto è costato"

    return f'''
<section class="section">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow has-n"><span class="eyebrow__n">4</span>Casi clinici</span>
      <h2 class="mt-4">{tit}</h2>
      <p class="lead">Pazienti dello studio, che hanno firmato per pubblicare le loro
      fotografie. Stessa luce, stessa distanza e stesso obiettivo nelle due sessioni:
      fra il prima e il dopo cambiano solo i denti.</p>
    </div>
    {corpo}
    <p class="ba-disclaimer">{ico('info')}<span>Casi reali trattati presso l'Ambulatorio Dentistico Dr. Piccardo U. S.r.l.
    I risultati variano da paziente a paziente in funzione del quadro clinico di partenza e non sono garantiti.
    Immagini pubblicate a scopo di informazione sanitaria ai sensi dell'art. 9 della L. 24/2017,
    previo consenso informato scritto degli interessati.</span></p>
  </div>
</section>'''


# ═════════════════════════════════════════════════════════════════ TEAM
def _foto_membro(m, depth=0, lazy=True):
    r = rel(depth)
    l = ' loading="lazy"' if lazy else ""
    return (f'<img src="{r}assets/img/team/{m["slug"]}.webp" width="720" height="900" '
            f'alt="{m["nome"]}, {m["ruolo"]}"{l}>')


def scheda_membro(m, depth=0, bottone=True):
    """Card di un membro dell'équipe."""
    tag = "button" if bottone else "div"
    attr = f' class="member" data-person="cv-{m["slug"]}" type="button"' if bottone else ' class="member"'
    piu = f'<span class="member__plus">{ico("piu")}</span>' if bottone else ""
    return f'''<{tag}{attr}>
  <span class="member__ph">{_foto_membro(m, depth)}{piu}</span>
  <span class="member__name">{m['nome']}</span>
  <span class="member__role">{m['ruolo'].split(' · ')[0]}</span>
</{tag}>'''


def striscia_team(depth=0):
    cards = "".join(scheda_membro(m, depth, bottone=False) for m in TEAM)
    r = rel(depth)
    return f'''
<section class="section bg-paper2">
  <div class="wrap">
    <div class="between section-head" style="max-width:none;align-items:flex-end" data-reveal>
      <div style="max-width:40rem">
        <span class="eyebrow has-n"><span class="eyebrow__n">5</span>L'équipe</span>
        <h2 class="mt-4">Ciascuno fa una disciplina sola, tutti i giorni</h2>
        <p class="lead">La Dott.ssa Gibelli si occupa solo di ortodonzia dal 2003. Il Dott. De Giovanni
        di parodontologia e chirurgia. La Dott.ssa Tuo solo di bambini. E il Dott. Piccardo, prima di
        laurearsi in odontoiatria, si era diplomato odontotecnico, e il laboratorio dove nascono le
        corone lo ha voluto per questo.</p>
      </div>
      <a class="btn btn--ghost hide-mobile" href="{r}team.html">Conosci il team {ico('freccia')}</a>
    </div>
    <div class="team-strip" data-reveal>{cards}</div>
    <div class="mt-6 hide-desktop"><a class="btn btn--ghost btn--block" href="{r}team.html">Conosci il team</a></div>
  </div>
</section>'''


def drawer_persona():
    """Contenitore del pannello laterale + sorgenti nascoste dei CV."""
    sorgenti = ""
    for m in TEAM:
        cv = "".join(f'<div class="cv-item"><time>{a}</time><span>{t}</span></div>' for a, t in m["cv"])
        cv_blk = f'<h4 class="mt-8">Formazione e percorso</h4><div class="cv-list">{cv}</div>' if cv else ""
        pub = "".join(f'<li style="font-size:var(--fs-xs);color:var(--muted);line-height:1.5">{p}</li>' for p in m["pubblicazioni"])
        pub_blk = f'<h4 class="mt-8">Pubblicazioni scientifiche</h4><ul class="stack gap-4 mt-4">{pub}</ul>' if pub else ""
        soc = "".join(f'<span class="pill">{x}</span>' for x in m["societa"])
        soc_blk = f'<h4 class="mt-8">Società scientifiche</h4><div class="row gap-2 mt-4">{soc}</div>' if soc else ""
        tratta = "".join(
            f'<a class="pill pill--brand" href="trattamenti/{s}.html">{TRATT_NAV.get(s, s)}</a>'
            for s in m["tratta"]
        )
        tratta_blk = f'<h4 class="mt-8">Si occupa di</h4><div class="row gap-2 mt-4">{tratta}</div>' if tratta else ""
        sintesi = f'<p class="lead mt-6">{m["sintesi"]}</p>' if m["sintesi"] else ""
        sorgenti += f'''<template id="cv-{m['slug']}">
  <div class="person-hero">
    <span class="person-hero__ph"><img src="assets/img/team/{m['slug']}.webp" alt="{m['nome']}, {m['ruolo']}" width="720" height="900"></span>
    <div>
      <span class="eyebrow is-bare">{m['albo'] or 'Équipe'}</span>
      <h2 class="mt-2" style="font-size:1.9rem">{m['nome']}</h2>
      <p class="small muted mt-2">{m['ruolo']}</p>
    </div>
  </div>
  {sintesi}
  {cv_blk}{pub_blk}{soc_blk}{tratta_blk}
  <div class="mt-12 row gap-3">
    <a class="btn" href="{S['booking']}" target="_blank" rel="noopener">{ico('calendario')} Prenota una visita</a>
    <a class="btn btn--ghost" href="tel:{S['tel']}">{ico('telefono')} {S['tel_display']}</a>
  </div>
</template>'''

    return f'''<div class="person-drawer" id="person-drawer" role="dialog" aria-modal="true" aria-label="Scheda del professionista">
  <div class="person-drawer__bd"></div>
  <div class="person-drawer__panel">
    <button class="person-drawer__close" aria-label="Chiudi">{ico('chiudi')}</button>
    <div class="person-drawer__body"></div>
  </div>
</div>
{sorgenti}'''


TRATT_NAV = {}   # popolato da make.py per evitare import circolari


# ═══════════════════════════════════════════════════════════ RECENSIONI
def _rev(r):
    iniziali = "".join(p[0] for p in r["nome"].split()[:2]).upper()
    guide = ' · Local Guide' if r.get("guide") else ""
    return f'''<figure class="rev">
  {stelle()}
  <blockquote class="rev__q mt-4">{r['testo']}</blockquote>
  <figcaption class="rev__foot">
    <span class="rev__av" aria-hidden="true">{iniziali}</span>
    <span><span class="rev__who">{r['nome']}</span><br><span class="rev__when">{r['quando']}{guide} · Google</span></span>
  </figcaption>
</figure>'''


def blocco_recensioni(depth=0, limite=9, titolo=None, occhiello="Recensioni", tema=None):
    dati = [r for r in RECENSIONI if tema is None or r["tema"] == tema][:limite]
    cards = "".join(_rev(r) for r in dati)
    temi = "".join(f'<span class="rev-theme">{n} <b>{c}</b></span>' for n, c in TEMI_RECENSIONI)
    tit = titolo or "Cosa dicono i pazienti"
    r = rel(depth)
    return f'''
<section class="section bg-tint">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="eyebrow">{occhiello}</span>
      <h2 class="mt-4">{tit}</h2>
    </div>

    <div class="rev-summary mb-8" data-reveal>
      <div class="rev-summary__score">
        <div class="n">{S['voto']}</div>
        <div class="mt-4">{stelle(5, 'stars--lg')}</div>
        <p class="xs muted mt-2">{S['n_recensioni']} recensioni Google<br>{S['voto_fb']} su oltre 200 valutazioni Facebook</p>
      </div>
      <div>
        <p class="small muted mb-4">Contate da Google:</p>
        <div class="rev-themes">{temi}</div>
        <a class="link-arrow mt-6" href="{S['recensioni_url']}" target="_blank" rel="noopener">Leggi tutte le recensioni su Google {ico('freccia')}</a>
      </div>
    </div>

    <div class="rev-grid">{cards}</div>
    <p class="xs muted mt-6">Testi pubblici riportati integralmente dalla scheda Google dello studio.
    L'evidenziazione tipografica è redazionale e non altera il contenuto delle recensioni.</p>
  </div>
</section>'''


# ═════════════════════════════════════════════════════════════ CONVENZIONI
def blocco_convenzioni(depth=0):
    pills = "".join(f'<span class="pill">{c}</span>' for c in CONVENZIONI)
    return f'''
<section class="sec--3" id="convenzioni">
  <div class="wrap center mb-6" data-reveal>
    <span class="eyebrow is-bare">Convenzioni attive</span>
    <h3 class="mt-4">Il tuo fondo sanitario è probabilmente fra questi</h3>
  <p class="lead mt-4" style="max-width:42rem;margin-inline:auto">Portane gli estremi quando
  prenoti: apriamo noi la pratica.</p>
  </div>
  <div class="marquee" data-reveal><div class="marquee__track">{pills}{pills}</div></div>
</section>'''


# ══════════════════════════════════════════════════════════════════ MAPPA
def mappa(depth=0, compatta=False):
    r = rel(depth)
    embed = (f"https://www.google.com/maps?q={S['lat']},{S['lng']}"
             f"&z=16&hl=it&output=embed")
    mezzi = f'''<ul class="ticks">
  <li>{ico('treno')}<span><b>In treno.</b> Scendi a Genova Brignole e in cinque minuti a piedi sei in Via Maragliano.</span></li>
  <li>{ico('bus')}<span><b>In bus.</b> Fermano in Via XX Settembre o in Via Macaggi le linee 14, 15, 17, 18, 19, 20, 30, 33, 36, 37, 39, 40, 42, 44, 46 e 47.</span></li>
  <li>{ico('auto')}<span><b>In auto.</b> Esci a Genova Ovest e segui le indicazioni per Genova Centro. Nel cortile interno abbiamo <b>tre posti auto gratuiti</b> riservati ai pazienti: basta chiederli in segreteria quando prenoti. In alternativa il parcheggio di Piazza della Vittoria dista cinque minuti.</span></li>
  <li>{ico('accessibile')}<span><b>Accessibilità.</b> Dalla strada alla poltrona è tutto in piano, secondo quanto prevede il D.M. 236/89. Il bagno è attrezzato per persone con disabilità e ha il fasciatoio.</span></li>
</ul>'''
    return f'''
<section class="section bg-paper2" id="dove-siamo">
  <div class="wrap split">
    <div data-reveal="left">
      <span class="eyebrow">Dove siamo</span>
      <h2 class="mt-4">Ci arrivi a piedi da <span class="accent-i">Brignole</span>, o parcheggi dentro</h2>
      <p class="lead mt-6">{S['via']}, {S['cap']} {S['citta']}. Lo studio è al piano terra e si
      entra direttamente dalla strada, tutto in piano.</p>
      {mezzi}
      <div class="mt-8 row gap-3">
        <a class="btn btn--ghost" href="{S['gmaps']}" target="_blank" rel="noopener">{ico('pin')} Apri in Google Maps</a>
        <a class="btn btn--ghost" href="{r}contatti.html">Orari e contatti</a>
      </div>
    </div>
    <div data-reveal="right">
      <div class="map-embed">
        <iframe src="{embed}" title="Mappa: {S['via']}, {S['citta']}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
      <div class="mt-6">{orari_lista()}</div>
    </div>
  </div>
</section>'''


# ═══════════════════════════════════════════════════════ FORM PREVENTIVO
def form_preventivo(depth=0, id_form="form-preventivo"):
    return f'''
<div class="grid g2" style="align-items:start">
  <div data-reveal="left">
    <span class="eyebrow">Gratuito</span>
    <h2 class="mt-4">Hai già una <span class="accent-i">panoramica</span>? Possiamo leggerla adesso</h2>
    <p class="lead mt-6">Il Dott. Piccardo la guarda e ti risponde con una prima lettura della
    situazione e un ordine di grandezza della spesa. Il servizio è gratuito e dopo resti libero
    di decidere: serve a farti un'idea prima di venire.</p>
    <ul class="ticks mt-8">
      <li>{ico('check')}<span>Ti risponde il Dott. Piccardo, via email o al telefono che ci lasci</span></li>
      <li>{ico('check')}<span>Il servizio è gratuito, e dopo resti libero di decidere</span></li>
      <li>{ico('check')}<span>In segreteria puoi chiedere il giustificativo per il lavoro e i buoni regalo per igiene o sbiancamento</span></li>
      <li>{ico('check')}<span>Quando la panoramica da sola non basta te lo scriviamo, con il motivo</span></li>
    </ul>
    <div class="form-note mt-8">{ico('info')}<span>Una valutazione a distanza serve a orientarti
    sui tempi e sull'ordine di grandezza della spesa. La diagnosi vera richiede la visita clinica,
    perché una radiografia non mostra lo stato delle gengive, la mobilità dei denti né come
    mastichi.</span></span></div>
  </div>

  <div data-reveal="right">
    <form class="card" data-validate id="{id_form}" novalidate>
      <div class="grid g2" style="gap:1.1rem">
        <label class="field" style="margin-top:0">
          <span class="field__lbl">Nome e cognome <span class="req">*</span></span>
          <input type="text" name="nome" required autocomplete="name">
          <span class="field__err"></span>
        </label>
        <label class="field" style="margin-top:0">
          <span class="field__lbl">Telefono <span class="req">*</span></span>
          <input type="tel" name="tel" required autocomplete="tel" inputmode="tel">
          <span class="field__err"></span>
        </label>
      </div>
      <label class="field">
        <span class="field__lbl">Email <span class="req">*</span></span>
        <input type="email" name="email" required autocomplete="email" inputmode="email">
        <span class="field__err"></span>
      </label>

      <div class="field">
        <span class="field__lbl">Di cosa hai bisogno?</span>
        <div class="chip-group">
          {"".join(f'<span><input type="checkbox" id="{id_form}-c{i}" name="motivo" value="{v}"><label for="{id_form}-c{i}">{v}</label></span>' for i, v in enumerate(["Impianti", "Invisalign", "Estetica", "Protesi", "Igiene", "Dolore", "Bambini", "Non lo so"]))}
        </div>
      </div>

      <label class="field">
        <span class="field__lbl">Raccontaci la situazione</span>
        <textarea name="messaggio" placeholder="Es. Mi mancano due denti in basso a sinistra da circa un anno. Ho già un preventivo di un altro studio e vorrei confrontarlo."></textarea>
      </label>

      <div class="field">
        <span class="field__lbl">Radiografia panoramica <span class="muted" style="font-weight:500">(facoltativa)</span></span>
        <label class="file-drop">
          {ico('upload')}
          <strong data-file-label>Trascina qui il file o scegli dal dispositivo</strong>
          <span>JPG, PNG o PDF · fino a 15 MB</span>
          <input type="file" name="panoramica" accept="image/*,.pdf" hidden>
        </label>
      </div>

      <div class="field">
        <label class="check">
          <input type="checkbox" name="privacy" required>
          <span>Ho letto l'<a href="{rel(depth)}note-legali.html#privacy">informativa privacy</a> e acconsento
          al trattamento dei miei dati per essere ricontattato. I dati sanitari sono trattati ai sensi
          dell'art. 9 del Regolamento UE 2016/679 (GDPR). <span class="req">*</span></span>
        </label>
        <span class="field__err"></span>
      </div>

      <button class="btn btn--lg btn--block mt-8" type="submit">Invia la richiesta</button>
      <p class="xs muted mt-4 center">Oppure scrivici su <a href="{wa_link()}" target="_blank" rel="noopener" style="color:var(--brand-700);font-weight:650">WhatsApp</a>, spesso è più veloce.</p>
    </form>

    <div class="form-success">
      {ico('check')}
      <h3>Richiesta inviata</h3>
      <p class="muted mt-4">Ti rispondiamo all'indirizzo che ci hai lasciato, il prima possibile.
      Se la questione è urgente chiama il <a href="tel:{S['tel']}" style="color:var(--brand-700);font-weight:650">{S['tel_display']}</a>.</p>
    </div>
  </div>
</div>'''
