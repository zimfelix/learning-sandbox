import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── Aufgabenzettel 1: gemischte Klausurübungen (2.1–4.1) ────────
#
# Erst auf Papier lösen, dann hier abtippen und ausführen.
# Variablen- und Funktionsnamen genau so verwenden wie angegeben.
#
# Aufgabe 1 (Schleife + Bedingung):
#   Summe aller Zahlen von 1 bis 200, die durch 7, aber NICHT durch 2
#   teilbar sind → Variable summe1, ausgeben.
#
# Aufgabe 2 (Funktion + if/elif):
#   Funktion versand(gewicht): bis einschließlich 2 kg → 4.99,
#   bis einschließlich 10 kg → 7.99, sonst → 14.99 zurückgeben.
#   versand(2) und versand(10.5) ausgeben.
#
# Aufgabe 3 (String-Methoden):
#   wort = 'Klausurvorbereitung' in Kleinbuchstaben umwandeln und die
#   'u' zählen → anzahl_u, ausgeben.
#
# Aufgabe 4 (Liste):
#   noten = [2.3, 1.7, 4.0, 3.3, 1.0]
#   2.0 anhängen, 4.0 entfernen, Durchschnitt auf 2 Nachkommastellen
#   runden → schnitt, ausgeben.
#
# Aufgabe 5 (Dictionary + Funktion):
#   lager = {'Stift': 12, 'Heft': 5, 'Lineal': 0}
#   Funktion nachbestellen(lager) gibt eine Liste aller Artikel zurück,
#   deren Bestand kleiner als 6 ist. Ergebnis ausgeben.
#
# Aufgabe 6 (Menge):
#   kurs_a = {'Anna', 'Ben', 'Cem', 'Dora'}, kurs_b = {'Ben', 'Dora', 'Emil'}
#   beide = wer in beiden Kursen ist, nur_a = wer nur in kurs_a ist.
#   Beide ausgeben.
#
# Aufgabe 7 (Zeitstempel):
#   start = 24.11.2026, 09:00 Uhr (datetime). Die Klausur dauert 90 Minuten
#   → ende (timedelta). Außerdem: Tage vom 24.11.2026 bis 24.12.2026
#   → tage_bis (int). Beides ausgeben.
#
# Aufgabe 8 (numpy):
#   arr = NumPy-Array mit 4, 8, 15, 16, 23, 42
#   gerade = alle geraden Elemente (bedingte Auswahl), mittel = Durchschnitt.
#   Beides ausgeben.
#
# Aufgabe 9 (pandas):
#   DataFrame df mit Spalten 'Name' (Anna, Ben, Cem, Dora) und
#   'Punkte' (72, 48, 50, 91). Neue Spalte 'Bestanden' = Punkte mindestens 50.
#   anzahl_bestanden = Anzahl der Bestandenen. df und Anzahl ausgeben.
#
# Aufgabe 10 (Exception):
#   Funktion sicher_teilen(a, b) gibt a / b zurück. Bei Division durch 0
#   wird stattdessen 'Division durch 0' zurückgegeben (try/except).
#   sicher_teilen(10, 4) und sicher_teilen(5, 0) ausgeben.
# ────────────────────────────────────────────────────────────────

# DEIN CODE:




# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    variablen={"summe1": 1372, "anzahl_u": 3, "schnitt": 2.06, "tage_bis": 30},
    aufrufe={"versand(2)": 4.99, "versand(10)": 7.99, "versand(10.5)": 14.99,
             "noten": [2.3, 1.7, 3.3, 1.0, 2.0],
             "sorted(nachbestellen(lager))": ["Heft", "Lineal"],
             "beide": {"Ben", "Dora"}, "nur_a": {"Anna", "Cem"},
             "str(ende)": "2026-11-24 10:30:00",
             "gerade.tolist()": [4, 8, 16, 42], "float(mittel)": 18.0,
             "df['Bestanden'].tolist()": [True, False, True, True],
             "int(anzahl_bestanden)": 3,
             "sicher_teilen(10, 4)": 2.5, "sicher_teilen(5, 0)": "Division durch 0"},
)
