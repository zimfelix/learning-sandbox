import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── 3.1 numpy ───────────────────────────────────────────────────
#
# 1. Erzeugen und Anzeigen:
#    - Importiere numpy als np.
#    - arr = NumPy-Array mit den Werten 1 bis 20
#    - ausgeben
#
# 2. Berechnungen:
#    - summe, durchschnitt, maximum, minimum von arr berechnen
#    - alle vier ausgeben
#
# 3. Elementweise Operation:
#    - jedes Element von arr mal 2 → neues Array verdoppelt
#    - ausgeben
#
# 4. Indexierung und Slicing:
#    - Elemente von Index 5 bis einschließlich 10 → ausschnitt, ausgeben
#    - in arr alle Elemente von Index 3 bis einschließlich 7 durch 100 ersetzen
#    - arr ausgeben
#
# 5. Bedingte Auswahl:
#    - alle Elemente von arr, die größer als 10 sind → groesser_10
#    - ausgeben
# ────────────────────────────────────────────────────────────────

# DEIN CODE:




# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    ausgabe=["[ 6  7  8  9 10 11]"],
    aufrufe={"type(arr).__name__": "ndarray",
             "int(summe)": 210,
             "float(durchschnitt)": 10.5,
             "int(maximum)": 20,
             "int(minimum)": 1,
             "verdoppelt.tolist()": list(range(2, 41, 2)),
             "arr.tolist()": [1, 2, 3] + [100] * 5 + list(range(9, 21)),
             "groesser_10.tolist()": [100] * 5 + list(range(11, 21))},
)
