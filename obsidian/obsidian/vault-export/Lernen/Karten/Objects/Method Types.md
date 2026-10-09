---
cssclasses:
  - learning-card
---
![[Bilder/Objects/Method Types.svg]]

# Method Types

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

Thema: [[Objects]]
