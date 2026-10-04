# Python-Lernkarten

Editierbare Referenz für Felix’ visuelles Lernboard. Diese Karten sind Erklärungen, kein Nachweis von Beherrschung. Codeblöcke sind einzelne Lesebeispiele und kein zusammenhängendes Programm; Namen wie `path`, `game` oder `text` setzen passende Objekte voraus. Fachbegriffe: Englisch, deutsche Bedeutung in Klammern. Merkregeln vereinfachen bewusst.

## Board-Struktur

- A · Python Basics: A1–A4
- B · Objects: B1–B4 (B3 und B4 zunächst als „Später“ gruppieren)
- C · Data & Files: C1–C4

Farben optional: A gelb, B blau, C grün. Zwischen Gruppen Platz lassen. Verbindungslinien zunächst nur innerhalb einer Gruppe; zusätzliche Querverbindungen erst bei Bedarf. Screenshots dienen als Ansicht, diese Datei als korrigierbare Quelle.

## A1 · Variable & Constant

Variable (Variable): Ein Name, der an ein Objekt gebunden ist.

```python
provider = "claude"
```

- `provider`: variable name (Variablenname)
- `"claude"`: value (Wert)
- `=`: assignment (Zuweisung)

**Merkregel: `=` bindet einen Namen an ein Ergebnis.**

```python
MAX_ATTEMPTS = 5
```

Constant (Konstante): Soll nicht neu zugewiesen werden. Großschreibung ist eine Konvention; Python erzwingt diese Regel nicht.

## A2 · Attribute Access & Call

Attribute access (Attributzugriff): Bei einem Objekt etwas nachschlagen.

```python
path.parent       # Property lesen
path.resolve      # Methode abrufen
path.resolve()    # Methode aufrufen
```

**Merkregel: Der Punkt greift zu; nachgestellte Klammern rufen auf.**

Ein attribute (Attribut) kann einen Wert oder eine Methode liefern. Eine method (Methode) ist eine Funktion, die einem Objekt bzw. seiner Klasse zugeordnet ist.

```python
print("Hallo")    # function call (Funktionsaufruf)
text.upper()     # method call (Methodenaufruf)
```

Nur callable objects (aufrufbare Objekte) können aufgerufen werden. Klammern zum Gruppieren, etwa `(2 + 3) * 4`, sind kein Aufruf.

## A3 · Parameter & Argument

Parameter (Parameter): Platzhalter in der Funktionsdefinition.
Argument (Argument): Konkrete Übergabe beim Aufruf.

```python
def show_provider(provider):
    print(provider)

show_provider("claude")
```

- `provider`: Parameter
- `"claude"`: Wert, beim Aufruf als Argument übergeben

**Merkregel: Parameter nimmt entgegen; Argument wird übergeben.**

```python
def show_provider(provider="claude"):
    print(provider)
```

Default value (Standardwert): Wird verwendet, wenn das Argument fehlt.

## A4 · Expression & Statement

Expression (Ausdruck): Ergibt einen Wert.
Statement (Anweisung): Ein vollständiger Arbeitsschritt.

```python
total = 2 + 3
```

- `2 + 3`: expression → ergibt `5`
- Ganze Zeile: assignment statement (Zuweisungsanweisung)

**Merkregel: Ausdruck liefert etwas; Anweisung macht einen Schritt.**

```python
def main():
    print("Hallo")

main()
```

`def` definiert die Funktion; `main()` ruft sie auf.

## B1 · Class & Object

```python
from pathlib import Path

path = Path("data/usage.json")
```

- `Path`: class (Klasse)
- `Path(...)`: Aufruf, der ein object (Objekt) erzeugt
- Das Objekt ist eine instance (Instanz) einer passenden Path-Klasse.
- `path`: Name für dieses Objekt

**Merkregel: Klasse = Bauplan; Objekt = konkretes Exemplar.**

## B2 · Property

Property (Eigenschaft): Zugriff wie auf einen Wert; intern kann Code ausgeführt werden.

```python
path.parent
```

Eigene Property innerhalb einer Klasse:

```python
@property
def remaining_attempts(self):
    return self.max_attempts - self.used_attempts
```

Verwendung: `game.remaining_attempts`

**Merkregel: Ergebnis lesen, ohne Aufrufklammern.**

Properties sind nicht zwingend nur lesbar; ein Setter kann Zuweisungen ermöglichen.

## B3 · Method Types

Diese Definitionen gehören innerhalb einer Klasse:

```python
def reset(self):
    ...

@classmethod
def from_random_word(cls):
    ...

@staticmethod
def is_valid_letter(letter):
    return len(letter) == 1
```

- Instance method (Instanzmethode): Erhält das Objekt als `self`.
- Class method (Klassenmethode): Erhält die Klasse als `cls`.
- Static method (statische Methode): Erhält keines von beiden automatisch.

**Merkregel: `self` = dieses Objekt; `cls` = diese Klasse; static = zugehörige Hilfsfunktion.**

`self` und `cls` sind konventionelle Parameternamen, keine Schlüsselwörter.

## B4 · Dataclass & Inheritance

```python
from dataclasses import dataclass

@dataclass
class Measurement:
    provider: str
    amount: float
```

Dataclass (Datenklasse): Erzeugt standardmäßig unter anderem `__init__`, `__repr__` und `__eq__`. Eigene Methoden sind weiterhin möglich.

**Merkregel: Daten zusammenhalten, Schreibarbeit sparen.**

```python
class Hangman(Game):
    pass
```

Inheritance (Vererbung): `Hangman` erbt von `Game`.

**Merkregel: In der Klassendefinition stehen Basisklassen in den Klammern.**

## C1 · Collections & Subscription

```python
["a", "b"]             # list (Liste): veränderbar
("a", "b")             # tuple (Tupel): Einträge nicht ersetzbar
{"provider": "claude"} # dict (Dictionary): Schlüssel → Wert
{"a", "b"}             # set (Menge): keine Duplikate
```

Listen und Tupel sind geordnet. Sets haben keine garantierte Reihenfolge. Ein Tupel kann veränderbare Objekte enthalten.

```python
measurement["provider"]
```

Subscription (Indexzugriff): Einen Eintrag holen.

**Merkregel: `.` greift auf Attribute zu; `[]` auf Einträge.**

## C2 · JSON

JSON: Strukturiertes Textformat, kein Python-Datentyp.

```text
{} JSON object → Python dict
[] JSON array  → Python list
```

```python
json.load(file)        # Datei → Python-Daten
json.loads(text)       # String → Python-Daten
json.dump(data, file)  # Python-Daten → Datei
json.dumps(data)       # Python-Daten → String
```

**Merkregel: `s` steht für string.**

JSON → Python: deserialization (Deserialisierung).
Python → JSON: serialization (Serialisierung).

Zum strukturierten Bearbeiten: einlesen → Python-Daten ändern → zurückschreiben. Andere Python-Funktionen können häufig direkt das Dictionary erhalten; JSON ist dafür nicht nötig. Manche APIs erwarten JSON, nicht alle.

## C3 · With & Paths

```python
with path.open(encoding="utf-8") as file:
    data = json.load(file)
```

Context management (Kontextverwaltung).

**Merkregel: Geordnet benutzen und anschließend aufräumen.**

- Datei: Anschließend schließen.
- SQLite-Verbindung: Commit oder Rollback für eine offene Transaktion; die Verbindung wird nicht geschlossen.

```python
path.mkdir()           # Ordner erstellen
path.with_suffix(".db") # Neues Pfadobjekt mit anderer Endung
```

`with_suffix()` benennt keine Datei auf der Festplatte um.

## C4 · Built-ins

```python
isinstance(data, dict)
```

Built-in function (eingebaute Funktion): Hier prüfen, ob `data` ein Dictionary ist (einschließlich Unterklassen).

Built-in types (eingebaute Typen): `dict`, `int`, `str`, `tuple` …

Built-in exceptions (eingebaute Ausnahmen): `FileNotFoundError`, `ValueError`, `TypeError` …

```python
try:
    with path.open() as file:
        text = file.read()
except FileNotFoundError:
    print("Datei fehlt.")
```

**Merkregel: `try` versucht; `except` behandelt die benannte Ausnahme.**

## Verbindung zum aktuellen Projekt

```python
PROJECT_DIR = Path(__file__).resolve().parent
```

```text
__file__    → Pfad dieser Python-Datei
Path(...)   → Pfadobjekt erzeugen
.resolve()  → Absoluten, aufgelösten Pfad liefern
.parent     → Übergeordneten Ordner holen
=           → Ergebnis an PROJECT_DIR binden
```

Die gesamte rechte Seite ist eine expression (Ausdruck). Diese Zeile ermittelt den Ordner; sie liest keinen Dateiinhalt.

Sinnvolle spätere Querverbindungen: A2 ↔ B2 (Property-Zugriff), A3 ↔ B3 (self/cls als Parameter), C2 ↔ C1 (JSON wird zu Python-Daten).
