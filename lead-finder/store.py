"""SQLite storage: one row per job posting."""

import json
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "leads.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
    refnr        TEXT PRIMARY KEY,
    titel        TEXT,
    firma        TEXT,
    plz          TEXT,
    ort          TEXT,
    region       TEXT,
    veroeffentlicht TEXT,
    berufe       TEXT,
    externe_url  TEXT,
    score        INTEGER DEFAULT 0,
    beschreibung TEXT,
    handwerk     INTEGER,          -- NULL = not classified yet
    gewerk       TEXT,
    aufgaben     TEXT,
    begruendung  TEXT
);
"""


# Columns added after the first version; created on demand for existing databases.
EXTRA_COLUMNS = {
    "status": "TEXT DEFAULT 'neu'",   # neu | angerufen | interessiert | kein_interesse
    "notiz": "TEXT DEFAULT ''",
    "telefon": "TEXT DEFAULT ''",
    "check_urteil": "TEXT",           # Sonnet: ok | zweifelhaft | falsch
    "check_notiz": "TEXT",
    "check_online": "INTEGER",        # 1 = posting still reachable at the BA
}


def _add_missing_columns(conn: sqlite3.Connection) -> None:
    existing = {row[1] for row in conn.execute("PRAGMA table_info(jobs)")}
    for name, definition in EXTRA_COLUMNS.items():
        if name not in existing:
            conn.execute(f"ALTER TABLE jobs ADD COLUMN {name} {definition}")


def connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    _add_missing_columns(conn)
    return conn


def _row_from_search(job: dict) -> tuple:
    address = (job.get("stellenlokationen") or [{}])[0].get("adresse", {})
    return (
        job["referenznummer"],
        job.get("stellenangebotsTitel", ""),
        job.get("firma", ""),
        address.get("plz", ""),
        address.get("ort", ""),
        address.get("region", ""),
        job.get("datumErsteVeroeffentlichung", ""),
        ", ".join(job.get("alleBerufe", [])),
        job.get("externeUrl"),
    )


def insert_jobs(conn: sqlite3.Connection, jobs: list[dict]) -> int:
    """Insert new postings; already known refnr are skipped. Returns new count."""
    before = conn.total_changes
    conn.executemany(
        "INSERT OR IGNORE INTO jobs (refnr, titel, firma, plz, ort, region,"
        " veroeffentlicht, berufe, externe_url) VALUES (?,?,?,?,?,?,?,?,?)",
        [_row_from_search(job) for job in jobs],
    )
    conn.commit()
    return conn.total_changes - before


def save_classification(conn: sqlite3.Connection, result: dict) -> None:
    conn.execute(
        "UPDATE jobs SET handwerk=?, gewerk=?, aufgaben=?, begruendung=? WHERE refnr=?",
        (
            int(bool(result.get("handwerk"))),
            result.get("gewerk") or "",
            json.dumps(result.get("aufgaben") or [], ensure_ascii=False),
            result.get("begruendung") or "",
            result["refnr"],
        ),
    )
