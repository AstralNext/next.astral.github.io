from pathlib import Path

root = Path(__file__).resolve().parents[1]
logos = root / "public" / "logos"

TEAL = "#0F766E"
TEAL_FG = "#F0FDFA"
INK = "#14201C"
INK_LIGHT = "#E8F0EC"
MUTED = "#6B7C74"
MUTED_DARK = "#84948C"
BLACK = "#000000"
WHITE = "#FFFFFF"
GRAY = "#737373"
GRAY_LIGHT = "#A3A3A3"


def mark_app(bg: str, fg: str) -> str:
    """Full app icon 512² — no nested fractional scale."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512" fill="none">
  <rect width="512" height="512" rx="112" fill="{bg}"/>
  <g fill="{fg}" stroke="{fg}" stroke-linecap="round">
    <line x1="235" y1="166" x2="333" y2="318" stroke-width="32"/>
    <line x1="333" y1="318" x2="154" y2="377" stroke-width="28"/>
    <circle cx="235" cy="166" r="96" stroke="none"/>
    <circle cx="333" cy="318" r="62" stroke="none"/>
    <circle cx="154" cy="377" r="42" stroke="none"/>
  </g>
</svg>
"""


def mark_lockup_group(bg: str, fg: str) -> str:
    """56×56 framed mark at lockup native coords (no scale())."""
    return f"""  <g transform="translate(8 8)">
    <rect width="56" height="56" rx="14" fill="{bg}"/>
    <g fill="{fg}" stroke="{fg}" stroke-linecap="round">
      <line x1="25.7" y1="18.1" x2="36.4" y2="34.8" stroke-width="3.5"/>
      <line x1="36.4" y1="34.8" x2="16.8" y2="41.2" stroke-width="3"/>
      <circle cx="25.7" cy="18.1" r="10.5" stroke="none"/>
      <circle cx="36.4" cy="34.8" r="6.8" stroke="none"/>
      <circle cx="16.8" cy="41.2" r="4.6" stroke="none"/>
    </g>
  </g>"""


def lockup_general(bg: str, fg: str, word: str, sub: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 72" width="300" height="72" fill="none" role="img" aria-label="Astral">
  <title>Astral</title>
{mark_lockup_group(bg, fg)}
  <text x="78" y="42" fill="{word}" font-family="Outfit, 'Noto Sans SC', system-ui, sans-serif" font-size="32" font-weight="800" letter-spacing="-0.04em">Astral</text>
  <text x="78" y="60" fill="{sub}" font-family="Outfit, 'Noto Sans SC', system-ui, sans-serif" font-size="10" font-weight="700" letter-spacing="0.22em">GENERAL</text>
</svg>
"""


def lockup_game(bg: str, fg: str, word: str, game_word: str, sub: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 72" width="320" height="72" fill="none" role="img" aria-label="Astral Game">
  <title>Astral Game</title>
{mark_lockup_group(bg, fg)}
  <text x="78" y="42" fill="{word}" font-family="Outfit, 'Noto Sans SC', system-ui, sans-serif" font-size="30" font-weight="800" letter-spacing="-0.04em">Astral</text>
  <text x="182" y="42" fill="{game_word}" font-family="Outfit, 'Noto Sans SC', system-ui, sans-serif" font-size="26" font-weight="700" letter-spacing="-0.02em">Game</text>
  <text x="78" y="60" fill="{sub}" font-family="Outfit, 'Noto Sans SC', system-ui, sans-serif" font-size="10" font-weight="700" letter-spacing="0.22em">MULTIPLAYER</text>
</svg>
"""


files = {
    logos / "astral-general-mark.svg": mark_app(TEAL, TEAL_FG),
    logos / "astral-game-mark.svg": mark_app(BLACK, WHITE),
    root / "public" / "favicon.svg": mark_app(TEAL, TEAL_FG),
    logos / "astral-general.svg": lockup_general(TEAL, TEAL_FG, INK, MUTED),
    logos / "astral-general-dark.svg": lockup_general(TEAL, TEAL_FG, INK_LIGHT, MUTED_DARK),
    logos / "astral-game.svg": lockup_game(BLACK, WHITE, BLACK, BLACK, GRAY),
    logos / "astral-game-dark.svg": lockup_game(BLACK, WHITE, WHITE, WHITE, GRAY_LIGHT),
    logos / "concepts" / "icon-classic-bold-general.svg": mark_app(TEAL, TEAL_FG),
    logos / "concepts" / "icon-classic-bold-game.svg": mark_app(BLACK, WHITE),
    logos / "concepts" / "icon-classic-bold-general-soft.svg": mark_app("#ECFDF5", TEAL),
    logos / "concepts" / "icon-classic-bold-game-soft.svg": mark_app(BLACK, WHITE),
}

for path, content in files.items():
    path.write_text(content, encoding="utf-8", newline="\n")
    print("wrote", path.relative_to(root))

print("done")
