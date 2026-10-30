# Learning Sandbox

Gemeinsames Repository für unabhängige Lernprojekte und Experimente. Kleine Vorhaben bleiben in eigenen Unterordnern statt in vielen einzelnen Repositories. Die Sandbox ist keine gemeinsame Anwendung: Code, Daten und fachlicher Kontext bleiben beim jeweiligen Vorhaben.

## Orientierung

```text
learning-sandbox/
├── AGENTS.md          gemeinsame Lern- und Arbeitsregeln
├── README.md          Übersicht
├── learning-state.md  Lernstand der Lernvorhaben (SQL/Python, Lernkarten)
├── SQL_learning/      JSON, Python und später SQLite
│   ├── README.md      Lernziel, Stand und Ausführung
│   ├── main.py
│   └── data/          künstliche Beispieldaten
└── obsidian/          unabhängiges Lernkarten-Vorhaben
    ├── AGENTS.md      spezielle Regeln für Lernkarten
    ├── README.md      Einstieg und Ablage
    ├── python-basics.md
    └── obsidian/      Workflow, Renderer, Vorlagen und Vault-Export
```

Die bestehende doppelte Ebene `obsidian/obsidian/` bleibt vorerst erhalten; es werden hier keine weiteren Dateien verschoben.

## Lernvorhaben

| Ordner | Zweck | Einstieg |
| --- | --- | --- |
| `SQL_learning/` | Künstliche JSON-Nutzungsdaten lesen; schrittweise SQLite und Auswertung kennenlernen | [SQL-Lernen](SQL_learning/README.md) |
| `obsidian/` | Lernkarten, SVG-Vorschauen und Darstellung in Obsidian erproben | [Obsidian](obsidian/README.md) |

Obsidian ist keine Voraussetzung für das SQL-Lernen. Weitere Vorhaben können nach Absprache eigene Unterordner erhalten. Es gibt keinen zentralen Programmstart; Ausführung und Dependencies (Abhängigkeiten) stehen in der jeweiligen README.

## Lernweise

Standard ist der Lernmodus (gilt für `SQL_learning/` und `obsidian/`): Problem verstehen und zerlegen → Lösungswege abwägen → überschaubaren Code verstehen und prüfen. Der Agent schreibt den Code; Felix untersucht Verhalten, Entscheidungen und Grenzen. Eigenes Codeschreiben und Auswendiglernen von Syntax sind keine Voraussetzung.

Vor einer Aufgabe bestimmen wir das aktive Vorhaben und den nächsten überprüfbaren Schritt. Andere Bereiche bleiben unberührt, sofern ihre Beteiligung nicht ausdrücklich vereinbart wird. Liefermodus ist auf ausdrücklichen Wunsch möglich.

**Ausgelagert (30.10.2026):** Liefer-Vorhaben liegen nicht mehr hier. `sales_learning/` ist jetzt das private Repo [`zimfelix/sales-training`](https://github.com/zimfelix/sales-training) (lokal `~/Code/sales-training`, mit Historie); `lead-finder/` ist als Prototyp „Büroautomatisierung“ nach [`zimfelix/leadfinder`](https://github.com/zimfelix/leadfinder) unter `prototypes/bueroautomatisierung-jobsuche/` umgezogen. Die Sandbox enthält nur noch Lernvorhaben.

## Regeln und Dokumentation

- Repositorybezogen: [AGENTS.md](AGENTS.md) ergänzt die globalen Arbeitspräferenzen um gemeinsame Sandbox-Lernregeln.
- Vorhabensbezogen: Die jeweilige README erklärt Ziel, Stand und Ausführung; zusätzliche lokale `AGENTS.md`-Dateien enthalten nur besondere Regeln.
- Lernstand: zentral in [learning-state.md](learning-state.md) für die Lernvorhaben, Themen als neu oder gefestigt markiert; Aktualisierung nur auf Auftrag. Keine automatische globale Übernahme oder Vault-Synchronisation.
- Gemeinsame Git-Historie, getrennte Lernvorhaben: Änderungen sind auch pro Ordner nachvollziehbar. GitHub-Profilbeiträge hängen von den GitHub-Bedingungen für Commits ab, nicht allein von Dateiänderungen.
- Commit und Push erfolgen ausschließlich auf ausdrücklichen Auftrag. Echte Daten, Anbieterzugriffe und Hintergrunddienste benötigen eine gesonderte Freigabe.
