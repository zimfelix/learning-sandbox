# Lead Finder: Bürojobs im Handwerk

Findet Teilzeit- und Minijob-Ausschreibungen für Bürokräfte bei Handwerksbetrieben (bundesweit, aktueller Monat). Gedacht als Lead-Liste für Büroautomatisierung: Wer eine Bürokraft sucht, hat nachweislich Bürolast.

## Ausführung

```bash
cd lead-finder
python3 main.py                      # 100 Leads seit Monatsanfang
python3 main.py --target 200 --since 2026-09-15
python3 main.py --skip-fetch         # nur weiter klassifizieren, ohne neue Suche
```

Danach:

```bash
python3 verify.py    # Sonnet prüft jeden Lead + Online-Check bei der BA → data/sonnet_review.md
python3 server.py    # Oberfläche: http://127.0.0.1:8765 (Status, Notiz, Telefon werden gespeichert)
```

Ergebnis: `data/handwerk_leads.csv` (Semikolon-getrennt, öffnet direkt in Excel/Numbers).

Voraussetzungen: Python 3.10+, eingeloggte Claude-Code-CLI (`claude`). Keine weiteren Pakete, kein API-Key.

## Ablauf

```
BA-Jobsuche (Teilzeit/Minijob, ohne Zeitarbeit/Vermittler, mehrere Suchbegriffe)
   ↓ ba_api.py           Duplikate über refnr entfernt (store.py)
SQLite data/leads.db
   ↓ prefilter.py        Stichwort-Score: wahrscheinliche Handwerker zuerst
   ↓ ba_api.fetch_detail Beschreibung nur für die nächsten Kandidaten
   ↓ classify.py         Haiku via `claude -p`: handwerk / gewerk / aufgaben
   ↓ main.py export      bis --target erreicht ist
data/handwerk_leads.csv
```

| Datei | Zuständigkeit |
|---|---|
| `ba_api.py` | Suche, Details, Link. 0,3 s Pause pro Anfrage |
| `store.py` | Tabelle `jobs`, Einfügen, Ergebnis speichern |
| `prefilter.py` | Stichwortlisten für die Reihenfolge (kein Ausschluss bei Score ≥ 0) |
| `classify.py` | Prompt, CLI-Aufruf, JSON auslesen |
| `main.py` | Ablauf, CLI-Parameter, CSV-Export |
| `verify.py` | Gegencheck durch Sonnet, prüft, ob die Anzeige noch online ist, Bericht |
| `server.py` + `ui/index.html` | lokaler Lead-Browser mit kleiner CRM-Funktion (nur `127.0.0.1`) |

`handwerk` in der DB: `1` = ja, `0` = nein, `-1` = Modell hat nicht geantwortet, `NULL` = noch offen.

## Grenzen

- **Quelle:** Die Schnittstelle ist inoffiziell (die App-Schnittstelle der Jobbörse, dokumentiert von bund.dev). Sie kann sich ohne Ankündigung ändern. Kommerzielle Nutzung vor dem Geschäftsstart prüfen.
- **Kein Ansprechpartner:** Die API liefert keine Kontaktdaten. Die BA zeigt sie nur auf der Website hinter einem Captcha.
- **Klassifizierung:** Haiku kann sich irren. Stichprobe prüfen, Spalte „Gewerk“ ansehen.
- **Abdeckung:** Nur die BA-Jobbörse. Betriebe, die nur bei StepStone/Indeed inserieren, fehlen.
- **Kontaktaufnahme:** keine Kalt-E-Mails (§ 7 UWG). Brief oder Telefon mit Bedacht.
