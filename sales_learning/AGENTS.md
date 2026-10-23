# Sales Learning – Agentenanweisungen

Ergänzt die repositorybezogene `AGENTS.md` im Root. Abweichend vom Sandbox-Standard gilt hier **Liefermodus (shipping mode)**: Ziel ist eine vollständige, saubere Auswertung, keine Lernsession. Keine Lernfragen, keine Drei-Phasen-Begleitung; Abwägungen und Korrekturen trotzdem knapp benennen.

## Vor dem Start lesen

- `sales_learning/README.md` vollständig – vor allem **„Was aus den Videos herausgezogen wird“** (Typen, Phasen K/T/A, Zielgruppe, Format) und **„Einstieg für einen neuen Chat“** (Befehle, Ablauf, bisherige Fehler).
- `mahnken-videos/notes.js` überfliegen, um Stil und bereits erfasste Formulierungen zu kennen.

## Feste Regeln

- Jedes Transkript **vollständig** lesen; kein Vorfiltern per Stichwort.
- Ziel ist ein Gesprächsskript für Handwerksbetriebe – nur Verwertbares aufnehmen. Priorität: Nr. 1–184 (letzte zwei Jahre), neueste zuerst; Handwerk-Bezug in `target` nennen.
- Pro Paket 5 Videos (`fetch.py --next 5`); Ergebnisse direkt in `mahnken-videos/notes.js`, danach Ladeprüfung mit `node`.
- Julians eigene Empfehlung klar von der des besprochenen Trainers trennen.
- Wörtliche Zitate nicht erfinden oder glätten; bei schlechten Untertiteln `s: 1` (sinngemäß).
- Transkripte bleiben lokal (`.gitignore`); Commit und Push nur auf ausdrücklichen Auftrag.
- Im Chat pro Paket kurz berichten: neue 👀-Empfehlungen, stärkste Formulierungen, Korrekturen.
