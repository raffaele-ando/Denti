# -*- coding: utf-8 -*-
"""Libreria visiva: icone SVG originali, diagrammi animati, componenti."""

# ══════════════════════════════════════════════════════════════════ ICONE
# Set disegnato per questo progetto. Griglia 24, tratto 1.6, terminali tondi.
_P = {
 "telefono": '<path d="M5.5 3.5h3l1.6 4-2 1.4a12.5 12.5 0 0 0 5.5 5.5l1.4-2 4 1.6v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 3.5 5.7 2 2 0 0 1 5.5 3.5Z"/>',
 "whatsapp": '<path d="M3.8 20.2 5 16.4A7.9 7.9 0 1 1 7.9 19l-4.1 1.2Z"/><path d="M9 9.2c0 3 2.3 5.2 5.1 5.4.7 0 1.4-.5 1.5-1.1l-1.8-.9-.8.9a5.4 5.4 0 0 1-2.4-2.4l.9-.8-.9-1.8c-.7.1-1.6.6-1.6 1.3"/>',
 "calendario": '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 9.8h17M8 3v4M16 3v4"/><circle cx="8.4" cy="14" r="1.1" fill="currentColor" stroke="none"/>',
 "freccia": '<path d="M4 12h15m-5.5-5.5L19.5 12l-6 5.5"/>',
 "frecciasu": '<path d="M12 19V5m-5.5 5.5L12 5l5.5 5.5"/>',
 "scambio": '<path d="M8 7 4.5 10.5 8 14M16 10 19.5 13.5 16 17"/>',
 "check": '<path d="M4.5 12.5 9.5 17.5 19.5 6.5"/>',
 "chevron": '<path d="M6 9.5 12 15.5l6-6"/>',
 "chiudi": '<path d="M6 6l12 12M18 6 6 18"/>',
 "piu": '<path d="M12 5v14M5 12h14"/>',
 "cerca": '<circle cx="11" cy="11" r="6.5"/><path d="m16 16 4 4"/>',
 "pin": '<path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/>',
 "orologio": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7v5.4l3.4 2"/>',
 "auto": '<path d="M4 16.5v2.2M20 16.5v2.2M3 16.5h18v-4l-1.6-.6-2-4.4H7.6l-2 4.4-2.6.6Z"/><circle cx="7.5" cy="16.5" r="0" /><path d="M5.6 11.9h12.8"/>',
 "scudo": '<path d="M12 3 5 5.8v5.4c0 4.3 2.9 7.9 7 9.8 4.1-1.9 7-5.5 7-9.8V5.8Z"/><path d="m9 12 2.2 2.2L15.4 10"/>',
 "dente": '<path d="M12 3.5c-2.7 0-4.6 1.7-4.6 4.4 0 1.7.5 3.1.8 4.8.3 1.6.2 3.2.5 4.8.2 1.1.6 2.2 1.4 2.2s1-1.1 1.2-2.3c.2-1 .3-2.1.7-2.1s.5 1 .7 2.1c.2 1.2.4 2.3 1.2 2.3s1.2-1.1 1.4-2.2c.3-1.6.2-3.2.5-4.8.3-1.7.8-3.1.8-4.8 0-2.7-1.9-4.4-4.6-4.4Z"/>',
 "impianto": '<path d="M12 3v3.5"/><path d="M9 6.5h6l-.7 3H9.7Z"/><path d="M10 9.5h4l-.5 3.5h-3Z"/><path d="M10.7 13h2.6l-.6 4.5a.7.7 0 0 1-1.4 0Z"/><path d="M8.6 8h6.8M9 11h6"/>',
 "mascherina": '<path d="M4 9.5c0-2.4 3.6-4 8-4s8 1.6 8 4c0 3.6-2.4 8.5-4.4 8.5-1.2 0-1.4-1.6-3.6-1.6s-2.4 1.6-3.6 1.6C6.4 18 4 13.1 4 9.5Z"/><path d="M7.5 8.6h9"/>',
 "scintilla": '<path d="M12 3.5 13.7 9l5.5 1.7-5.5 1.7L12 18l-1.7-5.6L4.8 10.7 10.3 9Z"/><path d="M18.6 4.2v2.6M17.3 5.5h2.6"/>',
 "corona": '<path d="M12 4.2c-3 0-5.2 1.9-5.2 4.7 0 2.3 1 3.6 1.4 5.9.3 1.6.4 4 1.6 4 1 0 1.1-1.9 1.3-3.1.2-.9.4-1.6.9-1.6s.7.7.9 1.6c.2 1.2.3 3.1 1.3 3.1 1.2 0 1.3-2.4 1.6-4 .4-2.3 1.4-3.6 1.4-5.9 0-2.8-2.2-4.7-5.2-4.7Z"/><path d="M7.5 10.2c1.6-1.2 7.4-1.2 9 0"/>',
 "bisturi": '<path d="m4 20 4.8-4.8"/><path d="M9.4 14.6 19 5V3h-2l-9.6 9.6a1.5 1.5 0 0 0 0 2.1 1.5 1.5 0 0 0 2 0Z"/><path d="M14.5 7.5 16.8 9.8"/>',
 "foglia": '<path d="M5 19c0-8 5-13 14-13 0 9-4.4 13-9.5 13A4.5 4.5 0 0 1 5 19Z"/><path d="M8.5 15.5C10.5 12 13.5 9.8 17 8.6"/>',
 "bimbo": '<circle cx="12" cy="8" r="4.2"/><path d="M4.8 20.5a7.2 7.2 0 0 1 14.4 0"/><path d="M10.3 7.6h.01M13.7 7.6h.01"/><path d="M10.6 10c.9.7 1.9.7 2.8 0"/>',
 "pronto": '<path d="M2.8 12.2h4l1.7-3.6 2.9 7.6 2.2-5.2 1.4 2.4h6.2"/><path d="M20.5 15.6a5 5 0 0 1-.8 1c-1.4 1.5-4.6 4.2-7.7 6.1"/>',
 "calma": '<path d="M4.2 19.8 9 15"/><path d="M6.6 17.4C3.9 14.7 4.4 9.4 8 5.8c3.1-3.1 7.3-3.6 10.4-2.2 1.4 3.1.9 7.3-2.2 10.4-3.6 3.6-8.9 4.1-11.6 1.4Z"/><path d="M15.4 5.2 8.9 11.7M12.8 7.1h3.6M10.6 9.3h3.4M8.6 11.5h3.2"/>',
 "goccia": '<path d="M12 3.5S5.8 10 5.8 14.2a6.2 6.2 0 0 0 12.4 0C18.2 10 12 3.5 12 3.5Z"/><path d="M9.2 15.2a2.9 2.9 0 0 0 2.6 2.6"/>',
 "onda": '<path d="M2.5 12c2-4 3.8-4 5.8 0s3.8 4 5.8 0 3.8-4 5.8 0"/><path d="M2.5 17c2-2.6 3.8-2.6 5.8 0s3.8 2.6 5.8 0 3.8-2.6 5.8 0" opacity=".45"/><path d="M2.5 7c2-2.6 3.8-2.6 5.8 0s3.8 2.6 5.8 0 3.8-2.6 5.8 0" opacity=".45"/>',
 "grafico": '<path d="M4 20V9M9.3 20V4.5M14.7 20v-8M20 20V7"/>',
 "scan": '<path d="M3.5 8V5.5a2 2 0 0 1 2-2H8M16 3.5h2.5a2 2 0 0 1 2 2V8M20.5 16v2.5a2 2 0 0 1-2 2H16M8 20.5H5.5a2 2 0 0 1-2-2V16"/><path d="M3.5 12h17"/>',
 "libro": '<path d="M4 4.5h6a3 3 0 0 1 2 2.6v12a2.4 2.4 0 0 0-2-1.6H4Z"/><path d="M20 4.5h-6a3 3 0 0 0-2 2.6v12a2.4 2.4 0 0 1 2-1.6h6Z"/>',
 "euro": '<circle cx="12" cy="12" r="8.5"/><path d="M15.6 8.4a4.4 4.4 0 0 0-6.6 3.6 4.4 4.4 0 0 0 6.6 3.6M7.6 10.8h5.2M7.6 13.2h5.2"/>',
 "stella": '<path d="m12 3.8 2.6 5.3 5.9.9-4.3 4.1 1 5.9-5.2-2.8-5.2 2.8 1-5.9L3.5 10l5.9-.9Z"/>',
 "cuore": '<path d="M12 20.3S3.8 15.6 3.8 9.7a4.5 4.5 0 0 1 8.2-2.6 4.5 4.5 0 0 1 8.2 2.6c0 5.9-8.2 10.6-8.2 10.6Z"/>',
 "occhio": '<path d="M2.5 12S6 5.8 12 5.8 21.5 12 21.5 12 18 18.2 12 18.2 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="3"/>',
 "info": '<circle cx="12" cy="12" r="8.5"/><path d="M12 11v5.2M12 7.9h.01"/>',
 "upload": '<path d="M4.5 15.5v3a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2v-3"/><path d="M12 3.5v11M7.8 7.7 12 3.5l4.2 4.2"/>',
 "play": '<circle cx="12" cy="12" r="8.5"/><path d="m10 8.6 6 3.4-6 3.4Z"/>',
 "camera": '<path d="M3.5 8.5h3l1.5-2.4h8l1.5 2.4h3a1 1 0 0 1 1 1v8.5a1.5 1.5 0 0 1-1.5 1.5H4a1.5 1.5 0 0 1-1.5-1.5V9.5a1 1 0 0 1 1-1Z"/><circle cx="12" cy="13.2" r="3.4"/>',
 "video": '<rect x="2.8" y="6" width="12.6" height="12" rx="2.4"/><path d="m15.4 12.6 5.8 3.4V8l-5.8 3.4Z"/>',
 "accessibile": '<circle cx="12" cy="4.6" r="1.8"/><path d="M7.5 8.2h9M12 8v5h3.6l2.4 6.4M12 13c-2.4 0-4.4 2-4.4 4.4A4.4 4.4 0 0 0 14 21.4"/>',
 "treno": '<rect x="5.5" y="3.5" width="13" height="12.5" rx="3"/><path d="M5.5 10.5h13M8.4 19.5l-2 2M15.6 19.5l2 2M8.5 16.5h.01M15.5 16.5h.01"/>',
 "bus": '<rect x="4" y="4" width="16" height="12.5" rx="2.5"/><path d="M4 11h16M8 19.5v1.5M16 19.5V21M7.5 14h.01M16.5 14h.01"/><path d="M6.5 16.5v3M17.5 16.5v3"/>',
 "battito": '<path d="M20.4 12h-4l-1.6 4.6-4-11.2L9.2 12H3.6"/>',
 "documento": '<path d="M13.5 3.5H7a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V9Z"/><path d="M13.5 3.5V9H19M8.6 13.4h6.8M8.6 16.6h4.4"/>',
 "virgolette": '<path d="M9.5 6C6.5 7.4 5 9.8 5 13.2V18h5.5v-5.6H8.2c0-1.9.7-3.3 2.1-4.2ZM19.5 6C16.5 7.4 15 9.8 15 13.2V18h5.5v-5.6h-2.3c0-1.9.7-3.3 2.1-4.2Z"/>',
 "instagram": '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17" cy="7" r="1" fill="currentColor" stroke="none"/>',
 "facebook": '<path d="M14.5 21v-8h2.7l.5-3.2h-3.2V7.7c0-.9.3-1.6 1.7-1.6h1.7V3.2A22 22 0 0 0 15.3 3c-2.6 0-4.3 1.6-4.3 4.4v2.4H8v3.2h3V21Z"/>',
 "youtube": '<rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="m10.3 9.5 5 2.5-5 2.5Z"/>',
 "linkedin": '<rect x="3.5" y="3.5" width="17" height="17" rx="3"/><path d="M8 10.5V17M8 7.4h.01M12 17v-3.6c0-1.6 2.4-1.7 2.4 0V17M12 10.5V17"/>',
 "x": '<path d="m4 4 7.6 9.6L4.4 20M20 4l-7.4 8.2L20 20h-3.6L4 4h3.6Z"/>',
}

_FILL = {"stella", "virgolette", "facebook", "x", "dente"}


def ico(nome, cls="", size=None):
    """Restituisce un'icona SVG inline."""
    p = _P.get(nome)
    if p is None:
        raise KeyError(f"icona sconosciuta: {nome}")
    riempita = nome in _FILL
    stile = 'fill="currentColor" stroke="none"' if riempita else \
            'fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'
    dim = f' width="{size}" height="{size}"' if size else ""
    c = f' class="{cls}"' if cls else ""
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"{dim}{c} {stile}>{p}</svg>'


def marchio(cls="brand__mark"):
    """Croce di San Giorgio costruita su griglia, con il dente in negativo."""
    return f'''<svg class="{cls}" viewBox="0 0 32 32" aria-hidden="true">
  <path class="cross" d="M11.6 0h8.8v11.6H32v8.8H20.4V32h-8.8V20.4H0v-8.8h11.6z"/>
  <path class="tooth" d="M16 8.4c-2.35 0-4 1.45-4 3.75 0 1.45.43 2.65.69 4.1.26 1.36.17 2.73.43 4.1.17.94.51 1.88 1.2 1.88.69 0 .86-.94 1.03-1.96.17-.85.26-1.79.65-1.79s.48.94.65 1.79c.17 1.02.34 1.96 1.03 1.96.69 0 1.03-.94 1.2-1.88.26-1.37.17-2.74.43-4.1.26-1.45.69-2.65.69-4.1 0-2.3-1.65-3.75-4-3.75z"/>
</svg>'''


def stelle(n=5, cls=""):
    return f'<span class="stars {cls}" aria-hidden="true">' + ico("stella") * n + '</span>'


# ═══════════════════════════════════════════════════════════════ DIAGRAMMI
# Illustrazioni vettoriali originali, animate all'ingresso in viewport.
# Sostituiscono i paragrafi descrittivi: è il "show, don't tell" del progetto.

_STILE_DIAG = """<style>
 .dg{font-family:'Manrope',sans-serif}
 .dg-lbl{font-size:8.5px;font-weight:700;fill:#5A6B7A;letter-spacing:.04em;text-transform:uppercase}
 .dg-n{font-size:9px;font-weight:800;fill:#134B7A}
 .dg-cap{font-size:9.5px;font-weight:600;fill:#0B1A28}
 .dg-bone{fill:#EAE5DC;stroke:#DDD9D2;stroke-width:.8}
 .dg-gum{fill:#E9C9C4}
 .dg-tooth{fill:#FBFAF7;stroke:#DDD9D2;stroke-width:.8}
 .dg-metal{fill:#134B7A}
 .dg-line{stroke:#DDD9D2;stroke-width:1;stroke-dasharray:3 3}
 .dg-acc{fill:#2A7CBF}
 [data-reveal].is-in .dg-draw{stroke-dashoffset:0}
 .dg-draw{stroke-dasharray:400;stroke-dashoffset:400;transition:stroke-dashoffset 1.6s cubic-bezier(.22,1,.36,1) .2s}
 .dg-pop{opacity:0;transform:scale(.7);transform-origin:center;transition:opacity .5s cubic-bezier(.22,1,.36,1),transform .5s cubic-bezier(.22,1,.36,1)}
 [data-reveal].is-in .dg-pop{opacity:1;transform:none}
 [data-reveal].is-in .dg-pop:nth-of-type(2){transition-delay:.15s}
 [data-reveal].is-in .dg-pop:nth-of-type(3){transition-delay:.3s}
 [data-reveal].is-in .dg-pop:nth-of-type(4){transition-delay:.45s}
 .dg-grow{transform:scaleY(0);transform-origin:bottom;transition:transform .9s cubic-bezier(.22,1,.36,1)}
 [data-reveal].is-in .dg-grow{transform:none}
 @media(prefers-reduced-motion:reduce){.dg-draw{stroke-dashoffset:0}.dg-pop{opacity:1;transform:none}.dg-grow{transform:none}}
</style>"""


def _fase_impianto(x, fase):
    """Un riquadro del diagramma implantare: osso, gengiva, denti con radici."""
    def dente(cx, w=26, h=30, r=26, op=1.0, bordo="#DDD9D2"):
        """Corona sopra gengiva + due radici nell'osso."""
        g = (f'<path d="M{cx-w/2} 62V{62-h}c0-{h*0.55:.0f} {w*0.22:.0f}-{h*0.42:.0f} {w/2:.0f}-{h*0.42:.0f}'
             f's{w/2:.0f} {h*0.14:.0f} {w/2:.0f} {h*0.42:.0f}V62z" class="dg-tooth" opacity="{op}"/>')
        g += (f'<path d="M{cx-w/2+2} 62c0 {r*0.5:.0f} 1.5 {r*0.75:.0f} 3.5 {r:.0f} 1.6 {r*0.16:.0f} 3-{r*0.1:.0f} 3.4-{r*0.5:.0f}'
              f'l1.1-{r*0.42:.0f}" fill="none" stroke="{bordo}" stroke-width="1.5" opacity="{op}"/>')
        g += (f'<path d="M{cx+w/2-2} 62c0 {r*0.5:.0f} -1.5 {r*0.75:.0f} -3.5 {r:.0f} -1.6 {r*0.16:.0f} -3-{r*0.1:.0f} -3.4-{r*0.5:.0f}'
              f'l-1.1-{r*0.42:.0f}" fill="none" stroke="{bordo}" stroke-width="1.5" opacity="{op}"/>')
        return g

    g = f'<g transform="translate({x},0)">'
    g += '<rect x="0" y="0" width="118" height="132" rx="10" fill="#FBFAF7" stroke="#ECE8E1"/>'
    g += '<path class="dg-bone" d="M12 58h94v54a6 6 0 0 1-6 6H18a6 6 0 0 1-6-6z"/>'
    for i in range(9):          # trabecolatura ossea
        g += f'<circle cx="{18+i*10.5}" cy="{86+((i*37)%17)-8}" r="1.6" fill="#DDD9D2" opacity=".8"/>'
    g += '<path class="dg-gum" d="M12 58h94v9H12z"/>'
    g += '<path d="M12 58h94" stroke="#D9AFA8" stroke-width="1"/>'

    if fase == 1:
        g += dente(34) + dente(84)
        g += '<ellipse cx="59" cy="63" rx="11" ry="4.5" fill="#D9AFA8" opacity=".55"/>'
        g += '<path d="M48 63q11 -9 22 0" fill="none" stroke="#C4342E" stroke-width="1.2" stroke-dasharray="2.5 2.5" opacity=".7"/>'
    elif fase == 2:
        g += dente(34, op=.35) + dente(84, op=.35)
        g += '<path class="dg-metal" d="M52 62h14l-1.6 40a5.4 5.4 0 0 1-10.8 0z"/>'
        for i in range(7):
            g += f'<path d="M52.4 {67+i*5.2}h13.2" stroke="#FBFAF7" stroke-width="1.2" opacity=".85"/>'
        g += '<path class="dg-draw" d="M59 16v34" stroke="#2A7CBF" stroke-width="1.6" stroke-dasharray="40" stroke-dashoffset="40"/>'
        g += '<path d="M55.4 48l3.6 6.4 3.6-6.4z" class="dg-acc"/>'
    elif fase == 3:
        g += dente(34, op=.35) + dente(84, op=.35)
        g += '<path class="dg-metal" d="M52 62h14l-1.6 40a5.4 5.4 0 0 1-10.8 0z"/>'
        for i in range(7):
            g += f'<path d="M52.4 {67+i*5.2}h13.2" stroke="#FBFAF7" stroke-width="1.2" opacity=".85"/>'
        g += '<ellipse cx="59" cy="84" rx="24" ry="26" fill="none" stroke="#2A7CBF" stroke-width="1.1" stroke-dasharray="3 4" opacity=".55"/>'
        for cx, cy in [(42, 74), (77, 80), (44, 96), (76, 98), (40, 86), (79, 90)]:
            g += f'<circle class="dg-pop" cx="{cx}" cy="{cy}" r="2.6" fill="#2A7CBF" opacity=".45"/>'
    else:
        g += '<path class="dg-metal" d="M52 62h14l-1.6 40a5.4 5.4 0 0 1-10.8 0z"/>'
        for i in range(7):
            g += f'<path d="M52.4 {67+i*5.2}h13.2" stroke="#FBFAF7" stroke-width="1.2" opacity=".85"/>'
        g += dente(34) + dente(84)
        g += ('<path d="M46 62V34c0-16 6-24 13-24s13 8 13 24v28z" fill="#FBFAF7" '
              'stroke="#2A7CBF" stroke-width="1.5"/>')
        g += '<path d="M50 24q9 -6 18 0" fill="none" stroke="#B4D3EC" stroke-width="2.4" stroke-linecap="round"/>'
    g += '</g>'
    return g


def diagramma(tipo):
    """Restituisce il markup SVG del diagramma richiesto."""

    if tipo == "impianto":
        eti = ["Il vuoto", "Inserimento", "Osteointegrazione", "Corona"]
        s = '<svg class="dg" viewBox="0 0 512 160" role="img" aria-label="Le quattro fasi dell\'inserimento di un impianto dentale">' + _STILE_DIAG
        for i in range(4):
            x = i * 131
            s += _fase_impianto(x, i + 1)
            s += f'<text class="dg-n" x="{x+10}" y="150">0{i+1}</text>'
            s += f'<text class="dg-lbl" x="{x+28}" y="150">{eti[i]}</text>'
            if i < 3:
                s += f'<path d="M{x+122} 66h5" stroke="#DDD9D2" stroke-width="1.4" stroke-linecap="round"/>'
        s += '</svg>'
        return s

    if tipo == "allineatori":
        s = '<svg class="dg" viewBox="0 0 512 170" role="img" aria-label="Progressione dell\'allineamento con le mascherine trasparenti">' + _STILE_DIAG
        # arcata che si allinea progressivamente
        import math
        for step in range(4):
            x0 = step * 131
            dis = 1 - step / 3.0           # disordine residuo
            s += f'<rect x="{x0}" y="0" width="118" height="120" rx="10" fill="#FBFAF7" stroke="#ECE8E1"/>'
            s += f'<path d="M{x0+18} 86a41 34 0 0 1 82 0" fill="none" class="dg-gum" stroke="#E9C9C4" stroke-width="9" stroke-linecap="round"/>'
            for k in range(9):
                a = math.pi * (0.09 + k * 0.1025)
                cx = x0 + 59 - 40 * math.cos(a)
                cy = 86 - 33 * math.sin(a)
                rot = (k - 4) * 11 + (((k * 37) % 13) - 6) * 2.6 * dis
                dx = (((k * 53) % 11) - 5) * 0.55 * dis
                w = 9.5 if 2 <= k <= 6 else 8
                s += (f'<rect x="{cx-w/2+dx:.1f}" y="{cy-6:.1f}" width="{w}" height="12.5" rx="2.6" '
                      f'class="dg-tooth" transform="rotate({rot:.1f} {cx+dx:.1f} {cy:.1f})"/>')
            # mascherina
            op = 0.85 if step > 0 else 0.0
            s += (f'<path d="M{x0+16} 88a43 36 0 0 1 86 0" fill="none" stroke="#2A7CBF" '
                  f'stroke-width="2" opacity="{op}" stroke-linecap="round"/>')
            lab = ["Situazione iniziale", "Mascherina 1", "A metà percorso", "Risultato"][step]
            s += f'<text class="dg-n" x="{x0+10}" y="140">0{step+1}</text>'
            s += f'<text class="dg-lbl" x="{x0+28}" y="140">{lab}</text>'
            if step == 0:
                s += f'<text class="dg-lbl" x="{x0+10}" y="156" fill="#74838F">ClinCheck: lo vedi prima</text>'
        s += '</svg>'
        return s

    if tipo == "ansia":
        # curva dell'ansia durante la seduta, con e senza sedazione
        s = '<svg class="dg" viewBox="0 0 512 220" role="img" aria-label="Andamento dell\'ansia durante la seduta, con e senza sedazione cosciente">' + _STILE_DIAG
        s += '<line x1="46" y1="20" x2="46" y2="168" class="dg-line"/>'
        s += '<line x1="46" y1="168" x2="486" y2="168" class="dg-line"/>'
        s += '<text class="dg-lbl" x="46" y="14" transform="rotate(0)">Ansia percepita</text>'
        for i, t in enumerate(["Sala d'attesa", "Poltrona", "Anestesia", "Intervento", "Fine"]):
            x = 76 + i * 100
            s += f'<text class="dg-lbl" x="{x}" y="184" text-anchor="middle">{t}</text>'
            s += f'<line x1="{x}" y1="164" x2="{x}" y2="172" stroke="#DDD9D2" stroke-width="1"/>'
        # senza sedazione
        s += ('<path class="dg-draw" d="M76 118 C126 92 146 44 176 40 C216 34 226 32 276 30 C326 28 346 60 376 92 L476 140" '
              'fill="none" stroke="#C4342E" stroke-width="2.2" stroke-linecap="round" opacity=".75"/>')
        # con sedazione
        s += ('<path class="dg-draw" d="M76 118 C126 122 146 136 176 142 C216 148 226 150 276 152 C326 153 346 152 376 152 L476 156" '
              'fill="none" stroke="#2A7CBF" stroke-width="2.8" stroke-linecap="round" style="transition-delay:.5s"/>')
        s += '<circle class="dg-pop" cx="276" cy="30" r="4" fill="#C4342E"/>'
        s += '<circle class="dg-pop" cx="276" cy="152" r="4" fill="#2A7CBF"/>'
        s += '<g class="dg-pop"><rect x="286" y="16" width="128" height="24" rx="12" fill="#FBEEED"/><text class="dg-cap" x="298" y="31" fill="#C4342E">Senza sedazione</text></g>'
        s += '<g class="dg-pop"><rect x="286" y="140" width="120" height="24" rx="12" fill="#DBEAF7"/><text class="dg-cap" x="298" y="155" fill="#134B7A">Con sedazione</text></g>'
        s += '<text class="dg-lbl" x="46" y="206" fill="#74838F">Rappresentazione qualitativa dell\'esperienza riferita dai pazienti.</text>'
        s += '</svg>'
        return s

    if tipo == "carie":
        s = '<svg class="dg" viewBox="0 0 512 168" role="img" aria-label="I quattro stadi di evoluzione di una carie">' + _STILE_DIAG
        prof = [12, 26, 44, 58]
        colori = ["#EAE5DC", "#D9CFBE", "#B08A5B", "#8C5A3C"]
        for i in range(4):
            x = i * 131
            s += f'<rect x="{x}" y="0" width="118" height="122" rx="10" fill="#FBFAF7" stroke="#ECE8E1"/>'
            s += f'<path class="dg-tooth" d="M{x+30} 96V44c0-13 9-22 29-22s29 9 29 22v52c0 9-6 14-11 14-6 0-7-8-9-14-2-5-4-9-9-9s-7 4-9 9c-2 6-3 14-9 14-5 0-11-5-11-14z"/>'
            # polpa
            s += f'<path d="M{x+52} 92V54c0-6 3-9 7-9s7 3 7 9v38z" fill="#E9C9C4"/>'
            # lesione
            s += (f'<path class="dg-grow" d="M{x+48} 26 q11 -6 22 0 l-3 {prof[i]} q-8 5 -16 0 z" '
                  f'fill="{colori[i]}" style="transition-delay:{i*.12}s"/>')
            if i == 3:
                s += f'<circle class="dg-pop" cx="{x+59}" cy="112" r="7" fill="#C4342E" opacity=".35"/>'
            lab = ["Smalto", "Dentina", "Polpa", "Ascesso"][i]
            cost = ["controllo", "130 €", "310 € + corona", "estrazione o 1.540 €"][i]
            s += f'<text class="dg-n" x="{x+10}" y="140">0{i+1}</text>'
            s += f'<text class="dg-lbl" x="{x+28}" y="140">{lab}</text>'
            s += f'<text class="dg-lbl" x="{x+10}" y="156" fill="#74838F">{cost}</text>'
        s += '</svg>'
        return s

    if tipo == "sterilizzazione":
        passi = ["Pre-lavaggio", "Ultrasuoni", "Multisteril", "Imbustamento", "Autoclave B", "Stoccaggio"]
        det = ["vasca", "lavaggio", "asciugatura", "tracciabilità", "135 °C", "ISO 9001"]
        s = '<svg class="dg" viewBox="0 0 512 116" role="img" aria-label="Il percorso di sterilizzazione dello strumentario in sei passaggi">' + _STILE_DIAG
        s += '<line x1="34" y1="40" x2="478" y2="40" stroke="#DDD9D2" stroke-width="1.4"/>'
        s += '<line class="dg-draw" x1="34" y1="40" x2="478" y2="40" stroke="#2A7CBF" stroke-width="1.8" stroke-dasharray="450" stroke-dashoffset="450"/>'
        for i in range(6):
            x = 34 + i * 88.8
            s += f'<circle class="dg-pop" cx="{x:.0f}" cy="40" r="10" fill="#FBFAF7" stroke="#2A7CBF" stroke-width="1.8" style="transition-delay:{i*.1}s"/>'
            s += f'<text class="dg-n" x="{x:.0f}" y="43.5" text-anchor="middle" font-size="8.5">{i+1}</text>'
            s += f'<text class="dg-cap" x="{x:.0f}" y="70" text-anchor="middle" font-size="8">{passi[i]}</text>'
            s += f'<text class="dg-lbl" x="{x:.0f}" y="83" text-anchor="middle" font-size="7" fill="#74838F">{det[i]}</text>'
        s += '</svg>'
        return s

    if tipo == "sorriso":
        fasi = [("Salute", "gengive e carie"), ("Posizione", "ortodonzia"),
                ("Colore", "igiene e sbiancamento"), ("Forma", "faccette e ceramica")]
        s = '<svg class="dg" viewBox="0 0 512 150" role="img" aria-label="L\'ordine corretto di un percorso estetico">' + _STILE_DIAG
        for i, (t, d) in enumerate(fasi):
            x = i * 131
            s += f'<rect x="{x}" y="8" width="118" height="90" rx="10" fill="#FBFAF7" stroke="#ECE8E1"/>'
            # bocca schematica che migliora
            y = 60
            s += f'<path d="M{x+26} {y} q33 {26 + i*2} 66 0" fill="none" stroke="#E9C9C4" stroke-width="8" stroke-linecap="round"/>'
            for k in range(6):
                dx = x + 32 + k * 11
                dy = y + 9 + abs(k - 2.5) * -1.6 + (3 - i) * (((k * 29) % 7) - 3) * 0.5
                w = 8.4
                s += f'<rect x="{dx-w/2:.1f}" y="{dy:.1f}" width="{w}" height="10" rx="2" class="dg-tooth" opacity="{0.55+i*0.15}"/>'
            s += f'<circle class="dg-pop" cx="{x+96}" cy="26" r="7.5" fill="#DBEAF7" style="transition-delay:{i*.12}s"/>'
            s += f'<path class="dg-pop" d="M{x+92.5} 26l2.5 2.6 4.5-5" fill="none" stroke="#134B7A" stroke-width="1.6" stroke-linecap="round" style="transition-delay:{i*.12}s"/>'
            s += f'<text class="dg-n" x="{x+10}" y="118">0{i+1}</text>'
            s += f'<text class="dg-lbl" x="{x+28}" y="118">{t}</text>'
            s += f'<text class="dg-lbl" x="{x+10}" y="134" fill="#74838F">{d}</text>'
        s += '</svg>'
        return s

    if tipo == "protesi":
        fasi = [("Scansione", "impronta digitale"), ("CAD", "progettazione 3D"),
                ("CAM", "fresatura in zirconia"), ("Prova", "e cementazione")]
        s = '<svg class="dg" viewBox="0 0 512 150" role="img" aria-label="Dal dente al manufatto protesico con flusso digitale">' + _STILE_DIAG
        for i, (t, d) in enumerate(fasi):
            x = i * 131
            s += f'<rect x="{x}" y="8" width="118" height="90" rx="10" fill="#FBFAF7" stroke="#ECE8E1"/>'
            cx, cy = x + 59, 54
            if i == 0:
                s += f'<path class="dg-tooth" d="M{cx-18} {cy+22}V{cy-8}c0-9 7-15 18-15s18 6 18 15v30z"/>'
                for k in range(5):
                    s += f'<path class="dg-pop" d="M{cx-20} {cy-14+k*9}h40" stroke="#2A7CBF" stroke-width="1" opacity=".5" style="transition-delay:{k*.06}s"/>'
            elif i == 1:
                s += f'<path d="M{cx-18} {cy+22}V{cy-8}c0-9 7-15 18-15s18 6 18 15v30z" fill="none" stroke="#2A7CBF" stroke-width="1.2" stroke-dasharray="3 2"/>'
                for k in range(4):
                    s += f'<circle class="dg-pop" cx="{cx-14+k*10}" cy="{cy-6}" r="2" fill="#2A7CBF" style="transition-delay:{k*.08}s"/>'
            elif i == 2:
                s += f'<rect x="{cx-22}" y="{cy-16}" width="44" height="40" rx="4" fill="#EAE5DC" stroke="#DDD9D2"/>'
                s += f'<path class="dg-tooth" d="M{cx-14} {cy+18}V{cy-6}c0-7 6-12 14-12s14 5 14 12v24z"/>'
                s += f'<path class="dg-pop" d="M{cx} {cy-30}v10" stroke="#134B7A" stroke-width="2.4" stroke-linecap="round"/>'
            else:
                s += f'<path class="dg-gum" d="M{cx-24} {cy+12}h48v14h-48z"/>'
                s += f'<path class="dg-tooth" d="M{cx-16} {cy+14}V{cy-10}c0-8 7-13 16-13s16 5 16 13v24z" stroke="#2A7CBF" stroke-width="1.2"/>'
            s += f'<text class="dg-n" x="{x+10}" y="118">0{i+1}</text>'
            s += f'<text class="dg-lbl" x="{x+28}" y="118">{t}</text>'
            s += f'<text class="dg-lbl" x="{x+10}" y="134" fill="#74838F">{d}</text>'
        s += '</svg>'
        return s

    if tipo == "prevenzione":
        val = [200, 160, 1080, 1540]
        lab = ["Igiene x2 / anno", "Otturazione", "Devitalizz. + corona", "Impianto + corona"]
        s = '<svg class="dg" viewBox="0 0 512 190" role="img" aria-label="Confronto dei costi: prevenzione contro trattamento tardivo">' + _STILE_DIAG
        base, hmax = 150, 108
        for i, v in enumerate(val):
            x = 44 + i * 116
            h = max(10, v / 1540 * hmax)
            col = "#2A7CBF" if i == 0 else ("#8FA9A1" if i == 1 else "#C4342E")
            op = "1" if i == 0 else (".55" if i == 1 else ".8")
            s += (f'<rect class="dg-grow" x="{x}" y="{base-h:.0f}" width="62" height="{h:.0f}" rx="5" '
                  f'fill="{col}" opacity="{op}" style="transition-delay:{i*.13}s"/>')
            s += f'<text class="dg-cap" x="{x+31}" y="{base-h-8:.0f}" text-anchor="middle">{v} €</text>'
            s += f'<text class="dg-lbl" x="{x+31}" y="166" text-anchor="middle">{lab[i]}</text>'
        s += f'<line x1="30" y1="{base}" x2="490" y2="{base}" stroke="#DDD9D2" stroke-width="1.2"/>'
        s += '<text class="dg-lbl" x="30" y="184" fill="#74838F">Prezzi reali del nostro tariffario, per singolo dente.</text>'
        s += '</svg>'
        return s

    if tipo == "chirurgia":
        fasi = [("TAC 3D", "si vede il nervo"), ("Anestesia", "e sedazione"),
                ("Intervento", "accesso e sutura"), ("Controllo", "rimozione punti")]
        s = '<svg class="dg" viewBox="0 0 512 150" role="img" aria-label="Le fasi di un\'estrazione pianificata">' + _STILE_DIAG
        for i, (t, d) in enumerate(fasi):
            x = i * 131
            cx, cy = x + 59, 54
            s += f'<rect x="{x}" y="8" width="118" height="90" rx="10" fill="#FBFAF7" stroke="#ECE8E1"/>'
            s += f'<path class="dg-bone" d="M{x+16} {cy+2}h86v30a5 5 0 0 1-5 5H{x+21}a5 5 0 0 1-5-5z"/>'
            if i == 0:
                s += f'<path class="dg-tooth" d="M{cx-14} {cy+2}V{cy-16}c0-7 6-11 14-11s14 4 14 11v18z" opacity=".9"/>'
                s += f'<path class="dg-tooth" d="M{cx-10} {cy+2}l3 22M{cx+10} {cy+2}l-3 22" stroke="#DDD9D2" fill="none"/>'
                s += f'<path class="dg-draw" d="M{x+20} {cy+26}h82" stroke="#C4342E" stroke-width="1.6" stroke-dasharray="90" stroke-dashoffset="90"/>'
                s += f'<text class="dg-lbl" x="{x+20}" y="{cy+38}" font-size="7" fill="#C4342E">nervo</text>'
            elif i == 1:
                s += f'<path class="dg-tooth" d="M{cx-14} {cy+2}V{cy-16}c0-7 6-11 14-11s14 4 14 11v18z" opacity=".55"/>'
                for k in range(3):
                    s += f'<circle class="dg-pop" cx="{cx}" cy="{cy-8}" r="{10+k*8}" fill="none" stroke="#2A7CBF" stroke-width="1" opacity="{.5-k*.13}" style="transition-delay:{k*.14}s"/>'
            elif i == 2:
                s += f'<path class="dg-pop" d="M{cx-16} {cy-4}q16 -16 32 0" fill="none" stroke="#2A7CBF" stroke-width="1.6"/>'
                for k in range(4):
                    s += f'<path class="dg-pop" d="M{cx-11+k*7.5} {cy-13}v10" stroke="#134B7A" stroke-width="1.4" style="transition-delay:{k*.09}s"/>'
            else:
                s += f'<path class="dg-gum" d="M{cx-18} {cy-4}h36v8h-36z"/>'
                s += f'<circle class="dg-pop" cx="{cx}" cy="{cy-16}" r="9" fill="#DBEAF7"/>'
                s += f'<path class="dg-pop" d="M{cx-4} {cy-16}l3 3 5.5-6" fill="none" stroke="#134B7A" stroke-width="1.7" stroke-linecap="round"/>'
            s += f'<text class="dg-n" x="{x+10}" y="118">0{i+1}</text>'
            s += f'<text class="dg-lbl" x="{x+28}" y="118">{t}</text>'
            s += f'<text class="dg-lbl" x="{x+10}" y="134" fill="#74838F">{d}</text>'
        s += '</svg>'
        return s

    if tipo == "bimbo":
        fasi = [("Si guarda", "la poltrona è un gioco"), ("Si conta", "«quanti denti hai?»"),
                ("Si spiega", "ai genitori, e a lui"), ("Si torna", "in un posto noto")]
        s = '<svg class="dg" viewBox="0 0 512 150" role="img" aria-label="La prima visita di un bambino, passo per passo">' + _STILE_DIAG
        for i, (t, d) in enumerate(fasi):
            x = i * 131
            cx, cy = x + 59, 52
            s += f'<rect x="{x}" y="8" width="118" height="90" rx="10" fill="#FBFAF7" stroke="#ECE8E1"/>'
            s += f'<circle class="dg-pop" cx="{cx}" cy="{cy-8}" r="13" fill="#EAE5DC" style="transition-delay:{i*.1}s"/>'
            s += f'<path class="dg-pop" d="M{cx-16} {cy+24}a16 16 0 0 1 32 0z" fill="#DBEAF7" style="transition-delay:{i*.1+.05}s"/>'
            s += f'<circle cx="{cx-4.5}" cy="{cy-10}" r="1.4" fill="#0B1A28"/><circle cx="{cx+4.5}" cy="{cy-10}" r="1.4" fill="#0B1A28"/>'
            arco = 4 + i * 1.6
            s += f'<path d="M{cx-5} {cy-3}q5 {arco} 10 0" fill="none" stroke="#0B1A28" stroke-width="1.3" stroke-linecap="round"/>'
            s += f'<text class="dg-n" x="{x+10}" y="118">0{i+1}</text>'
            s += f'<text class="dg-lbl" x="{x+28}" y="118">{t}</text>'
            s += f'<text class="dg-lbl" x="{x+10}" y="134" fill="#74838F">{d}</text>'
        s += '</svg>'
        return s

    return ""
