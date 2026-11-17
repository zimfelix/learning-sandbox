# Python Learning – Uni-Kurs

Python-Grundlagen für den Uni-Kurs **„Grundlagen der Programmierung“ (WS 2026/27)**. Die Aufgaben richten sich nach dem Uni-Material; Felix löst sie selbst, der Agent reviewt.

## Quellen

| Quelle | Rolle |
| --- | --- |
| `uni_material/Grundlagen_der_Programmierung_Uebung.ipynb` | Übungsreihenfolge: Uni-Aufgaben, Lösungen ab 2.5 direkt hier in PyCharm |
| `uni_material/Grundlagen_der_Programmierung.ipynb` | Code-Beispiele der Vorlesung, **klausurrelevant** (Syntax wie hier üben, z. B. `menge1.union(menge2)`) |
| `uni_material/Grundlagen_der_Programmierung_2026_2027.pdf` | Folien, **Klausurschwerpunkt** (laut Felix 2026-11-17 eher Folien als Übungsaufgaben) |
| [The Morpheus Tutorials – Python Tutorials Deutsch](https://www.youtube.com/playlist?list=PLNmsVeXQZj7q0ao69AIogD94oBgp3E9Zs) | schaut Felix **separat**; Aufgaben orientieren sich nicht daran |

## Ablauf pro Kapitel

Das **Übungs-Notebook gibt Reihenfolge und Inhalt vor**: Es gibt keine eigenen Zusatz- oder Bewerbungsaufgaben mehr, außer Felix wünscht sie ausdrücklich.

```text
Übungs-Notebook: nächste Aufgabe lesen
  →  passende Zellen im Vorlesungs-Notebook ausführen (Beispiele ansehen)
  →  Lösung direkt in die Code-Zelle im Übungs-Notebook schreiben + ausführen (PyCharm)
  →  Review mit dem Agenten  →  nächste Aufgabe
```

⚠️ Das Übungs-Notebook ist nur lokal und nicht in Git. PyCharm speichert automatisch. Ein Backup gibt es aber nur über die Local History von PyCharm. Die alten Lösungen zu 2.1–2.4 (`uni_loesungen.py`) wurden am 2026-11-13 gelöscht und liegen nur noch in der Git-History.

Reihenfolge nach Uni-Kapiteln: 2.1 Variable/Datentyp → 2.2 Operator → 2.3 Kontrollstruktur → 2.4 Funktion → 2.5 Datenstruktur → 2.6 Zeitstempel → 3.1–3.4 numpy, matplotlib, pandas, random → 4.1 Error/Exception → 4.2 API (`yfinance`) → 4.3 GUI (Roulette).

**Editor: PyCharm** (nicht VS Code). Das Uni-Material bleibt lokal, auch das Übungs-Notebook mit Felix' Lösungen.

## Klausurplan (Stand 2026-11-14)

**Schwerpunkt (2026-11-17):** Die Klausur orientiert sich eher an den Folien und der Vorlesung als an den Übungsaufgaben. Papier-Training deshalb an den Inhalten von Folien und Vorlesungs-Notebook ausrichten, nicht nur an den Übungsaufgaben.

**Niveau-Referenz:** drei Original-Aufgaben aus Vorklausuren (Summe mit Teilbarkeit, Funktion mit `if`/`return`, String `replace`/`count`) liegen mit Musterlösung und typischen Fehlern in `uni_material/uebungen/klausur_beispiele.py` (nur lokal). Papier-Training an diesem Schwierigkeitsgrad ausrichten.

Klausur **mit Stift und Papier**, ca. **24./25.11.2026** (genaues Datum offen, ob Unterlagen erlaubt sind, ebenfalls offen). Auf Papier gibt es keine Autovervollständigung: Die Kern-Syntax muss selbst geschrieben werden können.

**Umfang:** täglich ein 2-h-Block (50 min · 10 min Pause · 50 min · 5 min Lernkarten-Einzeiler). Lieber nach 1 h abbrechen als sich durchquälen; an Papier-Tagen bei Bedarf einen kurzen Zusatzblock.

| Tage | Inhalt |
| --- | --- |
| 15.–18.11. | Rest durchgehen: 3.3 pandas · 3.4 random · 4.1 Exception · 4.2 API · 4.3 GUI. Nur verstehen + Lernkarte, kein Pauken |
| 19.–23.11. | Papier-Training: 2–3 Kapitel pro Tag ohne PyCharm auf Papier lösen, abtippen/fotografieren, Agent korrigiert wie in einer Klausur |
| Tag vor der Klausur | nur die Lernkarten-Einzeiler (Obsidian, `Uni Grundlagen I`) wiederholen, Pause |

**Muss auswendig sitzen:**

| Kapitel | Kern |
| --- | --- |
| 2.1–2.4 | `+=`, `if/elif/else`, `for … in range()`, `while`, `def` + `return`; `range(start, stop, step)`: stop exklusiv, z. B. `range(1, 3, 2)` → nur `1`, `range(10, 0, -2)` → 10, 8, 6, 4, 2 (prüfungsrelevant) |
| 2.5 | Liste, Dict, Tupel, Set: anlegen, `[]`, `append`, `del`; Set: `intersection`, `union`, `difference` |
| 2.6 | `datetime.now()`, `objekt.strftime(format)`, `datetime.strptime(text, format)` |
| 3.1 | `np.array`, `np.sum/mean/max/min`, `x[5:11]`, `x[x > 10]` |
| 3.2 | `plt.plot / scatter / hist`, `plt.show()` |

**Nur erkennen:** `subplots`, `relativedelta`, Formatcode-Details, `np.arange`.

## Stand (2026-11-14)

- **Selbsteinschätzung 2026-11-14:** 2.1–2.5 relativ sicher; 2.6, 3.1, 3.2 noch wackelig, sollen morgen besser sitzen.
- **2026-11-14:** 2.6 (+ Wiederholung `u2_6b`), 3.1 und 3.2 durchgearbeitet; 3.2 Teil 3–4 und 2.6b Teil 4 per Lösung. Wackelig: `strptime`/`strftime` (Richtung, Klasse vs. Objekt), `timedelta` über `.days`/`.seconds`, `()` beim Aufruf vergessen (`plt.show`), `range`-Start/-Stop.
- **Erledigt (2026-11-13):** 2.1, 2.3, 2.4 und Zusatzaufgaben 1–3 zu 2.4.
- **Offen in 2.2:** Teil 1 (`x`/`y` statt `a`/`b`), Teil 3 (`+=` usw.), Teil 5 (`True`/`False` mit `and`/`or`/`not`).
- **Bewerbungs-Basics:** durchgearbeitet und gelöscht (2026-11-13). Wackelig: Methoden raten (`append[...]`, `.replace`/`.rename`), `dict[key] = wert`, `.items()`, FizzBuzz-Reihenfolge.
- **Eigene Zusatzaufgaben 4–6 zu 2.4:** entfallen, weil nur noch das Übungs-Notebook zählt.
- **Nächster Einstieg:** 3.3 pandas (laut Klausurplan). Reste aus 2.2 (Teil 1, 3, 5) im Papier-Training mitnehmen.
- **Wackelig:** `+=` (Variable verändern statt nur rechnen), `print` vs. `return`, Accumulator-Muster, `for` vs. `while`, Funktionen aufrufen statt nur definieren.

## Setup

```bash
cd learning-sandbox
python3.14 -m venv .venv                    # im Repo-Root, einmalig
.venv/bin/pip install -r python_learning/requirements.txt
```

PyCharm (Projekt `learning-sandbox`, erledigt am 2026-11-13): Interpreter → *Add Local Interpreter* → *Select existing* → `learning-sandbox/.venv/bin/python` (gemeinsame Root-venv). Notebooks (`.ipynb`) brauchen diese venv als Kernel. Den Kernel stellt das Paket `ipykernel` bereit. Beim ersten Öffnen eines Notebooks oben rechts **Trust Notebook** anklicken, sonst laufen die Zellen nicht.

`yfinance` (Kapitel 4.2) wird erst bei Bedarf nachinstalliert.

## Ordner

```text
python_learning/
├── README.md
├── requirements.txt   Dependencies der venv
├── notes.py           Felix' eigene Notizen / Mitcode
└── uni_material/      Uni-Dateien aus Google Drive (nur lokal, nicht in Git)
```
