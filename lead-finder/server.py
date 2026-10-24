"""Local lead browser: http://127.0.0.1:8765  (standard library only)."""

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import ba_api
import store

HOST, PORT = "127.0.0.1", 8765
INDEX = Path(__file__).parent / "ui" / "index.html"
EDITABLE = ("status", "notiz", "telefon")
FIELDS = ("refnr", "firma", "titel", "gewerk", "plz", "ort", "region", "veroeffentlicht",
          "beschreibung", "externe_url", "status", "notiz", "telefon",
          "check_urteil", "check_notiz", "check_online", "begruendung")


def list_leads() -> list[dict]:
    conn = store.connect()
    rows = conn.execute("SELECT * FROM jobs WHERE handwerk=1 ORDER BY veroeffentlicht DESC")
    leads = []
    for row in rows:
        lead = {field: row[field] for field in FIELDS}
        lead["aufgaben"] = json.loads(row["aufgaben"] or "[]")
        lead["link"] = ba_api.job_link(row["refnr"])
        leads.append(lead)
    return leads


def update_lead(refnr: str, changes: dict) -> None:
    allowed = {key: str(value) for key, value in changes.items() if key in EDITABLE}
    if not allowed:
        return
    conn = store.connect()
    assignments = ", ".join(f"{key}=?" for key in allowed)
    conn.execute(f"UPDATE jobs SET {assignments} WHERE refnr=?", [*allowed.values(), refnr])
    conn.commit()


class Handler(BaseHTTPRequestHandler):
    def _send(self, body: bytes, content_type: str, status: int = 200) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/":
            self._send(INDEX.read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/api/leads":
            body = json.dumps(list_leads(), ensure_ascii=False).encode()
            self._send(body, "application/json; charset=utf-8")
        else:
            self._send(b"not found", "text/plain", 404)

    def do_POST(self) -> None:
        if not self.path.startswith("/api/leads/"):
            return self._send(b"not found", "text/plain", 404)
        length = int(self.headers.get("Content-Length", 0))
        update_lead(self.path.rsplit("/", 1)[1], json.loads(self.rfile.read(length) or b"{}"))
        self._send(b'{"ok": true}', "application/json")

    def log_message(self, *args) -> None:  # keep the terminal quiet
        pass


if __name__ == "__main__":
    print(f"Lead-Browser: http://{HOST}:{PORT}")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
