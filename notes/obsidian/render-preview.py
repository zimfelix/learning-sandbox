"""Render one learning-card JSON file as a scalable SVG preview."""
import argparse
import json
import re
from html import escape
from pathlib import Path

COLORS = {
    "text": "#d9e1ec", "muted": "#a7b4c5",
    "code": "#89dceb", "rule": "#ffffff",
}
KEYWORDS = {"def", "from", "import", "class", "return", "try", "except", "with", "as", "pass"}
TOKEN_PATTERN = r'("[^"]*"|#[^\n]*|\b(?:' + "|".join(sorted(KEYWORDS)) + r')\b)'


def token_color(token):
    if token.startswith('"'):
        return "#a6e3a1"
    if token.startswith("#"):
        return "#94a3b8"
    return "#cba6f7" if token in KEYWORDS else COLORS["code"]


def code_spans(text):
    spans = []
    for token in re.split(TOKEN_PATTERN, text):
        color = token_color(token)
        spans.append(
            f'<tspan fill="{color}" xml:space="preserve">{escape(token)}</tspan>'
        )
    return "".join(spans)


def text_line(y, kind, text, accent):
    size = 29 if kind == "title" else 19 if kind == "code" else 21
    font = "monospace" if kind == "code" else "sans-serif"
    weight = "700" if kind in {"title", "rule"} else "400"
    color = accent if kind == "title" else COLORS[kind]
    content = code_spans(text) if kind == "code" else escape(text)
    return (
        f'<text x="36" y="{y}" fill="{color}" font-family="{font}" '
        f'font-size="{size}" font-weight="{weight}" xml:space="preserve">'
        f'{content}</text>'
    )


def render(card):
    lines = card["lines"]
    accent = card.get("accent", "#f6c85f")
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", accent):
        raise ValueError("Accent must be a six-digit hex color")
    height = 64 + sum(24 if kind == "gap" else 36 for kind, _ in lines)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="780" '
        f'height="{height}" viewBox="0 0 780 {height}">',
        '<rect width="100%" height="100%" rx="18" fill="#181c23"/>',
        f'<rect width="7" height="100%" rx="3" fill="{accent}"/>',
    ]
    y = 44
    for kind, text in lines:
        if kind != "gap":
            parts.append(text_line(y, kind, text, accent))
        y += 24 if kind == "gap" else 36
    return "\n".join(parts + ["</svg>"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    card = json.loads(args.source.read_text(encoding="utf-8"))
    svg = render(card)
    args.destination.parent.mkdir(parents=True, exist_ok=True)
    mode = "w" if args.overwrite else "x"
    with args.destination.open(mode, encoding="utf-8") as file:
        file.write(svg)


if __name__ == "__main__":
    main()
