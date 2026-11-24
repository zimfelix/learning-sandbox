import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── Drill 3.3 pandas ────────────────────────────────────────────
#
# Aufgabe 1:
#   DataFrame df mit den Spalten
#     Name:  Lena, Tom, Mia, Ali, Eva
#     Alter: 21, 25, 22, 30, 24
#     Stadt: Kronach, Coburg, Kronach, Bamberg, Coburg
#     Note:  1.7, 2.3, 1.3, 3.0, 2.0
#   df ausgeben.
#
# Aufgabe 2:
#   Neue Spalte 'Jahrgang' = 2026 minus Alter.
#
# Aufgabe 3:
#   Neue Spalte 'Gut' = Note höchstens 2.0 (True/False).
#   anzahl_gut = wie viele haben 'Gut'?
#
# Aufgabe 4:
#   Ändere die Note von Tom auf 1.7.
#   schnitt = Durchschnittsnote danach (auf 2 Stellen gerundet).
#   Frage: Ändert sich Toms Wert in 'Gut' automatisch?
#
# Aufgabe 5:
#   aeltester = Name der ältesten Person.
#
# Aufgabe 6:
#   alter_stadt = durchschnittliches Alter pro Stadt (groupby).
#
# Aufgabe 7:
#   nur_kronach = alle Zeilen mit Stadt Kronach,
#   anzahl_kronach = wie viele Zeilen sind das?
#
# Aufgabe 8:
#   Entferne die Zeile mit Index 3. zeilen = Anzahl Zeilen danach.
#   Speichere df als 'drill.csv' (ohne Index), lade sie in df2 und
#   gib df2 aus.
# ────────────────────────────────────────────────────────────────

# DEIN CODE:




# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    variablen={"aeltester": "Ali", "anzahl_kronach": 2, "zeilen": 4},
    aufrufe={"int(anzahl_gut)": 3, "float(schnitt)": 1.94,
             "df['Jahrgang'].tolist()": [2005, 2001, 2004, 2002],
             "df['Gut'].tolist()": [True, False, True, True],
             "df['Note'].tolist()": [1.7, 1.7, 1.3, 2.0],
             "alter_stadt.to_dict()": {"Bamberg": 30.0, "Coburg": 24.5, "Kronach": 21.5},
             "len(df2)": 4},
)
