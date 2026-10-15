#!/usr/bin/env python3
"""Generate the ghw-demo-repo social preview image (1280x640, dark theme).

Run from anywhere:

    python3 social-preview/make_social_preview.py

Outputs:
    social-preview/social-preview.png   (1280x640, the file GitHub wants)

GitHub social preview requirements: PNG / JPG / GIF, <= 1 MB, recommended
1280x640 (a 2:1 ratio). This script uses Pillow, which is available in the
build environment; if Pillow is missing, fall back to the SVG source
(social-preview/social-preview.svg) and render it with:

    rsvg-convert -w 1280 -h 640 social-preview/social-preview.svg -o social-preview.png
    # or:  npx svgexport social-preview.svg social-preview.png 1280:640
"""

from __future__ import annotations

import pathlib

from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
HERE = pathlib.Path(__file__).resolve().parent

# --- palette (GitHub dark) -------------------------------------------------
BG_TOP = (13, 17, 23)       # #0d1117
BG_BOTTOM = (1, 4, 9)       # #010409
ACCENT = (88, 166, 255)     # #58a6ff  (GitHub blue)
ACCENT2 = (126, 231, 135)   # #7ee787  (GitHub green)
FG = (230, 237, 243)        # #e6edf3
MUTED = (139, 148, 158)     # #8b949e

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def load(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


def vertical_gradient(draw: ImageDraw.ImageDraw, w: int, h: int) -> None:
    for y in range(h):
        t = y / max(h - 1, 1)
        color = tuple(int(BG_TOP[i] + (BG_BOTTOM[i] - BG_TOP[i]) * t) for i in range(3))
        draw.line([(0, y), (w, y)], fill=color)


def main() -> None:
    img = Image.new("RGB", (W, H), BG_TOP)
    draw = ImageDraw.Draw(img)

    # Background gradient
    vertical_gradient(draw, W, H)

    # Faint grid to give it texture (very low contrast).
    grid = (255, 255, 255)
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=tuple(int(c * 0.04 + BG_TOP[i]) for i, c in enumerate(grid)), width=1)
    for y in range(0, H, 80):
        draw.line([(0, y), (W, y)], fill=tuple(int(c * 0.04 + BG_TOP[i]) for i, c in enumerate(grid)), width=1)

    # Accent bar on the left edge
    draw.rectangle([0, 0, 10, H], fill=ACCENT)
    draw.rectangle([10, 0, 150, H], fill=(20, 30, 46))

    # --- "terminal" pill:  ghw-demo-repo ~ git:(main) --------------------
    draw.rounded_rectangle([90, 96, 1190, 200], radius=16, fill=(22, 27, 34), outline=(48, 54, 61), width=2)
    # traffic-light dots
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        cx = 130 + i * 34
        draw.ellipse([cx - 9, 139, cx + 9, 157], fill=c)
    mono = load("DejaVuSansMono-Bold.ttf", 28)
    draw.text((252, 134), "meetr1912@github : ~/ghw-demo-repo", font=mono, fill=MUTED)
    branch = "git:(main)"
    bw = draw.textlength(branch, font=mono)
    draw.text((1150 - bw, 134), branch, font=mono, fill=ACCENT2)

    # --- Title: ghw-demo-repo --------------------------------------------
    title = load("DejaVuSans-Bold.ttf", 96)
    draw.text((90, 250), "ghw-demo-repo", font=title, fill=FG)

    # --- Subtitle ---------------------------------------------------------
    sub = load("DejaVuSans.ttf", 34)
    draw.text((92, 372), "A minimal, production-shaped Python starter", font=sub, fill=MUTED)

    # --- Event line -------------------------------------------------------
    ev = load("DejaVuSans-Bold.ttf", 30)
    draw.text((92, 424), "MLH Global Hack Week", font=ev, fill=ACCENT)
    ev_w = draw.textlength("MLH Global Hack Week", font=ev)
    draw.text((92 + ev_w + 18, 424), "· Hacktoberfest 2026", font=load("DejaVuSans.ttf", 30), fill=MUTED)

    # --- Bottom badges row (drawn as pills; mirrors the README badges) ----
    badge_font = load("DejaVuSans-Bold.ttf", 24)
    x = 92
    y = 508
    pills = [
        ("CI passing", ACCENT2, (12, 40, 24)),
        ("MIT License", (210, 168, 255), (34, 24, 46)),
        ("Python 3.11+", ACCENT, (16, 32, 54)),
        ("PRs welcome", (255, 145, 200), (44, 20, 34)),
    ]
    for label, fg, bg in pills:
        tw = draw.textlength(label, font=badge_font)
        pad = 20
        draw.rounded_rectangle([x, y, x + tw + 2 * pad, y + 46], radius=23, fill=bg, outline=fg, width=2)
        draw.text((x + pad, y + 9), label, font=badge_font, fill=fg)
        x += tw + 2 * pad + 18

    # --- Owner handle, bottom-right --------------------------------------
    handle = load("DejaVuSansMono.ttf", 28)
    text = "github.com/meetr1912/ghw-demo-repo"
    tw = draw.textlength(text, font=handle)
    draw.text((W - 90 - tw, 575), text, font=handle, fill=MUTED)

    out = HERE / "social-preview.png"
    img.save(out, "PNG", optimize=True)
    size_kb = out.stat().st_size / 1024
    print(f"wrote {out} ({W}x{H}, {size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
