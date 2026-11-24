import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── Drill 3.1 numpy ─────────────────────────────────────────────
#
# Aufgabe 1:
#   a = NumPy-Array mit 5, 10, 15, … 50 (arange mit Schrittweite).
#   summe, mittel, groesster berechnen.
#
# Aufgabe 2:
#   b = jedes Element von a mal 3, c = jedes Element plus 100.
#   b2 = das dritte Element von b.
#
# Aufgabe 3:
#   mitte = Elemente von a mit Index 2 bis 5, ende3 = die letzten drei.
#
# Aufgabe 4 (bedingte Auswahl):
#   zwischen = alle Elemente von a größer 12 UND kleiner 38,
#   ungerade = alle ungeraden Elemente von a,
#   anzahl_ueber_30 = Anzahl Elemente größer 30.
#
# Aufgabe 5:
#   d = dasselbe Array wie a (neu erzeugen). Ersetze Index 0 bis 2
#   durch 0. summe_neu = Summe von d.
#
# Aufgabe 6 (Vorklausur-Typ):
#   Mittelwert m50 und Standardabweichung s50 (auf 2 Stellen gerundet)
#   aller Zahlen von 1 bis 50. Welche Werte kommen heraus?
# ────────────────────────────────────────────────────────────────

# DEIN CODE:




# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    variablen={"anzahl_ueber_30": 4},
    aufrufe={"int(summe)": 275, "float(mittel)": 27.5, "int(groesster)": 50,
             "b.tolist()": [15, 30, 45, 60, 75, 90, 105, 120, 135, 150], "int(b2)": 45,
             "c.tolist()[:2]": [105, 110], "mitte.tolist()": [15, 20, 25, 30],
             "ende3.tolist()": [40, 45, 50], "zwischen.tolist()": [15, 20, 25, 30, 35],
             "ungerade.tolist()": [5, 15, 25, 35, 45], "d.tolist()[:4]": [0, 0, 0, 20],
             "int(summe_neu)": 245, "float(m50)": 25.5, "float(s50)": 14.43},
)
