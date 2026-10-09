# Learning State – Learning Sandbox

Übersicht über alle bisher besprochenen Themen, projektübergreifend. Stand: 2026-10-09.

**Status:**
- **neu** – einmal oder kurz behandelt, noch unsicher.
- **gefestigt** – mehrfach behandelt und in Notizen oder Karten festgehalten. Das heißt **nicht** verinnerlicht: Alles ist noch wackelig und soll weiter aufgegriffen und wiederholt werden.

Quellen: `obsidian/python-basics.md`, `SQL_learning/README.md`, Felix’ Stickies-Notizen, global (Claude Code) `~/.claude/CLAUDE.md`.

## Python-Grundlagen

| Thema | Kern | Status |
|---|---|---|
| Variable & Constant | `=` bindet einen Namen an ein Objekt; KONSTANTEN nicht neu zuweisen | gefestigt |
| Attribute Access & Call | `.` greift auf ein Attribut zu, `()` ruft auf; eine Methode ist ein aufrufbares Attribut | gefestigt |
| Parameter & Argument | Parameter = Platzhalter in `def`, Argument = konkrete Übergabe | gefestigt |
| Expression & Statement | Expression liefert einen Wert, Statement führt eine Anweisung aus | neu |
| Function vs. Method Call | `show_provider("claude")` vs. `text.upper()` | gefestigt |
| Built-ins | `len()`, `isinstance()`, `type()` usw. | neu |

## Objekte und Klassen

| Thema | Kern | Status |
|---|---|---|
| Class & Object | `game = Hangman("python")`: `game` ist ein Name für eine instance | gefestigt |
| `__init__` & Default Parameter | `def __init__(self, word, tries=5)`; `self.word = word` macht den Wert zum Attribut | neu |
| `@property` | Zustand lesen ohne `()`, z. B. `game.remaining_attempts`, `path.parent` | gefestigt |
| `@staticmethod` / `@classmethod` | kein `self` (Hilfslogik) / bekommt `cls` (z. B. `Hangman.from_random_word()`) | neu |
| `@dataclass` | erzeugt `__init__`, `__repr__`, `__eq__`; für reine Datenobjekte | neu |
| Inheritance | `class Hangman(Game)` erbt von `Game` | neu |

## Daten und Dateien

| Thema | Kern | Status |
|---|---|---|
| Collections | list (veränderbar), tuple (unveränderbar), dict (Schlüssel-Wert), set (ohne Duplikate) | gefestigt |
| JSON | `load` (Datei) / `loads` (String): Text → Python; Object→`dict`, Array→`list`, Number→`int`/`float`, null→`None` | gefestigt |
| `with` & Paths | context manager öffnet und schließt sicher; `with_suffix()` liefert einen neuen Pfad, benennt nichts um | neu |
| Error Handling | `try/except` für `FileNotFoundError`, `JSONDecodeError`, `PermissionError`, `OSError`, `TypeError` | neu |
| Validation | `isinstance()`, `is None`, `dict.get()`, `len()`, `isalpha()`; fachliche Fehler selbst prüfen | neu |
| Atomic Write | erst in eine temporäre Datei schreiben, dann `Path.replace()`: alles oder nichts | neu |
| Speicheroptionen | JSON (verschachtelt) · CSV (Tabellen) · SQLite (viele Datensätze, Abfragen) · SQL = Sprache | neu |
| SQLite | noch nicht praktisch begonnen, nächster Schritt in `SQL_learning/` | neu |

## Konzepte und Werkzeuge

| Thema | Kern | Status |
|---|---|---|
| UI vs. API | UI: Mensch ↔ Programm; API: Programm ↔ Programm | neu |
| Data Format / Interface / Storage | JSON / CLI-HTTP / SQLite: drei verschiedene Rollen | neu |
| Virtual Environment | `venv` pro Vorhaben, wird nicht eingecheckt | neu |
| Harness | `harness/` regelt Agentenarbeit, `docs/` das Projektwissen; stabiler Core + Project Profile | neu |
| Agent-Isolation | Computer Use teilt Maus, Tastatur und Fokus; Abhilfe über DevTools Protocol, VM oder Container (z. B. Cua). Nicht live recherchiert | neu |
| Frontend-Stack | TypeScript/TSX, React (UI-Struktur), Vite, HTML/CSS/JS, Browser; nur notiert | neu |

## Häufige Verwechslungen

- Attribut ≠ Aufruf: `.` = Zugriff, `()` = Aufruf.
- Ein übergebener Wert wird zum **argument**, zum Attribut erst durch `self.x = …`.
- `type(x) is dict` prüft exakt, `isinstance(x, dict)` erlaubt Unterklassen und ist meist vorzuziehen.
- *decomposition* (Zerlegung) statt *composition*.
