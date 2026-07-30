from pathlib import Path
import math

out = Path(__file__).resolve().parents[1] / "public" / "logos" / "concepts"

TEAL = "#0F766E"
AMBER = "#C27803"
INK = "#14201C"


def svg(body, vb="0 0 512 512", defs=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none">
{defs}{body}
</svg>
"""


def pair(name_prefix, make_fn):
    """Write teal + amber variants from a builder(color)->body."""
    files = {}
    files[f"{name_prefix}-teal.svg"] = make_fn(TEAL)
    files[f"{name_prefix}-amber.svg"] = make_fn(AMBER)
    return files


# —— H form mutations of the classic 3-node mark ——

def h_arc(color):
    # curved connective ribs instead of straight bars
    return svg(f"""  <path d="M242 156 C310 180 340 260 363 343" stroke="{color}" stroke-width="15" stroke-linecap="round" fill="none"/>
  <path d="M363 343 C280 390 200 420 142 416" stroke="{color}" stroke-width="15" stroke-linecap="round" fill="none"/>
  <circle cx="242" cy="156" r="100" fill="{color}"/>
  <circle cx="363" cy="343" r="60" fill="{color}"/>
  <circle cx="142" cy="416" r="40" fill="{color}"/>""")


def h_orbit(color):
    # large orbit ring through the three nodes
    return svg(f"""  <ellipse cx="250" cy="270" rx="175" ry="195" stroke="{color}" stroke-width="14" opacity="0.28"/>
  <line x1="242" y1="156" x2="363" y2="343" stroke="{color}" stroke-width="15" stroke-linecap="round"/>
  <line x1="363" y1="343" x2="142" y2="416" stroke="{color}" stroke-width="15" stroke-linecap="round"/>
  <circle cx="242" cy="156" r="88" fill="{color}"/>
  <circle cx="363" cy="343" r="52" fill="{color}"/>
  <circle cx="142" cy="416" r="34" fill="{color}"/>""")


def h_chain(color):
    # overlapping chain / vesica between nodes
    return svg(f"""  <circle cx="242" cy="156" r="100" fill="{color}" fill-opacity="0.92"/>
  <circle cx="320" cy="270" r="78" fill="{color}" fill-opacity="0.78"/>
  <circle cx="363" cy="343" r="60" fill="{color}" fill-opacity="0.92"/>
  <circle cx="250" cy="380" r="48" fill="{color}" fill-opacity="0.7"/>
  <circle cx="142" cy="416" r="40" fill="{color}"/>""")


def h_triad(color):
    # equilateral-ish triad (rebalanced layout)
    c1, c2, c3 = (256, 118), (388, 360), (124, 360)
    return svg(f"""  <line x1="{c1[0]}" y1="{c1[1]}" x2="{c2[0]}" y2="{c2[1]}" stroke="{color}" stroke-width="16" stroke-linecap="round"/>
  <line x1="{c2[0]}" y1="{c2[1]}" x2="{c3[0]}" y2="{c3[1]}" stroke="{color}" stroke-width="16" stroke-linecap="round"/>
  <line x1="{c3[0]}" y1="{c3[1]}" x2="{c1[0]}" y2="{c1[1]}" stroke="{color}" stroke-width="16" stroke-linecap="round"/>
  <circle cx="{c1[0]}" cy="{c1[1]}" r="78" fill="{color}"/>
  <circle cx="{c2[0]}" cy="{c2[1]}" r="58" fill="{color}"/>
  <circle cx="{c3[0]}" cy="{c3[1]}" r="58" fill="{color}"/>""")


def h_spine(color):
    # vertical cascade spine (portrait mark)
    return svg(f"""  <line x1="256" y1="110" x2="256" y2="400" stroke="{color}" stroke-width="18" stroke-linecap="round"/>
  <circle cx="256" cy="110" r="78" fill="{color}"/>
  <circle cx="256" cy="255" r="54" fill="{color}"/>
  <circle cx="256" cy="390" r="36" fill="{color}"/>""")


def h_branch(color):
    # Y-branch from hub
    return svg(f"""  <line x1="256" y1="150" x2="140" y2="390" stroke="{color}" stroke-width="16" stroke-linecap="round"/>
  <line x1="256" y1="150" x2="372" y2="390" stroke="{color}" stroke-width="16" stroke-linecap="round"/>
  <circle cx="256" cy="140" r="86" fill="{color}"/>
  <circle cx="140" cy="390" r="48" fill="{color}"/>
  <circle cx="372" cy="390" r="48" fill="{color}"/>""")


def h_hex(color):
    # round nodes replaced by hex tiles, same classic positions
    def hex_pts(cx, cy, r):
        pts = []
        for i in range(6):
            a = math.radians(-90 + i * 60)
            pts.append(f"{cx + r*math.cos(a):.1f},{cy + r*math.sin(a):.1f}")
        return " ".join(pts)
    return svg(f"""  <line x1="242" y1="156" x2="363" y2="343" stroke="{color}" stroke-width="15" stroke-linecap="round"/>
  <line x1="363" y1="343" x2="142" y2="416" stroke="{color}" stroke-width="15" stroke-linecap="round"/>
  <polygon points="{hex_pts(242,156,92)}" fill="{color}"/>
  <polygon points="{hex_pts(363,343,56)}" fill="{color}"/>
  <polygon points="{hex_pts(142,416,38)}" fill="{color}"/>""")


def h_pulse(color):
    # concentric rings on main node + classic chain
    return svg(f"""  <circle cx="242" cy="156" r="128" stroke="{color}" stroke-width="10" opacity="0.22"/>
  <circle cx="242" cy="156" r="150" stroke="{color}" stroke-width="6" opacity="0.12"/>
  <line x1="242" y1="156" x2="363" y2="343" stroke="{color}" stroke-width="15" stroke-linecap="round"/>
  <line x1="363" y1="343" x2="142" y2="416" stroke="{color}" stroke-width="15" stroke-linecap="round"/>
  <circle cx="242" cy="156" r="86" fill="{color}"/>
  <circle cx="363" cy="343" r="52" fill="{color}"/>
  <circle cx="142" cy="416" r="34" fill="{color}"/>""")


def h_slash(color):
    # diagonal slash mark — compressed classic silhouette
    return svg(f"""  <g transform="translate(40 20) rotate(-18 256 256)">
    <line x1="210" y1="120" x2="340" y2="320" stroke="{color}" stroke-width="18" stroke-linecap="round"/>
    <line x1="340" y1="320" x2="160" y2="400" stroke="{color}" stroke-width="16" stroke-linecap="round"/>
    <circle cx="210" cy="120" r="82" fill="{color}"/>
    <circle cx="340" cy="320" r="52" fill="{color}"/>
    <circle cx="160" cy="400" r="34" fill="{color}"/>
  </g>""")


def h_frame(color):
    # soft rounded frame containing the classic mark
    return svg(f"""  <rect x="48" y="48" width="416" height="416" rx="88" stroke="{color}" stroke-width="18"/>
  <g transform="translate(36 28) scale(0.86)">
    <line x1="242" y1="156" x2="363" y2="343" stroke="{color}" stroke-width="15" stroke-linecap="round"/>
    <line x1="363" y1="343" x2="142" y2="416" stroke="{color}" stroke-width="15" stroke-linecap="round"/>
    <circle cx="242" cy="156" r="90" fill="{color}"/>
    <circle cx="363" cy="343" r="54" fill="{color}"/>
    <circle cx="142" cy="416" r="36" fill="{color}"/>
  </g>""")


def h_dotpath(color):
    # dashed bead path between nodes
    return svg(f"""  <path d="M242 156 L363 343 L142 416" stroke="{color}" stroke-width="10" stroke-linecap="round" stroke-dasharray="0 28" stroke-linejoin="round"/>
  <circle cx="242" cy="156" r="92" fill="{color}"/>
  <circle cx="363" cy="343" r="56" fill="{color}"/>
  <circle cx="142" cy="416" r="36" fill="{color}"/>
  <circle cx="290" cy="230" r="12" fill="{color}"/>
  <circle cx="330" cy="300" r="10" fill="{color}"/>
  <circle cx="270" cy="372" r="9" fill="{color}"/>
  <circle cx="200" cy="400" r="8" fill="{color}"/>""")


def h_wedge(color):
    # pie / sector nodes (gamey)
    return svg(f"""  <line x1="242" y1="156" x2="363" y2="343" stroke="{color}" stroke-width="14" stroke-linecap="round"/>
  <line x1="363" y1="343" x2="142" y2="416" stroke="{color}" stroke-width="14" stroke-linecap="round"/>
  <path d="M242 156 L342 156 A100 100 0 1 1 192 66 Z" fill="{color}"/>
  <circle cx="363" cy="343" r="56" fill="{color}"/>
  <circle cx="142" cy="416" r="36" fill="{color}"/>""")


def h_mirror(color):
    # mirrored twin hubs (duplex / P2P)
    return svg(f"""  <line x1="150" y1="180" x2="362" y2="180" stroke="{color}" stroke-width="16" stroke-linecap="round"/>
  <line x1="150" y1="180" x2="256" y2="380" stroke="{color}" stroke-width="14" stroke-linecap="round"/>
  <line x1="362" y1="180" x2="256" y2="380" stroke="{color}" stroke-width="14" stroke-linecap="round"/>
  <circle cx="150" cy="170" r="70" fill="{color}"/>
  <circle cx="362" cy="170" r="70" fill="{color}"/>
  <circle cx="256" cy="380" r="48" fill="{color}"/>""")


def h_signal(color):
    # radio / signal waves from main node
    return svg(f"""  <path d="M242 156 Q320 210 363 343" stroke="{color}" stroke-width="14" fill="none" stroke-linecap="round"/>
  <path d="M363 343 Q250 390 142 416" stroke="{color}" stroke-width="14" fill="none" stroke-linecap="round"/>
  <path d="M160 90 Q120 156 160 222" stroke="{color}" stroke-width="12" fill="none" stroke-linecap="round" opacity="0.45"/>
  <path d="M120 60 Q60 156 120 252" stroke="{color}" stroke-width="10" fill="none" stroke-linecap="round" opacity="0.28"/>
  <circle cx="242" cy="156" r="86" fill="{color}"/>
  <circle cx="363" cy="343" r="52" fill="{color}"/>
  <circle cx="142" cy="416" r="34" fill="{color}"/>""")


builders = {
    "h-arc": h_arc,
    "h-orbit": h_orbit,
    "h-chain": h_chain,
    "h-triad": h_triad,
    "h-spine": h_spine,
    "h-branch": h_branch,
    "h-hex": h_hex,
    "h-pulse": h_pulse,
    "h-slash": h_slash,
    "h-frame": h_frame,
    "h-dotpath": h_dotpath,
    "h-wedge": h_wedge,
    "h-mirror": h_mirror,
    "h-signal": h_signal,
}

count = 0
for prefix, fn in builders.items():
    for color_name, color in (("teal", TEAL), ("amber", AMBER)):
        path = out / f"{prefix}-{color_name}.svg"
        path.write_text(fn(color), encoding="utf-8")
        print("wrote", path.name)
        count += 1

# duo morph: teal structure + amber accent node (selected forms)
specials = {
    "h-branch-duo.svg": h_branch(TEAL).replace(
        f'<circle cx="372" cy="390" r="48" fill="{TEAL}"/>',
        f'<circle cx="372" cy="390" r="48" fill="{AMBER}"/>',
    ),
    "h-mirror-duo.svg": h_mirror(TEAL).replace(
        f'<circle cx="256" cy="380" r="48" fill="{TEAL}"/>',
        f'<circle cx="256" cy="380" r="48" fill="{AMBER}"/>',
    ),
    "h-signal-duo.svg": h_signal(TEAL).replace(
        f'<circle cx="142" cy="416" r="34" fill="{TEAL}"/>',
        f'<circle cx="142" cy="416" r="34" fill="{AMBER}"/>',
    ),
}
for name, content in specials.items():
    (out / name).write_text(content, encoding="utf-8")
    print("wrote", name)
    count += 1

print("done", count)
