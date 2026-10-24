"""Second opinion: Sonnet re-checks every Handwerk lead, plus a live check at the BA.

Usage:  python verify.py
Writes check_* columns and data/sonnet_review.md
"""

import json
import urllib.error
from pathlib import Path

import ba_api
import classify
import store

MODEL = "sonnet"
BATCH_SIZE = 10
REPORT_PATH = Path(__file__).parent / "data" / "sonnet_review.md"

PROMPT = """Du prüfst die Arbeit eines kleineren Modells. Jede Anzeige wurde als
"Handwerksbetrieb sucht Bürokraft in Teilzeit/Minijob" eingestuft. Prüfe kritisch:
1. Ist der Arbeitgeber wirklich ein Handwerksbetrieb (nicht Händler, Hersteller-Konzern,
   Hausverwaltung, Personalvermittler, Praxis)?
2. Passen Gewerk und Büroaufgaben zur Beschreibung, oder wurde etwas erfunden?
3. Ist es wirklich eine Bürostelle in Teilzeit oder Minijob?
urteil: "ok", "zweifelhaft" oder "falsch". notiz: ein konkreter Satz.
Antworte NUR mit einer JSON-Liste:
[{"refnr": "...", "urteil": "ok", "notiz": "..."}]

Anzeigen:
"""


def _payload(row) -> dict:
    return {
        "refnr": row["refnr"], "firma": row["firma"], "titel": row["titel"],
        "gewerk": row["gewerk"], "aufgaben": json.loads(row["aufgaben"] or "[]"),
        "beschreibung": (row["beschreibung"] or "")[:2000],
    }


def is_online(refnr: str) -> bool:
    try:
        return bool(ba_api.fetch_detail(refnr).get("referenznummer"))
    except urllib.error.HTTPError:
        return False


def review_batch(rows: list) -> list[dict]:
    text = PROMPT + json.dumps([_payload(r) for r in rows], ensure_ascii=False)
    output = classify.run_claude(text, MODEL)
    known = {r["refnr"] for r in rows}
    return [item for item in classify.extract_json_list(output) if item.get("refnr") in known]


def save_review(conn, rows: list, reviews: list[dict]) -> None:
    for item in reviews:
        conn.execute("UPDATE jobs SET check_urteil=?, check_notiz=? WHERE refnr=?",
                     (item.get("urteil"), item.get("notiz"), item["refnr"]))
    for row in rows:
        conn.execute("UPDATE jobs SET check_online=? WHERE refnr=?",
                     (int(is_online(row["refnr"])), row["refnr"]))
    conn.commit()


def write_report(conn) -> None:
    rows = conn.execute("SELECT * FROM jobs WHERE handwerk=1 ORDER BY check_urteil DESC").fetchall()
    counts = {}
    for r in rows:
        counts[r["check_urteil"] or "ohne"] = counts.get(r["check_urteil"] or "ohne", 0) + 1
    offline = sum(1 for r in rows if r["check_online"] == 0)
    lines = [f"# Sonnet-Gegencheck ({len(rows)} Leads)", "",
             "| Urteil | Anzahl |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(counts.items())]
    lines += ["", f"Nicht mehr online bei der BA: **{offline}**", "",
              "## Auffällige Leads", ""]
    lines += [f"- **{r['check_urteil']}** · {r['firma']} ({r['ort']}): {r['check_notiz']}"
              for r in rows if r["check_urteil"] != "ok"]
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    conn = store.connect()
    rows = conn.execute("SELECT * FROM jobs WHERE handwerk=1").fetchall()
    for start in range(0, len(rows), BATCH_SIZE):
        batch = rows[start:start + BATCH_SIZE]
        save_review(conn, batch, review_batch(batch))
        print(f"  {min(start + BATCH_SIZE, len(rows))}/{len(rows)} geprüft")
    write_report(conn)
    print(f"Bericht: {REPORT_PATH}")


if __name__ == "__main__":
    main()
