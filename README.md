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
- `main.py`: enthält eine kurze `main()`-Funktion, die einen künstlichen Messwert aus JSON liest und seine Felder ausgibt. SQLite folgt erst im nächsten Lernschritt.
- `data/sample_usage.json`: erfundene Beispieldaten, kein CodexBar-Export. `reporting_period` benennt die letzten 30 Tage relativ zum Messzeitpunkt; der Dollarwert ist nur ein Beispiel und wird nicht berechnet.
- Aktuell keine Datenbankspeicherung, Anbieteranbindung oder automatisierten Produkttests. Feldprüfung und Fehlerbehandlung fehlen noch.

## Lernkarten in Obsidian

Lernkarten sind eine optionale Nachschlagehilfe, keine automatische Mitschrift: Bei einem passenden neuen Thema kurz absprechen, dann Merkregel und Codebeispiel festhalten. Oben steht ein scharfes SVG-Vorschaubild, darunter editierbarer Text; Bilder und Notizen bleiben getrennt. Die Graph View zeigt farbige Themen und verknüpfte Karten, `⌘` + Hover die Bildvorschau ohne Properties.

- [Lernkarten-Inhalte](notes/python-basics.md)
- [Kurzer Workflow, Vorlage und Renderer](notes/obsidian/README.md)
- [Gezielter Vault-Export](notes/obsidian/vault-export/): Lernkarten, Bilder und Darstellungseinstellungen; keine archivierten Hochschulnotizen. Kein automatischer Abgleich mit dem lokalen Vault.

## Ausführen

Python 3 genügt; keine zusätzlichen Pakete nötig. Einmalig im Projektroot eine virtuelle Umgebung (virtual environment) erstellen:

```bash
python3 -m venv .venv
```

Für jede neue Terminalsitzung aktivieren und das Programm starten:

```bash
source .venv/bin/activate
python main.py
```

Mit `deactivate` verlässt du die Umgebung. `.venv/` bleibt lokal und wird nicht in Git eingecheckt.

Alternativ `main.py` in PyCharm ausführen; als Projektinterpreter `.venv/bin/python` auswählen. Die Beispieldatei wird relativ zum Speicherort von `main.py` gefunden, unabhängig vom Arbeitsverzeichnis.

```text
JSON-Datei → json.load() → Python-Dictionary → Felder ausgeben
```

Das Programm liest nur die JSON-Datei; es verändert keine Daten und stellt keine Anbieteranfragen. Eine eventuell aus dem vorherigen Lernschritt vorhandene SQLite-Datei wird nicht verwendet.
