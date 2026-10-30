# Sales Learning – Vertrieb und Telefonakquise

**🌐 Hauptseite (Leitfaden, Videos, Bewertungen Felix | Demi): https://claude.ai/artifact/WvLTv6W2EHNkAuwjJvFzgV** – Zugriff nur mit Einladung (claude.ai-Konto). Die Seite ist der **gültige Stand**. Ein Git-Push ändert sie nicht; ein Agent veröffentlicht sie neu.

**Ziel:** ein einsatzfertiges **Gesprächsskript für die Kaltakquise bei Handwerksbetrieben** (plus Einwand-Vorlagen und Empfehlungen fürs Verkaufsgespräch) – kein Informationssammelsurium. Quelle sind öffentlich verfügbare Vertriebsvideos von Julian Mahnken; herausgezogen werden wörtliche Gesprächseinstiege, Einwandantworten und Bedarfsfragen, getrennt nach **Kaltakquise** (erster Anruf) und **Verkaufsgespräch** (der Termin selbst).

**Eigenständiges Vorhaben:** unabhängig von `SQL_learning/`, `obsidian/` und `lead-finder/`. Arbeitsregeln und Abläufe für Agenten (Auswertung, Review, Veröffentlichen): [`AGENTS.md`](AGENTS.md).

## Ordnerstruktur

```text
sales_learning/
├── README.md               dieser Überblick
├── AGENTS.md               Arbeitsregeln, Auswertungsformat, Review, Veröffentlichen
├── leitfaden.docx          Leitfaden in Word – pausiert, veraltet (gültig ist die Seite)
├── leitfaden.pdf           PDF-Export daraus – veraltet, auf der Seite so markiert
├── einwand-sammlung.md     Arbeitsgrundlage der Einwand-Matrix
├── archiv/                 nur nachschlagen, wird nicht mehr gepflegt
│   ├── skript-zwischenstand.md  ausführliche Varianten und Quellen (bis 24.10.2026)
│   └── skript-basis.docx        erste Skript-Fassung (24.10.2026)
├── ideen/
│   └── trainings-prompt.md      offene Idee: Einwandbehandlung mit Claude üben
└── mahnken-videos/         die Seite und ihre Daten (YouTube-Kanal, 428 Videos)
    ├── uebersicht.html     die Seite: Suche, Filter, Anhör-Liste, Tab 📋 Leitfaden
    ├── videos.js           Videoliste (Titel, Länge, grobe Kategorie)
    ├── dates.js            Upload-Datum je Video
    ├── auswahl.js          Vorauswahl grün/gelb/grau, 💎 Kern-Video, 🎥 Live, Thema
    ├── notes.js            Auswertung je Video: Zielgruppe, 👀-Empfehlung, Learnings
    ├── leitfaden.js        aus leitfaden.docx erzeugt (nicht von Hand ändern)
    ├── kern.js             Details je Leitfaden-Schritt: Reaktionen, Ton, Videos
    ├── einwaende.js        Einwand-Matrix (Tab Leitfaden)
    ├── live-einwaende.js   Live-Einwände aus Julians Telefonaten (Tab Leitfaden)
    ├── online-backup.json  Sicherung der Online-Bewertungen (Datenbank der Seite)
    ├── fetch.py            lädt Untertitel der nächsten Videos
    ├── leitfaden_export.py Word → leitfaden.js (+ PDF-Kopie)
    └── transcripts/        Untertitel als .txt (nur lokal, nicht eingecheckt)
```

## Wie die Teile zusammenhängen

```text
YouTube-Untertitel ──fetch.py──▶ transcripts/ ──Agent liest──▶ notes.js (Learnings)
                                                                   │ verdichtet
leitfaden.docx ──leitfaden_export.py──▶ leitfaden.js ─┐            ▼
kern.js (Details, vorerst auch neue Sätze per `say`) ─┼──▶ uebersicht.html ──veröffentlichen──▶ claude.ai-Seite
einwaende.js · live-einwaende.js · videos/dates/auswahl ┘                                        │
                                       online-backup.json ◀──Agent sichert── Bewertungen F | D ◀─┘
```

⚠️ **Seit 30.10.2026 ist Word pausiert.** Der Leitfaden auf der Seite ist der gültige Gesprächsleitfaden. Neue Sätze stehen in `kern.js` (`say`) und überschreiben den Word-Text. `leitfaden.docx` und `leitfaden.pdf` bleiben drin, sind aber veraltet (auf der Seite markiert) und werden später wieder angeglichen.

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

## Online-Seite

Dieselbe Übersicht wie `uebersicht.html`, aber mit gemeinsamer Datenbank: Relevanz-Änderungen und 💎 gelten für alle, „angeschaut“, 🔁 und Kommentare werden je Person gespeichert. Transkripte liegen nicht online.

- **Personen:** oben rechts „Felix (F)“ / „Demi (D)“ wählen – kein Login, nur Zuordnung.
- **Zugriff** vergibt nur Felix über das Teilen-Menü. Mitarbeiten braucht ein claude.ai-Konto und die Stufe Mitwirkender oder Bearbeiter; über einen öffentlichen Link kann man nur lesen.
- **Word für Demi:** claude.ai liefert keine `.docx` aus. Nach Änderungen in Word *Datei → Als PDF exportieren* nach `sales_learning/leitfaden.pdf`; der Tab Leitfaden verlinkt es.
- Die lokale `uebersicht.html` ist nur Vorschau; Häkchen dort bleiben im Browser und kommen nicht online an.

## Grenzen

- Nur das Gesagte wird ausgewertet; eingeblendete Texte und Folien nicht.
- Automatische Untertitel älterer Videos sind fehlerhaft; solche Zitate sind als „sinngemäß“ markiert.
- Die Kategorien kommen aus Stichworten im Titel und sind grob.
- Transkripte liegen lokal in `mahnken-videos/transcripts/`, sind aber per `.gitignore` vom Commit ausgenommen (fremde Inhalte, jederzeit neu ladbar).
