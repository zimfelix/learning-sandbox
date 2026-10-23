# Sales Learning – Vertrieb und Telefonakquise

**Ziel:** ein einsatzfertiges **Gesprächsskript für die Kaltakquise bei Handwerksbetrieben** (plus Einwand-Vorlagen und Empfehlungen fürs Verkaufsgespräch) – kein Informationssammelsurium. Quelle sind öffentlich verfügbare Vertriebsvideos; herausgezogen werden wörtliche Gesprächseinstiege, Einwandantworten und Bedarfsfragen, getrennt nach **Kaltakquise** (erster Anruf) und **Verkaufsgespräch** (der Termin selbst).

**Priorität:** Videos der **letzten zwei Jahre** (Kanal-Nr. 1–184, ab Nov. 2024) und alles mit Bezug zu **Handwerk**. Ältere Videos (Nr. 185–428) nur bei Bedarf gezielt.

## Inhalt

```text
sales_learning/
└── mahnken-videos/       YouTube-Kanal Julian Mahnken (428 Videos)
    ├── uebersicht.html   Übersicht mit Suche, Filtern und Anschau-Empfehlungen
    ├── videos.js         Videoliste (Titel, Länge, grobe Kategorie)
    ├── notes.js          Auswertung pro Video: Zielgruppe, 👀-Empfehlung, Learnings
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
| **Prinzip** | K, T, A | Nur konkrete Regel, die das Gespräch verändert |

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

1. Der Agent lädt nur die Untertitel (`uvx yt-dlp`, kein Video), 5 Videos pro Paket. `fetch.py --next 5` wählt automatisch die nächsten offenen Videos aus Nr. 1–184, **neueste zuerst, alle Kategorien**.
2. **Jedes Transkript wird vollständig gelesen** – kein Vorfiltern per Stichwort, weil Kernmuster (z. B. die Reframing-Formel „Das heißt nur, wenn …“) sonst übersehen werden. Videos über 30 Min. werden in Abschnitten gelesen.
3. Handwerk-Bezug (Zielgruppe, Beispiele, Branchen-Einwände) in `target` ausdrücklich nennen, damit diese Learnings beim Zusammenführen Vorrang haben.
4. Ergebnisse landen in `notes.js`; `uebersicht.html` in Brave öffnen und mit ⌘R neu laden.
5. Am Ende werden alle Learnings zusammengefasst.

## Einstieg für einen neuen Chat

Arbeitsmodus: **Shipping** (Ergebnis zählt), Ergebnisse direkt in die Dateien, kurze Zusammenfassung im Chat. Effort-Stufe **high** empfohlen.

```bash
cd sales_learning/mahnken-videos
python3 fetch.py --next 5          # lädt die nächsten 5 offenen Videos (Nr. 1–184, neueste zuerst) nach transcripts/
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

## Grenzen

- Nur das Gesagte wird ausgewertet; eingeblendete Texte und Folien nicht.
- Automatische Untertitel älterer Videos sind fehlerhaft; solche Zitate sind als „sinngemäß“ markiert.
- Die Kategorien kommen aus Stichworten im Titel und sind grob.
- Transkripte liegen lokal in `mahnken-videos/transcripts/`, sind aber per `.gitignore` vom Commit ausgenommen (fremde Inhalte, jederzeit neu ladbar).
