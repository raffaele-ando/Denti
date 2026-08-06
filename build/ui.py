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
 "gruppo": '<circle cx="9" cy="8.4" r="3.4"/><path d="M2.6 19.6a6.4 6.4 0 0 1 12.8 0"/><path d="M16.4 5.4a3.4 3.4 0 0 1 0 6.1M17.6 14.2a6.4 6.4 0 0 1 3.8 5.4"/>',
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
 .dg-barra{transform:scaleX(0);transform-origin:left center;transition:transform .8s cubic-bezier(.22,1,.36,1) var(--dd,0s)}
 [data-reveal].is-in .dg-barra{transform:none}
 @media(prefers-reduced-motion:reduce){.dg-draw{stroke-dashoffset:0}.dg-pop{opacity:1;transform:none}.dg-grow,.dg-barra{transform:none}}
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


# ── primitive condivise dai diagrammi in quattro tempi ─────────────────────
#
# Una sequenza comunica per differenza. Se due riquadri contigui condividono il
# 97% dei pixel, per il sistema visivo la sequenza non esiste e restano solo le
# didascalie, cioè testo travestito da illustrazione. Queste primitive servono a
# costruire riquadri che cambiano silhouette, non solo dettaglio: la posizione
# di un corpo nello spazio e il contorno di un oggetto sono le due variabili
# visive che si leggono per prime (Cleveland e McGill, 1984).

def _pannello(x, y=6, w=118, h=108):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#FBFAF7" stroke="#ECE8E1"/>'


def _passo(x, i, tit, det, y1=134, y2=150):
    s = f'<text class="dg-n" x="{x+10}" y="{y1}">0{i+1}</text>'
    s += f'<text class="dg-lbl" x="{x+28}" y="{y1}">{tit}</text>'
    s += f'<text class="dg-lbl" x="{x+10}" y="{y2}" fill="#74838F">{det}</text>'
    return s


def _riunito(bx, by=100):
    """Poltrona odontoiatrica vista di lato, schienale a destra."""
    g = f'<rect x="{bx+8}" y="{by-18}" width="8" height="18" rx="2" fill="#DDD9D2"/>'
    g += f'<rect x="{bx-2}" y="{by-5}" width="28" height="5" rx="2.5" fill="#C9C4BB"/>'
    g += f'<rect x="{bx-16}" y="{by-27}" width="42" height="9" rx="4.5" fill="#DBEAF7" stroke="#B4D3EC" stroke-width=".9"/>'
    g += f'<rect x="{bx+16}" y="{by-62}" width="10" height="36" rx="5" fill="#DBEAF7" stroke="#B4D3EC" stroke-width=".9"/>'
    g += f'<rect x="{bx+12}" y="{by-72}" width="17" height="10" rx="5" fill="#DBEAF7" stroke="#B4D3EC" stroke-width=".9"/>'
    return g


def _figura(cx, by=100, alto=False, seduto=False, col="#DBEAF7", bordo="#B4D3EC"):
    """Sagoma di persona vista di lato. `alto` distingue l'adulto dal bambino."""
    r = 8 if alto else 7.5
    if seduto:
        g = f'<circle cx="{cx}" cy="{by-52}" r="{r}" fill="#EAE5DC" stroke="#DDD9D2" stroke-width=".8"/>'
        g += f'<path d="M{cx-6} {by-28}v-13a6 6 0 0 1 12 0v13z" fill="{col}" stroke="{bordo}" stroke-width=".9"/>'
        g += (f'<path d="M{cx-3} {by-28}h-13v9" fill="none" stroke="{bordo}" stroke-width="3" '
              f'stroke-linecap="round" stroke-linejoin="round"/>')
        return g
    testa, spalla, anca = (by - 54, by - 37, by - 18) if alto else (by - 40, by - 25, by - 14)
    g = f'<circle cx="{cx}" cy="{testa}" r="{r}" fill="#EAE5DC" stroke="#DDD9D2" stroke-width=".8"/>'
    g += (f'<path d="M{cx-6.5} {anca}v{spalla-anca}a6.5 6.5 0 0 1 13 0v{anca-spalla}z" '
          f'fill="{col}" stroke="{bordo}" stroke-width=".9"/>')
    g += (f'<path d="M{cx-3.5} {anca}v{by-anca}M{cx+3.5} {anca}v{by-anca}" stroke="{bordo}" '
          f'stroke-width="3" stroke-linecap="round"/>')
    return g


def _molare(cx, cy, w=32, h=42, cls="dg-tooth", stile=""):
    """Molare visto di lato: corona bombata e due radici che si assottigliano."""
    hw, hh = w / 2, h / 2
    d = (f"M{cx-hw:.1f} {cy}"
         f"V{cy-hh*.30:.1f}"
         f"C{cx-hw:.1f} {cy-hh:.1f} {cx-hw*.55:.1f} {cy-hh:.1f} {cx:.1f} {cy-hh:.1f}"
         f"C{cx+hw*.55:.1f} {cy-hh:.1f} {cx+hw:.1f} {cy-hh:.1f} {cx+hw:.1f} {cy-hh*.30:.1f}"
         f"V{cy}"
         f"L{cx+hw*.62:.1f} {cy+hh*.86:.1f}"
         f"Q{cx+hw*.34:.1f} {cy+hh:.1f} {cx+hw*.20:.1f} {cy+hh*.20:.1f}"
         f"L{cx-hw*.20:.1f} {cy+hh*.20:.1f}"
         f"Q{cx-hw*.34:.1f} {cy+hh:.1f} {cx-hw*.62:.1f} {cy+hh*.86:.1f}"
         f"Z")
    c = f' class="{cls}"' if cls else ""
    return f'<path{c} {stile} d="{d}"/>'


def _corona(cx, cy, w=30, h=34, stroke="#2A7CBF", sw="1.3"):
    """Corona protesica: cupola senza radici."""
    hw, hh = w / 2, h / 2
    return (f'<path class="dg-tooth" style="stroke:{stroke};stroke-width:{sw}" '
            f'd="M{cx-hw:.1f} {cy+hh:.1f}V{cy-hh*.15:.1f}c0-{hh*.85:.1f} {hw*.42:.1f}-{hh*.85:.1f} '
            f'{hw:.1f}-{hh*.85:.1f}s{hw:.1f} 0 {hw:.1f} {hh*.85:.1f}v{hh*1.15:.1f}z"/>')


def _arcata(x0, cy=62, rot=None, giu=None, tinta=None):
    """Sorriso frontale schematico: banda gengivale e otto denti.

    `tinta` va passata come stile inline: una classe CSS batte l'attributo di
    presentazione `fill`, quindi scriverlo come attributo non avrebbe effetto.
    """
    larg = [7.5, 8.5, 10, 11.5, 11.5, 10, 8.5, 7.5]
    alt = [15, 18, 21, 24, 24, 21, 18, 15]
    su = [7, 4, 1.2, 0, 0, 1.2, 4, 7]             # le laterali stanno più in alto
    gap = 1.3
    tot = sum(larg) + gap * 7
    sx = x0 + 59 - tot / 2
    g = (f'<path d="M{sx-6:.1f} {cy-22}h{tot+12:.1f}v10q-{(tot+12)/2:.1f} 15 -{tot+12:.1f} 0z" '
         f'fill="#E9C9C4"/>')
    xx = sx
    for k in range(8):
        w, h = larg[k], alt[k]
        r = (rot or {}).get(k, 0)
        dy = (giu or {}).get(k, 0)
        t = (tinta or {}).get(k)
        st = f' style="fill:{t}"' if t else ""
        cx, top = xx + w / 2, cy - 6 + su[k] + dy
        g += (f'<path class="dg-tooth"{st} stroke="#C9C4BB" stroke-width="1" '
              f'transform="rotate({r} {cx:.1f} {top+h/2:.1f})" '
              f'd="M{xx:.1f} {top:.1f}h{w}v{h-4}a{w/2:.1f} 4.6 0 0 1 -{w} 0z"/>')
        xx += w + gap
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
        # L'arcata vista dall'alto. Il disordine di partenza è marcato, e
        # nell'ultimo riquadro la posizione iniziale resta in filigrana: senza
        # il termine di paragone il lettore non può misurare lo spostamento.
        import math
        eti = [("Situazione iniziale", "il ClinCheck la fotografa"), ("Mascherina 1", "prime settimane"),
               ("A metà percorso", "circa venti mascherine"), ("Risultato", "e contenzione")]
        s = ('<svg class="dg" viewBox="0 0 512 168" role="img" aria-label="Progressione '
             'dell\'allineamento con le mascherine trasparenti">' + _STILE_DIAG)

        CX, CY, RX, RY = 59, 84, 33, 27

        def posa(k, dis):
            a = math.pi * (0.11 + k * 0.0975)
            cx = CX - RX * math.cos(a)
            cy = CY - RY * math.sin(a)
            rot = math.degrees(a) - 90 + (((k * 37) % 13) - 6) * 5.0 * dis
            dx = (((k * 53) % 11) - 5) * 1.1 * dis
            dy = (((k * 29) % 7) - 3) * 1.2 * dis
            return cx + dx, cy + dy, rot

        def arco(rx, ry, ang=0.055):
            x1 = CX - rx * math.cos(math.pi * ang)
            y1 = CY - ry * math.sin(math.pi * ang)
            return f'M{x1:.1f} {y1:.1f}A{rx} {ry} 0 0 1 {2*CX-x1:.1f} {y1:.1f}'

        for step in range(4):
            x0 = step * 131
            dis = (1, 0.7, 0.32, 0)[step]
            s += _pannello(x0)
            s += (f'<g transform="translate({x0},0)">'
                  f'<path d="{arco(40, 33)}" fill="none" stroke="#E9C9C4" stroke-width="11" '
                  f'stroke-linecap="round"/>')
            if step == 3:                       # filigrana della posizione iniziale
                for k in range(9):
                    cx, cy, rot = posa(k, 1)
                    w = 10 if 2 <= k <= 6 else 8.4
                    s += (f'<rect x="{cx-w/2:.1f}" y="{cy-7:.1f}" width="{w}" height="14" rx="2.8" '
                          f'fill="none" stroke="#C9C4BB" stroke-width=".9" stroke-dasharray="2 2" '
                          f'transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})"/>')
            for k in range(9):
                cx, cy, rot = posa(k, dis)
                w = 10 if 2 <= k <= 6 else 8.4
                s += (f'<rect x="{cx-w/2:.1f}" y="{cy-7:.1f}" width="{w}" height="14" rx="2.8" '
                      f'class="dg-tooth" transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})"/>')
            if step:                            # guscio della mascherina sopra le corone
                s += (f'<path d="{arco(40.5, 34, .075)}" fill="none" stroke="#2A7CBF" '
                      f'stroke-width="5" opacity=".14" stroke-linecap="round"/>')
                s += (f'<path d="{arco(40.5, 34, .075)}" fill="none" stroke="#2A7CBF" '
                      f'stroke-width="1.3" opacity=".85" stroke-linecap="round"/>')
            s += '</g>'
            s += _passo(x0, step, *eti[step])
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
        # Le quattro fasi non sono gradi dello stesso miglioramento: sono quattro
        # oggetti diversi (gengiva, posizione, colore, forma). Ogni riquadro
        # mostra lo stesso sorriso e mette in evidenza un elemento diverso con
        # uno strumento grafico diverso: cerchio, freccia, campionario, contorno.
        fasi = [("Salute", "gengive e carie"), ("Posizione", "ortodonzia"),
                ("Colore", "igiene e sbiancamento"), ("Forma", "faccette e ceramica")]
        s = ('<svg class="dg" viewBox="0 0 512 168" role="img" aria-label="L\'ordine corretto '
             'di un percorso estetico">' + _STILE_DIAG)
        for i, (t, d) in enumerate(fasi):
            x = i * 131
            s += _pannello(x)
            if i == 0:
                s += _arcata(x, 62)
                s += f'<ellipse cx="{x+73}" cy="70" rx="3.6" ry="4.6" fill="#8C5A3C" opacity=".8"/>'
                s += (f'<circle class="dg-pop" cx="{x+73}" cy="70" r="10.5" fill="none" stroke="#C4342E" '
                      f'stroke-width="1.5" stroke-dasharray="2.5 2.5"/>')
                s += (f'<path d="M{x+31} 47q8 -6 16 0" fill="none" stroke="#C4342E" stroke-width="2.4" '
                      f'stroke-linecap="round" opacity=".85"/>')
                s += (f'<circle class="dg-pop" cx="{x+39}" cy="47" r="10.5" fill="none" stroke="#C4342E" '
                      f'stroke-width="1.5" stroke-dasharray="2.5 2.5" style="transition-delay:.16s"/>')
            elif i == 1:
                s += _arcata(x, 62, rot={2: -22, 5: 18}, giu={3: 3})
                s += (f'<path class="dg-draw" d="M{x+26} 36q12 -10 22 4" fill="none" stroke="#2A7CBF" '
                      f'stroke-width="1.7" stroke-dasharray="40" stroke-dashoffset="40" stroke-linecap="round"/>')
                s += f'<path d="M{x+43} 38l6 3-2 6z" fill="#2A7CBF"/>'
                s += (f'<path class="dg-draw" d="M{x+92} 36q-12 -10 -22 4" fill="none" stroke="#2A7CBF" '
                      f'stroke-width="1.7" stroke-dasharray="40" stroke-dashoffset="40" '
                      f'stroke-linecap="round" style="transition-delay:.35s"/>')
                s += f'<path d="M{x+75} 38l-6 3 2 6z" fill="#2A7CBF"/>'
            elif i == 2:
                s += _arcata(x, 62, tinta={0: "#D3C4A6", 1: "#DCCFB5", 2: "#E6DCC8", 3: "#EFE9DC"})
                s += f'<path d="M{x+59} 38v52" stroke="#134B7A" stroke-width="1" stroke-dasharray="3 3"/>'
                for k, col in enumerate(["#D3C4A6", "#DCCFB5", "#EAE2D3", "#FBFAF7"]):
                    s += (f'<rect class="dg-pop" x="{x+30+k*15}" y="94" width="13" height="10" rx="2" '
                          f'fill="{col}" stroke="#C9C4BB" stroke-width=".8" style="transition-delay:{k*.09}s"/>')
            else:
                s += _arcata(x, 62)
                s += (f'<path class="dg-pop" d="M{x+40} 52h26v30a10 8 0 0 1-26 0z" '
                      f'fill="none" stroke="#2A7CBF" stroke-width="1.6" stroke-dasharray="3.5 2.5"/>')
                s += (f'<path class="dg-pop" d="M{x+84} 50q10 4 10 21t-10 21q5-21 0-42z" fill="#DBEAF7" '
                      f'stroke="#2A7CBF" stroke-width="1.1" style="transition-delay:.2s"/>')
                s += (f'<path class="dg-pop" d="M{x+87} 56q5 6 5 15" fill="none" stroke="#FBFAF7" '
                      f'stroke-width="1.6" stroke-linecap="round" style="transition-delay:.3s"/>')
            s += _passo(x, i, t, d)
        s += '</svg>'
        return s

    if tipo == "protesi":
        # Quattro silhouette diverse: il dente, il reticolo, il disco di zirconia
        # da cui la corona viene ricavata, la corona in bocca. Il terzo riquadro
        # è il salto percettivo che tiene insieme la sequenza.
        fasi = [("Scansione", "impronta digitale"), ("CAD", "progettazione 3D"),
                ("CAM", "fresatura in zirconia"), ("Prova", "e cementazione")]
        s = ('<svg class="dg" viewBox="0 0 512 168" role="img" aria-label="Dal dente al manufatto '
             'protesico con flusso digitale">' + _STILE_DIAG)
        for i, (t, d) in enumerate(fasi):
            x = i * 131
            cx, cy = x + 59, 62
            s += _pannello(x)
            if i == 0:
                s += (f'<path class="dg-pop" d="M{cx} 32L{cx-30} {cy+26}L{cx+30} {cy+26}z" fill="#2A7CBF" '
                      f'fill-opacity=".10"/>')
                s += _molare(cx, cy + 2, 34, 46, stile='style="stroke:#C9C4BB;stroke-width:1.2"')
                for k in range(5):
                    s += (f'<path class="dg-pop" d="M{cx} 32L{cx-26+k*13:.0f} {cy+26}" '
                          f'stroke="#2A7CBF" stroke-width=".9" stroke-opacity=".5" '
                          f'style="transition-delay:{k*.07}s"/>')
                s += f'<rect x="{cx-8}" y="18" width="16" height="8" rx="2.5" fill="#134B7A"/>'
                s += f'<path d="M{cx-3.5} 26h7l-3.5 5z" fill="#134B7A"/>'
            elif i == 1:
                s += _molare(cx, cy, 34, 46, cls="",
                             stile='fill="none" stroke="#2A7CBF" stroke-width="1.4" stroke-dasharray="3.5 2.5"')
                s += f'<clipPath id="cad{i}{x}"><rect x="{cx-17}" y="{cy-23}" width="34" height="46"/></clipPath>'
                s += f'<g clip-path="url(#cad{i}{x})" opacity=".4">'
                for k in range(5):
                    s += f'<path d="M{cx-17} {cy-20+k*10}h34" stroke="#2A7CBF" stroke-width=".7"/>'
                for k in range(4):
                    s += f'<path d="M{cx-19+k*11} {cy-23}l10 46" stroke="#2A7CBF" stroke-width=".7"/>'
                s += '</g>'
                for k in range(4):
                    s += (f'<rect class="dg-pop" x="{cx-18+k*11}" y="{cy-27}" width="4.5" height="4.5" '
                          f'fill="#134B7A" style="transition-delay:{k*.08}s"/>')
            elif i == 2:
                s += f'<circle cx="{cx}" cy="{cy+4}" r="34" fill="#EAE5DC" stroke="#C9C4BB" stroke-width="1.2"/>'
                s += (f'<circle cx="{cx}" cy="{cy+4}" r="28" fill="none" stroke="#DDD9D2" '
                      f'stroke-width=".8" stroke-dasharray="2 3"/>')
                s += _corona(cx, cy + 6, 28, 34)
                s += (f'<g class="dg-pop"><rect x="{cx-4}" y="16" width="8" height="13" rx="2" fill="#134B7A"/>'
                      f'<path d="M{cx} 29v7" stroke="#134B7A" stroke-width="1.6"/>'
                      f'<path d="M{cx-2.5} 36h5l-2.5 4z" fill="#134B7A"/></g>')
            else:
                s += (f'<path class="dg-bone" d="M{x+20} {cy+16}h78a6 6 0 0 1 6 6v10a6 6 0 0 1-6 6H'
                      f'{x+20}a6 6 0 0 1-6-6v-10a6 6 0 0 1 6-6z"/>')
                s += f'<path class="dg-gum" d="M{x+20} {cy+10}h78v8H{x+20}z"/>'
                s += (f'<path d="M{cx-8} {cy+22}V{cy+2}q0-5 8-5t8 5v20z" fill="#E0D9CC" '
                      f'stroke="#C9C4BB" stroke-width=".8"/>')
                s += _corona(cx, cy - 6, 30, 36, sw="1.5")
                s += (f'<path d="M{cx-15} {cy+12}h30" stroke="#2A7CBF" stroke-width=".9" '
                      f'stroke-dasharray="2.5 2"/>')
                s += f'<circle class="dg-pop" cx="{cx+28}" cy="{cy-24}" r="9.5" fill="#DBEAF7"/>'
                s += (f'<path class="dg-pop" d="M{cx+24} {cy-24}l3 3.2 5.5-6" fill="none" stroke="#134B7A" '
                      f'stroke-width="1.8" stroke-linecap="round" style="transition-delay:.1s"/>')
            s += _passo(x, i, t, d)
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
        # Il terzo riquadro è quello che porta l'informazione: il dente non c'è
        # più, l'alveolo è vuoto e i due frammenti sono sopra l'osso. Prima la
        # sequenza cambiava solo di qualche tratto e i quattro riquadri
        # sembravano lo stesso disegno ripetuto.
        fasi = [("TAC 3D", "si vede il nervo"), ("Anestesia", "e sedazione"),
                ("Intervento", "odontotomia"), ("Controllo", "rimozione punti")]
        s = ('<svg class="dg" viewBox="0 0 512 168" role="img" aria-label="Le fasi di '
             'un\'estrazione pianificata">' + _STILE_DIAG)

        def dente(cx, cy, op=1.0):
            return (f'<g opacity="{op}">' +
                    _molare(cx, cy - 4, 32, 44, stile='style="stroke:#C9C4BB;stroke-width:1.1"') +
                    '</g>')

        for i, (t, d) in enumerate(fasi):
            x = i * 131
            cx, cy = x + 59, 68
            s += _pannello(x)
            s += f'<path class="dg-bone" d="M{x+14} {cy}h90v32a6 6 0 0 1-6 6H{x+20}a6 6 0 0 1-6-6z"/>'
            s += f'<path class="dg-gum" d="M{x+14} {cy-6}h90v6H{x+14}z"/>'
            if i == 0:
                s += dente(cx, cy)
                s += (f'<path class="dg-draw" d="M{x+20} {cy+26}h78" stroke="#C4342E" stroke-width="2.2" '
                      f'stroke-dasharray="90" stroke-dashoffset="90" stroke-linecap="round"/>')
                s += (f'<path d="M{cx+12} {cy+21}v5" stroke="#C4342E" stroke-width="1" '
                      f'stroke-dasharray="2 2"/>')
                s += f'<text class="dg-lbl" x="{x+20}" y="{cy+38}" font-size="7" fill="#C4342E">nervo</text>'
            elif i == 1:
                s += dente(cx, cy, .45)
                s += (f'<g class="dg-pop"><rect x="{cx+22}" y="{cy-48}" width="8" height="20" rx="2" '
                      f'fill="#DBEAF7" stroke="#134B7A" stroke-width="1"/>'
                      f'<path d="M{cx+26} {cy-28}v9" stroke="#134B7A" stroke-width="1.4"/></g>')
                for k in range(3):
                    s += (f'<circle class="dg-pop" cx="{cx}" cy="{cy-12}" r="{10+k*8}" fill="none" '
                          f'stroke="#2A7CBF" stroke-width="1.2" opacity="{.6-k*.16}" '
                          f'style="transition-delay:{k*.14}s"/>')
            elif i == 2:
                # alveolo vuoto: il buco è il contenuto informativo del riquadro
                s += (f'<path d="M{cx-15} {cy-6}v20a15 20 0 0 0 30 0v-20z" fill="#C9C4BB"/>')
                s += (f'<path d="M{cx-11} {cy-4}v18a11 16 0 0 0 22 0v-18z" fill="#B9B3A8"/>')
                s += (f'<g class="dg-pop"><g transform="rotate(-24 {cx-19} {cy-32})">'
                      f'<path class="dg-tooth" d="M{cx-26} {cy-42}h14v10q0 12 -7 14 -7-2 -7-14z"/></g></g>')
                s += (f'<g class="dg-pop" style="transition-delay:.16s"><g transform="rotate(26 {cx+19} {cy-32})">'
                      f'<path class="dg-tooth" d="M{cx+12} {cy-42}h14v10q0 12 -7 14 -7-2 -7-14z"/></g></g>')
                s += (f'<g class="dg-pop" style="transition-delay:.3s">'
                      f'<rect x="{cx-3}" y="{cy-48}" width="6" height="14" rx="2" fill="#134B7A"/>'
                      f'<path d="M{cx} {cy-34}v6" stroke="#134B7A" stroke-width="1.6"/>'
                      f'<path d="M{cx-2.5} {cy-28}h5l-2.5 4z" fill="#134B7A"/></g>')
            else:
                s += f'<path class="dg-gum" d="M{cx-19} {cy-8}h38v10h-38z"/>'
                for k in range(3):
                    s += (f'<path class="dg-pop" d="M{cx-15+k*14} {cy-11}l7 8M{cx-8+k*14} {cy-11}l-7 8" '
                          f'stroke="#134B7A" stroke-width="1.3" stroke-linecap="round" '
                          f'style="transition-delay:{k*.1}s"/>')
                s += (f'<circle class="dg-pop" cx="{cx+30}" cy="{cy-34}" r="9.5" fill="#DBEAF7" '
                      f'style="transition-delay:.34s"/>')
                s += (f'<path class="dg-pop" d="M{cx+26} {cy-34}l3 3.2 5.5-6" fill="none" stroke="#134B7A" '
                      f'stroke-width="1.8" stroke-linecap="round" style="transition-delay:.42s"/>')
            s += _passo(x, i, t, d)
        s += '</svg>'
        return s

    if tipo == "bimbo":
        # La variabile che cambia da un riquadro all'altro è la posizione del
        # bambino rispetto alla poltrona: lontano, seduto, seduto con i genitori,
        # fuori con una traiettoria di ritorno. La posizione lungo un asse comune
        # è la variabile visiva che si legge con più precisione, e qui è anche
        # la cosa che il testo vuole dire: la prima visita serve ad avvicinarsi.
        fasi = [("Si guarda", "la poltrona è un gioco"), ("Si conta", "«quanti denti hai?»"),
                ("Si spiega", "ai genitori, e a lui"), ("Si torna", "in un posto noto")]
        s = ('<svg class="dg" viewBox="0 0 512 168" role="img" aria-label="La prima visita di un '
             'bambino, passo per passo">' + _STILE_DIAG)
        for i, (t, d) in enumerate(fasi):
            x = i * 131
            s += _pannello(x)
            s += f'<path d="M{x+10} 100h98" stroke="#ECE8E1" stroke-width="1.4" stroke-linecap="round"/>'
            s += _riunito(x + 66)
            if i == 0:
                s += _figura(x + 20)
                # linea di sguardo, non freccia: nel primo riquadro il bambino guarda
                s += (f'<path class="dg-draw" d="M{x+29} 60h18" stroke="#2A7CBF" stroke-width="1.2" '
                      f'stroke-dasharray="20" stroke-dashoffset="20" stroke-linecap="round"/>')
                s += (f'<path class="dg-pop" d="M{x+47} 60a6 4 0 0 1 11 0 6 4 0 0 1-11 0z" fill="none" '
                      f'stroke="#2A7CBF" stroke-width="1.2"/>')
                s += f'<circle class="dg-pop" cx="{x+52.5}" cy="60" r="1.7" fill="#2A7CBF" style="transition-delay:.12s"/>'
            elif i == 1:
                s += _figura(x + 70, seduto=True)
                s += (f'<circle class="dg-pop" cx="{x+56}" cy="50" r="4.2" fill="#FBFAF7" '
                      f'stroke="#134B7A" stroke-width="1.3"/>')
                s += (f'<path class="dg-pop" d="M{x+53} 53l-10 7" stroke="#134B7A" stroke-width="1.6" '
                      f'stroke-linecap="round"/>')
                for k in range(4):
                    s += (f'<path class="dg-pop dg-tooth" d="M{x+15+k*11} 22h8v7a4 3.4 0 0 1 -8 0z" '
                          f'style="transition-delay:{.1+k*.11}s"/>')
                s += f'<text class="dg-lbl" x="{x+15}" y="44" font-size="7.5" fill="#134B7A">1 2 3 4</text>'
            elif i == 2:
                s += _figura(x + 70, seduto=True)
                s += _figura(x + 20, alto=True, col="#E7E2DA", bordo="#C9C4BB")
                s += _figura(x + 38, alto=True, col="#E7E2DA", bordo="#C9C4BB")
                s += (f'<g class="dg-pop"><rect x="{x+10}" y="14" width="44" height="20" rx="9" '
                      f'fill="#DBEAF7"/><path d="M{x+22} 34l-2 7 9-7z" fill="#DBEAF7"/>'
                      f'<path d="M{x+18} 21h28M{x+18} 27h18" stroke="#134B7A" stroke-width="1.5" '
                      f'stroke-linecap="round" opacity=".55"/></g>')
            else:
                # la sagoma tratteggiata sulla poltrona è la memoria della prima volta
                s += (f'<g opacity=".55"><path d="M{x+64} 72v-13a6 6 0 0 1 12 0v13z" fill="none" '
                      f'stroke="#B4D3EC" stroke-width="1.1" stroke-dasharray="3 2.5"/>'
                      f'<circle cx="{x+70}" cy="48" r="7.5" fill="none" stroke="#C9C4BB" '
                      f'stroke-width="1.1" stroke-dasharray="3 2.5"/></g>')
                s += _figura(x + 22)
                s += (f'<path class="dg-draw" d="M{x+30} 46q20 -22 40 -4" fill="none" stroke="#2A7CBF" '
                      f'stroke-width="1.4" stroke-dasharray="64" stroke-dashoffset="64" '
                      f'stroke-linecap="round"/>')
                s += f'<path d="M{x+65} 36l6 5-6 4z" fill="#2A7CBF"/>'
                s += (f'<g class="dg-pop" style="transition-delay:.5s">'
                      f'<rect x="{x+40}" y="16" width="20" height="18" rx="3" fill="#FBFAF7" '
                      f'stroke="#2A7CBF" stroke-width="1.1"/>'
                      f'<path d="M{x+40} 22h20" stroke="#2A7CBF" stroke-width="1.1"/>'
                      f'<circle cx="{x+50}" cy="28" r="2.6" fill="#2A7CBF"/></g>')
            s += _passo(x, i, t, d)
        s += '</svg>'
        return s

    if tipo == "orari":
        # La settimana come sei barre della stessa lunghezza. Il fatto che lo
        # studio sia aperto il sabato quanto il lunedì è la cosa che distingue
        # questi orari da quelli di quasi tutti gli studi, e in un elenco di
        # righe «8:00 – 20:30» ripetute sei volte non si vede: si legge il
        # primo rigo e si smette. In forma di barre si vede al primo sguardo.
        #
        # Il viewBox è stretto di proposito: un diagramma disegnato su 512 unità
        # e mostrato dentro 340 px di telefono rimpicciolisce il testo sotto la
        # soglia di lettura. Qui l'unità del disegno è vicina al pixel reale.
        giorni = [("Lunedì", 1), ("Martedì", 1), ("Mercoledì", 1), ("Giovedì", 1),
                  ("Venerdì", 1), ("Sabato", 1), ("Domenica", 0)]
        s = ('<svg class="dg" viewBox="0 0 360 196" role="img" aria-label="Gli orari di apertura '
             'della settimana: dal lunedì al sabato 8:00-20:30, domenica chiuso">' + _STILE_DIAG)
        x0, x1 = 74, 348                                  # 8:00 → 21:00
        scala = (x1 - x0) / 13.0
        for h in range(8, 22, 2):
            gx = x0 + (h - 8) * scala
            s += f'<line x1="{gx:.0f}" y1="18" x2="{gx:.0f}" y2="190" stroke="#ECE8E1" stroke-width="1"/>'
            s += f'<text class="dg-lbl" x="{gx:.0f}" y="12" text-anchor="middle" font-size="8">{h}</text>'
        for i, (g, aperto) in enumerate(giorni):
            y = 24 + i * 24
            s += f'<text class="dg-lbl" x="66" y="{y+13}" text-anchor="end" font-size="8.5">{g}</text>'
            larghezza = 12.5 * scala
            if aperto:
                s += (f'<rect class="dg-barra" x="{x0}" y="{y}" width="{larghezza:.0f}" height="18" rx="9" '
                      f'fill="#2A7CBF" fill-opacity=".9" style="--dd:{i*.07:.2f}s"/>')
                s += (f'<text class="dg-cap" x="{x0+larghezza/2:.0f}" y="{y+13}" text-anchor="middle" '
                      f'fill="#FBFAF7" font-size="10">8:00 – 20:30</text>')
            else:
                s += (f'<rect x="{x0}" y="{y}" width="{larghezza:.0f}" height="18" rx="9" fill="none" '
                      f'stroke="#DDD9D2" stroke-width="1" stroke-dasharray="3 3"/>')
                s += (f'<text class="dg-lbl" x="{x0+larghezza/2:.0f}" y="{y+13}" text-anchor="middle" '
                      f'font-size="9" fill="#74838F">chiuso</text>')
        s += '</svg>'
        return s

    if tipo == "preventivo":
        # Il foglio che si porta a casa. La pagina afferma che il piano di cura
        # arriva scritto voce per voce: mostrarlo costa meno parole che
        # descriverlo, e rende verificabile la promessa invece di ripeterla.
        righe = [("Igiene orale professionale", "100,00"), ("Otturazione media, 2 elementi", "260,00"),
                 ("Devitalizzazione, 2 canali", "210,00"), ("Corona in zirconia", "770,00")]
        s = ('<svg class="dg" viewBox="0 0 424 244" role="img" aria-label="Il piano di cura scritto: '
             'ogni lavorazione con il suo prezzo e il totale in fondo">' + _STILE_DIAG)
        s += '<rect x="16" y="10" width="316" height="220" rx="8" fill="#FBFAF7" stroke="#DDD9D2"/>'
        s += '<path d="M16 48h316" stroke="#DDD9D2"/>'
        s += '<path d="M16 18a8 8 0 0 1 8-8h300a8 8 0 0 1 8 8v30H16z" fill="#F3F0EA"/>'
        s += '<text class="dg-cap" x="32" y="34" font-size="12">Piano di cura</text>'
        s += '<text class="dg-lbl" x="316" y="34" text-anchor="end" font-size="8.5">Prezzo</text>'
        for i, (voce, prezzo) in enumerate(righe):
            y = 70 + i * 28
            s += (f'<g class="dg-pop" style="transition-delay:{i*.11}s">'
                  f'<text class="dg-cap" x="32" y="{y}" font-size="10.5">{voce}</text>'
                  f'<text class="dg-cap" x="316" y="{y}" text-anchor="end" font-size="10.5">{prezzo} €</text>'
                  f'<path d="M32 {y+8}h284" stroke="#ECE8E1"/></g>')
        s += '<path d="M16 190h316" stroke="#DDD9D2"/>'
        s += ('<g class="dg-pop" style="transition-delay:.55s">'
              '<rect x="160" y="196" width="156" height="26" rx="6" fill="#DBEAF7"/>'
              '<text class="dg-cap" x="174" y="213" font-size="10.5" fill="#134B7A">Totale</text>'
              '<text class="dg-cap" x="304" y="213" text-anchor="end" font-size="12" fill="#134B7A">1.340,00 €</text></g>')
        s += '<text class="dg-lbl" x="32" y="213" font-size="8" fill="#74838F">In visita</text>'
        s += ('<path class="dg-draw" d="M342 46v144" stroke="#2A7CBF" stroke-width="1.4" '
              'stroke-dasharray="150" stroke-dashoffset="150"/>')
        for k, w in enumerate(["Ogni", "voce", "separata"]):
            s += f'<text class="dg-lbl" x="350" y="{104+k*13}" font-size="8" fill="#2A7CBF">{w}</text>'
        s += '</svg>'
        return s

    if tipo == "dente-espulso":
        # Quattro gesti in ordine, con il tempo che li governa. Chi ha appena
        # perso un dente in un trauma non legge un paragrafo: guarda le figure
        # e agisce. L'ultimo riquadro porta la finestra temporale, perché è
        # l'informazione che decide l'esito.
        eti = [("Raccoglilo", "mai per la radice"),
               ("Non pulirlo", "niente sfregamenti"),
               ("Nel latte", "o fisiologica"),
               ("Vieni subito", "entro 30–60 minuti")]
        s = ('<svg class="dg" viewBox="0 0 512 168" role="img" aria-label="Che cosa fare con un dente '
             'espulso da un trauma, in quattro passaggi">' + _STILE_DIAG)
        for i, (t, d) in enumerate(eti):
            x = i * 131
            cx = x + 59
            s += _pannello(x)
            if i == 0:
                s += _molare(cx, 62, 32, 44, stile='style="stroke:#C9C4BB;stroke-width:1.1"')
                s += (f'<path class="dg-pop" d="M{cx-24} 50a24 16 0 0 1 48 0" fill="none" stroke="#2A7CBF" '
                      f'stroke-width="2" stroke-linecap="round"/>')          # presa sulla corona
                s += (f'<path class="dg-pop" d="M{cx-14} 92l28 0" stroke="#C4342E" stroke-width="2" '
                      f'stroke-linecap="round" style="transition-delay:.12s"/>')
                s += (f'<path class="dg-pop" d="M{cx-12} 86l24 12M{cx+12} 86l-24 12" stroke="#C4342E" '
                      f'stroke-width="1.6" stroke-linecap="round" style="transition-delay:.12s"/>')
            elif i == 1:
                s += _molare(cx, 62, 32, 44, stile='style="stroke:#C9C4BB;stroke-width:1.1"')
                s += (f'<g class="dg-pop"><circle cx="{cx}" cy="60" r="30" fill="none" stroke="#C4342E" '
                      f'stroke-width="2.2"/><path d="M{cx-21} 39l42 42" stroke="#C4342E" stroke-width="2.2" '
                      f'stroke-linecap="round"/></g>')
                s += (f'<path class="dg-pop" d="M{cx+24} 26q10 -6 16 2" fill="none" stroke="#C9C4BB" '
                      f'stroke-width="2" stroke-linecap="round" style="transition-delay:.14s"/>')
            elif i == 2:
                s += (f'<path d="M{cx-20} 34h40v50a10 10 0 0 1-10 10h-20a10 10 0 0 1-10-10z" '
                      f'fill="#FBFAF7" stroke="#C9C4BB" stroke-width="1.2"/>')
                s += f'<path d="M{cx-20} 30h40v6h-40z" fill="#DDD9D2"/>'
                s += (f'<path class="dg-grow" d="M{cx-20} 56h40v28a10 10 0 0 1-10 10h-20a10 10 0 0 1-10-10z" '
                      f'fill="#DBEAF7"/>')
                s += _molare(cx, 72, 22, 30, stile='style="stroke:#B4D3EC;stroke-width:1"')
                s += f'<text class="dg-lbl" x="{cx}" y="24" text-anchor="middle" font-size="7.5">latte</text>'
            else:
                s += f'<circle cx="{cx}" cy="60" r="30" fill="none" stroke="#DDD9D2" stroke-width="2.5"/>'
                s += (f'<path class="dg-draw" d="M{cx} 30a30 30 0 0 1 26 45" fill="none" stroke="#C4342E" '
                      f'stroke-width="3.5" stroke-dasharray="70" stroke-dashoffset="70" stroke-linecap="round"/>')
                s += (f'<path d="M{cx} 60V40M{cx} 60l13 8" stroke="#134B7A" stroke-width="2.2" '
                      f'stroke-linecap="round"/>')
                s += f'<circle cx="{cx}" cy="60" r="3" fill="#134B7A"/>'
                s += (f'<text class="dg-cap" x="{cx}" y="106" text-anchor="middle" font-size="9.5" '
                      f'fill="#C4342E">30–60 min</text>')
            s += _passo(x, i, t, d)
        s += '</svg>'
        return s

    return ""


def barre_temi(temi):
    """Le etichette che Google estrae dalle recensioni, in scala.

    Erano sei riquadri con un numero grande dentro. Confrontare due numeri
    scritti costringe a leggerli e a tenerli a mente; confrontare due lunghezze
    non costa nulla, ed è il motivo per cui una tabella di frequenze si disegna.
    """
    if not temi:
        return ""
    massimo = max(c for _, c in temi) or 1
    x0, larg, alt = 96, 224, 28
    s = (f'<svg class="dg" viewBox="0 0 360 {len(temi)*alt + 34}" role="img" '
         f'aria-label="Quante volte ciascun tema compare nelle recensioni">' + _STILE_DIAG)
    for i, (nome, conta) in enumerate(temi):
        y = 8 + i * alt
        w = max(18, larg * conta / massimo)
        s += f'<text class="dg-lbl" x="{x0-12}" y="{y+14}" text-anchor="end" font-size="9">{nome.lower()}</text>'
        s += (f'<rect class="dg-barra" x="{x0}" y="{y}" width="{w:.0f}" height="19" rx="9.5" '
              f'fill="#2A7CBF" fill-opacity="{0.9 - i*0.06:.2f}" style="--dd:{i*.08:.2f}s"/>')
        s += f'<text class="dg-cap" x="{x0+w+9:.0f}" y="{y+14}" font-size="11" fill="#134B7A">{conta}</text>'
    s += (f'<text class="dg-lbl" x="{x0}" y="{len(temi)*alt+26}" font-size="8" fill="#74838F">'
          f'Conteggi generati da Google sul testo delle recensioni.</text>')
    s += '</svg>'
    return s
