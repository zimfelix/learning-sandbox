# Python Learning – Uni-Kurs

Python-Grundlagen für den Uni-Kurs **„Grundlagen der Programmierung“ (WS 2026/27)**. Die Aufgaben richten sich nach dem Uni-Material; Felix löst sie selbst, der Agent reviewt.

## Quellen

| Quelle | Rolle |
| --- | --- |
| `uni_material/Grundlagen_der_Programmierung_Uebung.ipynb` | **Leitfaden** – Uni-Aufgaben, hier wird gelöst |
| `uni_material/Grundlagen_der_Programmierung.ipynb` | Code-Beispiele der Vorlesung |
| `uni_material/Grundlagen_der_Programmierung_2026_2027.pdf` | Folien, eher generisch – nur zum Nachschlagen |
| [The Morpheus Tutorials – Python Tutorials Deutsch](https://www.youtube.com/playlist?list=PLNmsVeXQZj7q0ao69AIogD94oBgp3E9Zs) | schaut Felix **separat**; Aufgaben orientieren sich nicht daran |

## Ablauf pro Kapitel

```text
Vorlesungs-Notebook lesen + ausführen  →  Aufgabe im Übungs-Notebook lesen
  →  Lösung in uni_loesungen.py schreiben  →  Review mit dem Agenten
```

Reihenfolge nach Uni-Kapiteln: 2.1 Variable/Datentyp → 2.2 Operator → 2.3 Kontrollstruktur → 2.4 Funktion → 2.5 Datenstruktur → 2.6 Zeitstempel → 3.1–3.4 numpy, matplotlib, pandas, random → 4.1 Error/Exception → 4.2 API (`yfinance`) → 4.3 GUI (Roulette).

**Editor: PyCharm** (nicht VS Code). Lösungen stehen in `uni_loesungen.py`: nur eigener Code ohne Aufgabentexte, deshalb darf die Datei ins öffentliche Repo. Das Uni-Material selbst bleibt lokal.

## Stand (2026-11-13)

- **Erledigt:** 2.1, 2.3, 2.4 und Zusatzaufgaben 1–3 zu 2.4 (gesichert in `uni_loesungen.py`).
- **Offen in 2.2:** Teil 1 (`x`/`y` statt `a`/`b`), Teil 3 (`+=` usw.), Teil 5 (`True`/`False` mit `and`/`or`/`not`).
- **Offen in 2.4 Zusatz:** 4 `zaehle_gerade`, 5 global/lokal mit `bonus`, 6 Default-Wert `potenz`. Die Aufgabentexte stehen im Chat vom 2026-11-13, kurz: zählen mit `ist_gerade`, `print(gesamt)` außerhalb der Funktion testen, `potenz(basis, exponent=2)`.
- **Bewerbungs-Basics:** durchgearbeitet und gelöscht (2026-11-13). Wackelig: Methoden raten (`append[...]`, `.replace`/`.rename`), `dict[key] = wert`, `.items()`, FizzBuzz-Reihenfolge.
- **Nächster Einstieg:** 2.5 Datenstruktur.
- **Wackelig:** `+=` (Variable verändern statt nur rechnen), `print` vs. `return`, Accumulator-Muster, `for` vs. `while`, Funktionen aufrufen statt nur definieren.

## Setup

```bash
cd python_learning
python3 -m venv .venv                       # einmalig, Python 3.14
.venv/bin/pip install -r requirements.txt
```

PyCharm: `python_learning/` öffnen → Settings → Python Interpreter → *Add Local Interpreter* → *Existing* → `python_learning/.venv/bin/python`. Notebooks (`.ipynb`) laufen dann über `ipykernel` aus dieser venv.

`yfinance` (Kapitel 4.2) wird erst bei Bedarf nachinstalliert.

## Ordner

```text
python_learning/
├── README.md
├── requirements.txt   Dependencies der venv
├── uni_loesungen.py   Felix' Lösungen zu den Uni-Übungen
├── python_basics.py   Felix' eigene Mitcode-Datei
├── .venv/             lokale Umgebung (nicht in Git)
└── uni_material/      Uni-Dateien aus Google Drive (nur lokal, nicht in Git)
```
