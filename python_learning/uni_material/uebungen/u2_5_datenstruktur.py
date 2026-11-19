import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── 2.5 Datenstruktur ───────────────────────────────────────────
#
# 1. Tupel:
#    - mein_tupel mit 1, 'Hallo', 3.14, True
#    - drittes Element ausgeben
#
# 2. Liste:
#    - meine_liste mit 1, 'Hallo', 3.14, True
#    - zweiten Wert zu 'Welt' ändern
#    - 42 am Ende hinzufügen
#    - ersten Wert entfernen
#    - ganze Liste ausgeben
#
# 3. Dictionary:
#    - mein_dict mit 'Name': 'Max', 'Alter': 25, 'Stadt': 'Berlin'
#    - Wert von 'Name' ausgeben
#    - 'Alter' auf 26 ändern
#    - 'Beruf': 'Ingenieur' hinzufügen
#    - 'Stadt' entfernen
#    - ganzes Dictionary ausgeben
#
# 4. Menge:
#    - meine_menge mit 1, 2, 3, 4, 4, 5
#    - 6 hinzufügen, 3 entfernen
#    - prüfen, ob 2 enthalten ist, und das Ergebnis ausgeben
#    - ganze Menge ausgeben
#    - zweite_menge mit 4, 5, 6, 7
#    - Schnittmenge (intersection), Vereinigung (union) und
#      Differenz (difference) von meine_menge und zweite_menge ausgeben
# ────────────────────────────────────────────────────────────────

# DEIN CODE:

def summe(a, b, c):
    step1 = a + b
    step2 = plus * b
    return step2
summe(1, 2, 3)
print(summe)
























# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    ausgabe=["3.14",
             "['Welt', 3.14, True, 42]",
             "Max", "{'Name': 'Max', 'Alter': 26, 'Beruf': 'Ingenieur'}",
             "True", "{1, 2, 4, 5, 6}",
             "{4, 5, 6}", "{1, 2, 4, 5, 6, 7}", "{1, 2}"],
    variablen={"mein_tupel": (1, "Hallo", 3.14, True),
               "meine_liste": ["Welt", 3.14, True, 42],
               "mein_dict": {"Name": "Max", "Alter": 26, "Beruf": "Ingenieur"},
               "meine_menge": {1, 2, 4, 5, 6},
               "zweite_menge": {4, 5, 6, 7}},
)
