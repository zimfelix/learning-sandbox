---
cssclasses:
  - learning-card
---
![[Bilder/Data & Files/With & Paths.svg]]

# With & Paths

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

Thema: [[Data & Files]]
