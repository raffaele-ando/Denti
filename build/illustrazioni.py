# -*- coding: utf-8 -*-
"""Illustrazioni vettoriali originali.

Servono dove una fotografia manca ancora, e dove comunque una foto direbbe meno
di un disegno: un'illustrazione può mostrare una sezione, un movimento o una
sequenza che l'obiettivo non inquadra.

Linguaggio comune a tutte: campiture piatte su tre valori di blu, un solo
richiamo in ambra per punto, contorni a 1,8 e nessuna ombra. Ogni scena entra
animata quando raggiunge il viewport.
"""

# Palette locale, allineata ai token del sito
BLU_900 = "#08243C"
BLU_700 = "#134B7A"
BLU_500 = "#2A7CBF"
BLU_200 = "#B4D3EC"
BLU_100 = "#DBEAF7"
BLU_050 = "#EEF6FC"
AMBRA = "#E4913B"
AMBRA_CH = "#FBE9CF"
CARTA = "#FAF8F5"
LINEA = "#9CB8CE"

_CSS = """<style>
 .il-l{fill:none;stroke:%s;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
 .il-f{fill:%s}
 .il-f2{fill:%s}
 .il-a{fill:%s}
 .il-p{fill:%s}
 .il-fade{opacity:0;transition:opacity .7s cubic-bezier(.22,1,.36,1)}
 .il-rise{opacity:0;transform:translateY(10px);transform-origin:center;
   transition:opacity .7s cubic-bezier(.22,1,.36,1),transform .7s cubic-bezier(.22,1,.36,1)}
 .il-pop{opacity:0;transform:scale(.72);transform-origin:center;
   transition:opacity .55s cubic-bezier(.34,1.56,.64,1),transform .55s cubic-bezier(.34,1.56,.64,1)}
 [data-reveal].is-in .il-fade,[data-reveal].is-in .il-rise,[data-reveal].is-in .il-pop{opacity:1;transform:none}
 [data-reveal].is-in .d1{transition-delay:.10s}[data-reveal].is-in .d2{transition-delay:.20s}
 [data-reveal].is-in .d3{transition-delay:.30s}[data-reveal].is-in .d4{transition-delay:.42s}
 [data-reveal].is-in .d5{transition-delay:.54s}[data-reveal].is-in .d6{transition-delay:.66s}
 .il-sway{transform-origin:50%% 90%%;animation:ilsway 6s ease-in-out infinite}
 @keyframes ilsway{0%%,100%%{transform:rotate(-1.2deg)}50%%{transform:rotate(1.2deg)}}
 @media(prefers-reduced-motion:reduce){
   .il-fade,.il-rise,.il-pop{opacity:1;transform:none}.il-sway{animation:none}}
</style>""" % (BLU_700, BLU_200, BLU_100, AMBRA, CARTA)


def _cornice(w=400, h=300, caldo=False):
    """Fondo della scena.

    Il rettangolo di base è sempre dello stesso azzurro chiarissimo del
    contenitore, così i bordi si fondono con il riquadro qualunque sia il
    formato. Le due macchie di luce danno profondità; `caldo` ne amplia
    quella ambra, per le scene che devono risultare accoglienti.
    """
    amb = (0.52, 0.62) if caldo else (0.30, 0.45)
    return (f'<rect x="-40" y="-40" width="{w+80}" height="{h+80}" fill="{BLU_050}"/>'
            f'<circle cx="{w*0.80:.0f}" cy="{h*0.16:.0f}" r="{h*0.46:.0f}" fill="{BLU_100}" opacity=".75"/>'
            f'<circle cx="{w*0.14:.0f}" cy="{h*0.9:.0f}" r="{h*amb[0]:.0f}" fill="{AMBRA_CH}" opacity="{amb[1]}"/>')


def _svg(corpo, w=400, h=300, etichetta=""):
    return (f'<svg class="il" viewBox="0 0 {w} {h}" role="img" aria-label="{etichetta}" '
            f'preserveAspectRatio="xMidYMid meet" style="width:100%;height:100%;display:block">'
            f'{_CSS}{corpo}</svg>')


# ══════════════════════════════════════════════════════════════ SCENE
def poltrona():
    c = _cornice()
    c += '<g class="il-rise d1">'
    c += f'<path class="il-f" d="M96 208c0-10 8-18 18-18h150c10 0 18 8 18 18v10H96z"/>'          # seduta
    c += f'<path class="il-f2" d="M112 190V116c0-11 9-20 20-20h34c11 0 20 9 20 20v74z"/>'        # schienale
    c += f'<path class="il-l" d="M112 190V116c0-11 9-20 20-20h34c11 0 20 9 20 20v74"/>'
    c += f'<path class="il-f2" d="M186 190v-34c0-9 7-16 16-16h58c9 0 16 7 16 16v34z"/>'          # poggiagambe
    c += f'<path class="il-l" d="M186 190v-34c0-9 7-16 16-16h58c9 0 16 7 16 16v34"/>'
    c += f'<path class="il-l" d="M96 218v34M282 218v34M120 252h138"/>'                            # base
    c += f'<path class="il-f" d="M100 104c0-8 7-15 15-15h4c8 0 15 7 15 15v22h-34z"/>'            # poggiatesta
    c += '</g>'
    # braccio della lampada
    c += ('<g class="il-sway"><g class="il-rise d3">'
          f'<path class="il-l" d="M300 62v56l-58 22"/>'
          f'<ellipse cx="236" cy="146" rx="26" ry="11" class="il-a"/>'
          f'<ellipse cx="236" cy="143" rx="26" ry="11" fill="{AMBRA_CH}"/>'
          f'<circle cx="300" cy="60" r="6" fill="{BLU_700}"/>'
          '</g></g>')
    # raggio di luce
    c += (f'<path class="il-fade d4" d="M214 152 L166 214 L294 214 L258 152Z" fill="{AMBRA}" opacity=".16"/>')
    # monitor
    c += ('<g class="il-pop d5">'
          f'<rect x="44" y="70" width="58" height="42" rx="6" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<path d="M56 96l10-12 8 9 7-8 9 11z" fill="{BLU_200}"/>'
          f'<circle cx="60" cy="82" r="3.5" class="il-a"/>'
          f'<path class="il-l" d="M73 112v10M62 122h22"/></g>')
    return _svg(c, etichetta="Illustrazione di una zona operativa con riunito, lampada e monitor")


def maschera():
    c = _cornice(400, 300, caldo=True)
    # testa di profilo rivolta a sinistra, con naso e mento leggibili
    c += ('<g class="il-rise d1">'
          f'<path d="M300 60c-40 0-72 30-78 70l-4 26-22 20c-4 4-2 10 4 11l14 3 2 24c1 12 11 20 24 20h24v30h74c16 0 28-12 28-28V132c0-40-26-72-66-72z" '
          f'fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<path class="il-l" d="M243 122h.01" stroke-width="7"/>'
          f'<path class="il-l" d="M212 200q20 8 38 4"/>'
          f'<path class="il-l" d="M204 176h18" stroke-width="1.4" opacity=".55"/>'
          f'<path class="il-l" d="M312 60q26 20 26 62" opacity=".35" stroke-width="1.4"/>'
          '</g>')
    # mascherina nasale, appoggiata sul dorso del naso
    c += ('<g class="il-pop d3">'
          f'<path d="M196 130c-10 6-14 20-8 30 7 12 26 15 40 8 12-6 18-20 13-31-6-13-32-14-45-7z" fill="{BLU_500}"/>'
          f'<path d="M202 136c8-5 22-6 30 1" fill="none" stroke="{CARTA}" stroke-width="2.4" stroke-linecap="round"/>'
          f'<path class="il-l" d="M238 132c14-8 30-8 44 2" stroke-width="1.8"/>'
          '</g>')
    # tubo del gas e flusso
    c += (f'<path class="il-fade d4" d="M192 152c-38 18-52 46-50 88" fill="none" stroke="{BLU_200}" stroke-width="8" stroke-linecap="round"/>')
    c += (f'<path class="il-fade d5" d="M192 152c-38 18-52 46-50 88" fill="none" stroke="{BLU_500}" stroke-width="2" stroke-dasharray="5 9" stroke-linecap="round"/>')
    for x, y, r, d in [(96, 202, 8, 4), (114, 232, 5, 5), (80, 168, 6, 6)]:
        c += f'<circle class="il-pop d{d}" cx="{x}" cy="{y}" r="{r}" fill="{BLU_500}" opacity=".3"/>'
    # etichetta della miscela
    c += ('<g class="il-pop d6">'
          f'<rect x="264" y="34" width="98" height="34" rx="17" fill="{CARTA}" stroke="{AMBRA}" stroke-width="1.8"/>'
          f'<text x="313" y="56" text-anchor="middle" font-family="Manrope,sans-serif" font-size="14" '
          f'font-weight="800" fill="{BLU_700}">O₂ + N₂O</text>'
          '</g>')
    return _svg(c, etichetta="Illustrazione di una mascherina nasale per la sedazione cosciente")


def laboratorio():
    c = _cornice()
    # banco
    c += f'<rect class="il-rise d1" x="40" y="196" width="320" height="16" rx="6" class="il-f"/>'
    c += f'<rect x="40" y="196" width="320" height="16" rx="6" fill="{BLU_200}"/>'
    c += f'<path class="il-l" d="M70 212v52M330 212v52"/>'
    # fresatrice
    c += ('<g class="il-rise d2">'
          f'<rect x="74" y="96" width="130" height="100" rx="12" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<rect x="90" y="112" width="98" height="60" rx="6" fill="{BLU_100}"/>'
          f'<path class="il-l" d="M139 112v26"/>'
          f'<path d="M132 138h14l-3 18h-8z" fill="{BLU_700}"/>'
          f'<circle class="il-a" cx="176" cy="184" r="5"/>'
          '</g>')
    # blocchetto di zirconia con corona
    c += ('<g class="il-pop d4">'
          f'<rect x="120" y="152" width="38" height="22" rx="4" fill="{AMBRA_CH}" stroke="{AMBRA}" stroke-width="1.6"/>'
          '</g>')
    # corona finita, grande, a destra
    c += ('<g class="il-pop d5">'
          f'<path d="M262 196v-40c0-22 14-36 34-36s34 14 34 36v40z" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<path class="il-l" d="M272 148q24-14 48 0"/>'
          f'<circle class="il-a" cx="296" cy="106" r="7"/>'
          '</g>')
    # scintille del lavoro
    c += (f'<path class="il-fade d6" d="M232 120l6-12M246 130l12-6M228 140l-12 4" '
          f'stroke="{AMBRA}" stroke-width="2" stroke-linecap="round" fill="none"/>')
    return _svg(c, etichetta="Illustrazione del laboratorio odontotecnico con fresatrice e corona in zirconia")


def radiologia():
    c = _cornice()
    # colonna e braccio della TAC
    c += ('<g class="il-rise d1">'
          f'<rect x="60" y="52" width="18" height="200" rx="8" fill="{BLU_200}"/>'
          f'<path class="il-l" d="M78 84h96"/>'
          f'<rect x="168" y="60" width="16" height="52" rx="6" fill="{BLU_700}"/>'
          f'<rect x="296" y="60" width="16" height="52" rx="6" fill="{BLU_700}"/>'
          f'<path class="il-l" d="M184 68h112"/>'
          '</g>')
    # testa scansionata
    c += ('<g class="il-rise d2">'
          f'<circle cx="240" cy="164" r="52" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<path d="M212 176q28 22 56 0" fill="none" stroke="{LINEA}" stroke-width="1.6"/>'
          '</g>')
    # arcata dentro la testa
    c += ('<g class="il-pop d4">'
          f'<path d="M212 168a28 22 0 0 1 56 0" fill="none" stroke="{AMBRA}" stroke-width="3.4" stroke-linecap="round"/>')
    for i in range(7):
        import math
        a = math.pi * (0.1 + i * 0.133)
        x = 240 - 28 * math.cos(a); y = 168 - 22 * math.sin(a)
        c += f'<rect x="{x-3:.1f}" y="{y-4:.1f}" width="6" height="8" rx="1.6" fill="{CARTA}" stroke="{AMBRA}" stroke-width="1.2"/>'
    c += '</g>'
    # fasci di scansione
    for i, y in enumerate([120, 140, 160, 180, 200]):
        c += (f'<path class="il-fade d{i+2}" d="M186 {y}h108" stroke="{BLU_500}" '
              f'stroke-width="1.4" opacity=".45" stroke-dasharray="4 6"/>')
    c += f'<text class="il-fade d6" x="240" y="252" text-anchor="middle" font-family="Manrope,sans-serif" font-size="13" font-weight="700" fill="{BLU_700}">TAC Cone Beam 3D</text>'
    return _svg(c, etichetta="Illustrazione della TAC Cone Beam che scansiona le arcate")


def sterilizzazione():
    c = _cornice()
    # autoclave
    c += ('<g class="il-rise d1">'
          f'<rect x="52" y="80" width="150" height="140" rx="14" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<circle cx="127" cy="140" r="42" fill="{BLU_100}" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<circle cx="127" cy="140" r="30" fill="{BLU_050}"/>'
          f'<circle class="il-a" cx="127" cy="140" r="8"/>'
          f'<path class="il-l" d="M78 198h98"/>'
          f'<circle cx="88" cy="198" r="4" fill="{BLU_500}"/>'
          '</g>')
    # buste sterili impilate
    for i in range(3):
        c += ('<g class="il-pop d%d">' % (i + 3) +
              f'<rect x="{236+i*6}" y="{104+i*40}" width="118" height="30" rx="6" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.6"/>'
              f'<path class="il-l" d="M{244+i*6} {119+i*40}h34" stroke-width="1.4"/>'
              f'<rect x="{326+i*6}" y="{111+i*40}" width="18" height="16" rx="3" fill="{AMBRA_CH}" stroke="{AMBRA}" stroke-width="1.2"/>'
              '</g>')
    # vapore
    c += (f'<path class="il-fade d5" d="M112 68q8-12 0-24M127 62q8-12 0-24M142 68q8-12 0-24" '
          f'stroke="{BLU_500}" stroke-width="2" stroke-linecap="round" fill="none" opacity=".5"/>')
    c += f'<text class="il-fade d6" x="127" y="248" text-anchor="middle" font-family="Manrope,sans-serif" font-size="13" font-weight="700" fill="{BLU_700}">135 °C</text>'
    return _svg(c, etichetta="Illustrazione dell'autoclave e delle buste sterili tracciate")


def ingresso():
    c = _cornice(400, 300)
    # facciata
    c += ('<g class="il-rise d1">'
          f'<rect x="52" y="46" width="296" height="206" rx="10" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<rect x="52" y="46" width="296" height="34" rx="10" fill="{BLU_700}"/>'
          '</g>')
    c += (f'<text class="il-fade d2" x="200" y="69" text-anchor="middle" font-family="Fraunces,Georgia,serif" '
          f'font-size="19" fill="{CARTA}">Piccardo</text>')
    # vetrina
    c += ('<g class="il-rise d3">'
          f'<rect x="76" y="102" width="106" height="126" rx="6" fill="{BLU_100}" stroke="{BLU_700}" stroke-width="1.6"/>'
          f'<rect x="218" y="102" width="106" height="126" rx="6" fill="{BLU_100}" stroke="{BLU_700}" stroke-width="1.6"/>'
          f'<path class="il-l" d="M129 102v126M271 102v126" stroke-width="1.4"/>'
          '</g>')
    # porta e luce che esce
    c += ('<g class="il-pop d4">'
          f'<rect x="182" y="128" width="36" height="100" rx="4" fill="{AMBRA_CH}" stroke="{AMBRA}" stroke-width="1.8"/>'
          f'<circle cx="211" cy="180" r="3" fill="{BLU_700}"/>'
          '</g>')
    # croce insegna
    c += ('<g class="il-pop d5">'
          f'<rect x="322" y="96" width="42" height="42" rx="8" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.6"/>'
          f'<path d="M339 104h8v9h9v8h-9v9h-8v-9h-9v-8h9z" fill="#C4342E"/>'
          '</g>')
    # gradino zero
    c += f'<path class="il-l il-fade d6" d="M40 252h320"/>'
    return _svg(c, etichetta="Illustrazione dell'ingresso dello studio su strada")


def parcheggio():
    c = _cornice()
    # cortile
    c += f'<rect class="il-rise d1" x="40" y="150" width="320" height="110" rx="12" fill="{BLU_100}"/>'
    c += (f'<path class="il-l il-fade d2" d="M92 150v110M200 150v110M308 150v110" stroke-dasharray="8 8" stroke-width="1.6"/>')
    # auto vista dall'alto, nel posto centrale
    c += ('<g class="il-rise d3">'
          f'<rect x="112" y="168" width="76" height="74" rx="16" fill="{BLU_700}"/>'
          f'<rect x="122" y="180" width="56" height="26" rx="8" fill="{BLU_200}"/>'
          f'<rect x="122" y="212" width="56" height="18" rx="6" fill="{BLU_500}"/>'
          '</g>')
    # cartelli "riservato"
    for i, x in enumerate([236, 300]):
        c += ('<g class="il-pop d%d">' % (i + 4) +
              f'<rect x="{x-22}" y="184" width="44" height="30" rx="6" fill="{AMBRA_CH}" stroke="{AMBRA}" stroke-width="1.6"/>'
              f'<path class="il-l" d="M{x-12} 199h24" stroke="{AMBRA}" stroke-width="2.4"/>'
              '</g>')
    # muri del cortile
    c += f'<path class="il-l il-fade d2" d="M40 150h320"/>'
    c += (f'<text class="il-fade d6" x="200" y="290" text-anchor="middle" font-family="Manrope,sans-serif" '
          f'font-size="13" font-weight="700" fill="{BLU_700}">3 posti riservati ai pazienti</text>')
    # tetto/cielo
    c += f'<rect x="40" y="60" width="320" height="80" rx="12" fill="{CARTA}" stroke="{BLU_200}" stroke-width="1.6"/>'
    c += f'<path class="il-l" d="M70 100h60M70 118h100" stroke="{BLU_200}" stroke-width="4"/>'
    return _svg(c, etichetta="Illustrazione dei tre posti auto nel cortile interno")


def bimbi():
    c = _cornice(400, 300, caldo=True)
    # tappeto
    c += f'<ellipse class="il-rise d1" cx="200" cy="228" rx="140" ry="42" fill="{BLU_100}"/>'
    # bambino di spalle sulla poltrona-gioco
    c += ('<g class="il-rise d2">'
          f'<rect x="146" y="140" width="108" height="76" rx="18" fill="{BLU_500}"/>'
          f'<circle cx="200" cy="118" r="30" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<path class="il-l" d="M188 122h.01M212 122h.01" stroke-width="5"/>'
          f'<path class="il-l" d="M188 134q12 12 24 0"/>'
          '</g>')
    # cubi e palla
    c += f'<rect class="il-pop d3" x="70" y="188" width="34" height="34" rx="6" fill="{AMBRA}"/>'
    c += f'<rect class="il-pop d4" x="86" y="154" width="26" height="26" rx="5" fill="{BLU_700}"/>'
    c += f'<circle class="il-pop d5" cx="316" cy="200" r="24" fill="{AMBRA}"/>'
    c += f'<path class="il-pop d5" d="M292 200h48M316 176v48" stroke="{CARTA}" stroke-width="2.4" fill="none"/>'
    # denti che sorridono, come decorazione a parete
    c += ('<g class="il-pop d6">'
          f'<path d="M300 78c-9 0-15 5-15 14 0 5 2 10 3 15 1 6 1 12 2 18 1 4 2 8 5 8s4-4 5-8c1-4 1-8 3-8s2 4 3 8c1 4 2 8 5 8s4-4 5-8c1-6 1-12 2-18 1-5 3-10 3-15 0-9-6-14-15-14z" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.6"/>'
          '</g>')
    return _svg(c, etichetta="Illustrazione dell'area gioco per i bambini in sala d'attesa")


def equipe():
    c = _cornice(400, 300)
    posti = [(84, 200, 30, BLU_200), (150, 186, 34, BLU_100), (222, 186, 34, BLU_100), (300, 200, 30, BLU_200)]
    for i, (x, y, r, col) in enumerate(posti):
        c += ('<g class="il-rise d%d">' % (i + 1) +
              f'<path d="M{x-r-6} 264c0-{r*0.95:.0f} {r*0.5:.0f}-{r*1.4:.0f} {r+6}-{r*1.4:.0f}s{r+6} {r*0.45:.0f} {r+6} {r*1.4:.0f}z" fill="{col}"/>'
              f'<circle cx="{x}" cy="{y-r-4}" r="{r*0.72:.0f}" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.8"/>'
              f'<path class="il-l" d="M{x-7} {y-r-8}h.01M{x+7} {y-r-8}h.01" stroke-width="4.5"/>'
              f'<path class="il-l" d="M{x-8} {y-r+2}q8 7 16 0"/>'
              '</g>')
    # camice bianco con la crocetta ambra
    c += f'<rect class="il-pop d5" x="176" y="216" width="12" height="12" rx="2" fill="{AMBRA}"/>'
    c += f'<rect class="il-pop d6" x="248" y="216" width="12" height="12" rx="2" fill="{AMBRA}"/>'
    return _svg(c, etichetta="Illustrazione dell'équipe dello studio")


def mascherine():
    import math
    c = _cornice(400, 300)

    def guscio(cx, cy, sc, op, denti):
        g = f'<g transform="translate({cx},{cy}) scale({sc})" opacity="{op}">'
        g += (f'<path d="M-96 -34a96 76 0 0 1 192 0c0 52-34 98-52 98-14 0-16-20-44-20s-30 20-44 20c-18 0-52-46-52-98z" '
              f'fill="{BLU_200}" opacity=".5"/>')
        g += (f'<path d="M-96 -34a96 76 0 0 1 192 0c0 52-34 98-52 98-14 0-16-20-44-20s-30 20-44 20c-18 0-52-46-52-98z" '
              f'fill="none" stroke="{BLU_700}" stroke-width="2.6"/>')
        if denti:
            for k in range(9):
                a = math.pi * (0.075 + k * 0.10625)
                x = -76 * math.cos(a); y = -8 - 58 * math.sin(a)
                g += (f'<rect x="{x-8:.1f}" y="{y-11:.1f}" width="16" height="23" rx="4" '
                      f'fill="{CARTA}" stroke="{LINEA}" stroke-width="1.6"/>')
        g += '</g>'
        return g

    # due gusci in secondo piano suggeriscono la serie di allineatori
    c += f'<g class="il-fade d1">{guscio(150, 122, .52, .5, False)}</g>'
    c += f'<g class="il-fade d2">{guscio(188, 116, .62, .7, False)}</g>'
    c += f'<g class="il-rise d3">{guscio(248, 132, .78, 1, True)}</g>'
    # riflesso sul guscio in primo piano
    c += (f'<path class="il-fade d5" d="M196 96q30-26 70-28" fill="none" stroke="{CARTA}" '
          f'stroke-width="6" stroke-linecap="round" opacity=".9"/>')
    # freccia della progressione
    c += ('<g class="il-fade d6">'
          f'<path d="M96 244h180" stroke="{AMBRA}" stroke-width="2.4" stroke-linecap="round" fill="none"/>'
          f'<path d="M268 236l12 8-12 8" fill="none" stroke="{AMBRA}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
          f'<text x="96" y="272" font-family="Manrope,sans-serif" font-size="12" font-weight="700" fill="{BLU_700}">una mascherina ogni due settimane</text>'
          '</g>')
    return _svg(c, etichetta="Illustrazione della serie di mascherine trasparenti Invisalign")


def faccetta():
    c = _cornice(400, 300, caldo=True)
    # dente naturale, di tre quarti, con la superficie da correggere
    c += ('<g class="il-rise d1">'
          f'<path d="M150 236V128c0-38 22-62 56-62s56 24 56 62v108c0 22-12 34-24 34-14 0-16-20-24-38-5-11-8-18-14-18s-9 7-14 18c-8 18-10 38-24 38-12 0-12-12-12-34z" '
          f'fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<path class="il-l" d="M178 122q28-16 56 0" opacity=".4" stroke-width="1.4"/>'
          f'<path class="il-l" d="M170 176q36-10 72 0" opacity=".3" stroke-width="1.4"/>'
          '</g>')
    # lamina in ceramica che scende sulla faccia esterna
    c += ('<g class="il-pop d3">'
          f'<path d="M146 214V126c0-36 20-58 52-58 10 0 18 2 25 6-24 4-41 26-41 58v82z" '
          f'fill="{BLU_200}" opacity=".85" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<path d="M156 138c2-24 14-40 32-46" fill="none" stroke="{CARTA}" stroke-width="4" stroke-linecap="round"/>'
          '</g>')
    # freccia di applicazione
    c += (f'<path class="il-fade d4" d="M96 122h32" fill="none" stroke="{AMBRA}" stroke-width="2.4" stroke-linecap="round"/>'
          f'<path class="il-fade d4" d="M120 114l10 8-10 8" fill="none" stroke="{AMBRA}" stroke-width="2.4" '
          f'stroke-linecap="round" stroke-linejoin="round"/>')
    # quota dello spessore
    c += ('<g class="il-fade d5">'
          f'<path d="M300 96v72" stroke="{AMBRA}" stroke-width="1.6"/>'
          f'<path d="M294 96h12M294 168h12" stroke="{AMBRA}" stroke-width="1.6"/>'
          f'<text x="312" y="136" font-family="Manrope,sans-serif" font-size="15" font-weight="800" fill="{BLU_700}">0,3 mm</text>'
          f'<path d="M266 132h28" stroke="{AMBRA}" stroke-width="1.4" stroke-dasharray="3 3"/>'
          '</g>')
    c += f'<path class="il-pop d6" d="M112 208l5-16 5 16 16 5-16 5-5 16-5-16-16-5z" fill="{AMBRA}"/>'
    return _svg(c, etichetta="Illustrazione di una faccetta in ceramica applicata sulla faccia esterna del dente")


def video():
    c = _cornice(400, 300, BLU_900)
    c += f'<rect width="400" height="300" rx="22" fill="{BLU_900}"/>'
    c += f'<circle cx="316" cy="60" r="120" fill="{BLU_700}" opacity=".5"/>'
    c += f'<circle cx="70" cy="266" r="90" fill="{BLU_500}" opacity=".22"/>'
    # sagoma di una persona che parla
    c += ('<g class="il-rise d1">'
          f'<path d="M118 262c0-38 26-66 62-66s62 28 62 66z" fill="{BLU_500}" opacity=".6"/>'
          f'<circle cx="180" cy="164" r="36" fill="{BLU_200}"/>'
          '</g>')
    # onde della voce
    for i in range(3):
        c += (f'<path class="il-fade d{i+3}" d="M{258+i*20} {160-i*14}a{22+i*20} {22+i*20} 0 0 1 0 {44+i*40}" '
              f'fill="none" stroke="{AMBRA}" stroke-width="2.4" opacity="{0.9-i*0.25}" stroke-linecap="round"/>')
    # pulsante play
    c += ('<g class="il-pop d5">'
          f'<circle cx="200" cy="150" r="40" fill="{AMBRA}"/>'
          f'<path d="M190 134l24 16-24 16z" fill="{BLU_900}"/>'
          '</g>')
    return _svg(c, etichetta="Segnaposto per un video da produrre")


def prima_dopo_ill():
    c = _cornice()
    for i, (x, col) in enumerate([(24, BLU_100), (208, AMBRA_CH)]):
        c += ('<g class="il-rise d%d">' % (i + 1) +
              f'<rect x="{x+18}" y="70" width="150" height="160" rx="14" fill="{col}" stroke="{BLU_700}" stroke-width="1.8"/>')
        import math
        for k in range(7):
            a = math.pi * (0.12 + k * 0.127)
            cx = x + 93 - 52 * math.cos(a); cy = 172 - 40 * math.sin(a)
            # nel riquadro "prima" i denti sono ruotati, sfalsati e con un vuoto
            rot = 0 if i else (((k * 31) % 11) - 5) * 6.5
            dx = 0 if i else (((k * 17) % 9) - 4) * 2.4
            if not i and k == 4:      # elemento mancante, solo nel "prima"
                continue
            dy = 0 if i else abs(((k * 23) % 7) - 3) * 1.8
            c += (f'<rect x="{cx-6+dx:.1f}" y="{cy-9+dy:.1f}" width="12" height="20" rx="3" fill="{CARTA}" '
                  f'stroke="{LINEA}" stroke-width="1.2" transform="rotate({rot:.1f} {cx+dx:.1f} {cy+dy:.1f})"/>')
        c += (f'<path d="M{x+40} 190a53 40 0 0 0 106 0" fill="none" stroke="{BLU_700}" stroke-width="2.2" opacity=".35"/>')
        c += (f'<text x="{x+93}" y="256" text-anchor="middle" font-family="Manrope,sans-serif" font-size="12" '
              f'font-weight="800" letter-spacing="1.6" fill="{BLU_700}">{"DOPO" if i else "PRIMA"}</text>')
        c += '</g>'
    c += f'<path class="il-fade d3" d="M200 60v190" stroke="{CARTA}" stroke-width="4"/>'
    c += ('<g class="il-pop d4">'
          f'<circle cx="200" cy="150" r="21" fill="{CARTA}" stroke="{BLU_700}" stroke-width="1.8"/>'
          f'<path d="M192 143l-7 7 7 7M208 143l7 7-7 7" fill="none" stroke="{BLU_700}" stroke-width="2" stroke-linecap="round"/>'
          '</g>')
    return _svg(c, etichetta="Segnaposto per un caso clinico fotografato prima e dopo")


SCENE = {
    "poltrona": poltrona, "maschera": maschera, "laboratorio": laboratorio,
    "radiologia": radiologia, "sterilizzazione": sterilizzazione, "ingresso": ingresso,
    "parcheggio": parcheggio, "bimbi": bimbi, "equipe": equipe,
    "mascherine": mascherine, "faccetta": faccetta, "video": video,
    "prima-dopo": prima_dopo_ill,
}


def illustrazione(nome):
    """Restituisce il markup della scena richiesta."""
    return SCENE[nome]()
