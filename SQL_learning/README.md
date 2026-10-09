# SQL-Lernen – JSON, Python und SQLite

Dieses Lernvorhaben nutzt einen lokalen Claude-Code-/Codex-Abo-Tracker als Übungsbeispiel. Es ist unabhängig vom Obsidian-Vorhaben und definiert nicht den Zweck der gesamten Sandbox.

## Lernziel

```text
Künstliche JSON-Daten → Python → SQLite → Auswertung
                                      ↑
                    später echte Anbieter-/CodexBar-Daten
```

Zunächst Daten einlesen und verstehen, danach Speicherung und Abfragen mit SQLite kennenlernen. Ein mögliches späteres Ziel ist die Auswertung von Tokenverbrauch, geschätzten API-Kostenäquivalenten und Abo-Limitständen. API-Kostenäquivalente sind keine tatsächlichen Abo-Ausgaben oder garantierten Guthaben.

SQLite ist neu; JSON und APIs wurden bereits kurz behandelt, aber nicht als beherrscht vorausgesetzt. JSON ist ein Datenformat (data format), eine CLI-/HTTP-Schnittstelle ein interface (Schnittstelle), SQLite dient der database storage (Datenbankspeicherung).

## Aktueller Stand

- `main.py`: `main()` liest einen künstlichen Messwert aus JSON und gibt seine Felder aus.
- `data/sample_usage.json`: erfundene Beispieldaten, kein CodexBar-Export. `reporting_period` benennt die letzten 30 Tage relativ zum Messzeitpunkt; der Dollarwert ist nur ein Beispiel und wird nicht berechnet.
- Noch keine Datenbankspeicherung, Anbieteranbindung oder automatisierten Produkttests. Feldprüfung und Fehlerbehandlung fehlen.
- Beginne mit künstlichen Daten. Echte Anbieteranbindung, Importe und automatische Beobachtung folgen nur im jeweils ausdrücklich beauftragten Schritt.

## Ausführen

Python 3 und seine Standardbibliothek genügen; keine zusätzlichen Pakete nötig. Vom Repositoryroot aus:

```bash
python3 SQL_learning/main.py
```

Optional eine eigene virtual environment (virtuelle Umgebung) für dieses Vorhaben anlegen:

```bash
python3 -m venv SQL_learning/.venv
source SQL_learning/.venv/bin/activate
python SQL_learning/main.py
```

Mit `deactivate` verlässt du die Umgebung. `.venv/` bleibt lokal und wird nicht eingecheckt. Eine bereits vorhandene Umgebung kann weiter genutzt werden; eine gemeinsame Umgebung aller Lernvorhaben ist nicht erforderlich.

Alternativ `main.py` in PyCharm mit einem Python-3-Interpreter ausführen. Die Beispieldatei wird relativ zum Speicherort des Skripts gefunden, unabhängig vom Arbeitsverzeichnis.

## Verhalten und Prüfgrenzen

```text
JSON-Datei → json.load() → Python-Dictionary → Felder ausgeben
```

Das Programm liest nur die JSON-Datei; es verändert keine Daten und stellt keine Anbieteranfragen. Eine eventuell vorhandene SQLite-Datei wird nicht verwendet. Ein erfolgreicher Lauf zeigt das Einlesen dieser Beispieldatei, nicht die Verarbeitung beliebiger oder fehlerhafter Eingaben.

Es gelten die gemeinsamen Lern- und Arbeitsregeln aus `../AGENTS.md`. Obsidian-Karten sind keine Voraussetzung und werden nur nach eigener Absprache erstellt.
