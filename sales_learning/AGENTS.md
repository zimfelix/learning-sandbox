# Sales Learning – Agentenanweisungen

Ergänzt die repositorybezogene `AGENTS.md` im Root. Abweichend vom Sandbox-Standard gilt hier **Liefermodus (shipping mode)**: Ziel ist eine vollständige, saubere Auswertung, keine Lernsession. Keine Lernfragen, keine Drei-Phasen-Begleitung; Abwägungen und Korrekturen trotzdem knapp benennen.

**Eigenständiges Vorhaben:** unabhängig von `SQL_learning/`, `obsidian/` und `lead-finder/`. Wer hier arbeitet, fasst diese Ordner nicht an; die Root-`learning-state.md` (SQL-/Python-Lernstand) ist für dieses Vorhaben nicht relevant.

## Vor dem Start lesen

- `sales_learning/README.md` vollständig – vor allem **„Was aus den Videos herausgezogen wird“** (Typen, Phasen K/T/A, Zielgruppe, Format) und **„Einstieg für einen neuen Chat“** (Befehle, Ablauf, bisherige Fehler).
- `mahnken-videos/notes.js` überfliegen, um Stil und bereits erfasste Formulierungen zu kennen.

## Feste Regeln

- Jedes Transkript **vollständig** lesen; kein Vorfiltern per Stichwort.
- Ziel ist ein Gesprächsskript für Handwerksbetriebe – nur Verwertbares aufnehmen. Ausgewertet werden die in `mahnken-videos/auswahl.js` grün markierten Videos, neueste zuerst (`fetch.py --next` wählt sie automatisch); Segment `seg` (Handwerk/KMU/Großunternehmen/Privat/allgemein) setzen; Fokus Handwerk und KMU. Jedes Learning muss einem Baustein aus „Ziel-Skript“ (README) dienen; Planung/Motivation/Adressen als `Organisation`, nicht als `Prinzip`.
- Pro Paket 5 Videos (`fetch.py --next 5`); Ergebnisse direkt in `mahnken-videos/notes.js`, danach Ladeprüfung mit `node`.
- Julians eigene Empfehlung klar von der des besprochenen Trainers trennen.
- Wörtliche Zitate nicht erfinden oder glätten; bei schlechten Untertiteln `s: 1` (sinngemäß).
- Transkripte bleiben lokal (`.gitignore`); Commit und Push nur auf ausdrücklichen Auftrag.
- Im Chat pro Paket kurz berichten: neue 👀-Empfehlungen, stärkste Formulierungen, Korrekturen.
