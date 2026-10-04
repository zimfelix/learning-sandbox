---
cssclasses:
  - learning-card
---
![[Bilder/Python Basics/Parameter & Argument.svg]]

# Parameter & Argument

**Merkregel: Parameter nimmt entgegen; Argument wird übergeben.**

## Parameter (Parameter) und Argument (Argument)

Parameter: Platzhalter in der Funktionsdefinition.
Argument: konkrete Übergabe beim Aufruf.

```python
def show_provider(provider):
    print(provider)

show_provider("claude")
```

- `provider` → parameter (Parameter)
- `"claude"` → value (Wert), beim Aufruf als argument (Argument) übergeben

## Default value (Standardwert)

```python
def show_provider(provider="claude"):
    print(provider)

show_provider()  # verwendet "claude"
```

Der Standardwert wird verwendet, wenn das Argument fehlt.

Thema: [[Python Basics]]
