import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── 2.5b Mengen – Wiederholung (klausurrelevant) ────────────────
#
# Erst auf Papier lösen, dann hier abtippen und ausführen.
#
# Gegeben:
a = {'apple', 'banana', 'cherry'}
b = {'cherry', 'strawberry', 'banana'}
#
# Teil 2 – selbst schreiben:
# 1. Lege die Menge c mit 'kiwi' und 'apple' an, und zwar auf zwei
#    Arten: einmal mit {}, einmal mit set([...]).
# 2. Füge 'banana' zu c hinzu. Was passiert, wenn du 'banana' ein
#    zweites Mal hinzufügst?
# 3. Gib alle Früchte aus, die in a und in c vorkommen.
# 4. Gib alle Früchte aus, die in b, aber nicht in c vorkommen.
#
# Teil 3 – Verständnis (Antwort als Kommentar):
# Warum schreibt man c = set() statt c = {} für eine leere Menge?
# ────────────────────────────────────────────────────────────────

# DEIN CODE:




# Teil 3 – Antwort:
#




# ── Test (nicht ändern) ─────────────────────────────────────────
# Prüft nur c; die Reihenfolge in Mengen-Ausgaben ist nicht fest.
check.ende(
    globals(),
    variablen={"c": {"kiwi", "apple", "banana"}},
)
