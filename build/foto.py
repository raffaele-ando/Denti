# -*- coding: utf-8 -*-
"""Estrae dall'archivio del sito precedente le poche fotografie utilizzabili.

L'archivio contiene 102 immagini, quasi tutte collage di più scatti fatti in
anni e con luci diverse. Nessuna regge come immagine d'apertura. Alcune però
documentano fatti che il testo afferma e che il lettore non ha motivo di
credere sulla parola: il defibrillatore appeso al muro, il carrello delle
emergenze, il riunito portatile per le visite a domicilio, il cortile con il
posto auto. Su quelle si interviene così:

1. ritaglio stretto sull'oggetto, per togliere il contesto sfocato e le persone
   riconoscibili (nell'archivio non risultano liberatorie);
2. desaturazione parziale e viraggio diviso, ombre verso il blu del marchio e
   alte luci verso la carta: è ciò che fa sembrare un set fotografie scattate
   in momenti diversi;
3. larghezza massima 720 px e WebP, perché il ruolo è di dettaglio documentario
   accanto al testo, non di apertura a piena pagina.

Il file targa dell'auto viene sfocato prima di tutto il resto.
"""
import pathlib
import sys

try:
    from PIL import Image, ImageFilter, ImageEnhance
except ImportError:                                    # pragma: no cover
    sys.exit("serve Pillow: pip install pillow")

SORGENTE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else
                        "/tmp/originale/output/asset")
USCITA = pathlib.Path(__file__).resolve().parent.parent / "site/assets/img/studio"

# (file di destinazione, sorgente, ritaglio, didascalia tecnica)
SCATTI = [
    ("unita-portatile", "serviziodomicilio", (105, 10, 490, 585),
     "Il riunito portatile nella sua valigia, aperto"),
    ("defibrillatore", "emergenze1", (58, 95, 288, 402),
     "Il defibrillatore semiautomatico appeso alla parete, sotto il cartello DAE"),
    ("carrello-emergenze", "emergenze1", (548, 400, 772, 604),
     "Il carrello delle emergenze con le scatole dei farmaci"),
    ("laboratorio", "laboratorioodontotecnico2", (8, 12, 462, 315),
     "Il banco del laboratorio odontotecnico interno, con gli strumenti in uso"),
    ("sala-raggi", "tac-dentale", (92, 4, 342, 212),
     "L'ortopantomografo nella sala raggi dello studio"),
    ("cortile", "posteggio", (58, 0, 902, 562),
     "Il cortile interno con il posto auto e l'ingresso dello studio"),
    ("sala-attesa", "sala-attesa", (0, 8, 332, 402),
     "La sala d'attesa con i diplomi alle pareti e la carrozzina a disposizione"),
]

# Targhe da sfocare prima del ritaglio: (sorgente, riquadro).
TARGHE = [("posteggio", (312, 308, 382, 338))]

OMBRA = (0.94, 0.97, 1.06)      # viraggio delle ombre verso il blu del marchio
LUCE = (1.03, 1.01, 0.96)       # viraggio delle alte luci verso la carta
SATURAZIONE = 0.55
LARGHEZZA_MAX = 720


def vira(im):
    """Viraggio diviso: la luminanza del pixel pesa fra i due viraggi."""
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            t = (r * 299 + g * 587 + b * 114) / 255000.0     # 0 ombra, 1 luce
            px[x, y] = tuple(
                min(255, int(c * (OMBRA[i] * (1 - t) + LUCE[i] * t)))
                for i, c in enumerate((r, g, b)))
    return im


def main():
    if not SORGENTE.is_dir():
        sys.exit(f"cartella sorgente non trovata: {SORGENTE}")
    USCITA.mkdir(parents=True, exist_ok=True)

    sfocature = {}
    for nome, box in TARGHE:
        sfocature.setdefault(nome, []).append(box)

    for dest, sorg, box, didascalia in SCATTI:
        p = SORGENTE / f"{sorg}.webp"
        if not p.exists():
            print(f"  manca {p.name}, salto")
            continue
        im = Image.open(p).convert("RGB")
        for b in sfocature.get(sorg, []):
            im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(9)), b)
        im = im.crop(box)
        if im.width > LARGHEZZA_MAX:
            im = im.resize((LARGHEZZA_MAX, round(im.height * LARGHEZZA_MAX / im.width)),
                           Image.LANCZOS)
        im = ImageEnhance.Color(im).enhance(SATURAZIONE)
        im = ImageEnhance.Contrast(im).enhance(1.06)
        im = vira(im)
        out = USCITA / f"{dest}.webp"
        im.save(out, "WEBP", quality=80, method=6)
        print(f"  {out.name:26} {im.width}×{im.height}  {out.stat().st_size/1024:.0f} KB")

    print(f"\n{len(SCATTI)} fotografie in {USCITA.relative_to(USCITA.parents[3])}")


if __name__ == "__main__":
    main()
