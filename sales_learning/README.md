# Sales Learning – Vertrieb und Telefonakquise

**Ziel:** ein einsatzfertiges **Gesprächsskript für die Kaltakquise bei Handwerksbetrieben** (plus Einwand-Vorlagen und Empfehlungen fürs Verkaufsgespräch) – kein Informationssammelsurium. Quelle sind öffentlich verfügbare Vertriebsvideos; herausgezogen werden wörtliche Gesprächseinstiege, Einwandantworten und Bedarfsfragen, getrennt nach **Kaltakquise** (erster Anruf) und **Verkaufsgespräch** (der Termin selbst).

**Eigenständiges Vorhaben:** unabhängig von `SQL_learning/`, `obsidian/` und `lead-finder/`. Wer hier arbeitet, fasst diese Ordner nicht an; die Root-`learning-state.md` (SQL-/Python-Lernstand) ist für dieses Vorhaben nicht relevant.

**Priorität:** die in `mahnken-videos/auswahl.js` **grün** markierten Videos, neueste zuerst. **Ab 1.12.2025 (Nr. 1–73) wird jedes Video per Transkript geprüft** (alle grün, unabhängig vom Titel); ältere Videos sind nur **nach Titel** grün/gelb/grau eingeteilt, dazu alles mit Bezug zu **Handwerk**. Gelb markierte nur, wenn eine Skript-Lücke offen bleibt.

## Inhalt

```text
sales_learning/
└── mahnken-videos/       YouTube-Kanal Julian Mahnken (428 Videos)
    ├── uebersicht.html   Übersicht mit Suche, Filtern, Anhör-Liste und Bewertungsspalte (auch online, siehe unten)
    ├── videos.js         Videoliste (Titel, Länge, grobe Kategorie)
    ├── notes.js          Auswertung pro Video: Zielgruppe, 👀-Empfehlung, Learnings
    ├── auswahl.js        Vorauswahl: Relevanz grün/gelb/grau, 💎 Kern-Video, 🎥 Live, Thema `th` (Filter in der Übersicht)
    ├── dates.js          Upload-Datum je Video
    └── transcripts/      Transkripte als .txt (lokal, nicht eingecheckt)
```

## Ziel-Skript (wohin alles einzahlt)

Am Ende entsteht daraus ein Skript mit festen Bausteinen; pro Baustein 1 empfohlene Formulierung + Varianten, Handwerk/KMU zuerst:

```text
KALTAKQUISE (K)                         TERMIN (T)
1 Sekretärin                            1 Gesprächseinstieg
2 Opener + Erlaubnis                    2 Bedarfsfrage / Bedarfsanalyse
3 Bedarfsfrage (Interesse wecken)       3 Präsentation
4 Reaktion des Kunden:                  4 Preis
   ├ Interesse  → 6                     5 Einwand → Antwort
   ├ Einwand    → 5 → 6                 6 Abschluss
   └ Rückfrage  → kurz → 6
5 Einwand → Antwort (Reframing)
6 Terminvereinbarung
```

Jedes Learning sollte einem dieser Bausteine zugeordnet werden können. Was keinem Baustein dient, gehört nicht hinein.

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
4. Ergebnisse landen in `notes.js`; `uebersicht.html` in Brave öffnen und mit ⌘R neu laden.
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
5. **Leitfaden Thema für Thema abschließen** (seit 24.10.2026; `skript-zwischenstand.md` ist nur noch Archiv der ausführlichen Varianten):
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

## Online-Seiten

⚠️ **Cloudflare außer Betrieb** (Build schlägt fehl, ignorieren). Gearbeitet wird **lokal** (`uebersicht.html` in Brave) plus **claude.ai-Seite**.

| Seite | Link | Wofür |
| --- | --- | --- |
| **claude.ai** | https://claude.ai/artifact/WvLTv6W2EHNkAuwjJvFzgV | gemeinsames Bewerten (Konto nötig); muss von einem Agent neu veröffentlicht werden, siehe unten. **Einzige aktive Online-Seite.** |
| ~~Cloudflare Pages~~ | https://mahnken-videos.pages.dev | außer Betrieb (Build schlägt fehl). War: öffentlich, aktualisiert bei jedem Push auf `main`. |

### claude.ai-Seite (gemeinsam bewerten)

**Link:** https://claude.ai/artifact/WvLTv6W2EHNkAuwjJvFzgV – dieselbe Übersicht wie `uebersicht.html`, aber mit gemeinsamer Datenbank: Relevanz-Änderungen gelten für alle, „angeschaut“ und Kommentare sieht jeder (je Person gespeichert). Transkripte liegen nicht online.

Zugriff vergibt nur Felix über das Teilen-Menü der Seite. Zum Mitarbeiten braucht der Kollege ein claude.ai-Konto und die Stufe Mitwirkender oder Bearbeiter; über einen öffentlichen Link kann man nur lesen.

```text
Agent ändert notes.js / auswahl.js / uebersicht.html ──▶ Online-Seite neu veröffentlichen (unten)
Felix / Kollege bewerten online ──▶ Datenbank (kern, notizen) ──▶ Agent liest sie beim Review aus
```

Diese Seite aktualisiert sich nie automatisch. Darum wird nach jeder Änderung an den Dateien unten neu veröffentlicht, spätestens vor einem lokalen Commit. (Der lokale `pre-push`-Hook erinnert daran.) Die Seite bleibt online, bis sie gelöscht wird.

**Neu veröffentlichen** (nach jeder Änderung an diesen Dateien, im Ordner `mahnken-videos`):

1. Falls `leitfaden.docx` geändert wurde: `python3 leitfaden_export.py`. Dann `tail -n +2 uebersicht.html > .online.html` (erste Zeile = Doctype, den setzt claude.ai selbst; Datei ist per `.gitignore` ausgenommen).
2. In einem neuen Chat zuerst einmal das Artifact mit der URL oben lesen (`Artifact`, `action: "read"`), sonst wird das Veröffentlichen abgelehnt.
3. Veröffentlichen mit `Artifact` (publish): `url` = Link oben, `file_path` = `mahnken-videos/.online.html`, `files` = `videos.js`, `notes.js`, `dates.js`, `auswahl.js`, `leitfaden.js`, `kern.js` (Quellpfade **absolut** angeben, z. B. `/Users/felix/Code/python/learning-sandbox/sales_learning/mahnken-videos/notes.js`). Kein `capabilities`-Feld mitgeben – die Datenbank-Einstellung bleibt so erhalten; Bewertungen bleiben ebenfalls erhalten.

**Hauptseite ist die claude.ai-Seite** (seit 28.10.2026). Die lokale `uebersicht.html` ist nur Vorschau; Häkchen dort bleiben im Browser und kommen nicht online an.

**Personen:** oben rechts „Felix (F)“ / „Demi (D)“ wählen – kein Login, nur Zuordnung. Je Person: 👁 angeschaut, 🔁 nochmal, Kommentar (Collection `notizen`, Dokument `F` bzw. `D`, Feld `videos.<ID>.seen/.again/.text`, dazu `u`/`ed`/`add`). Gemeinsam für beide: 💎 Kern-Video (Collection `kern`, Dokument = Video-ID, Feld `g` true/false; fehlt es, gilt der Vorschlag aus `auswahl.js`). Schreiben darf jeder Eingeladene ab Stufe Mitwirkender.

**Word für Demi:** claude.ai liefert keine `.docx` aus. Nach Änderungen in Word zusätzlich *Datei → Als PDF exportieren* nach `sales_learning/leitfaden.pdf`; `leitfaden_export.py` kopiert es mit, der Tab Leitfaden verlinkt es (beim Veröffentlichen `leitfaden.pdf` in `files` mitgeben).

**Backup:** Die Online-Datenbank liegt bei claude.ai. Beim Review zusätzlich `mahnken-videos/online-backup.json` aktualisieren (Collections `notizen` und `kern` per `ArtifactData` auslesen) und mitcommitten.

**Online-Bewertungen auslesen** (beim Review): `ArtifactData` `list` auf die Collections `kern` und `notizen` (Dokumente `F`, `D`).

## Ideen für später (beim Review ansprechen)

- **Einwandbehandlung mit Claude trainieren** (notiert 24.10.2026, offen). Vorbild ist das Video `eCUNXUw6EZ8` „Ich terminiere LIVE eine Trainings-KI für Kaltakquise“ (https://youtu.be/eCUNXUw6EZ8); es ist bereits ausgewertet. Felix hat schon kalte Einwand-Quizze mit Claude gemacht, die gut funktionieren. Ziel: täglich morgens 15 Minuten üben, auch am Handy. Die Übung beginnt mit den 30–40 häufigsten Einwand-Formulierungen. Zuerst prüfen, wie das im Video aufgebaut ist. Dann zwei Wege abwägen:
  - **(a)** Nur einen Trainings-Prompt für den Claude-Chat schreiben, mit Einwandliste und Antworten aus dem Leitfaden bzw. aus `kern.js`.
  - **(b)** Ein kleines Trainingswerkzeug bauen.

### Entwurf: Trainings-Prompt für Weg (a) (24.10.2026, noch nicht getestet)

Den Text unten in einen neuen Claude-Chat kopieren, z. B. am Handy. Die Antwortmuster stammen aus `notes.js`, vor allem aus der Reframing-Formel (`639wCGS1SA4`) und dem Unterlagen-Einwand (`eCUNXUw6EZ8`, `YDWXfK8tFtc`). Die Angebotszeile ist eine Annahme und muss noch angepasst werden.

```text
Du bist mein Trainingspartner für Einwandbehandlung in der Kaltakquise. Wir üben 15 Minuten, ich antworte meist per Spracheingabe am Handy – halte deine Nachrichten kurz.

KONTEXT
Ich rufe Inhaber von Handwerksbetrieben kalt an. Mein Angebot: mehr passende Online-Anfragen für den Betrieb (Website / Online-Marketing). Ziel jedes Anrufs ist ein kurzer Termin, kein Verkauf am Telefon.

ABLAUF
1. Du spielst den Handwerker und bringst EINEN Einwand, realistisch und knapp formuliert (wie am Telefon, auch mal ruppig). Nur der Einwand, kein Kommentar.
2. Ich antworte.
3. Du gibst Feedback in höchstens 4 Zeilen:
   – Bewertung 1–5
   – Was gut war (nur wenn wirklich gut)
   – Was fehlte oder falsch war
   – Musterantwort in einem Satz
4. Manchmal (etwa jedes dritte Mal) reagierst du als Kunde noch einmal mit einem zweiten Einwand (Ketteneinwand), bevor du bewertest.
5. Nächster Einwand. Nach 10 Einwänden: kurze Auswertung – meine 2 schwächsten Einwände und ein Satz, worauf ich morgen achten soll.

MEINE REGELN (danach bewertest du)
– Grundformel Reframing: „Okay, das heißt nur, wenn [Bedingung, die den Einwand auflöst] – nur dann macht es Sinn, dass wir sprechen. Stimmt's?“ Danach sofort ein konkreter Terminvorschlag („Wie sieht's morgen Vormittag aus?“).
– Nicht dagegen argumentieren, nicht mit „aber“ widersprechen, den Einwand nicht loben („Danke, dass Sie das offen ansprechen“), keine Suggestivfragen.
– Keine Konjunktive (würde, könnte, hätte, wäre) in meinen eigenen Sätzen – jeden einzeln anmerken.
– Ergänzen statt ersetzen, wenn der Kunde schon jemanden hat.
– Ketteneinwand: noch einmal reframen und beide Bedingungen zusammenfassen.
– Ruhig bleiben, nicht rechtfertigen, nicht abkürzen („ich mach's ganz kurz“ ist falsch).

MUSTERANTWORTEN (Referenz)
– Schlechte Erfahrungen: „Das heißt nur, wenn wir sicherstellen, dass sich die schlechte Erfahrung nicht wiederholt – nur dann macht es Sinn, dass wir sprechen, stimmt's?“
– Haben schon jemanden: „Das heißt nur, wenn wir ein viel besseres Angebot machen als Ihr aktueller Partner – nur dann hat sich ein Vergleich für Sie gelohnt. Stimmt's?“
– Machen wir intern: „Das heißt nur, wenn wir zu dem, was intern schon gut läuft, eine wirklich sinnvolle Ergänzung sind – nur dann macht es Sinn, dass wir sprechen. Richtig?“
– Keine Zeit: „Das heißt nur, wenn wir einen Zeitpunkt finden, der gut reinpasst, und es kurz halten – dann macht es Sinn, dass wir kurz in den Kalender schauen. Stimmt's?“
– Zu teuer: „Das heißt nur, wenn wir ein Angebot machen, das in Ihr Budget passt – dann macht es Sinn, dass wir konkret drüber schauen, richtig?“
– Schicken Sie Unterlagen: „Schicke ich Ihnen gleich gerne. Lassen Sie uns trotzdem schon in den Kalender schauen – der Termin findet nur statt, wenn die Unterlagen zusagen. Wie sieht's morgen Nachmittag aus?“
– Rufen Sie später an: „Gerne. Wann passt es besser?“ → konkrete Uhrzeit festmachen.
– Kein Bedarf / läuft gut / voll ausgelastet: alles derselbe Einwand mit anderer Begründung → gleich reframen.

EINWANDLISTE (zufällig mischen, häufige öfter)
Kein Interesse · Kein Bedarf · Haben wir schon · Haben schon eine Agentur · Wir haben einen Neffen, der macht die Website · Machen wir selbst · Schlechte Erfahrungen mit Agenturen · Sie sind schon der Zehnte diese Woche · Keine Zeit · Bin gerade auf der Baustelle · Rufen Sie später an · Schicken Sie mir was per Mail · Schicken Sie Unterlagen, ich melde mich · Zu teuer · Was kostet das? · Wir sind voll ausgelastet · Läuft gut bei uns · Wir leben von Stammkunden und Empfehlungen · Über die Website kommen nur Schein-Anfragen · Online-Marketing bringt bei uns nichts · Nicht der richtige Zeitpunkt, nächstes Jahr · Muss ich mit meiner Frau / meinem Partner besprechen · Bin nicht zuständig · Ich glaube Ihnen das nicht · Woher haben Sie meine Nummer? · Machen Sie's schnell · Kein Personal für mehr Aufträge · Sind gerade mit einem anderen Anbieter gestartet · Haben gerade erst eine neue Website · Dafür haben wir kein Budget

Starte jetzt mit dem ersten Einwand.
```

## Grenzen

- Nur das Gesagte wird ausgewertet; eingeblendete Texte und Folien nicht.
- Automatische Untertitel älterer Videos sind fehlerhaft; solche Zitate sind als „sinngemäß“ markiert.
- Die Kategorien kommen aus Stichworten im Titel und sind grob.
- Transkripte liegen lokal in `mahnken-videos/transcripts/`, sind aber per `.gitignore` vom Commit ausgenommen (fremde Inhalte, jederzeit neu ladbar).
