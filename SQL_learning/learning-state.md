# Learning State – SQL-Lernen

Zwischenspeicher für Lernstand und offene Erkenntnisse. **Behandelt ≠ beherrscht**: Alle Punkte gelten als *offen*, bis sie gemeinsam geprüft wurden (z. B. durch Erklären eines Verhaltens am Code).

Quellen (Stand 2026-10-09): `README.md` dieses Vorhabens, `../obsidian/python-basics.md` (Lernkarten A–C), Felix’ Stickies-Notizen, global (Claude Code) `~/.claude/CLAUDE.md`.

## Vorwissen: Python-Grundlagen (offen)

Aus den Lernkarten `../obsidian/python-basics.md` und den Notizen:

- **A · Basics:** variable vs. constant (`MAX_ATTEMPTS` nicht neu zuweisen), attribute access (`game.word`) vs. call (`game.guess("a")`), parameter (Platzhalter in `def`) vs. argument (konkrete Übergabe), expression vs. statement.
- **B · Objects:** class & object (`game = Hangman("python")`), `@property` (Zustand lesen ohne `()`), `@staticmethod` (kein `self`, Hilfslogik), `@classmethod` (bekommt `cls`, z. B. `Hangman.from_random_word()`), `@dataclass` (erzeugt `__init__`, `__repr__`, `__eq__`), inheritance (`class Hangman(Game)`), default parameter in `__init__`.
- **C · Data & Files:** list / tuple / dict / set, JSON, `with` (context manager: Ressource öffnen und sicher schließen), `pathlib` (`path.parent`, `with_suffix()` liefert neuen Pfad und benennt keine Datei um), built-ins.

## JSON und Datenfluss (offen)

- `json.load()` liest eine Datei, `json.loads()` einen String: Text → Python-Objekte.
- Zuordnung: Object → `dict`, Array → `list`, String → `str`, Number → `int` **oder `float`**, Boolean → `bool`, null → `None`.
- Begriffe: JSON = data format, CLI/HTTP-API = interface, SQLite = database storage. UI: Mensch ↔ Programm; API: Programm ↔ Programm.

## Fehlerbehandlung und Validierung (offen)

- Erwartbare Fehler: `FileNotFoundError`, `json.JSONDecodeError`, `PermissionError`, `OSError`, `TypeError`; fachliche Fehler eigenständig prüfen (z. B. `ValueError` auslösen).
- Prüfwerkzeuge: `isinstance()`, `is None`, `dict.get()`, `len()`, `str.isalpha()` / `isdigit()`.
- Atomic write (atomares Schreiben): in eine temporäre Datei schreiben, dann `Path.replace()`; die Zieldatei ist entweder ganz alt oder ganz neu.

## Speicheroptionen (offen)

JSON (verschachtelt, Austausch) · CSV (Tabellen) · SQLite (viele Datensätze, Suchen, Filtern, dauerhaft) · SQL = Abfragesprache, nicht die Datenbank selbst.

## Präzisierungen aus den Notizen

| Notiz | Präzise Fassung |
|---|---|
| „attribute = etwas, das ich aufrufen kann, durch `()` oder `.`“ | `.` = attribute access (Zugriff); `()` = call (Aufruf). Eine Methode ist ein aufrufbares Attribut, nicht jedes Attribut ist aufrufbar. |
| „Value wird zum attribute, wenn wir ihn einem Aufruf übergeben“ | Beim Übergeben wird ein Wert zum **argument**. Zum Attribut wird er erst durch Zuweisung, z. B. `self.word = word`. |
| „`game` = Wert“ | `game` ist ein **Name** (Variable), gebunden an ein Objekt (instance) von `Hangman`. |
| „`type(value) == …`“ | `type(x) is dict` prüft exakt; `isinstance(x, dict)` erlaubt auch Unterklassen und ist meist vorzuziehen. |

## Harness-Themen (offen)

- `harness/` regelt die Arbeit des Agenten aufgabenübergreifend, `docs/` enthält projektspezifisches Wissen; stabiler Core plus Project Profile (bestätigt global).
- Agent-Isolation (2026-10-09): Computer Use teilt Maus, Tastatur und Fokus. Gegenmittel: Browser-Automation über DevTools Protocol, VM oder Container (z. B. Cua). Ungeprüft, nicht live recherchiert.

## Nächster Lernschritt

SQLite einführen: `sample_usage.json` → Python → Tabelle in SQLite → erste `SELECT`-Abfrage.
