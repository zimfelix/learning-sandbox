"""Classify postings with Claude Haiku via the headless Claude Code CLI (uses the subscription)."""

import json
import re
import subprocess

MODEL = "haiku"

PROMPT = """Du bekommst Stellenanzeigen als JSON-Liste. Entscheide für jede:
- handwerk: true, wenn der ARBEITGEBER ein Handwerksbetrieb ist (z. B. Elektro, SHK,
  Dach, Maler, Tischler, Bau, Kfz-Werkstatt, Garten- und Landschaftsbau). Händler,
  Praxen, Kanzleien, Hotels, Behörden, Personalvermittler: false.
- gewerk: kurzes Gewerk oder "".
- aufgaben: bis zu 5 Büroaufgaben aus der Anzeige, kurz (z. B. "Rechnungen schreiben").
- begruendung: ein kurzer Satz.
Antworte NUR mit einer JSON-Liste:
[{"refnr": "...", "handwerk": true, "gewerk": "...", "aufgaben": ["..."], "begruendung": "..."}]

Anzeigen:
"""


def _job_payload(row) -> dict:
    return {
        "refnr": row["refnr"],
        "firma": row["firma"],
        "titel": row["titel"],
        "beschreibung": (row["beschreibung"] or "")[:1500],
    }


def extract_json_list(text: str) -> list[dict]:
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON list in model output: {text[:200]}")
    return json.loads(match.group(0))


def run_claude(prompt: str, model: str) -> str:
    """One headless Claude Code call; returns the plain text answer."""
    result = subprocess.run(
        ["claude", "-p", "--model", model],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=600,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "claude CLI failed")
    return result.stdout


def classify_batch(rows: list) -> list[dict]:
    payload = json.dumps([_job_payload(row) for row in rows], ensure_ascii=False)
    output = run_claude(PROMPT + payload, MODEL)
    known = {row["refnr"] for row in rows}
    return [item for item in extract_json_list(output) if item.get("refnr") in known]
