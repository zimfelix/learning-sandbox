# Learning State – Learning Sandbox

Übersicht über alle bisher besprochenen Themen, projektübergreifend. Stand: 2026-10-22.

**Status:**
- **neu** – kurz angesprochen oder noch nicht begonnen, z. B. SQL/SQLite und seine Besonderheiten.
- **gefestigt** – in Arbeit: in den Lernkarten (`obsidian/python-basics.md`) erarbeitet, z. B. Python-Grundlagen und Objekte. Das heißt **nicht** verinnerlicht: Alles ist noch wackelig und soll weiter aufgegriffen und wiederholt werden.

Quellen: `obsidian/python-basics.md`, `SQL_learning/README.md`, Felix’ Stickies-Notizen, global (Claude Code) `~/.claude/CLAUDE.md`.

## Lernanspruch (Stand 2026-10-19)

Ziel ist **Agentic Coding auf Review-Niveau**, kein Vibe Coding: Agents schreiben den Code, Felix versteht ihn, findet Fehler und kann ihn beurteilen. Hintergrund: Büro- und Softwareautomatisierung für die eigene Firma.

- **Python und SQL:** Basics sicher lesen und erklären können, einfache Abfragen bzw. Code am besten auch selbst schreiben. Profi-Niveau ohne Agents ist nicht das Ziel.
- **Vorgehen:** Basics nicht vorab „abhaken“, sondern möglichst an realistischen Fällen lernen (z. B. Kunden, Rechnungen, offene Posten) und dabei Agentencode reviewen.
- **Nächster Schritt – SQL-Kern:** `SELECT`/`WHERE`/`ORDER BY`, `JOIN` (was wird verbunden, was fällt weg), `GROUP BY` mit `COUNT`/`SUM`, `INSERT`/`UPDATE`/`DELETE` (fehlt das `WHERE`?), Tabellen mit Primary/Foreign Key. Dazu Orientierung: Wo liegt die Datenbank, wie öffnet man sie, Konsole vs. Datenbank-Tool.
- Kann warten: Window Functions, Performance-Tuning, Stored Procedures, komplexe Subqueries.

## Python-Grundlagen

| Thema | Kern | Status |
|---|---|---|
| Variable & Constant | `=` bindet einen Namen an ein Objekt; KONSTANTEN nicht neu zuweisen | gefestigt |
| Attribute Access & Call | `.` greift auf ein Attribut zu, `()` ruft auf; eine Methode ist ein aufrufbares Attribut | gefestigt |
| Parameter & Argument | Parameter = Platzhalter in `def`, Argument = konkrete Übergabe | gefestigt |
| Expression & Statement | Expression liefert einen Wert, Statement führt eine Anweisung aus | gefestigt |
| Function vs. Method Call | `show_provider("claude")` vs. `text.upper()` | gefestigt |
| Built-ins | `len()`, `isinstance()`, `type()` usw. | gefestigt |

## Objekte und Klassen

| Thema | Kern | Status |
|---|---|---|
| Class & Object | `game = Hangman("python")`: `game` ist ein Name für eine instance | gefestigt |
| `__init__` & Default Parameter | `def __init__(self, word, tries=5)`; `self.word = word` macht den Wert zum Attribut | gefestigt |
| `@property` | Zustand lesen ohne `()`, z. B. `game.remaining_attempts`, `path.parent` | gefestigt |
| `@staticmethod` / `@classmethod` | kein `self` (Hilfslogik) / bekommt `cls` (z. B. `Hangman.from_random_word()`) | gefestigt |
| `@dataclass` | erzeugt `__init__`, `__repr__`, `__eq__`; für reine Datenobjekte | gefestigt |
| Inheritance | `class Hangman(Game)` erbt von `Game` | gefestigt |

## Daten und Dateien

| Thema | Kern | Status |
|---|---|---|
| Collections | list (veränderbar), tuple (unveränderbar), dict (Schlüssel-Wert), set (ohne Duplikate) | gefestigt |
| JSON | `load` (Datei) / `loads` (String): Text → Python; Object→`dict`, Array→`list`, Number→`int`/`float`, null→`None` | gefestigt |
| `with` & Paths | context manager öffnet und schließt sicher; `with_suffix()` liefert einen neuen Pfad, benennt nichts um | gefestigt |
| Error Handling | `try/except` für `FileNotFoundError`, `JSONDecodeError`, `PermissionError`, `OSError`, `TypeError` | neu |
| Validation | `isinstance()`, `is None`, `dict.get()`, `len()`, `isalpha()`; fachliche Fehler selbst prüfen | neu |
| Atomic Write | erst in eine temporäre Datei schreiben, dann `Path.replace()`: alles oder nichts | neu |
| Speicheroptionen | JSON (verschachtelt) · CSV (Tabellen) · SQLite (viele Datensätze, Abfragen) · SQL = Sprache | neu |
| SQLite | praktisch begonnen, siehe Abschnitt „SQL“ | neu |

## SQL (Stand 2026-10-22)

Übungen in `SQL_learning/tutorial/`, Aufbau je Etappe: A vorhersagen · B selbst schreiben · C Fehler finden (Review).

| Thema | Kern | Status |
|---|---|---|
| Werkzeug | `.sql` = Text (Skript), `.db` = binary file, nur über DB Browser/`sqlite3` öffnen; Konsole = ausprobieren, `.sql`-Datei = behalten | gefestigt |
| Skript vs. Abfragen-Sammlung | Skript ganz ausführen; einzelne Abfragen per Cursor + ⌘↩. execute (ausführen) ≠ commit | neu |
| `PRIMARY KEY`, `DROP`/`CREATE` | doppelte ID → constraint violation, kein Ersetzen; `DROP`+`CREATE`+`INSERT` = Reset-Skript | neu |
| Transaction | `BEGIN`/`COMMIT` = alles oder nichts; schützt nur, wenn bei Fehler auch Rollback passiert | neu |
| Etappe 1: `SELECT`/`WHERE`/`ORDER BY` | `etappe1_select.sql` abgeschlossen. `WHERE` streicht Zeilen, `SELECT` Spalten; `AND` prüft pro Zeile, jede condition vollständig; `NOT`/`!=`/`NOT IN` zum Ausschließen; Komma zählt auf, verbindet keine conditions | gefestigt |
| Etappe 2: `COUNT`/`SUM`/`GROUP BY`/`HAVING` | `etappe2_aggregate.sql` **in Arbeit**: Teil A gelesen (A1, A3, A4 beantwortet), B und C offen. Kern: `GROUP BY` bildet die Gruppen, aggregate function rechnet pro Gruppe; `AS` = alias, nur Name | neu |
| Foreign Key + `JOIN` | `bond_fk.sql` vorbereitet, noch nicht bearbeitet | neu |
| Noch offen | `INSERT`/`UPDATE`/`DELETE` (fehlendes `WHERE`), größere Datenbank erkunden, CTE (`WITH`) | neu |

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
- Bei SQL: `'Text'` = Wert, `"Name"` = Spalte/Tabelle; Text-Vergleiche unterscheiden Groß-/Kleinschreibung; fehlendes Komma macht still einen alias.
- `COUNT(*)` zählt Zeilen der aktuellen Gruppe; „pro Schauspieler“ entsteht erst durch `GROUP BY`, nicht durch `SELECT`.
