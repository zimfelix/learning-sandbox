---
cssclasses:
  - learning-card
---
![[Bilder/Code Examples/Projektordner ermitteln.svg]]

# Projektordner ermitteln

**Merkregel: Rechts auswerten → Ergebnis links an einen Namen binden.**

Diese Zeile steht in `learning-sandbox/main.py`:

```python
PROJECT_DIR = Path(__file__).resolve().parent
```

| Bestandteil | Einordnung |
|---|---|
| `PROJECT_DIR` | variable name (Variablenname), nach Konvention eine constant (Konstante) |
| `=` | assignment (Zuweisung) |
| `Path` | class (Klasse) |
| `__file__` | variable (Variable) mit dem Pfad dieser Python-Datei |
| `Path(__file__)` | Klassenaufruf, der ein Path-object (Pfadobjekt) erzeugt |
| `.resolve()` | attribute access (Attributzugriff) und method call (Methodenaufruf) |
| `.parent` | attribute access (Attributzugriff) auf eine property (Eigenschaft) |
| gesamte rechte Seite | expression (Ausdruck) |

```text
Pfad dieser Python-Datei
    → Pfadobjekt erzeugen
    → absoluten, aufgelösten Pfad liefern
    → übergeordneten Ordner holen
    → Ergebnis an PROJECT_DIR binden
```

**Diese Zeile liest keinen Dateiinhalt.** Die Großschreibung verhindert keine spätere Neuzuweisung.

Thema: [[Code Examples]]
