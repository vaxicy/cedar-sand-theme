# -*- coding: utf-8 -*-
"""Render the README banner (icon + wordmark + palette dots).

    py -3 scripts/generate-banner.py

Output: docs/banner.png  (1600 x 420)
"""

import importlib.util
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
OUT = os.path.join(BASE, "docs", "banner.png")

S = 2
W, H = 1600, 420

BONE = (241, 239, 226, 255)
BORDER = (217, 212, 191, 255)
INK = (30, 59, 47, 255)
MUTED = (122, 131, 112, 255)

DOTS = [
    (30, 59, 47, 255),      # forest
    (121, 131, 108, 255),   # sage
    (178, 157, 107, 255),   # sand
    (217, 203, 174, 255),   # pale sand
]

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except Exception:
        return ImageFont.load_default()


def load_candidates():
    spec = importlib.util.spec_from_file_location(
        "cands", os.path.join(HERE, "generate-icon-candidates.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    cands = load_candidates()
    icon = [c for c in cands.CANDIDATES if c[0] == "01"][0][2]()
    icon = icon.resize((300 * S, 300 * S), Image.LANCZOS)

    img = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, W * S - 1, H * S - 1], radius=28 * S,
                        fill=BONE, outline=BORDER, width=2 * S)

    img.alpha_composite(icon, (78 * S, 60 * S))

    f_title = font("segoeuib.ttf", 74 * S)
    f_tag = font("segoeui.ttf", 30 * S)
    f_small = font("segoeuib.ttf", 22 * S)

    tx = 424 * S
    d.text((tx, 96 * S), "Cedar & Sand Theme", font=f_title, fill=INK)
    d.text((tx, 196 * S), "deep cedar green and warm sand gold",
           font=f_tag, fill=MUTED)
    d.text((tx, 252 * S), "LIGHT                          DARK",
           font=f_small, fill=MUTED)

    x = tx
    for col in DOTS:
        d.ellipse([x, 302 * S, x + 26 * S, 302 * S + 26 * S], fill=col)
        x += 40 * S

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.resize((W, H), Image.LANCZOS).save(OUT)
    print("wrote", os.path.relpath(OUT, BASE))


if __name__ == "__main__":
    main()
