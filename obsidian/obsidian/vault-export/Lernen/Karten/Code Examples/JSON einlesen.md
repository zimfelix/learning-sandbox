---
cssclasses:
  - learning-card
---
![[Bilder/Code Examples/JSON einlesen.svg]]

# JSON einlesen

**Merkregel: Datei öffnen → JSON einlesen → Datei schließen.**

Dieser Ausschnitt steht innerhalb von `main()` in `learning-sandbox/main.py`:

```python
with data_path.open(encoding="utf-8") as file:
    measurement = json.load(file)
```

| Bestandteil | Einordnung |
|---|---|
| `data_path` | variable name (Variablenname), gebunden an ein Path-object (Pfadobjekt) |
| `.open(...)` | method call (Methodenaufruf) |
| `encoding="utf-8"` | keyword argument (benanntes Argument): Name `encoding`, Wert `"utf-8"` |
| `with` | context management (Kontextverwaltung) |
| `as file` | name binding (Namensbindung): geöffnetes Dateiobjekt als `file` verfügbar machen |
| `json` | module (Modul) |
| `.load` | attribute access (Attributzugriff), hier auf eine Funktion im Modul |
| `json.load(file)` | function call (Funktionsaufruf), keine Objektmethode |
| `file` im Aufruf | argument (Argument) |
| `measurement = ...` | assignment (Zuweisung) des zurückgegebenen Ergebnisses |

**Wichtig:** Nicht jedes `=` bedeutet eine normale Zuweisung. Im Aufruf benennt `encoding=` ein Argument.

```text
JSON-Datei auf der Festplatte
    → Dateiobjekt öffnen
    → json.load(file)
    → Python-Dictionary erhalten
    → Ergebnis an measurement binden
```

Unser Beispiel-JSON enthält ein Objekt, deshalb erhalten wir ein Dictionary. Andere JSON-Werte können andere Python-Datentypen ergeben. Beim Verlassen dieses `with`-Blocks wird die Datei geschlossen.

Thema: [[Code Examples]]
