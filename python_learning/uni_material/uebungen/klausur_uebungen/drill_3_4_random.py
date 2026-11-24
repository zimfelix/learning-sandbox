import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── Drill 3.4 random ────────────────────────────────────────────
#
# Folie: seed, uniform, randint, choice · Übung: shuffle, sample
# Wegen seed sind alle Ergebnisse fest und testbar.
#
# Aufgabe 1:
#   Seed 3. Danach in DIESER Reihenfolge:
#   wurf = ganze Zahl 1 bis 6,
#   temp = Kommazahl zwischen -5 und 30 (auf 1 Stelle gerundet),
#   farbe = zufälliges Element aus ['rot', 'gruen', 'blau'].
#
# Aufgabe 2:
#   Seed 10. 8-mal würfeln (1 bis 6), Würfe in der Liste wuerfe sammeln.
#   vieren = wie oft wurde eine 4 gewürfelt?
#
# Aufgabe 3:
#   Seed 5. lotto = 6 verschiedene Zahlen aus 1 bis 49 (ohne Zurücklegen),
#   danach aufsteigend sortiert.
#
# Aufgabe 4:
#   Seed 0. karten = ['A', 'K', 'D', 'B', '10'] mischen.
#   erste = erste Karte nach dem Mischen.
#
# Aufgabe 5 (Vorklausur-Stil):
#   Funktion 'zufall_liste' mit zwei Inputs (n, s): setzt den Seed s und
#   gibt eine Liste mit n ganzen Zufallszahlen von 1 bis 100 zurück.
#   gleich = zufall_liste(5, 1) == zufall_liste(5, 1). Was kommt heraus
#   und warum?
# ────────────────────────────────────────────────────────────────

# DEIN CODE:




# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    variablen={"wurf": 2, "temp": 15.7, "farbe": "rot", "vieren": 3,
               "erste": "D", "gleich": True},
    aufrufe={"wuerfe": [5, 1, 4, 4, 5, 1, 2, 4], "lotto": [17, 23, 34, 40, 42, 45],
             "karten": ["D", "K", "A", "10", "B"],
             "zufall_liste(5, 1)": [18, 73, 98, 9, 33]},
)
