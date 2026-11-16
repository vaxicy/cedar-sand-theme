"""Claret Atelier Theme - icon candidates.

Code-drawn candidates (no AI images), a light/dark contact sheet and an inline
strip. Re-runnable: every mark is redrawn from scratch.

Run from the project root:  py -3 scripts/generate-icon-candidates.py
"""

import io
import math
import os

from PIL import Image, ImageDraw, ImageFont

S = 3
W = 1024

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "logo-candidates")

# palette - forest green + sand gold + bone (de-collided from
# emerald-clear / jade-veil / olive-dream / quartz-orchid)
FOREST = (30, 59, 47, 255)            # #1E3B2F  cedar forest
FOREST_D = (22, 41, 31, 255)          # #16291F  deep cedar
FOREST_L = (61, 92, 73, 255)          # #3D5C49  lit cedar
SAGE = (121, 131, 108, 255)           # #79836C  cedar sage
SAND = (192, 172, 132, 255)           # #C0AC84  warm sand
SAND_D = (168, 144, 95, 255)          # #A8905F  shaded sand
SAND_L = (217, 203, 174, 255)         # #D9CBAE  pale sand
BONE = (246, 242, 232, 255)           # #F6F2E8  bone
BONE_D = (237, 230, 214, 255)         # #EDE6D6  shaded bone
INK = FOREST_D

# No-outline render (matches the flat look chosen for the gelato set).
OUTLINE = None

LIGHT_BG = (246, 242, 232, 255)
DARK_BG = (22, 41, 31, 255)
LIGHT_INK = (30, 59, 47, 255)
DARK_INK = (237, 230, 214, 255)

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except Exception:
        return ImageFont.load_default()


def scr(p):
    return (p[0] * S, p[1] * S)


def wd(v):
    return max(1, int(round(v * S)))


def canvas():
    return Image.new("RGBA", (W * S, W * S), (0, 0, 0, 0))


def finish(img):
    return img.resize((W, W), Image.LANCZOS)


def bez(p0, p1, p2, n=64):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1.0 - t
        pts.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return pts


def poly(draw, pts, fill, outline=None, width=0):
    draw.polygon([scr(p) for p in pts], fill=fill,
                 outline=outline, width=wd(width) if width else 0)


def disc(draw, center, r, fill, outline=None, width=0):
    draw.ellipse([center[0] * S - r * S, center[1] * S - r * S,
                  center[0] * S + r * S, center[1] * S + r * S],
                 fill=fill, outline=outline, width=wd(width) if width else 0)


def rrect(draw, box, radius, fill, outline=None, width=0):
    draw.rounded_rectangle([box[0] * S, box[1] * S, box[2] * S, box[3] * S],
                           radius=radius * S, fill=fill, outline=outline,
                           width=wd(width) if width else 0)


def line(draw, pts, color, width, joint="curve"):
    draw.line([scr(p) for p in pts], fill=color, width=wd(width), joint=joint)


# ---------------------------------------------------------------- candidates

def cand_cedar():
    """01 - a single cedar: three stepped tiers over a sand line."""
    img = canvas()
    d = ImageDraw.Draw(img)

    # sand ground
    rrect(d, (268, 800, 756, 884), 42, SAND)

    # trunk
    rrect(d, (486, 660, 538, 856), 10, FOREST_D)

    # stepped canopy
    poly(d, [(302, 748), (722, 748), (512, 502)], FOREST)
    poly(d, [(352, 574), (672, 574), (512, 336)], FOREST)
    poly(d, [(404, 408), (620, 408), (512, 202)], FOREST)

    return finish(img)


def cand_dunes():
    """02 - rolling sand dunes with one small cedar on the crest."""
    img = canvas()
    d = ImageDraw.Draw(img)

    def dune(x0, x1, base, peak, crest_x, color):
        top = bez((x0, base), (crest_x, peak), (x1, base))
        poly(d, top + [(x1, base), (x0, base)], color)

    # low sun behind the crests
    disc(d, (668, 424), 96, SAND_L)

    dune(90, 934, 884, 618, 320, SAND)
    dune(90, 934, 942, 742, 640, SAND_D)
    dune(90, 934, 942, 878, 280, FOREST)

    return finish(img)


def cand_rings():
    """03 - cedar log cross-section: concentric growth rings."""
    img = canvas()
    d = ImageDraw.Draw(img)

    disc(d, (512, 512), 300, FOREST_D)   # bark
    disc(d, (512, 512), 282, SAND)
    disc(d, (512, 512), 246, BONE)
    disc(d, (512, 512), 212, SAND_D)
    disc(d, (512, 512), 176, BONE)
    disc(d, (512, 512), 140, SAND)
    disc(d, (512, 512), 104, BONE)
    disc(d, (512, 512), 64, SAND_D)
    disc(d, (512, 512), 24, FOREST)

    return finish(img)


def cand_ridge():
    """04 - forest ridge over a sand band, sun behind."""
    img = canvas()
    d = ImageDraw.Draw(img)

    # sun
    disc(d, (690, 366), 92, SAND_L)

    # back ridge
    poly(d, [(90, 744), (316, 452), (536, 744)], FOREST_L)
    # front ridges
    poly(d, [(214, 782), (466, 498), (734, 782)], FOREST)
    poly(d, [(534, 782), (752, 552), (934, 782)], FOREST)

    # sand band
    rrect(d, (90, 736, 934, 934), 0, SAND)
    rrect(d, (90, 870, 934, 934), 0, SAND_D)

    return finish(img)


def cand_hourglass():
    """05 - sand timer: two bulbs, forest caps, running sand."""
    img = canvas()
    d = ImageDraw.Draw(img)

    # glass bulbs
    poly(d, [(332, 236), (692, 236), (512, 505)], BONE_D)
    poly(d, [(332, 788), (692, 788), (512, 519)], BONE_D)

    # sand sits at the neck of the upper bulb and piles up in the lower one
    poly(d, [(446, 414), (578, 414), (512, 505)], SAND)
    poly(d, [(404, 788), (620, 788), (512, 690)], SAND)

    # falling grain
    line(d, [(512, 505), (512, 696)], SAND_D, 16)

    # caps + rails
    rrect(d, (300, 186, 724, 244), 18, FOREST)
    rrect(d, (300, 780, 724, 838), 18, FOREST)
    rrect(d, (356, 240, 386, 784), 12, FOREST_D)
    rrect(d, (638, 240, 668, 784), 12, FOREST_D)

    return finish(img)


def cand_grove():
    """06 - a small cedar grove standing on a sand shelf."""
    img = canvas()
    d = ImageDraw.Draw(img)

    # sand shelf
    rrect(d, (196, 812, 828, 882), 34, SAND)

    specs = [
        (320, 636, 118, 30),   # cx, base_y, half-width, trunk_h
        (700, 636, 126, 30),
        (512, 690, 152, 44),
    ]
    for cx, base, half, trunk_h in specs:
        rrect(d, (cx - 9, base - 6, cx + 9, base + trunk_h), 5, FOREST_D)
        poly(d, [(cx - half, base), (cx + half, base), (cx, base - half * 2.05)],
             FOREST)

    return finish(img)


CANDIDATES = [
    ("01", "cedar", cand_cedar),
    ("02", "dunes", cand_dunes),
    ("03", "tree-ring", cand_rings),
    ("04", "ridge", cand_ridge),
    ("05", "hourglass", cand_hourglass),
    ("06", "grove", cand_grove),
]


# ---------------------------------------------------------------- sheet bits

def centered_text(d, center, text, fnt, fill):
    b = d.textbbox((0, 0), text, font=fnt)
    x = center[0] - (b[2] - b[0]) / 2 - b[0]
    y = center[1] - (b[3] - b[1]) / 2 - b[1]
    d.text((x, y), text, font=fnt, fill=fill)


def contact_sheet(icons, bg, ink, path):
    cell_w, cell_h = 420, 540
    margin, gap = 40, 26
    head = 118
    sheet_w = margin * 2 + cell_w * 3 + gap * 2
    sheet_h = margin + head + cell_h * 2 + gap + margin

    sheet = Image.new("RGBA", (sheet_w, sheet_h), bg)
    d = ImageDraw.Draw(sheet)

    f_title = font("segoeuib.ttf", 40)
    f_num = font("segoeuib.ttf", 30)
    f_name = font("segoeui.ttf", 26)
    f_small = font("segoeui.ttf", 20)

    centered_text(d, (sheet_w / 2, margin + 34), "CEDAR & SAND THEME", f_title, ink)
    centered_text(d, (sheet_w / 2, margin + 82), "icon candidates", f_small, ink)

    for idx, (num, name, icon) in enumerate(icons):
        row, col = divmod(idx, 3)
        gx = margin + col * (cell_w + gap)
        gy = margin + head + row * (cell_h + gap)

        sheet.alpha_composite(icon.resize((260, 260), Image.LANCZOS),
                              (gx + (cell_w - 260) // 2, gy + 30))

        centered_text(d, (gx + cell_w / 2, gy + 330), num, f_num, ink)
        centered_text(d, (gx + cell_w / 2, gy + 372), name, f_name, ink)
        centered_text(d, (gx + cell_w / 2, gy + 404), "1024 x 1024  PNG", f_small, ink)

        thumb = icon.resize((32, 32), Image.LANCZOS)
        tx, ty = gx + cell_w - 32 - 22, gy + cell_h - 32 - 22
        d.rectangle([tx - 10, ty - 10, tx + 42, ty + 42],
                    outline=(ink[0], ink[1], ink[2], 70), width=1)
        sheet.alpha_composite(thumb, (tx, ty))

    save_png(sheet.convert("RGB"), path)


def inline_strip(icons, path):
    size, gap, margin = 150, 18, 30
    strip_w = margin * 2 + size * len(icons) + gap * (len(icons) - 1)
    strip_h = margin * 2 + size + 34
    strip = Image.new("RGBA", (strip_w, strip_h), LIGHT_BG)
    d = ImageDraw.Draw(strip)
    f_num = font("segoeuib.ttf", 20)

    for idx, (num, _name, icon) in enumerate(icons):
        x = margin + idx * (size + gap)
        strip.alpha_composite(icon.resize((size, size), Image.LANCZOS), (x, margin))
        centered_text(d, (x + size / 2, margin + size + 16), num, f_num, LIGHT_INK)

    save_png(strip.convert("RGB"), path)


def save_png(img, path):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(buf.getvalue())


def main():
    os.makedirs(OUT, exist_ok=True)

    icons = []
    for num, name, fn in CANDIDATES:
        icon = fn()
        box = icon.getbbox()
        if box is None:
            raise AssertionError("%s rendered empty" % name)
        left, top, right, bottom = box
        lo, hi = 70, 954
        if left < lo or top < lo or right > hi or bottom > hi:
            raise AssertionError("%s out of safe area: %s" % (name, box))
        path = os.path.join(OUT, "%s-%s.png" % (num, name))
        save_png(icon, path)
        print("wrote", os.path.relpath(path, ROOT), box)
        icons.append((num, name, icon))

    contact_sheet(icons, LIGHT_BG, LIGHT_INK, os.path.join(OUT, "contact-light.png"))
    contact_sheet(icons, DARK_BG, DARK_INK, os.path.join(OUT, "contact-dark.png"))
    inline_strip(icons, os.path.join(OUT, "inline-strip.png"))
    print("wrote contact-light.png / contact-dark.png / inline-strip.png")


if __name__ == "__main__":
    main()
