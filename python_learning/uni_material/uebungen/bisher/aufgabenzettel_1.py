import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── Aufgabenzettel 1: gemischte Klausurübungen (2.1–4.1) ────────
#
# Erst auf Papier lösen, dann hier abtippen und ausführen.
# Variablen- und Funktionsnamen genau so verwenden wie angegeben.
#
# Aufgabe 1 (Schleife + Bedingung):
#   Summe aller Zahlen von 1 bis 200, die durch 7, aber NICHT durch 2
#   teilbar sind → Variable summe1, ausgeben.

summe1 = 0
for i in range(1, 201):
    if i % 7 == 0 and not i % 2 == 0:
        summe1 += i
print(summ1)

# Aufgabe 2.
#   Funktion versand(gewicht): bis einschließlich 2 kg → 4.99,
#   bis einschließlich 10 kg → 7.99, sonst → 14.99 zurückgeben.
#   versand(2) und versand(10.5) ausgeben.
def versand(gewicht):
    if gewicht <= 2:
        cost = 4.99
        return cost

    elif gewicht <= 10:
        cost = 7.99
        return cost

    else:
        cost = 14.99
        return cost

print(versand(2))
print(versand(10.5))

# Aufgabe 3 (String-Methoden):
#   wort = 'Klausurvorbereitung' in Kleinbuchstaben umwandeln und die
#   'u' zählen → anzahl_u, ausgeben.

wort = 'Klausurvorbereitung'

wort = wort.lower()

anzahl_u = wort.count('u')
print(wort)
print(anzahl_u)

# Aufgabe 4 (Liste):
#   noten = [2.3, 1.7, 4.0, 3.3, 1.0]
#   2.0 anhängen, 4.0 entfernen, Durchschnitt auf 2 Nachkommastellen
#   runden → schnitt, ausgeben.

noten = [2.3, 1.7, 4.0, 3.3, 1.0]

noten.append(2.0)
noten.remove(4.0)

import numpy as np

aufgabe4 = np.array(noten)
#Bestimmt .round, sehe grade nicht im cheatsheet
# sowas wie noten.round
avg = np.mean(aufgabe4)

# Aufgabe 5 (Dictionary + Funktion):
#   lager = {'Stift': 12, 'Heft': 5, 'Lineal': 0}
#   Funktion nachbestellen(lager) gibt eine Liste aller Artikel zurück,
#   deren Bestand kleiner als 6 ist. Ergebnis ausgeben.
lager = {'Stift': 12, 'Heft': 5, 'Lineal': 0}

def nachbestellen(lager):
    if lager.values() > 6:
        return
print(nachbestellen())

# Aufgabe 6 (Menge):
#   kurs_a = {'Anna', 'Ben', 'Cem', 'Dora'}, kurs_b = {'Ben', 'Dora', 'Emil'}
#   beide = wer in beiden Kursen ist, nur_a = wer nur in kurs_a ist.
#   Beide ausgeben.
kurs_a = {'Anna', 'Ben', 'Cem', 'Dora'}; kurs_b = {'Ben', 'Dora', 'Emil'}
5: Dict filtern = Schleife + Liste aufbauen

lager.values() > 6 vergleicht alle Werte auf einmal mit 6, und das geht nicht. Außerdem fehlen das Argument beim Aufruf und der Rückgabewert.

def nachbestellen(lager):
    erg = []
    for name, menge in lager.items():   # items() = Key UND Value
        if menge < 6:                   # „kleiner als 6“, nicht > 6
            erg.append(name)
    return erg                          # NACH der Schleife
print(nachbestellen(lager))             # ['Heft', 'Lineal']

7: Was die Aufgabe will

start    = 24.11.2026 09:00             → datetime aus ZAHLEN, kein strp/strf
ende     = start + 90 Minuten           → 2026-11-24 10:30:00
tage_bis = Tage vom 24.11. bis 24.12.   → (d2 - d1).days → 30

from datetime import datetime, timedelta
start = datetime(2026, 11, 24, 9, 0)
ende = start + timedelta(minutes=90)
tage_bis = (datetime(2026, 12, 24) - datetime(2026, 11, 24)).days
print(ende, tage_bis)                   # 2026-11-24 10:30:00 30
beide = kurs_a.intersection(kurs_b)
nur_a = kurs_a.difference(kurs_b)
print(beide)
print(nur_a)
# Aufgabe 7 (Zeitstempel):
#   start = 24.11.2026, 09:00 Uhr (datetime). Die Klausur dauert 90 Minuten
#   → ende (timedelta). Außerdem: Tage vom 24.11.2026 bis 24.12.2026
#   → tage_bis (int). Beides ausgeben.
import datetime as datetime

start = datetime(2026, 11, 24, 9, 0, 0)
# Hier weiss ich nicht mehr wann ich strp und wann strf brauche, bitte inn sheet mit einbringen fuer konkrete Aufgabenstellung
from dateutil.relativedelta import relativedelta
#Bei den Live Uebungen im sheet bitte auch dei aufgabenstellung drueebr schreiben kurz
ende = start + relativedelta(minute=90)

#Aufgabenstellung nicht verstanden, bitte wiederholen

# Aufgabe 8 (numpy):
#   arr = NumPy-Array mit 4, 8, 15, 16, 23, 42
#   gerade = alle geraden Elemente (bedingte Auswahl), mittel = Durchschnitt.
#   Beides ausgeben.

import numpy as np

arr = np.array([4, 8, 15, 16, 23, 42])
#Keine Ahnung wie man hier gerade zahlen macht, dachte an for schleife mit % 2 == 0, aber ist kein numpy - Frage: Muss man array immer mit ([]) schrieben oder nur () sthte im sheet nicht genau

mittel = np.mean(arr)
print(mittel)


# Aufgabe 9 (pandas):
#   DataFrame df mit Spalten 'Name' (Anna, Ben, Cem, Dora) und
#   'Punkte' (72, 48, 50, 91). Neue Spalte 'Bestanden' = Punkte mindestens 50.
#   anzahl_bestanden = Anzahl der Bestandenen. df und Anzahl ausgeben.

import pandas as pd

data = {'Name': ['Anna', 'Ben,', 'Cem', 'Dora'],
        'Punkte': [72, 48, 50 , 91],
        'Bestanden': ['']}

df = pd.DataFrame(data)

anzahl_bestanden = 0
if df['Punkte'] > 50:
    anzahl_bestanden += 1

print(anzahl_bestanden)

# Aufgabe 10 (Exception):
#   Funktion sicher_teilen(a, b) gibt a / b zurück. Bei Division durch 0
#   wird stattdessen 'Division durch 0' zurückgegeben (try/except).
#   sicher_teilen(10, 4) und sicher_teilen(5, 0) ausgeben.
# ────────────────────────────────────────────────────────────────

##Nicht pruefrelevant


# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    variablen={"summe1": 1372, "anzahl_u": 3, "schnitt": 2.06, "tage_bis": 30},
    aufrufe={"versand(2)": 4.99, "versand(10)": 7.99, "versand(10.5)": 14.99,
             "noten": [2.3, 1.7, 3.3, 1.0, 2.0],
             "sorted(nachbestellen(lager))": ["Heft", "Lineal"],
             "beide": {"Ben", "Dora"}, "nur_a": {"Anna", "Cem"},
             "str(ende)": "2026-11-24 10:30:00",
             "gerade.tolist()": [4, 8, 16, 42], "float(mittel)": 18.0,
             "df['Bestanden'].tolist()": [True, False, True, True],
             "int(anzahl_bestanden)": 3,
             "sicher_teilen(10, 4)": 2.5, "sicher_teilen(5, 0)": "Division durch 0"},
)
