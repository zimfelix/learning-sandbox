import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── Drill 2.5 Datenstrukturen (Schwerpunkt) ─────────────────────
#
# Kurz, viele Wiederholungen. Erst auf Papier, Cheat Sheet erlaubt.
# Variablennamen genau so verwenden. Am Ende jeweils print(...).
#
# ── Tupel & Liste: Zugriff ───────────────────────────────────────
# Aufgabe 1:
#   t = (3, 'Uni', 7.5, False, 'Kronach')
#   el2 = zweites Element, letztes = letztes Element (negativer Index),
#   n_t = Anzahl Elemente.
#
# Aufgabe 2:
#   liste = [10, 20, 30, 40, 50]
#   teil = Elemente von Index 1 bis 3 (Slicing), anfang = die ersten zwei.
#
# Aufgabe 3:
#   punkte = [('Anna', 72), ('Ben', 48), ('Cem', 91)]
#   wert = die Punktzahl von Cem, name2 = der Name im zweiten Tupel.
#
# ── Liste: verändern ─────────────────────────────────────────────
# Aufgabe 4:
#   zahlen = [3, 8, 1, 8, 5]
#   9 ans Ende anhängen, 7 an Index 0 einfügen, den Wert 8 entfernen
#   (nur das erste Vorkommen), das letzte Element mit pop() entfernen.
#   anzahl_8 = wie oft kommt 8 danach noch vor? zahlen ausgeben.
#
# Aufgabe 5:
#   noten = [2.7, 1.3, 3.0, 1.0]
#   Aufsteigend sortieren. beste = erstes Element, schlechteste = letztes.
#   Danach [2.0, 4.0] in EINEM Schritt anhängen. laenge = Anzahl Noten.
#
# Aufgabe 6:
#   obst = ['Apfel', 'Kiwi', 'Birne'] umdrehen.
#   hat_kiwi / hat_mango = ist 'Kiwi' / 'Mango' enthalten? (True/False)
#
# ── Dictionary ───────────────────────────────────────────────────
# Aufgabe 7:
#   student = {'Name': 'Lena', 'Alter': 21, 'Fach': 'WI'}
#   Alter auf 22 ändern, 'Semester': 1 hinzufügen, 'Fach' entfernen.
#   schluessel = alle Keys als Liste. student ausgeben.
#
# Aufgabe 8:
#   lager = {'Apfel': 5, 'Brot': 0, 'Milch': 12, 'Ei': 3}
#   Mit EINER Schleife über die Key-Value-Paare:
#   gesamt = Summe aller Bestände, leer = Liste der Artikel mit Bestand 0.
#
# Aufgabe 9:
#   ist_key = ist 'Milch' ein Key von lager?
#   ist_wert = ist 12 ein Wert von lager?
#   ist_key_12 = was liefert 12 in lager? (Erst überlegen, dann testen!)
#
# ── Menge ────────────────────────────────────────────────────────
# Aufgabe 10:
#   doppelt = [1, 2, 2, 3, 3, 3, 4]
#   einzigartig = Menge daraus, anzahl_einzig = wie viele verschiedene?
#
# Aufgabe 11:
#   a = {'Python', 'SQL', 'Java'}, b = {'SQL', 'Excel', 'Python'}
#   gemeinsam = in beiden, nur_b = nur in b, anzahl_alle = Anzahl
#   aller verschiedenen Fächer.
#
# Aufgabe 12:
#   m = {1, 2, 3}. Füge 3 und 4 hinzu, entferne 10 OHNE Fehler,
#   entferne 1. laenge_m = Anzahl Elemente. Was steht in m?
#
# ── Funktion + Datenstruktur (Vorklausur-Stil) ───────────────────
# Aufgabe 13:
#   Funktion 'filter_gross' mit zwei Inputs (werte, grenze). Gibt eine
#   Liste aller Werte zurück, die mindestens so groß wie grenze sind.
#   Was gibt filter_gross([5, 12, 7, 20], 7) zurück?
#
# Aufgabe 14 (Bonus, schwerer):
#   Funktion 'zaehle_woerter' mit einem Input (text). Gibt ein Dictionary
#   zurück: Wort → wie oft es vorkommt. Was gibt
#   zaehle_woerter('a b a c b a') zurück?
# ────────────────────────────────────────────────────────────────

# DEIN CODE:




# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    variablen={"el2": "Uni", "letztes": "Kronach", "n_t": 5, "wert": 91, "name2": "Ben",
               "anzahl_8": 1, "beste": 1.0, "schlechteste": 3.0, "laenge": 6,
               "hat_kiwi": True, "hat_mango": False, "gesamt": 20,
               "ist_key": True, "ist_wert": True, "ist_key_12": False,
               "anzahl_einzig": 4, "anzahl_alle": 4, "laenge_m": 3},
    aufrufe={"teil": [20, 30, 40], "anfang": [10, 20], "zahlen": [7, 3, 1, 8, 5],
             "noten": [1.0, 1.3, 2.7, 3.0, 2.0, 4.0], "obst": ["Birne", "Kiwi", "Apfel"],
             "student": {"Name": "Lena", "Alter": 22, "Semester": 1},
             "schluessel": ["Name", "Alter", "Semester"], "leer": ["Brot"],
             "einzigartig": {1, 2, 3, 4}, "gemeinsam": {"SQL", "Python"}, "nur_b": {"Excel"},
             "m": {2, 3, 4}, "filter_gross([5, 12, 7, 20], 7)": [12, 7, 20],
             "zaehle_woerter('a b a c b a')": {"a": 3, "b": 2, "c": 1}},
)
