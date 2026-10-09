---
cssclasses:
  - learning-card
---
![[Bilder/Objects/Dataclass & Inheritance.svg]]

# Dataclass & Inheritance

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

Thema: [[Objects]]
