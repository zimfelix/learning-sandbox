---
cssclasses:
  - learning-card
---
![[Bilder/Python Basics/Attribute Access & Call.svg]]

# Attribute Access & Call

**Merkregel: Der Punkt greift zu; nachgestellte Klammern rufen auf.**

## Attribute access (Attributzugriff)

Bei einem Objekt etwas nachschlagen.

```python
from pathlib import Path

path = Path("data/usage.json")
path.parent       # Property lesen
path.resolve      # Methode abrufen
path.resolve()    # Methode aufrufen
```

Ein attribute (Attribut) kann einen Wert oder eine Methode liefern. Eine method (Methode) ist eine Funktion, die einem Objekt bzw. seiner Klasse zugeordnet ist.

## Call (Aufruf)

```python
print("Hallo")    # function call (Funktionsaufruf)
text = "claude"
text.upper()      # method call (Methodenaufruf)
```

Nur callable objects (aufrufbare Objekte) lassen sich aufrufen. `(2 + 3) * 4` ist dagegen eine Gruppierung, kein Aufruf.

Thema: [[Python Basics]]
