"""Client for the (unofficial) Jobsuche interface of the Bundesagentur für Arbeit."""

import base64
import json
import time
import urllib.parse
import urllib.request

BASE = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service"
HEADERS = {"X-API-Key": "jobboerse-jobsuche"}
PAUSE_SECONDS = 0.3  # stay polite: at most ~3 requests per second


def _get(url: str, params: dict | None = None) -> dict:
    time.sleep(PAUSE_SECONDS)
    if params:
        url += "?" + urllib.parse.urlencode(params, safe=";")
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def search_page(term: str, days: int, page: int, size: int = 100) -> list[dict]:
    """One result page for a search term (part-time and mini jobs only)."""
    params = {
        "was": term,
        "arbeitszeit": "tz;mj",
        "veroeffentlichtseit": days,
        "angebotsart": 1,
        "zeitarbeit": "false",
        "pav": "false",
        "page": page,
        "size": size,
    }
    data = _get(f"{BASE}/pc/v6/jobs", params)
    return data.get("ergebnisliste", [])


def search_all(term: str, days: int, max_pages: int) -> list[dict]:
    """All pages for a term until the results run out or max_pages is reached."""
    jobs = []
    for page in range(1, max_pages + 1):
        batch = search_page(term, days, page)
        jobs.extend(batch)
        if len(batch) < 100:
            break
    return jobs


def fetch_detail(refnr: str) -> dict:
    code = base64.b64encode(refnr.encode()).decode()
    return _get(f"{BASE}/pc/v4/jobdetails/{code}")


def job_link(refnr: str) -> str:
    return f"https://www.arbeitsagentur.de/jobsuche/jobdetail/{refnr}"
