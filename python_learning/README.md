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
Vorlesungs-Notebook lesen + ausführen  →  Übungs-Notebook selbst lösen  →  Review mit dem Agenten
```

Reihenfolge nach Uni-Kapiteln: 2.1 Variable/Datentyp → 2.2 Operator → 2.3 Kontrollstruktur → 2.4 Funktion → 2.5 Datenstruktur → 2.6 Zeitstempel → 3.1–3.4 numpy, matplotlib, pandas, random → 4.1 Error/Exception → 4.2 API (`yfinance`) → 4.3 GUI (Roulette).

Die Notebooks laufen in VS Code oder PyCharm mit der `.venv` als Kernel. Lösungen bleiben wie das Uni-Material lokal (Repo ist öffentlich).

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
├── python_basics.py   Felix' eigene Mitcode-Datei
├── bewerbung_basics.py     7 "Mach mal …"-Aufgaben + FizzBuzz, zum Wiederholen
├── bewerbung_loesungen.py  Lösungen dazu (erst nach eigenem Versuch)
├── .venv/             lokale Umgebung (nicht in Git)
└── uni_material/      Uni-Dateien aus Google Drive (nur lokal, nicht in Git)
```
