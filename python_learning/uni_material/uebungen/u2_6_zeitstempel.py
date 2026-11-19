import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── 2.6 Zeitstempel ─────────────────────────────────────────────
#
# 1. Aktuellen Zeitstempel erhalten:
#    - Importiere datetime aus der Bibliothek datetime.
#    - aktueller_zeitstempel = aktueller Zeitpunkt
#    - ausgeben
#
# 2. Zeitstempel formatieren:
#    - aktueller_zeitstempel als String im Format TT.MM.JJJJ HH:MM:SS
#    - ausgeben
#
# 3. Zeitdifferenz berechnen:
#    - frueher_zeitstempel = fester Zeitpunkt, z. B. 2022-01-01 12:00:00
#    - Differenz aktueller - früherer Zeitstempel berechnen
#    - Differenz in Tagen und Stunden ausgeben
#
# 4. Zeitstempel aus String parsen:
#    - zeitstempel_string = '2023-06-15 08:30:00'
#    - in ein datetime-Objekt umwandeln → geparster_zeitstempel
#    - ausgeben
# ────────────────────────────────────────────────────────────────

# DEIN CODE:



# ── Test (nicht ändern) ─────────────────────────────────────────
import datetime as _dt

check.ende(
    globals(),
    ausgabe=["2023-06-15 08:30:00"],
    variablen={"frueher_zeitstempel": _dt.datetime(2022, 1, 1, 12, 0, 0),
               "zeitstempel_string": "2023-06-15 08:30:00",
               "geparster_zeitstempel": _dt.datetime(2023, 6, 15, 8, 30, 0)},
    aufrufe={"type(aktueller_zeitstempel).__name__": "datetime"},
)
