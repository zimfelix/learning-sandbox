import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── Drill 2.6 Zeitstempel ───────────────────────────────────────
#
# Merke: Zahlen → datetime(...) · Text → strptime · „als Text“ → strftime
#        „dauert / +X Minuten“ → timedelta · „+X Monate“ → relativedelta
#
# Aufgabe 1:
#   Parse '26.11.2026 10:00' in ein datetime → klausur.
#   text = klausur als String im Format '26.11.2026 um 10:00'.
#
# Aufgabe 2:
#   Die Klausur dauert 120 Minuten → ende (datetime).
#
# Aufgabe 3:
#   tage = ganze Tage vom 26.11.2026 bis 24.12.2026 (int).
#
# Aufgabe 4:
#   Lernstart war am 25.11.2026 um 18:30. stunden = Stunden bis
#   Klausurbeginn (float, gesamt).
#
# Aufgabe 5:
#   Parse '2027-03-01' → d. monat und jahr aus d auslesen (int).
#
# Aufgabe 6:
#   in3 = klausur plus 3 Monate, erster = klausur auf den 1. des
#   Monats gesetzt (relativedelta).
#
# Aufgabe 7:
#   diff = klausur minus 20.11.2026 08:00. diff_tage = ganze Tage,
#   rest_std = verbleibende Stunden (ohne die ganzen Tage).
# ────────────────────────────────────────────────────────────────

# DEIN CODE:




# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    variablen={"text": "26.11.2026 um 10:00", "tage": 28, "stunden": 15.5,
               "monat": 3, "jahr": 2027, "diff_tage": 6, "rest_std": 2},
    aufrufe={"str(klausur)": "2026-11-26 10:00:00", "str(ende)": "2026-11-26 12:00:00",
             "str(in3)": "2027-02-26 10:00:00", "str(erster)": "2026-11-01 10:00:00"},
)
