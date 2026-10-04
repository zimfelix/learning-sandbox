---
cssclasses:
  - learning-card
---
![[Bilder/Objects/Property.svg]]

# Property

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

Thema: [[Objects]]
