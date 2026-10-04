---
cssclasses:
  - learning-card
---
![[Bilder/Data & Files/Built-ins.svg]]

# Built-ins

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

Thema: [[Data & Files]]
