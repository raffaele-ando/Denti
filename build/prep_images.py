"""Prepara gli asset fotografici riutilizzabili dal sito originale.

Regole:
- Ritratti team -> 4:5, scala di grigi, highlight normalizzati a bianco puro
  (cosi' in pagina possono essere fusi con `mix-blend-mode: multiply`).
- Casi clinici -> ritaglio del pannello, bilanciamento esposizione, 4:3.
- Tutto il resto resta fuori: va rifotografato (vedi docs/04-photo-brief.md).
"""
from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path

SRC = Path("/tmp/claude-0/-home-user-Denti/8b7e07a5-43f7-5945-a9b3-6e0f54577b99/scratchpad/orig/output/asset")
OUT = Path("site/assets/img")

# nome file sorgente -> (slug, crop relativo opzionale (l,t,r,b) in frazioni)
RITRATTI = {
    "uberto-piccardo":  ("20180228_212244.webp",      (0.06, 0.00, 0.94, 1.00)),
    "francesca-gibelli":("p_040-edit-edit.webp",      (0.05, 0.00, 0.95, 1.00)),
    "federico-parodi":  ("p_015-edit-edit.webp",      (0.08, 0.00, 0.92, 1.00)),
    "ludovica-tuo":     ("tuo-ludovica.webp",         (0.06, 0.00, 0.94, 1.00)),
    "emanuele-degiovanni":("de-giovanni-emenuele.webp",(0.00, 0.00, 1.00, 0.94)),
    "gianluca-grasso":  ("dott-grasso-2.webp",        (0.00, 0.00, 1.00, 0.94)),
    "carmela-pulitano": ("carmela-pilitano.webp",     (0.04, 0.00, 0.96, 0.92)),
    "carlotta-fabiano": ("p_059-edit-edit.webp",      (0.08, 0.00, 0.92, 1.00)),
    "virginia":         ("p_056-edit-edit.webp",      (0.05, 0.00, 0.95, 1.00)),
    "erika-carbone":    ("ceciliapirone.webp",        (0.05, 0.00, 0.95, 1.00)),
}

def crop_ratio(im, ratio):
    """Ritaglia al centro-alto mantenendo il rapporto richiesto (w/h)."""
    w, h = im.size
    if w / h > ratio:
        nw = int(h * ratio)
        left = (w - nw) // 2
        return im.crop((left, 0, left + nw, h))
    nh = int(w / ratio)
    top = int((h - nh) * 0.12)          # taglia piu' dal basso: le teste restano alte
    return im.crop((0, top, w, top + nh))

def normalizza_alte_luci(im, soglia=0.985):
    """Porta il fondo chiaro a bianco puro senza bruciare l'incarnato."""
    g = im.convert("L")
    isto = g.histogram()
    tot = sum(isto)
    cum = 0
    punto_bianco = 255
    for v in range(255, -1, -1):
        cum += isto[v]
        if cum / tot > (1 - soglia) + 0.06:   # ~6% dei pixel piu' chiari -> bianco
            punto_bianco = max(v, 200)
            break
    punto_nero = 8
    lut = []
    for v in range(256):
        nv = (v - punto_nero) * 255.0 / max(1, (punto_bianco - punto_nero))
        lut.append(max(0, min(255, int(nv))))
    return g.point(lut).convert("RGB")

def salva(im, path, w, q=86):
    path.parent.mkdir(parents=True, exist_ok=True)
    h = int(im.size[1] * w / im.size[0])
    r = im.resize((w, h), Image.LANCZOS)
    r.save(path.with_suffix(".webp"), "WEBP", quality=q, method=6)
    return r.size

print("- Ritratti -")
for slug, (fname, box) in RITRATTI.items():
    im = Image.open(SRC / fname).convert("RGB")
    w, h = im.size
    im = im.crop((int(w*box[0]), int(h*box[1]), int(w*box[2]), int(h*box[3])))
    im = crop_ratio(im, 4/5)
    im = normalizza_alte_luci(im)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    print(f"  {slug:22s} {salva(im, OUT/'team'/slug, 720)}")

print("- Casi clinici -")
CASI = {
    "caso-riabilitazione-prima": ("protesi3.webp",       (2, 214, 276, 414)),
    "caso-riabilitazione-dopo":  ("protesi3.webp",       (280, 214, 554, 414)),
    "caso-ortodonzia-prima":     ("ortodonziacasi.webp", (5, 53, 313, 217)),
    "caso-ortodonzia-dopo":      ("ortodonziacasi.webp", (326, 53, 622, 217)),
}
for slug, (fname, box) in CASI.items():
    im = Image.open(SRC / fname).convert("RGB").crop(box)
    im = crop_ratio(im, 4/3)
    im = ImageEnhance.Color(im).enhance(0.88)      # meno saturazione sul rosso gengivale
    im = ImageEnhance.Brightness(im).enhance(1.05)
    im = ImageEnhance.Contrast(im).enhance(1.06)
    print(f"  {slug:28s} {salva(im, OUT/'casi'/slug, 900, 88)}")

print("- Editoriale -")
im = Image.open(SRC / "al-lavoro-3.webp").convert("RGB")
im = crop_ratio(im, 3/2)
im = ImageOps.grayscale(im).convert("RGB")
im = ImageEnhance.Contrast(im).enhance(1.12)
print(f"  intervento {salva(im, OUT/'studio'/'equipe-intervento', 1100)}")
