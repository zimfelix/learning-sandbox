# Obsidian-Lernkarten: bestätigte Vorlage

Diese Gestaltung wurde von Felix für Lernkarten gewählt. Neue Karten in learning-sandbox nach diesem Muster erstellen, aber **nur nach ausdrücklicher Absprache**. Kein Automatismus und keine globale Übernahme.

## Kurzer Ablauf

1. Neues Thema: Ist eine kurze Nachschlagekarte sinnvoll? Bei Bedarf anbieten und Freigabe abwarten.
2. Nach Freigabe: Merkregel und echtes bzw. konkretes Codebeispiel klären; Notiz und SVG nach Vorlage erstellen.
3. Themenknoten verlinken, passende Gruppenfarbe verwenden und die Hover-Vorschau prüfen.
4. Spätere Korrekturen in Text und Bild gemeinsam vornehmen. Export/Commit/Push nur auf Auftrag, nicht automatisch.

## Aufbau

- Dateiname, Hauptüberschrift und Bildtitel stimmen überein; keine technischen Nummern im Graph-Titel.
- Oben ein eingebettetes SVG-Vorschaubild, darunter der editierbare Markdown-Text.
- Eine kurze Merkregel und konkrete, fachlich korrekte Beispiele; Fachbegriffe Englisch zuerst, Deutsch in Klammern.
- SVG statt niedrig aufgelöster Screenshots: Schrift bleibt beim Vergrößern scharf. SVGs sind gestaltete Vorschau-Bilder, keine PyCharm-Screenshots.
- Dunkler Hintergrund `#181c23`, helle Schrift, farbiger Titel und schmaler Farbstreifen links. Syntaxfarben dienen nur der Lesbarkeit.
- Nur diese Karten bekommen `cssclasses: [learning-card]`. Das CSS blendet Properties aus und zeigt im Hover nur den ersten Bildabsatz. Beim Öffnen bleibt der Erklärungstext sichtbar.
- Markdown: `Lernen/Karten/<Thema>/<Titel>.md`; Bilder: `Bilder/<Thema>/<Titel>.svg`.
- Themenknoten in `Lernen/Übersichten/` enthalten nützliche Links, keine leeren Platzhalter. Zusätzliche allgemeine Lernübersicht ist derzeit nicht nötig.
- Graph-Farben: Themenknoten cyan, Basics gelb, Objects violett, Data & Files grün, Code Examples orange. Graph-Positionen sind dynamisch. Verbindungsabstand und Abstoßung steuern die räumliche Trennung.
- Neue Anhänge landen in `Bilder/`. Vorhandene Inhalte nicht endgültig löschen; Änderungen prüfen und bei Bedarf sichern.

## Wiederverwenden

1. `templates/learning-card.md` als Notizvorlage nehmen. Sie ist auch im lokalen Vault unter `Vorlagen/Lernkarte.md` verfügbar. Obsidian ersetzt `{{title}}`; Thema, Erklärung und Beispiel werden manuell ausgefüllt.
2. Eine Vorschau als JSON mit `title`, `accent` und `lines` anlegen. Zeilentypen: `title`, `muted`, `text`, `rule`, `code`, `gap`.
3. SVG erzeugen:

```bash
python3 notes/obsidian/render-preview.py card.json /pfad/zur/vorschau.svg
```

Der Renderer überschreibt bestehende Dateien nur mit `--overwrite`. Inhalt und Bild müssen gemeinsam aktualisiert werden; SVG ist eine Ansicht, Markdown bleibt editierbar. Lange Inhalte nicht durch winzige Schrift passend machen, sondern kürzen oder in Karten teilen.

4. `learning-card-preview.css` in `.obsidian/snippets/` ablegen und in Obsidian aktivieren.
5. Vorschau und vollständige Notiz prüfen: SVG geladen, keine Properties im Hover, keine abgeschnittenen Zeilen, Links aufgelöst.

Kein Community-Plugin nötig. Obsidian Page preview und die offizielle CLI reichen aus.

## Export und Wiederherstellung

`vault-export/` ist eine ausdrücklich erstellte Momentaufnahme der Lernkarten, nicht der gesamten privaten Notizensammlung. Enthalten sind Markdown-Notizen, SVGs, Vorlage, CSS sowie ausgewählte Graph-/Ablageeinstellungen. Die bearbeitbaren SVG-Quelldaten liegen zusätzlich unter `previews/`.

Zum Wiederherstellen den Export als eigenen Vault öffnen oder seine Inhalte nach Prüfung in einen vorhandenen Vault übernehmen; vorhandene Dateien nicht blind überschreiben. Page preview aktivieren und das CSS-Snippet `learning-card-preview` einschalten. Die enthaltenen `.obsidian`-Einstellungen nicht ungeprüft über bestehende persönliche Einstellungen kopieren.

Lokaler Vault und Export werden **nicht automatisch synchronisiert**. Die Notizen im lokalen Vault sind während der Arbeit die aktuelle Fassung; Export und SVG-Quelldaten nur im beauftragten Schritt nachziehen.
