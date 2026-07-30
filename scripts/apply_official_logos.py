from pathlib import Path

root = Path(__file__).resolve().parents[1]
logos = root / "public" / "logos"
concepts = logos / "concepts"
public = root / "public"

TEAL = "#0F766E"
AMBER = "#C27803"
TEAL_LIGHT = "#2DD4BF"
AMBER_LIGHT = "#FBBF24"
TEAL_FG = "#F0FDFA"
AMBER_FG = "#FFFBEB"
INK = "#14201C"
INK_LIGHT = "#E8F0EC"
MUTED = "#6B7C74"
MUTED_DARK = "#84948C"


def bold_mark(color):
    return f"""  <line x1="242" y1="156" x2="363" y2="343" stroke="{color}" stroke-width="40" stroke-linecap="round"/>
  <line x1="363" y1="343" x2="142" y2="416" stroke="{color}" stroke-width="34" stroke-linecap="round"/>
  <circle cx="242" cy="156" r="118" fill="{color}"/>
  <circle cx="363" cy="343" r="76" fill="{color}"/>
  <circle cx="142" cy="416" r="52" fill="{color}"/>"""


def app_icon(bg, fg, size=512, rx=112, pad=48):
    scale = (size - pad * 2) / 512
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" fill="none">
  <rect width="{size}" height="{size}" rx="{rx}" fill="{bg}"/>
  <g transform="translate({pad} {pad}) scale({scale:.6f})">
{bold_mark(fg)}
  </g>
</svg>
"""


def lockup(bg, fg, word, sub, word_fill, sub_fill, title, width=300):
    # framed mark 56x56 inside 72-tall lockup
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 72" fill="none" role="img" aria-label="{title}">
  <title>{title}</title>
  <g transform="translate(8 8)">
    <rect width="56" height="56" rx="14" fill="{bg}"/>
    <g transform="translate(5.25 5.25) scale(0.089)">
{bold_mark(fg)}
    </g>
  </g>
  <text x="78" y="42" fill="{word_fill}" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="32" font-weight="800" letter-spacing="-0.04em">{word}</text>
  <text x="78" y="60" fill="{sub_fill}" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="10" font-weight="700" letter-spacing="0.22em">{sub}</text>
</svg>
"""


def lockup_game(bg, fg, word_fill, sub_fill, title):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 72" fill="none" role="img" aria-label="{title}">
  <title>{title}</title>
  <g transform="translate(8 8)">
    <rect width="56" height="56" rx="14" fill="{bg}"/>
    <g transform="translate(5.25 5.25) scale(0.089)">
{bold_mark(fg)}
    </g>
  </g>
  <text x="78" y="42" fill="{word_fill}" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="30" font-weight="800" letter-spacing="-0.04em">Astral</text>
  <text x="182" y="42" fill="{fg if fg != TEAL_FG and fg != AMBER_FG else AMBER}" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="26" font-weight="700" letter-spacing="-0.02em">Game</text>
  <text x="78" y="60" fill="{sub_fill}" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="10" font-weight="700" letter-spacing="0.22em">MULTIPLAYER</text>
</svg>
"""


files = {
    logos / "astral-general-mark.svg": app_icon(TEAL, TEAL_FG),
    logos / "astral-game-mark.svg": app_icon(AMBER, AMBER_FG),
    public / "favicon.svg": app_icon(TEAL, TEAL_FG),
    logos / "astral-general.svg": lockup(TEAL, TEAL_FG, "Astral", "GENERAL", INK, MUTED, "Astral"),
    logos / "astral-general-dark.svg": lockup(TEAL, TEAL_FG, "Astral", "GENERAL", INK_LIGHT, MUTED_DARK, "Astral"),
    logos / "astral-game.svg": lockup_game(AMBER, AMBER_FG, INK, MUTED, "Astral Game"),
    logos / "astral-game-dark.svg": lockup_game(AMBER, AMBER_FG, INK_LIGHT, MUTED_DARK, "Astral Game"),
}

# Fix game lockup "Game" accent color — for light fg mark plate, use AMBER for Game word
def lockup_game_fixed(bg, mark_fg, game_word_color, word_fill, sub_fill, title):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 72" fill="none" role="img" aria-label="{title}">
  <title>{title}</title>
  <g transform="translate(8 8)">
    <rect width="56" height="56" rx="14" fill="{bg}"/>
    <g transform="translate(5.25 5.25) scale(0.089)">
{bold_mark(mark_fg)}
    </g>
  </g>
  <text x="78" y="42" fill="{word_fill}" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="30" font-weight="800" letter-spacing="-0.04em">Astral</text>
  <text x="182" y="42" fill="{game_word_color}" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="26" font-weight="700" letter-spacing="-0.02em">Game</text>
  <text x="78" y="60" fill="{sub_fill}" font-family="Outfit, Noto Sans SC, system-ui, sans-serif" font-size="10" font-weight="700" letter-spacing="0.22em">MULTIPLAYER</text>
</svg>
"""

files[logos / "astral-game.svg"] = lockup_game_fixed(AMBER, AMBER_FG, AMBER, INK, MUTED, "Astral Game")
files[logos / "astral-game-dark.svg"] = lockup_game_fixed(AMBER, AMBER_FG, AMBER_LIGHT, INK_LIGHT, MUTED_DARK, "Astral Game")

# Keep concepts in sync
files[concepts / "icon-classic-bold-general.svg"] = app_icon(TEAL, TEAL_FG)
files[concepts / "icon-classic-bold-game.svg"] = app_icon(AMBER, AMBER_FG)
files[concepts / "icon-classic-bold-general-soft.svg"] = app_icon("#ECFDF5", TEAL)
files[concepts / "icon-classic-bold-game-soft.svg"] = app_icon("#FFFBEB", AMBER)

for path, content in files.items():
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(root))

print("applied A1 Classic Bold")
