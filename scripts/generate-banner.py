# -*- coding: utf-8 -*-
"""Render the README banner (icon + wordmark + one colour card per cut).

    py -3 scripts/generate-banner.py

Output:
    docs/banner.png  light banner (bone paper) with a LIGHT and a DARK colour card
"""

import importlib.util
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
OUT_LIGHT = os.path.join(BASE, "docs", "banner.png")

S = 2
W, H = 1600, 420

# light banner
BONE = (241, 239, 226, 255)
BORDER = (217, 212, 191, 255)
INK = (30, 59, 47, 255)
MUTED = (122, 131, 112, 255)
RING = (200, 194, 174, 255)

# colour cards: one row per cut, from that cut's surfaces to its accent
CARDS = [
    ("LIGHT", [
        (241, 239, 226, 255),   # bone
        (221, 216, 193, 255),   # sand shadow
        (121, 131, 108, 255),   # sage
        (30, 59, 47, 255),     # forest
    ]),
    ("DARK", [
        (22, 41, 31, 255),     # deep cedar
        (30, 59, 47, 255),     # forest
        (121, 131, 108, 255),   # sage
        (178, 157, 107, 255),   # sand
    ]),
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


def render(cands, bg, border, title_col, tag_col, ring, icon_colors, out):
    saved = {k: getattr(cands, k) for k in icon_colors}
    for k, v in icon_colors.items():
        setattr(cands, k, v)
    try:
        icon = [c for c in cands.CANDIDATES if c[0] == "01"][0][2]()
    finally:
        for k, v in saved.items():
            setattr(cands, k, v)
    icon = icon.resize((300 * S, 300 * S), Image.LANCZOS)

    img = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, W * S - 1, H * S - 1], radius=28 * S,
                        fill=bg, outline=border, width=2 * S)

    img.alpha_composite(icon, (78 * S, 60 * S))

    f_title = font("segoeuib.ttf", 74 * S)
    f_tag = font("segoeui.ttf", 30 * S)
    f_label = font("segoeuib.ttf", 22 * S)

    tx = 424 * S
    d.text((tx, 84 * S), "Cedar & Sand Theme", font=f_title, fill=title_col)
    d.text((tx, 172 * S), "deep cedar green and warm sand gold",
           font=f_tag, fill=tag_col)

    for row, (label, colors) in enumerate(CARDS):
        y = 238 * S + row * 58 * S
        d.text((tx, y + 4 * S), label, font=f_label, fill=tag_col)
        x = tx + 128 * S
        for col in colors:
            d.ellipse([x, y, x + 26 * S, y + 26 * S], fill=col,
                      outline=ring, width=2 * S)
            x += 40 * S

    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.resize((W, H), Image.LANCZOS).save(out)
    print("wrote", os.path.relpath(out, BASE))


def main():
    cands = load_candidates()
    render(cands, BONE, BORDER, INK, MUTED, RING, {}, OUT_LIGHT)


if __name__ == "__main__":
    main()
