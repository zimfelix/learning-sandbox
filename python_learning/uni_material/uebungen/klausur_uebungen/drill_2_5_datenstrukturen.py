import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
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
t = (3, 'Uni', 7.5, False, 'Kronach')
el2 = t[1]
letztes = t[-1]
n_t = len(t)
print(el2)
print(letztes)
print(n_t)

# Aufgabe 2:
#   liste = [10, 20, 30, 40, 50]
#   teil = Elemente von Index 1 bis 3 (Slicing), anfang = die ersten zwei.
liste = [10, 20, 30, 40, 50]
teil = liste[1:4]
anfang = liste[0:2]
print(teil)
print(anfang)

# Aufgabe 3:
#   punkte = [('Anna', 72), ('Ben', 48), ('Cem', 91)]
#   wert = die Punktzahl von Cem, name2 = der Name im zweiten Tupel.
punkte = [('Anna', 72), ('Ben', 48), ('Cem', 91)]

for name, p in punkte:
    if name == 'Cem':
        wert = p

name2 = punkte[1][0]
print(wert)
print(name2)
#Fraglich obr ichitg/

# ── Liste: verändern ─────────────────────────────────────────────
# Aufgabe 4:
#   zahlen = [3, 8, 1, 8, 5]
#   9 ans Ende anhängen, 7 an Index 0 einfügen, den Wert 8 entfernen
#   (nur das erste Vorkommen), das letzte Element mit pop() entfernen.
#   anzahl_8 = wie oft kommt 8 danach noch vor? zahlen ausgeben.
zahlen = [3, 8, 1, 8, 5]
zahlen.append(9)
zahlen.insert(0, 7)  # Fix: zwei Argumente (Index, Wert), keine Liste
zahlen.remove(8)
print(zahlen)

zahlen.pop(-1)
print(zahlen)

anzahl_8 = zahlen.count(8)
print(anzahl_8)

# Aufgabe 5:
#   noten = [2.7, 1.3, 3.0, 1.0]
#   Aufsteigend sortieren. beste = erstes Element, schlechteste = letztes.
#   Danach [2.0, 4.0] in EINEM Schritt anhängen. laenge = Anzahl Noten.
noten = [2.7, 1.3, 3.0, 1.0]

noten.sort()
beste = noten[0]  # Fix: VOR extend, sonst falsche Liste
schlechteste = noten[-1]
print(beste, schlechteste)

noten.extend([2.0, 4.0])
print(noten)

laenge = len(noten)
print(laenge)

# Aufgabe 6:
#   obst = ['Apfel', 'Kiwi', 'Birne'] umdrehen.
#   hat_kiwi / hat_mango = ist 'Kiwi' / 'Mango' enthalten? (True/False)

obst = ['Apfel', 'Kiwi', 'Birne']
print(obst.reverse())


for x in obst:
    if x == 'Kiwi':
        hat_kiwi = True
    else:
        hat_kiwi = False
for i in obst:
    if x == 'Mango':
        hat_mango = True
    else:
        hat_mango = False
print(hat_kiwi)
print(hat_mango)

# ── Dictionary ───────────────────────────────────────────────────
# Aufgabe 7:
#   student = {'Name': 'Lena', 'Alter': 21, 'Fach': 'WI'}
#   Alter auf 22 ändern, 'Semester': 1 hinzufügen, 'Fach' entfernen.
#   schluessel = alle Keys als Liste. student ausgeben.
\\
# Aufgabe 9:
#   ist_key = ist 'Milch' ein Key von lager?
#   ist_wert = ist 12 ein Wert von lager?
#   ist_key_12 = was liefert 12 in lager? (Erst überlegen, dann testen!)


# Aufgabe 10:
#   doppelt = [1, 2, 2, 3, 3, 3, 4]
#   einzigartig = Menge daraus, anzahl_einzig = wie viele verschiedene?
doppelt = [1, 2, 2, 3, 3, 3, 4]

einzigartig = set(doppelt)
anzahl_einzig = len(einzigartig)


# Aufgabe 11:
#   a = {'Python', 'SQL', 'Java'}, b = {'SQL', 'Excel', 'Python'}
#   gemeinsam = in beiden, nur_b = nur in b, anzahl_alle = Anzahl
#   aller verschiedenen Fächer.
a = {'Python', 'SQL', 'Java'}
b = {'SQL', 'Excel', 'Python'}

gemeinsam = a.intersection(b)
nur_b = b.difference(a)
anzahle_alle = len(a.union(b))

# Aufgabe 12:
#   m = {1, 2, 3}. Füge 3 und 4 hinzu, entferne 10 OHNE Fehler,
#   entferne 1. laenge_m = Anzahl Elemente. Was steht in m?



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
