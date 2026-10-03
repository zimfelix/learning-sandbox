# Learning Sandbox – Abo-Tracker

Lernprojekt für einen lokalen Vergleich der Nutzung von Claude Code und Codex. Langfristig soll das Tool Tokenverbrauch, geschätzte API-Kostenäquivalente und Abo-Limitstände speichern und auswerten. API-Kostenäquivalente sind keine tatsächlichen Abo-Ausgaben oder garantierten Guthaben.

## Lernweise

Anspruch: Probleme vor der Implementierung verstehen und zerlegen, Technologien und Fachbegriffe kennenlernen sowie Lösungswege mit ihren Vor- und Nachteilen abwägen. Der Agent schreibt den Code; Felix lernt, ihn zu lesen, zu erklären und auf Verhalten, Risiken und Grenzen zu prüfen – ohne Pflicht zum eigenen Codeschreiben oder Auswendiglernen von Syntax.

```text
Künstliche JSON-Daten → Python → SQLite → Auswertung
                                      ↑
                    später echte CodexBar-Daten
```

SQLite ist ein neues Lernthema. Anbieterzugriffe, echte Daten und automatische Beobachtung werden erst im jeweils ausdrücklich beauftragten Schritt eingebunden.

## Aktueller Stand

- `AGENTS.md`: projektbezogene Lern- und Arbeitsregeln.
- `main.py`: liest einen künstlichen Messwert aus JSON ein und zeigt die Felder an.
- `data/sample_usage.json`: erfundene Beispieldaten, kein CodexBar-Export. `reporting_period` benennt die letzten 30 Tage relativ zum Messzeitpunkt; der Dollarwert ist nur ein Beispiel und wird nicht berechnet.
- Noch keine Datenbank, Anbieteranbindung oder Produkttests eingerichtet. Feldprüfung und Fehlerbehandlung sind noch nicht umgesetzt.

## Ausführen

Python 3 genügt; keine zusätzlichen Pakete nötig. Aus dem Projektroot:

```bash
python3 main.py
```

Alternativ `main.py` in PyCharm ausführen. Die Beispieldatei wird relativ zum Speicherort von `main.py` gefunden, unabhängig vom Arbeitsverzeichnis.

```text
JSON-Datei → json.load() → Python-Dictionary → Felder ausgeben
```

Das Programm liest nur die Datei; es verändert keine Messwerte und stellt keine Anbieteranfragen.
