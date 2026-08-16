from pathlib import Path
import json

out = Path(__file__).resolve().parents[1] / "public" / "logos" / "concepts"

TEAL = "#0F766E"
INK = "#14201C"
TEAL_FG = "#F0FDFA"
INK_FG = "#F8FAFC"

SIZE = 512
RX = 112
PAD = 48  # slightly less pad so bold mark fills better


def icon(bg, body):
    inner = SIZE - PAD * 2
    scale = inner / 512
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" fill="none">
  <rect width="{SIZE}" height="{SIZE}" rx="{RX}" fill="{bg}"/>
  <g transform="translate({PAD} {PAD}) scale({scale:.6f})">
{body}
  </g>
</svg>
"""


def classic_bold(color):
    # thicker bars + larger nodes than previous A1
    return f"""  <line x1="242" y1="156" x2="363" y2="343" stroke="{color}" stroke-width="40" stroke-linecap="round"/>
  <line x1="363" y1="343" x2="142" y2="416" stroke="{color}" stroke-width="34" stroke-linecap="round"/>
  <circle cx="242" cy="156" r="118" fill="{color}"/>
  <circle cx="363" cy="343" r="76" fill="{color}"/>
  <circle cx="142" cy="416" r="52" fill="{color}"/>"""


forms = {
    "classic-bold": ("Classic Bold", "原版三圆连线 · 加粗", classic_bold),
}

keep_names = set()
meta = []

for key, (title, desc, fn) in forms.items():
    for product, bg, fg in (("general", TEAL, TEAL_FG), ("game", INK, INK_FG)):
        name = f"icon-{key}-{product}.svg"
        (out / name).write_text(icon(bg, fn(fg)), encoding="utf-8")
        keep_names.add(name)
        print("wrote", name)
    meta.append({"id": key, "title": title, "desc": desc})

for key, (title, desc, fn) in forms.items():
    for product, plate, mark in (("general", "#ECFDF5", TEAL), ("game", "#F4F4F5", INK)):
        name = f"icon-{key}-{product}-soft.svg"
        (out / name).write_text(icon(plate, fn(mark)), encoding="utf-8")
        keep_names.add(name)
        print("wrote", name)

keep_names.add("icons-meta.json")
deleted = 0
for p in out.iterdir():
    if p.is_file() and p.name not in keep_names:
        p.unlink()
        deleted += 1
        print("deleted", p.name)

(out / "icons-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("done", deleted, "deleted")
