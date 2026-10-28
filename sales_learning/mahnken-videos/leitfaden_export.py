"""Exportiert ../leitfaden.docx (Word, die Quelle) als leitfaden.js für den Tab „Leitfaden“ in uebersicht.html.

Aufruf: python3 leitfaden_export.py   (nur macOS: nutzt das eingebaute textutil)
"""
import json
import re
import shutil
import subprocess
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
SRC, OUT = HERE.parent / "leitfaden.docx", HERE / "leitfaden.js"
# Optional: aus Word gespeichertes PDF (Datei → Als PDF exportieren → sales_learning/leitfaden.pdf).
# Wird neben die Seite kopiert und im Tab „Leitfaden“ verlinkt (.docx kann claude.ai nicht ausliefern).
PDF_SRC, PDF_OUT = HERE.parent / "leitfaden.pdf", HERE / "leitfaden.pdf"


def docx_html(path):
    cmd = ["textutil", "-convert", "html", "-stdout", str(path)]
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout


def tag_for(size, underlined):
    """Aufbau wie Julians Vorlage: Titel groß und fett, Abschnitte unterstrichen, Sätze normal."""
    return "h1" if size >= 19.5 else "h2" if underlined else "p"


def paragraph(sizes, under, m):
    inner = m[2].strip()
    text = re.sub(r"<[^>]+>", "", inner).strip()
    if not text:
        return ""
    spans = re.findall(r'<span class="(s\d+)">', inner)
    t = tag_for(sizes.get(m[1], 12), bool(spans) and all(c in under for c in spans))
    return f"<{t}>{re.sub(r'</?span[^>]*>', '', inner)}</{t}>"


def clean(html):
    sizes = {c: float(s) for c, s in re.findall(r"p\.(p\d+) \{[^}]*?font: ([\d.]+)px", html)}
    under = set(re.findall(r"span\.(s\d+) \{[^}]*underline", html))
    body = html.split("<body>", 1)[1].split("</body>", 1)[0]
    body = re.sub(r'<span class="Apple-tab-span">\s*</span>', "", body)
    body = re.sub(r'<p class="(p\d+)">(.*?)</p>', lambda m: paragraph(sizes, under, m), body, flags=re.S)
    return re.sub(r'(?<![">])(https?://[^\s<]+)', r'<a href="\1" target=_blank>\1</a>', body)


def main():
    html = clean(docx_html(SRC))
    pdf = PDF_SRC.exists()
    if pdf:
        shutil.copyfile(PDF_SRC, PDF_OUT)
    OUT.write_text(f"window.LEITFADEN={json.dumps(html, ensure_ascii=False)};\n"
                   f"window.LEITFADEN_STAND={json.dumps(date.today().isoformat())};\n"
                   f"window.LEITFADEN_PDF={json.dumps(pdf)};\n")
    print("PDF:", "kopiert" if pdf else "fehlt – in Word als sales_learning/leitfaden.pdf exportieren")
    print(f"{OUT.name}: {len(html)} Zeichen, Videos verlinkt: {len(set(re.findall(r'youtu.be/([\w-]{11})', html)))}")


if __name__ == "__main__":
    main()
