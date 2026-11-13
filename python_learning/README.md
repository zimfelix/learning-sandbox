# Python Learning – Uni-Kurs

Python-Grundlagen für den Uni-Kurs **„Grundlagen der Programmierung“ (WS 2026/27)**. Die Aufgaben richten sich nach dem Uni-Material; Felix löst sie selbst, der Agent reviewt.

## Quellen

| Quelle | Rolle |
| --- | --- |
| `uni_material/Grundlagen_der_Programmierung_Uebung.ipynb` | **Leitfaden**: Uni-Aufgaben, Lösungen ab 2.5 direkt hier in PyCharm |
| `uni_material/Grundlagen_der_Programmierung.ipynb` | Code-Beispiele der Vorlesung |
| `uni_material/Grundlagen_der_Programmierung_2026_2027.pdf` | Folien, eher generisch – nur zum Nachschlagen |
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

## Stand (2026-11-13)

- **Erledigt:** 2.1, 2.3, 2.4 und Zusatzaufgaben 1–3 zu 2.4.
- **Offen in 2.2:** Teil 1 (`x`/`y` statt `a`/`b`), Teil 3 (`+=` usw.), Teil 5 (`True`/`False` mit `and`/`or`/`not`).
- **Bewerbungs-Basics:** durchgearbeitet und gelöscht (2026-11-13). Wackelig: Methoden raten (`append[...]`, `.replace`/`.rename`), `dict[key] = wert`, `.items()`, FizzBuzz-Reihenfolge.
- **Eigene Zusatzaufgaben 4–6 zu 2.4:** entfallen, weil nur noch das Übungs-Notebook zählt.
- **Nächster Einstieg:** 2.5 Teil 1 (Tupel), danach die Reste aus 2.2.
- **Wackelig:** `+=` (Variable verändern statt nur rechnen), `print` vs. `return`, Accumulator-Muster, `for` vs. `while`, Funktionen aufrufen statt nur definieren.

## Setup

```bash
cd python_learning
python3 -m venv .venv                       # einmalig, Python 3.14
.venv/bin/pip install -r requirements.txt
```

PyCharm (Projekt `learning-sandbox`, erledigt am 2026-11-13): Interpreter → *Add Local Interpreter* → *Select existing* → `python_learning/.venv/bin/python`. Notebooks (`.ipynb`) brauchen diese venv als Kernel. Den Kernel stellt das Paket `ipykernel` bereit. Beim ersten Öffnen eines Notebooks oben rechts **Trust Notebook** anklicken, sonst laufen die Zellen nicht.

`yfinance` (Kapitel 4.2) wird erst bei Bedarf nachinstalliert.

## Ordner

```text
python_learning/
├── README.md
├── requirements.txt   Dependencies der venv
├── notes.py           Felix' eigene Notizen / Mitcode
├── .venv/             lokale Umgebung (nicht in Git)
└── uni_material/      Uni-Dateien aus Google Drive (nur lokal, nicht in Git)
```
