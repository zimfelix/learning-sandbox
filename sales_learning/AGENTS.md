# Sales Learning – Agentenanweisungen

Ergänzt die repositorybezogene `AGENTS.md` im Root. Abweichend vom Sandbox-Standard gilt hier **Liefermodus (shipping mode)**: Ziel ist eine vollständige, saubere Auswertung, keine Lernsession. Keine Lernfragen, keine Drei-Phasen-Begleitung; Abwägungen und Korrekturen trotzdem knapp benennen.

**Eigenständiges Vorhaben:** unabhängig von `SQL_learning/`, `obsidian/` und `lead-finder/`. Wer hier arbeitet, fasst diese Ordner nicht an; die Root-`learning-state.md` (SQL-/Python-Lernstand) ist für dieses Vorhaben nicht relevant.

## Vor dem Start lesen

- `sales_learning/README.md` vollständig – vor allem **„Was aus den Videos herausgezogen wird“** (Typen, Phasen K/T/A, Zielgruppe, Format) und **„Einstieg für einen neuen Chat“** (Befehle, Ablauf, bisherige Fehler).
- `mahnken-videos/notes.js` überfliegen, um Stil und bereits erfasste Formulierungen zu kennen.

## Feste Regeln

- Jedes Transkript **vollständig** lesen; kein Vorfiltern per Stichwort.
- Ziel ist ein Gesprächsskript für Handwerksbetriebe – nur Verwertbares aufnehmen. Ausgewertet werden die in `mahnken-videos/auswahl.js` grün markierten Videos, neueste zuerst (`fetch.py --next` wählt sie automatisch). Videos ab 1.12.2025 sind immer grün (Prüfung per Transkript); ältere nur nach Titel eingeteilt – neue Kanal-Videos daher grün eintragen; Segment `seg` (Handwerk/KMU/Großunternehmen/Privat/allgemein) setzen; Fokus Handwerk und KMU. Jedes Learning muss einem Baustein aus „Ziel-Skript“ (README) dienen; Planung/Motivation/Adressen als `Organisation`, nicht als `Prinzip`.
- Pro Paket 5 Videos (`fetch.py --next 5`); Ergebnisse direkt in `mahnken-videos/notes.js`, danach Ladeprüfung mit `node`.
- Julians eigene Empfehlung klar von der des besprochenen Trainers trennen.
- Wörtliche Zitate nicht erfinden oder glätten; bei schlechten Untertiteln `s: 1` (sinngemäß).
- Transkripte bleiben lokal (`.gitignore`); Commit und Push nur auf ausdrücklichen Auftrag.
- Im Chat pro Paket kurz berichten: neue 👀-Empfehlungen, stärkste Formulierungen, Korrekturen.
- 👀 sparsam vergeben: nur wenn Tonfall/Timing entscheidend ist oder der Wortlaut in den Untertiteln unverständlich bleibt. Ausgewertete Videos mit 👀 oder 💎 bilden die **Anhör-Liste**; Ziel: höchstens 30–50 Videos. Alles andere gilt nach der Auswertung als erledigt.
- Erweist sich ein ausgewertetes Video als wenig lehrreich (nur Motivation/Organisation, reine Wiederholung, kein Skript-Beitrag), in `auswahl.js` auf `"r":"x"` setzen; dann erscheint es grau.
- **Arbeitskopie ist `~/Code/python/learning-sandbox`** (dort liegen die Transkripte). Der zweite Klon `~/Code/learning-sandbox` hinkt sonst hinterher: Startet ein Chat dort, zuerst `git pull` und nichts daraus veröffentlichen, solange er nicht auf dem neuesten Stand ist.
- **Gearbeitet und geprüft wird auf der claude.ai-Seite**, nicht lokal. Nach jeder Änderung an `notes.js`, `auswahl.js`, `dates.js`, `videos.js`, `kern.js`, `leitfaden.docx`/`leitfaden.js`/`leitfaden.pdf` oder `uebersicht.html` die Seite **neu veröffentlichen** (README, Abschnitt „Online-Seiten“), damit Felix und Demi denselben Stand sehen. Spätestens **vor jedem Commit** solcher Änderungen, und im Abschlussbericht die veröffentlichte Version nennen. 🎯 Veröffentlichen (Artifact publish) ≠ `git push`; ein Push ändert die Seite nicht.
- Vor dem Veröffentlichen kurz prüfen, ob die Online-Dateien neuer sind als die lokalen (Artifact `read` mit `paths`, dann `cmp`). Wenn ja, nicht überschreiben, sondern erst abgleichen.
- **Cloudflare ist außer Betrieb** (Build schlägt fehl): ignorieren. Aktive Online-Seite ist die claude.ai-Seite.
