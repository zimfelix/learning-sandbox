---
cssclasses:
  - learning-card
---
![[Bilder/Data & Files/JSON.svg]]

# JSON

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

Thema: [[Data & Files]]
