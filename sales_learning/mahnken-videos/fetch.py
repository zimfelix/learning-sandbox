"""Lädt deutsche YouTube-Untertitel und speichert sie als lesbare .txt in transcripts/.

Aufruf:  python3 fetch.py VIDEO_ID [VIDEO_ID ...]
         python3 fetch.py --next 5        # die nächsten 5 offenen Videos der letzten 2 Jahre, neueste zuerst
Braucht: uv (für `uvx yt-dlp`), node (zum Lesen von notes.js/videos.js).
"""
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "transcripts"


def load_js(name: str, var: str) -> object:
    """Liest window.VAR aus einer der .js-Datendateien über node."""
    code = f"global.window={{}};require('./{name}');console.log(JSON.stringify(window.{var}))"
    result = subprocess.run(["node", "-e", code], cwd=HERE, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


# Nr. 1–184 = Uploads der letzten zwei Jahre (Nr. 184 ≈ Ende Okt. 2024, Nr. 185 = 27.09.2024).
RECENT_MAX_NR = 184


def next_ids(count: int) -> list[str]:
    """Die nächsten noch nicht ausgewerteten Videos der letzten zwei Jahre, neueste zuerst."""
    videos = load_js("videos.js", "VIDEOS")
    notes = load_js("notes.js", "NOTES")
    open_videos = [v for v in videos if v["n"] <= RECENT_MAX_NR and v["id"] not in notes]
    return [v["id"] for v in open_videos][:count]


def download_vtt(video_id: str, folder: Path) -> Path | None:
    """Lädt nur die Untertitel (Original-Deutsch bevorzugt). None, wenn es keine gibt."""
    subprocess.run(
        ["uvx", "yt-dlp", "-q", "--skip-download", "--write-auto-subs", "--sub-langs", "de-orig,de",
         "--sub-format", "vtt", "-o", str(folder / video_id), f"https://www.youtube.com/watch?v={video_id}"],
        capture_output=True, text=True,
    )
    for suffix in (".de-orig.vtt", ".de.vtt"):
        path = folder / f"{video_id}{suffix}"
        if path.exists():
            return path
    return None


def vtt_to_text(vtt: Path) -> str:
    """Entfernt Dubletten und Zeitcodes; setzt pro Minute einen Zeitstempel [m:ss]."""
    parts, seen, minute, stamp = [], set(), None, (0, "00")
    for line in vtt.read_text().splitlines():
        match = re.match(r"(\d+):(\d+):(\d+)\.\d+ -->", line)
        if match:
            stamp = (int(match[1]) * 60 + int(match[2]), match[3])
            continue
        text = re.sub(r"<[^>]+>", "", line).strip()
        if not text or text in seen or text.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        seen.add(text)
        if minute != stamp[0]:
            parts.append(f"\n[{stamp[0]}:{stamp[1]}] ")
            minute = stamp[0]
        parts.append(text + " ")
    return "".join(parts).strip() + "\n"


def main(args: list[str]) -> None:
    ids = next_ids(int(args[1])) if args[:1] == ["--next"] else args
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for video_id in ids:
            vtt = download_vtt(video_id, Path(tmp))
            if vtt is None:
                print(f"{video_id}\tKEIN TRANSKRIPT  → in notes.js nosubs: true setzen")
            else:
                text = vtt_to_text(vtt)
                (OUT / f"{video_id}.txt").write_text(text)
                print(f"{video_id}\t{len(text.split())} Wörter")
            time.sleep(3)  # YouTube blockt sonst (HTTP 429)


if __name__ == "__main__":
    main(sys.argv[1:])
