# Sales Learning – Agentenanweisungen

Ergänzt die repositorybezogene `AGENTS.md` im Root. Abweichend vom Sandbox-Standard gilt hier **Liefermodus (shipping mode)**: Ziel ist eine vollständige, saubere Auswertung, keine Lernsession. Keine Lernfragen, keine Drei-Phasen-Begleitung; Abwägungen und Korrekturen trotzdem knapp benennen.

**Eigenständiges Vorhaben:** unabhängig von `SQL_learning/`, `obsidian/` und `lead-finder/`. Wer hier arbeitet, fasst diese Ordner nicht an; die Root-`learning-state.md` (SQL-/Python-Lernstand) ist für dieses Vorhaben nicht relevant.

## Vor dem Start lesen

- `sales_learning/README.md` (Überblick, Ordnerstruktur, Ziel-Skript) und diese Datei vollständig – vor allem **„Was aus den Videos herausgezogen wird“** (Typen, Phasen K/T/A, Zielgruppe, Format) und **„Einstieg für einen neuen Chat“** (Befehle, Ablauf, bisherige Fehler).
- Aufteilung: `README.md` = für Menschen (was ist wo, wie hängt es zusammen); `AGENTS.md` = Arbeitsregeln und Abläufe für Agenten; `archiv/` = nur nachschlagen, nicht mehr pflegen; `ideen/` = offene Ideen, beim Review ansprechen.
- `mahnken-videos/notes.js` überfliegen, um Stil und bereits erfasste Formulierungen zu kennen.

## Feste Regeln

- Jedes Transkript **vollständig** lesen; kein Vorfiltern per Stichwort.
- Ziel ist ein Gesprächsskript für Handwerksbetriebe – nur Verwertbares aufnehmen. Ausgewertet werden die in `mahnken-videos/auswahl.js` grün markierten Videos, neueste zuerst (`fetch.py --next` wählt sie automatisch). Videos ab 1.12.2025 sind immer grün (Prüfung per Transkript); ältere nur nach Titel eingeteilt, dazu alles mit Bezug zu Handwerk; gelb markierte nur, wenn eine Skript-Lücke offen bleibt – neue Kanal-Videos daher grün eintragen; Segment `seg` (Handwerk/KMU/Großunternehmen/Privat/allgemein) setzen; Fokus Handwerk und KMU. Jedes Learning muss einem Baustein aus „Ziel-Skript“ (README) dienen; Planung/Motivation/Adressen als `Organisation`, nicht als `Prinzip`.
- Pro Paket 5 Videos (`fetch.py --next 5`); Ergebnisse direkt in `mahnken-videos/notes.js`, danach Ladeprüfung mit `node`.
- Julians eigene Empfehlung klar von der des besprochenen Trainers trennen.
- Wörtliche Zitate nicht erfinden oder glätten; bei schlechten Untertiteln `s: 1` (sinngemäß).
- Transkripte bleiben lokal (`.gitignore`); Commit und Push nur auf ausdrücklichen Auftrag.
- Im Chat pro Paket kurz berichten: neue 👀-Empfehlungen, stärkste Formulierungen, Korrekturen.
- 👀 sparsam vergeben: nur wenn Tonfall/Timing entscheidend ist oder der Wortlaut in den Untertiteln unverständlich bleibt. Ausgewertete Videos mit 👀 oder 💎 bilden die **Anhör-Liste**; Ziel: höchstens 30–50 Videos. Alles andere gilt nach der Auswertung als erledigt.
- Erweist sich ein ausgewertetes Video als wenig lehrreich (nur Motivation/Organisation, reine Wiederholung, kein Skript-Beitrag), in `auswahl.js` auf `"r":"x"` setzen; dann erscheint es grau.
- **Arbeitskopie ist `~/Code/python/learning-sandbox`** (dort liegen die Transkripte). Der zweite Klon `~/Code/learning-sandbox` hinkt sonst hinterher: Startet ein Chat dort, zuerst `git pull` und nichts daraus veröffentlichen, solange er nicht auf dem neuesten Stand ist.
- **Gearbeitet und geprüft wird auf der claude.ai-Seite**, nicht lokal. Nach jeder Änderung an `notes.js`, `auswahl.js`, `dates.js`, `videos.js`, `kern.js`, `einwaende.js` (Einwand-Matrix, Grundlage `einwand-sammlung.md`), `live-einwaende.js` (Live-Einwände, nicht in die Matrix), `leitfaden.docx`/`leitfaden.js`/`leitfaden.pdf` oder `uebersicht.html` die Seite **neu veröffentlichen** (unten, Abschnitt „Online-Seite“), damit Felix und Demi denselben Stand sehen. Spätestens **vor jedem Commit** solcher Änderungen, und im Abschlussbericht die veröffentlichte Version nennen. 🎯 Veröffentlichen (Artifact publish) ≠ `git push`; ein Push ändert die Seite nicht.
- Vor dem Veröffentlichen kurz prüfen, ob die Online-Dateien neuer sind als die lokalen (Artifact `read` mit `paths`, dann `cmp`). Wenn ja, nicht überschreiben, sondern erst abgleichen.
- **Gültiger Leitfaden ist die claude.ai-Seite** (seit 30.10.2026); Felix arbeitet dort täglich mit ihr als Gesprächsleitfaden. **Word ist pausiert:** `leitfaden.docx`/`leitfaden.pdf` sind veraltet (auf der Seite als „(veraltet)“ markiert), bleiben aber samt Verweisen bestehen. Neue oder geänderte gesprochene Sätze kommen in `kern.js` (`say`), nicht nach Word; `say`-Felder nicht löschen und `leitfaden_export.py` nicht ausführen, bis Felix Word wieder aufnimmt.

## Was aus den Videos herausgezogen wird

Gesucht sind **sofort am Telefon nutzbare Formulierungen**, keine allgemeinen Tipps.

| Typ | Phase | Skript-Baustein |
| --- | --- | --- |
| **Sekretärin** | K | Durchstellen; Antwort auf „Worum geht es?“ |
| **Opener** | K | Begrüßung bis Erlaubnis („Darf ich gleich mal sagen, warum ich anrufe?“) |
| **Bedarfsfrage** | K, T | Interesse wecken / Bedarf ermitteln |
| **Rückfrage** | K | Kunde fragt „Was kostet das?“, „Wie macht ihr das?“ → kurze Antwort + Überleitung zum Termin |
| **Einwand** | K, T | Einwand wörtlich (`e`) + Antwort wörtlich |
| **Terminvereinbarung** | K | Vorschlag, Zeitrahmen, Festnageln, Mail-Bestätigung, Absicherung gegen Absagen |
| **Gesprächseinstieg** | T | Erste Minuten im Termin: Agenda, Rahmen, Rollen klären |
| **Präsentation** | T | Angebot vorstellen, an Bedarf koppeln |
| **Preis** | T | Preis nennen und begründen |
| **Abschluss** | T | Abschlussfrage, Entscheidung herbeiführen, mehrere Entscheider |
| **Leitfaden** | K, T, A | Kompletter Ablauf oder Struktur mehrerer Bausteine |
| **Nachfassen** | K | Erneuter Anruf: nach Monaten, nach Postsendung, Reaktivierung alter Kontakte |
| **Prinzip** | K, T, A | Nur Regel, die eine Formulierung in einem Baustein verändert (z. B. „bei der Sekretärin nicht sagen, worum es geht“) |
| **Organisation** | K, T, A | Rund ums Telefonieren, aber nicht im Gespräch selbst: Tagesplanung, Adressen, Motivation, Quoten, Geschäftsmodell. Fließt nicht ins Skript, nur in einen Anhang |

Der ältere Sammeltyp „Verkaufsgespräch“ ist durch Gesprächseinstieg/Präsentation/Preis/Abschluss ersetzt.

**Drei Phasen, nie vermischen:**

| Kürzel | Phase | Umfasst |
| --- | --- | --- |
| `K` | Kaltakquise | Erster Anruf: Sekretärin, Opener, Bedarfsfrage, Einwände, bis der Termin steht |
| `T` | Termin / Verkaufsgespräch | Das vereinbarte Gespräch (ca. 15–60 Min.): Aufbau, Präsentation, Preis, Abschluss |
| `A` | Andere Verkaufsform | Alles andere, z. B. Messe, E-Mail, Social Selling, Empfehlungen |

**Segment pro Video** (`seg`): `Handwerk` · `KMU` · `Großunternehmen` · `Privat` · `allgemein`. Fokus ist **Handwerk und KMU**; Großunternehmen und Privat bleiben drin, aber klar markiert.

**Zielgruppe pro Video** (`target`): an wen genau verkauft wird, z. B. „Industrie (Produktionsleiter)“, „Immobilienmakler → Privatverkäufer“. Learnings aus fremden Branchen bleiben drin, sind aber so erkennbar und lassen sich beim Zusammenführen anpassen.

**Format in `notes.js`** – ein Eintrag pro Video, darin eine Liste von Learnings:

```js
"VIDEO_ID": {seg: "Handwerk", target: "Zielgruppe", watch: true, why: "Grund fürs Anschauen", items: [
  {p: "K", y: "Einwand", e: "Haben wir schon", t: "3:00", x: "„Wörtliche Antwort …“"},
  {p: "K", y: "Opener", t: "2:13", s: 1, x: "… (s: 1 = sinngemäß)"}
]}
```

Videos ohne verwertbaren Inhalt: `items: []` und `skip: "Grund"`.

Videos **ohne Untertitel/Transkript**: `nosubs: true` – erscheinen mit ⚠️ und gelten als „selbst anschauen“, weil der Inhalt nicht erfasst werden kann.

Wörtliche Zitate in „…“; vollständige Abläufe (z. B. Einwand → Rückfrage → Lösung) als mehrere Einträge in Reihenfolge.

**Nicht aufnehmen:** Motivation und Mindset ohne konkrete Handlung, Eigenwerbung (Coaching, Abo, Masterclass), Zahlen ohne Beleg (z. B. 60/30/10-Regel), Wiederholungen bereits erfasster Formulierungen (dann nur „wie Video X“).

**👀 Anschau-Empfehlung**, wenn mindestens eins zutrifft:
- echtes Live-Telefonat oder Rollenspiel, bei dem Tonfall und Timing wichtig sind
- ein Einwand wird im echten Gespräch gelöst
- eine Formulierung ist nur im Zusammenhang verständlich

## Ablauf

1. Der Agent lädt nur die Untertitel (`uvx yt-dlp`, kein Video), 5 Videos pro Paket. `fetch.py --next 5` wählt automatisch die nächsten offenen Videos, die in `auswahl.js` **grün** markiert sind, **neueste zuerst, alle Kategorien** (dadurch kommen die letzten 12 Monate, Nr. 1–77, vor den älteren).
2. **Jedes Transkript wird vollständig gelesen** – kein Vorfiltern per Stichwort, weil Kernmuster (z. B. die Reframing-Formel „Das heißt nur, wenn …“) sonst übersehen werden. Videos über 30 Min. werden in Abschnitten gelesen.
3. Handwerk-Bezug (Zielgruppe, Beispiele, Branchen-Einwände) in `target` ausdrücklich nennen, damit diese Learnings beim Zusammenführen Vorrang haben.
4. Ergebnisse landen in `notes.js`; danach neu veröffentlichen und auf der claude.ai-Seite prüfen (lokal `uebersicht.html` in Brave nur als Vorschau).
5. Am Ende werden alle Learnings zusammengefasst.

## Einstieg für einen neuen Chat

Arbeitsmodus: **Shipping** (Ergebnis zählt), Ergebnisse direkt in die Dateien, kurze Zusammenfassung im Chat. Effort-Stufe **high** empfohlen.

```bash
cd sales_learning/mahnken-videos
python3 fetch.py --next 5          # lädt die nächsten 5 offenen grün markierten Videos (auswahl.js, neueste zuerst) nach transcripts/
python3 fetch.py --next 5 --cat B  # nur eine Kategorie (A Kaltakquise, B Verkaufsgespräch, C Einwand, D Sonstiges)
python3 fetch.py ID1 ID2           # oder gezielt einzelne Videos
```

Pro Video dann:

1. `transcripts/<ID>.txt` **vollständig** lesen (lange Dateien abschnittsweise, nichts überspringen).
2. Eintrag in `notes.js` nach dem Schema oben ergänzen – auch für Videos ohne Ertrag (`skip`) oder ohne Transkript (`nosubs: true`), damit sie als erledigt gelten.
3. Prüfen, dass die Datei lädt: `node -e "global.window={};require('./notes.js');console.log(Object.keys(window.NOTES).length)"`
4. Im Chat pro Paket kurz berichten: neue 👀-Empfehlungen, stärkste Formulierungen, Korrekturen.

Wichtig aus bisheriger Arbeit:

- Vorfiltern per Stichwort hat einmal zu einer **falschen** Notiz geführt („Darf ich gleich zum Punkt kommen?“ wurde als abgelehnt notiert, wird aber empfohlen). Deshalb immer vollständig lesen und Julians **eigene** Meinung von der des besprochenen Trainers trennen.
- Der stärkste Fund bisher ist die Reframing-Formel aus Video `639wCGS1SA4` („Das heißt nur, wenn …, nur dann macht es Sinn …“). Ähnliche Muster in anderen Videos als wiederkehrend kennzeichnen.
- `videos.js` (Liste aller 428 Videos) ist fest. Neu erzeugen nur bei neuen Kanal-Videos: `uvx yt-dlp --flat-playlist --extractor-args "youtube:lang=de" --print "%(id)s\t%(duration)s\t%(title)s" <Kanal-URL>/videos`.

## Review und Skript-Update (Hauptchat)

Nach einigen Arbeits-Chats, wenn **kein** anderer Chat in `notes.js` schreibt:

1. **Stand prüfen** (im Ordner `mahnken-videos`):
   `node -e "global.window={};require('./notes.js');require('./videos.js');const N=window.NOTES;require('./auswahl.js');const A=window.AUSWAHL;const r=window.VIDEOS.filter(v=>A[v.id]?.r=='g');console.log(Object.keys(N).length,'ausgewertet;',r.filter(v=>N[v.id]).length,'von',r.length,'grünen');const y={};for(const n of Object.values(N))for(const i of n.items)y[i.p+' '+i.y]=(y[i.p+' '+i.y]||0)+1;console.log(y)"`
2. **Alle Learnings gruppiert exportieren** (statt notes.js roh zu lesen):
   `node -e "global.window={};require('./notes.js');require('./videos.js');const N=window.NOTES,V=Object.fromEntries(window.VIDEOS.map(v=>[v.id,v]));const g={};for(const[id,n]of Object.entries(N))for(const i of n.items||[]){const k=i.p+' | '+i.y;(g[k]??=[]).push('['+V[id]?.n+'|'+(n.seg||'-')+'|'+id+'@'+i.t+(i.s?'|s':'')+'] '+(i.e?'«'+i.e+'» ':'')+i.x)}for(const k of Object.keys(g).sort())console.log('\n## '+k+' ('+g[k].length+')\n'+g[k].join('\n'))" > /tmp/learnings.txt`
3. **Stichprobe Zitate** (5–6 Stück, auch neue Videos): Zitat-Ausschnitt in `transcripts/<ID>.txt` suchen (Python `str.find`, nicht `grep` – Umlaute) und mit Zeitstempel vergleichen.
4. **Qualität prüfen:** richtige Typen (Planung/Motivation = `Organisation`, Follow-up = `Nachfassen`), `seg` gesetzt, Julians Meinung vs. besprochener Trainer getrennt, Widersprüche mit ⚠️ markiert.
5. **Leitfaden Thema für Thema abschließen** (seit 24.10.2026; `archiv/skript-zwischenstand.md` ist nur noch Archiv der ausführlichen Varianten):
   - **`leitfaden.docx`** (Word, `sales_learning/`) = **nur der reine Leitfaden**: oben „Sekretär“, dann „Schritt 1: Begrüßung“ … „Schritt 6: Terminfestigung und Verabschiedung“ (Aufbau wie Julians Vorlage „Telefonakquise Skript: B2B Dienstleistungen“), darunter nur gesprochene Sätze – keine Tipps, Quellen oder Videos. Der Agent schreibt nur, wenn Felix die Datei gespeichert hat.
   - **`mahnken-videos/kern.js`** = Details je Abschnitt (Reaktionen, Ton, Videos zum Anschauen, `ok` = abgeschlossen), Schlüssel = Anfang der Word-Überschrift. Nur im Tab „Leitfaden“ sichtbar; knapp halten.
   - **Trennung:** Word = nur der kleine, saubere Ablauf. Alle Eventualitäten (Reaktionen des Kunden, Sonderfälle) stehen ausschließlich in `kern.js` beim passenden Schritt, größere als **Mini-Thema** (`<h4>🛡 Mini-Thema: … („Auslöser-Sätze“)</h4>`, darunter Antwortsatz, 2–3 Kernpunkte, ❌, Warum, Anschauen), z. B. „Dominanter Typ“ bei Schritt 2.
   - Je Thema: Agent schlägt den Kern vor (Sätze, Tonalität, Videos zum Anschauen – Umfang je nach Thema, keine feste Zahl), Felix bestätigt, Abschnitt bekommt ✅. Videos, die nur wiederholen, verlieren ihr 👀.
   - Verarbeitete Learnings in `notes.js` mit `"u":"<Abschnitt>"` markieren (z. B. `"u":"1 Sekretärin"`), auch überholte und Negativbeispiele. Felix/Kollege können zusätzlich in der Sammlung „✅ umgesetzt“ anhaken (gespeichert je Person als `notizen.videos.<ID>.u` = Learning-Nummern; beim Review per `ArtifactData` auslesen und nach `notes.js` übernehmen). Auf der Seite bearbeitete Learnings liegen ebenso je Person unter `notizen.videos.<ID>.ed` (`{"<Index>": {x} | {del:true}}`) und `.add` (`[{p,y,t,x}]`): beim Review prüfen, in `notes.js` übernehmen (gelöschte entfernen) und Felix kurz berichten. `notes.js` bleibt bis dahin das Original (Backup). Umgesetzte Learnings sind in der Sammlung ausgeblendet; Videos, deren Learnings alle umgesetzt sind, gelten als **✅ abgearbeitet** und fallen aus der Hauptliste (außer 📌).
   - Danach `python3 mahnken-videos/leitfaden_export.py` → `leitfaden.js`; Tab **📋 Leitfaden** zeigt Sätze (Word) + Details (`kern.js`); dort verlinkte Videos (`youtu.be/<ID>`) erscheinen als 📌.

```text
leitfaden.docx (Word, nur Sätze) ──leitfaden_export.py──▶ leitfaden.js ─┐
kern.js (Details: Reaktionen, Ton, Videos) ─────────────────────────────┴▶ uebersicht.html: Tab Leitfaden + 📌
```
6. Committen und pushen nur auf Auftrag.

## Online-Seite

**Link:** https://claude.ai/artifact/WvLTv6W2EHNkAuwjJvFzgV – einzige Online-Seite (die frühere Cloudflare-Seite ist abgeschaltet). Was Nutzer dort sehen: README, Abschnitt „Online-Seite“.

```text
Agent ändert notes.js / auswahl.js / uebersicht.html ──▶ Online-Seite neu veröffentlichen (unten)
Felix / Kollege bewerten online ──▶ Datenbank (kern, notizen) ──▶ Agent liest sie beim Review aus
```

Diese Seite aktualisiert sich nie automatisch. Darum wird nach jeder Änderung an den Dateien unten neu veröffentlicht, spätestens vor einem lokalen Commit. (Der lokale `pre-push`-Hook erinnert daran.) Die Seite bleibt online, bis sie gelöscht wird.

**Neu veröffentlichen** (nach jeder Änderung an diesen Dateien, im Ordner `mahnken-videos`):

1. Falls `leitfaden.docx` geändert wurde: `python3 leitfaden_export.py`. Dann `tail -n +2 uebersicht.html > .online.html` (erste Zeile = Doctype, den setzt claude.ai selbst; Datei ist per `.gitignore` ausgenommen).
2. In einem neuen Chat zuerst einmal das Artifact mit der URL oben lesen (`Artifact`, `action: "read"`), sonst wird das Veröffentlichen abgelehnt.
3. Veröffentlichen mit `Artifact` (publish): `url` = Link oben, `file_path` = `mahnken-videos/.online.html`, `files` = `videos.js`, `notes.js`, `dates.js`, `auswahl.js`, `leitfaden.js`, `kern.js`, `einwaende.js`, `live-einwaende.js`, `leitfaden.pdf` (Quellpfade **absolut** angeben, z. B. `/Users/felix/Code/python/learning-sandbox/sales_learning/mahnken-videos/notes.js`). Läuft der Chat im zweiten Klon, lehnt das Tool Pfade der Arbeitskopie ab: dann die Dateien erst in den Scratchpad kopieren und von dort mit `root` veröffentlichen. Kein `capabilities`-Feld mitgeben – die Datenbank-Einstellung bleibt so erhalten; Bewertungen bleiben ebenfalls erhalten.

**Hauptseite ist die claude.ai-Seite** (seit 28.10.2026). Die lokale `uebersicht.html` ist nur Vorschau; Häkchen dort bleiben im Browser und kommen nicht online an.

**Personen:** oben rechts „Felix (F)“ / „Demi (D)“ wählen – kein Login, nur Zuordnung. Je Person: 👁 angeschaut, 🔁 nochmal, Kommentar (Collection `notizen`, Dokument `F` bzw. `D`, Feld `videos.<ID>.seen/.again/.text`, dazu `u`/`ed`/`add`). Gemeinsam für beide: 💎 Kern-Video (Collection `kern`, Dokument = Video-ID, Feld `g` true/false; fehlt es, gilt der Vorschlag aus `auswahl.js`). Schreiben darf jeder Eingeladene ab Stufe Mitwirkender.

**Word für Demi:** claude.ai liefert keine `.docx` aus. Nach Änderungen in Word zusätzlich *Datei → Als PDF exportieren* nach `sales_learning/leitfaden.pdf`; `leitfaden_export.py` kopiert es mit, der Tab Leitfaden verlinkt es (beim Veröffentlichen `leitfaden.pdf` in `files` mitgeben).

**Backup:** Die Online-Datenbank liegt bei claude.ai. Beim Review zusätzlich `mahnken-videos/online-backup.json` aktualisieren (Collections `notizen` und `kern` per `ArtifactData` auslesen) und mitcommitten.

**Online-Bewertungen auslesen** (beim Review): `ArtifactData` `list` auf die Collections `kern` und `notizen` (Dokumente `F`, `D`).

## Live-Einwände (`mahnken-videos/live-einwaende.js`)

Erscheinen im Tab 📋 Leitfaden als Abschnitt „🎥 Live-Einwände“ unter der Einwand-Matrix; die Videos dazu zeigt der Filter „🛡 Einwand-Fokus“.

- Einwände aus echten Telefonaten, KI-Rollenspiel und Coachings – **nicht direkt übernehmen**, Kontext beachten (was wird verkauft? Julian verkauft meist laufende Dienstleistungen).
- **Nicht** in die Einwand-Matrix (`einwaende.js`) übernehmen und nicht als Grundlage für eigene Antworten nutzen, bis Felix es sagt.
- Felix ergänzt beim Videogucken (diktiert an den Agenten oder im gemeinsamen Kommentarfeld des Videos mit „🎥 Live: …“); der Agent trägt es in `live-einwaende.js` ein.
- In `live-einwaende.js` keine youtu.be-Links, sonst werden die Videos zu 📌; Quellen als „Nr. X @m:ss“.
