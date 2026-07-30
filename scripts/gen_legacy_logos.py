from pathlib import Path

out = Path(__file__).resolve().parents[1] / "public" / "logos" / "concepts"

BAR1 = (
    'matrix(0.33034422993659973,-0.9438605904579163,'
    '0.9438604712486267,0.3303442597389221,'
    '-291.52531891700346,421.10342406318523)'
)
BAR2 = (
    'matrix(-0.5432449579238892,-0.8395742774009705,'
    '0.8395742774009705,-0.5432449579238892,'
    '268.6207212216759,832.2849449105124)'
)


def bars(bar1, bar2, width=15):
    return f"""  <g transform="{BAR1}">
    <line x1="151.00390625" y1="408.5" x2="426.46832275390625" y2="408.5" stroke="{bar1}" stroke-width="{width}"/>
  </g>
  <g transform="{BAR2}">
    <rect x="360.705078125" y="335.5733642578125" width="230.231" height="{width}" rx="{width/2}" fill="{bar2}"/>
  </g>"""


def nodes_fill(c1, c2, c3):
    return f"""  <circle cx="242" cy="156" r="100" fill="{c1}"/>
  <circle cx="363" cy="343" r="60" fill="{c2}"/>
  <circle cx="142" cy="416" r="40" fill="{c3}"/>"""


def nodes_ring(color, w1=18, w2=14, w3=12):
    # hollow rings — keep centers aligned with original
    return f"""  <circle cx="242" cy="156" r="{100 - w1/2}" fill="none" stroke="{color}" stroke-width="{w1}"/>
  <circle cx="363" cy="343" r="{60 - w2/2}" fill="none" stroke="{color}" stroke-width="{w2}"/>
  <circle cx="142" cy="416" r="{40 - w3/2}" fill="none" stroke="{color}" stroke-width="{w3}"/>"""


def wrap(body, defs=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none">
{defs}{body}
</svg>
"""


def mark_svg(color, c1=None, c2=None, c3=None, bar1=None, bar2=None, width=15):
    c1 = c1 or color
    c2 = c2 or color
    c3 = c3 or color
    bar1 = bar1 or color
    bar2 = bar2 or color
    return wrap(bars(bar1, bar2, width) + "\n" + nodes_fill(c1, c2, c3))


def app_svg(bg, fg, rx=14):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <rect width="64" height="64" rx="{rx}" fill="{bg}"/>
  <g transform="translate(4.5 4.5) scale(0.1074)">
{bars(fg, fg)}
{nodes_fill(fg, fg, fg)}
  </g>
</svg>
"""


def lockup_svg(color, label, label_color, word="#14201C", word_text="Astral"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 220" fill="none">
  <g transform="translate(8 10) scale(0.38)">
{bars(color, color)}
{nodes_fill(color, color, color)}
  </g>
  <text x="230" y="118" fill="{word}" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="78" font-weight="800" letter-spacing="-0.04em">{word_text}</text>
  <text x="230" y="168" fill="{label_color}" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="22" font-weight="700" letter-spacing="0.2em">{label}</text>
</svg>
"""


TEAL = "#0F766E"
AMBER = "#C27803"
INK = "#14201C"
SOFT = "#0D9488"
SKY = "#0369A1"
CORAL = "#C2410C"
TEAL_LIGHT = "#5EEAD4"
AMBER_LIGHT = "#FBBF24"

files = {}

# —— base confirmed pair ——
files["e-legacy-teal.svg"] = mark_svg(TEAL)
files["e-legacy-amber.svg"] = mark_svg(AMBER)
files["e-legacy-ink.svg"] = mark_svg(INK)
files["e-legacy-soft.svg"] = mark_svg(SOFT)
files["e-legacy-sky.svg"] = mark_svg(SKY)
files["e-legacy-duo.svg"] = mark_svg(TEAL, c3=AMBER, bar2=AMBER)
files["e-legacy-split.svg"] = mark_svg(TEAL, c3=AMBER, bar1=TEAL, bar2=AMBER)
files["e-legacy-game-hot.svg"] = mark_svg(CORAL)
files["e-legacy-teal-on-dark.svg"] = mark_svg(TEAL_LIGHT)
files["e-legacy-amber-on-dark.svg"] = mark_svg(AMBER_LIGHT)
files["e-legacy-teal-app.svg"] = app_svg(TEAL, "#F8FAFC")
files["e-legacy-amber-app.svg"] = app_svg(AMBER, "#FFFBEB")
files["e-legacy-ink-app.svg"] = app_svg(INK, "#F8FAFC")
files["e-legacy-teal-lockup.svg"] = lockup_svg(TEAL, "GENERAL", TEAL)
files["e-legacy-amber-lockup.svg"] = lockup_svg(AMBER, "GAME", AMBER)
files["e-legacy-ink-lockup.svg"] = lockup_svg(INK, "NEXT", INK)

# —— G: extensions of the confirmed mark ——

# G1 outline / ring
files["g-outline-teal.svg"] = wrap(bars(TEAL, TEAL, 12) + "\n" + nodes_ring(TEAL))
files["g-outline-amber.svg"] = wrap(bars(AMBER, AMBER, 12) + "\n" + nodes_ring(AMBER))

# G2 gradient solid
files["g-gradient-teal.svg"] = wrap(
    bars("url(#gt)", "url(#gt)") + "\n" + nodes_fill("url(#gt)", "url(#gt)", "url(#gt)"),
    defs="""  <defs>
    <linearGradient id="gt" x1="120" y1="80" x2="400" y2="440" gradientUnits="userSpaceOnUse">
      <stop stop-color="#0F766E"/><stop offset="1" stop-color="#14B8A6"/>
    </linearGradient>
  </defs>
""",
)
files["g-gradient-amber.svg"] = wrap(
    bars("url(#ga)", "url(#ga)") + "\n" + nodes_fill("url(#ga)", "url(#ga)", "url(#ga)"),
    defs="""  <defs>
    <linearGradient id="ga" x1="120" y1="80" x2="400" y2="440" gradientUnits="userSpaceOnUse">
      <stop stop-color="#C27803"/><stop offset="1" stop-color="#F59E0B"/>
    </linearGradient>
  </defs>
""",
)

# G3 hierarchy fade (smaller nodes lighter)
files["g-fade-teal.svg"] = wrap(
    bars(TEAL, TEAL) + "\n"
    + '  <circle cx="242" cy="156" r="100" fill="#0F766E"/>\n'
    + '  <circle cx="363" cy="343" r="60" fill="#0F766E" fill-opacity="0.72"/>\n'
    + '  <circle cx="142" cy="416" r="40" fill="#0F766E" fill-opacity="0.5"/>'
)
files["g-fade-amber.svg"] = wrap(
    bars(AMBER, AMBER) + "\n"
    + '  <circle cx="242" cy="156" r="100" fill="#C27803"/>\n'
    + '  <circle cx="363" cy="343" r="60" fill="#C27803" fill-opacity="0.72"/>\n'
    + '  <circle cx="142" cy="416" r="40" fill="#C27803" fill-opacity="0.5"/>'
)

# G4 thick bars (bolder mark)
files["g-bold-teal.svg"] = mark_svg(TEAL, width=22)
files["g-bold-amber.svg"] = mark_svg(AMBER, width=22)

# G5 ring + solid small accent (duo structure)
files["g-ring-accent-teal.svg"] = wrap(
    bars(TEAL, TEAL, 12) + "\n"
    + nodes_ring(TEAL)
    + '\n  <circle cx="142" cy="416" r="22" fill="#0F766E"/>'
)
files["g-ring-accent-amber.svg"] = wrap(
    bars(AMBER, AMBER, 12) + "\n"
    + nodes_ring(AMBER)
    + '\n  <circle cx="142" cy="416" r="22" fill="#C27803"/>'
)

# G6 nested core on large node
files["g-core-teal.svg"] = wrap(
    bars(TEAL, TEAL) + "\n" + nodes_fill(TEAL, TEAL, TEAL)
    + '\n  <circle cx="242" cy="156" r="42" fill="#F0FDFA"/>'
)
files["g-core-amber.svg"] = wrap(
    bars(AMBER, AMBER) + "\n" + nodes_fill(AMBER, AMBER, AMBER)
    + '\n  <circle cx="242" cy="156" r="42" fill="#FFFBEB"/>'
)

# G7 currentColor mono (for CSS)
files["g-mono.svg"] = wrap(bars("currentColor", "currentColor") + "\n" + nodes_fill("currentColor", "currentColor", "currentColor"))

# G8 circle badge (round app)
files["g-badge-teal.svg"] = app_svg(TEAL, "#F8FAFC", rx=32)
files["g-badge-amber.svg"] = app_svg(AMBER, "#FFFBEB", rx=32)

# G9 soft pastel plate
files["g-plate-teal.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none">
  <rect width="512" height="512" rx="96" fill="#ECFDF5"/>
  <g transform="translate(24 24) scale(0.906)">
{bars(TEAL, TEAL)}
{nodes_fill(TEAL, TEAL, TEAL)}
  </g>
</svg>
"""
files["g-plate-amber.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none">
  <rect width="512" height="512" rx="96" fill="#FFFBEB"/>
  <g transform="translate(24 24) scale(0.906)">
{bars(AMBER, AMBER)}
{nodes_fill(AMBER, AMBER, AMBER)}
  </g>
</svg>
"""

# G10 CN lockups
files["g-lockup-general-cn.svg"] = lockup_svg(TEAL, "通用版", TEAL)
files["g-lockup-game-cn.svg"] = lockup_svg(AMBER, "游戏版", AMBER)

# G11 stacked wordmark (mark above text)
files["g-stacked-teal.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 520" fill="none">
  <g transform="translate(54 8) scale(0.61)">
{bars(TEAL, TEAL)}
{nodes_fill(TEAL, TEAL, TEAL)}
  </g>
  <text x="210" y="390" text-anchor="middle" fill="#14201C" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="64" font-weight="800" letter-spacing="-0.04em">Astral</text>
  <text x="210" y="440" text-anchor="middle" fill="#0F766E" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="22" font-weight="700" letter-spacing="0.28em">GENERAL</text>
</svg>
"""
files["g-stacked-amber.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 520" fill="none">
  <g transform="translate(54 8) scale(0.61)">
{bars(AMBER, AMBER)}
{nodes_fill(AMBER, AMBER, AMBER)}
  </g>
  <text x="210" y="390" text-anchor="middle" fill="#14201C" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="64" font-weight="800" letter-spacing="-0.04em">Astral</text>
  <text x="210" y="440" text-anchor="middle" fill="#C27803" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="22" font-weight="700" letter-spacing="0.28em">GAME</text>
</svg>
"""

# G12 duo product pair strip
files["g-pair-strip.svg"] = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1040 420" fill="none">
  <rect x="0" y="0" width="500" height="420" rx="36" fill="#F8FAFC"/>
  <rect x="540" y="0" width="500" height="420" rx="36" fill="#FFFBEB"/>
  <g transform="translate(74 34) scale(0.68)">
{bars(TEAL, TEAL)}
{nodes_fill(TEAL, TEAL, TEAL)}
  </g>
  <g transform="translate(614 34) scale(0.68)">
{bars(AMBER, AMBER)}
{nodes_fill(AMBER, AMBER, AMBER)}
  </g>
  <text x="250" y="390" text-anchor="middle" fill="#0F766E" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="28" font-weight="700" letter-spacing="0.18em">GENERAL</text>
  <text x="790" y="390" text-anchor="middle" fill="#C27803" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="28" font-weight="700" letter-spacing="0.18em">GAME</text>
</svg>
"""

for name, content in files.items():
    (out / name).write_text(content, encoding="utf-8")
    print("wrote", name)

print("done", len(files))
