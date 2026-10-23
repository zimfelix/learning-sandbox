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
    ├── auswahl.js        Vorauswahl: Relevanz grün/gelb/grau, 💎 Kern-Video, 🎥 Live
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
5. **`skript-zwischenstand.md` aktualisieren:** neue stärkere Formulierungen einsetzen, Lücken (Abschnitt „Nächste Schritte“) abhaken, Termin-Phase ausbauen; Kopfzeile „Stand / Basis X Videos“ anpassen.
6. Committen und pushen nur auf Auftrag.

## Online-Seiten

⚠️ **Vorerst außer Betrieb (Stand 24.10.2026): GitHub-Push und Cloudflare.** Das GitHub-Konto ist von außen ausgeblendet (404), der Cloudflare-Build schlägt fehl. Nicht pushen, Cloudflare ignorieren. Gearbeitet wird **lokal** (`uebersicht.html` in Brave) plus **claude.ai-Seite**; lokale Commits nur auf ausdrücklichen Auftrag.

| Seite | Link | Wofür |
| --- | --- | --- |
| **claude.ai** | https://claude.ai/artifact/WvLTv6W2EHNkAuwjJvFzgV | gemeinsames Bewerten (Konto nötig); muss von einem Agent neu veröffentlicht werden, siehe unten. **Einzige aktive Online-Seite.** |
| ~~Cloudflare Pages~~ | https://mahnken-videos.pages.dev | außer Betrieb (Build schlägt fehl). War: öffentlich, aktualisiert bei jedem Push auf `main`. |

### claude.ai-Seite (gemeinsam bewerten)

**Link:** https://claude.ai/artifact/WvLTv6W2EHNkAuwjJvFzgV – dieselbe Übersicht wie `uebersicht.html`, aber mit gemeinsamer Datenbank: Relevanz-Änderungen gelten für alle, „angeschaut“ und Kommentare sieht jeder (je Person gespeichert). Transkripte liegen nicht online.

Zugriff vergibt nur Felix über das Teilen-Menü der Seite. Zum Mitarbeiten braucht der Kollege ein claude.ai-Konto und die Stufe Mitwirkender oder Bearbeiter; über einen öffentlichen Link kann man nur lesen.

```text
Agent ändert notes.js / auswahl.js / uebersicht.html ──▶ Online-Seite neu veröffentlichen (unten)
Felix / Kollege bewerten online ──▶ Datenbank (relevanz, notizen) ──▶ Agent liest sie beim Review aus
```

Diese Seite aktualisiert sich nie automatisch. Darum wird nach jeder Änderung an den Dateien unten neu veröffentlicht, spätestens vor einem lokalen Commit. (Der lokale `pre-push`-Hook erinnert daran; Push ist derzeit aber außer Betrieb, siehe oben.) Die Seite bleibt online, bis sie gelöscht wird.

**Neu veröffentlichen** (nach jeder Änderung an diesen Dateien, im Ordner `mahnken-videos`):

1. `tail -n +2 uebersicht.html > .online.html` (erste Zeile = Doctype, den setzt claude.ai selbst; Datei ist per `.gitignore` ausgenommen).
2. In einem neuen Chat zuerst einmal das Artifact mit der URL oben lesen (`Artifact`, `action: "read"`), sonst wird das Veröffentlichen abgelehnt.
3. Veröffentlichen mit `Artifact` (publish): `url` = Link oben, `file_path` = `mahnken-videos/.online.html`, `files` = `videos.js`, `notes.js`, `dates.js`, `auswahl.js` (Quellpfade **absolut** angeben, z. B. `/Users/felix/Code/python/learning-sandbox/sales_learning/mahnken-videos/notes.js`). Kein `capabilities`-Feld mitgeben – die Datenbank-Einstellung bleibt so erhalten; Bewertungen bleiben ebenfalls erhalten.

**Online-Bewertungen auslesen** (beim Review): `ArtifactData` `list` auf die Collections `relevanz` (Dokument-ID = Video-ID, Feld `r`: g/y/x/rot/w) und `notizen` (ein Dokument je Person, `videos.<ID>.seen/.text`). Übernahmen nach `auswahl.js` nur nach Absprache.

## Grenzen

- Nur das Gesagte wird ausgewertet; eingeblendete Texte und Folien nicht.
- Automatische Untertitel älterer Videos sind fehlerhaft; solche Zitate sind als „sinngemäß“ markiert.
- Die Kategorien kommen aus Stichworten im Titel und sind grob.
- Transkripte liegen lokal in `mahnken-videos/transcripts/`, sind aber per `.gitignore` vom Commit ausgenommen (fremde Inhalte, jederzeit neu ladbar).
