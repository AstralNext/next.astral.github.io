"""Rasterize Classic Bold app icons into Astral2 / AstralGame assets."""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw

TEAL = (15, 118, 110, 255)       # #0F766E
BLACK = (0, 0, 0, 255)           # #000000
TEAL_FG = (240, 253, 250, 255)   # #F0FDFA
WHITE = (255, 255, 255, 255)     # #FFFFFF

ASTRAL2 = Path(r"C:\Users\baika\Documents\GitHub\Astral2")
ASTRAL_GAME = Path(r"J:\Documents\GitHub\AstralGame")
PORTAL = Path(r"J:\Documents\GitHub\next.astral.github.io")


def draw_classic_bold(size: int, bg: tuple, fg: tuple) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    rx = size * 112 / 512
    d.rounded_rectangle((0, 0, size - 1, size - 1), radius=rx, fill=bg)

    pad = size * 48 / 512
    s = (size - 2 * pad) / 512

    def xy(x: float, y: float) -> tuple[float, float]:
        return pad + x * s, pad + y * s

    def r(v: float) -> float:
        return v * s

    def thick_line(x1, y1, x2, y2, width):
        p1, p2 = xy(x1, y1), xy(x2, y2)
        d.line([p1, p2], fill=fg, width=max(1, int(round(r(width)))))
        # round caps
        rad = r(width) / 2
        for p in (p1, p2):
            d.ellipse((p[0] - rad, p[1] - rad, p[0] + rad, p[1] + rad), fill=fg)

    def disk(cx, cy, radius):
        c = xy(cx, cy)
        rr = r(radius)
        d.ellipse((c[0] - rr, c[1] - rr, c[0] + rr, c[1] + rr), fill=fg)

    thick_line(242, 156, 363, 343, 40)
    thick_line(363, 343, 142, 416, 34)
    disk(242, 156, 118)
    disk(363, 343, 76)
    disk(142, 416, 52)
    return img


def save_png(path: Path, img: Image.Image) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, format="PNG", optimize=True)
    print("wrote", path)


def save_ico(path: Path, base: Image.Image, sizes=(16, 24, 32, 48, 64, 128, 256)) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Use a large source; Pillow generates requested sizes into one ICO
    src = base if base.size[0] >= 256 else base.resize((256, 256), Image.Resampling.LANCZOS)
    src.save(path, format="ICO", sizes=[(s, s) for s in sizes])
    print("wrote", path)


def write_android_mipmaps(app_root: Path, img: Image.Image) -> None:
    densities = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
    }
    res = app_root / "android" / "app" / "src" / "main" / "res"
    for folder, sz in densities.items():
        out = res / folder / "ic_launcher.png"
        save_png(out, img.resize((sz, sz), Image.Resampling.LANCZOS))


def apply_product(app_root: Path, bg, fg, also_android=True) -> None:
    master = draw_classic_bold(1024, bg, fg)
    logo = master.resize((512, 512), Image.Resampling.LANCZOS)

    save_png(app_root / "assets" / "logo.png", logo)
    save_ico(app_root / "assets" / "icon.ico", logo)
    save_ico(app_root / "windows" / "runner" / "resources" / "app_icon.ico", logo)

    if also_android:
        write_android_mipmaps(app_root, logo)


def main() -> None:
    if ASTRAL2.exists():
        apply_product(ASTRAL2, TEAL, TEAL_FG, also_android=True)
    apply_product(ASTRAL_GAME, BLACK, WHITE, also_android=True)

    # also drop PNGs next to portal concepts for reference
    save_png(
        PORTAL / "public" / "logos" / "concepts" / "icon-classic-bold-general.png",
        draw_classic_bold(512, TEAL, TEAL_FG),
    )
    save_png(
        PORTAL / "public" / "logos" / "concepts" / "icon-classic-bold-game.png",
        draw_classic_bold(512, BLACK, WHITE),
    )
    print("done")


if __name__ == "__main__":
    main()
