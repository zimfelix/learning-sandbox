"""Lead finder: part-time office jobs at craft businesses (Handwerk), nationwide.

Usage:  python main.py [--target 100] [--since 2026-10-01]
Steps:  search → keyword score → details → Haiku classification → CSV export
"""

import argparse
import csv
import json
from datetime import date
from pathlib import Path

import ba_api
import classify
import store
from prefilter import score

SEARCH_TERMS = [
    "Bürokraft", "Büroassistenz", "Bürokaufmann", "Büromitarbeiter",
    "Sekretärin", "Kaufmännische Mitarbeiter", "Büro Handwerk", "Verwaltung",
]
BATCH_SIZE = 20
EXPORT_PATH = Path(__file__).parent / "data" / "handwerk_leads.csv"


def fetch(conn, since: date, max_pages: int) -> None:
    days = min((date.today() - since).days + 1, 100)
    for term in SEARCH_TERMS:
        jobs = ba_api.search_all(term, days, max_pages)
        new = store.insert_jobs(conn, jobs)
        print(f"  {term:<28} {len(jobs):>5} gefunden, {new:>5} neu")


def rescore(conn) -> None:
    rows = conn.execute("SELECT refnr, firma, titel, berufe FROM jobs").fetchall()
    conn.executemany(
        "UPDATE jobs SET score=? WHERE refnr=?",
        [(score(r["firma"], r["titel"], r["berufe"]), r["refnr"]) for r in rows],
    )
    conn.commit()


def next_candidates(conn, since: date, limit: int) -> list:
    return conn.execute(
        "SELECT * FROM jobs WHERE handwerk IS NULL AND veroeffentlicht >= ?"
        " AND score >= 0 ORDER BY score DESC, veroeffentlicht DESC LIMIT ?",
        (since.isoformat(), limit),
    ).fetchall()


def load_details(conn, rows: list) -> list:
    for row in rows:
        if row["beschreibung"] is None:
            detail = ba_api.fetch_detail(row["refnr"])
            text = detail.get("stellenangebotsBeschreibung", "")
            conn.execute("UPDATE jobs SET beschreibung=? WHERE refnr=?", (text, row["refnr"]))
    conn.commit()
    refnrs = [row["refnr"] for row in rows]
    marks = ",".join("?" * len(refnrs))
    return conn.execute(f"SELECT * FROM jobs WHERE refnr IN ({marks})", refnrs).fetchall()


def count_leads(conn, since: date) -> int:
    query = "SELECT COUNT(*) FROM jobs WHERE handwerk=1 AND veroeffentlicht >= ?"
    return conn.execute(query, (since.isoformat(),)).fetchone()[0]


def classify_until(conn, since: date, target: int) -> None:
    while count_leads(conn, since) < target:
        rows = next_candidates(conn, since, BATCH_SIZE)
        if not rows:
            print("  Keine weiteren Kandidaten.")
            return
        rows = load_details(conn, rows)
        results = classify.classify_batch(rows)
        for result in results:
            store.save_classification(conn, result)
        # Postings the model skipped get -1 so the loop does not ask again.
        conn.executemany("UPDATE jobs SET handwerk=-1 WHERE refnr=? AND handwerk IS NULL",
                         [(row["refnr"],) for row in rows])
        conn.commit()
        print(f"  {len(rows)} geprüft → bisher {count_leads(conn, since)} Handwerk-Leads")


def export(conn, since: date, target: int) -> int:
    rows = conn.execute(
        "SELECT * FROM jobs WHERE handwerk=1 AND veroeffentlicht >= ?"
        " ORDER BY veroeffentlicht DESC LIMIT ?",
        (since.isoformat(), target),
    ).fetchall()
    with EXPORT_PATH.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Firma", "Gewerk", "Stelle", "PLZ", "Ort", "Veröffentlicht",
                         "Büroaufgaben", "Link", "Externer Link"])
        for r in rows:
            tasks = ", ".join(json.loads(r["aufgaben"] or "[]"))
            writer.writerow([r["firma"], r["gewerk"], r["titel"], r["plz"], r["ort"],
                             r["veroeffentlicht"], tasks, ba_api.job_link(r["refnr"]),
                             r["externe_url"] or ""])
    return len(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=int, default=100)
    parser.add_argument("--since", type=date.fromisoformat,
                        default=date.today().replace(day=1))
    parser.add_argument("--max-pages", type=int, default=20)
    parser.add_argument("--skip-fetch", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    conn = store.connect()
    if not args.skip_fetch:
        print(f"1) Suche seit {args.since} …")
        fetch(conn, args.since, args.max_pages)
    rescore(conn)
    print(f"2) Klassifizierung mit {classify.MODEL} bis {args.target} Leads …")
    classify_until(conn, args.since, args.target)
    print(f"3) Export: {export(conn, args.since, args.target)} Leads → {EXPORT_PATH}")


if __name__ == "__main__":
    main()
