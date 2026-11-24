import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── Aufgabenzettel 2: Klausurübungen im Vorklausur-Stil (2.1–3.4) ─
#
# Erst auf Papier lösen (Cheat Sheet erlaubt), dann hier abtippen.
# Variablen- und Funktionsnamen genau so verwenden wie angegeben.
# Jede Frage „Welchen Wert …?“ zusätzlich als Zahl auf Papier notieren.
#
# Aufgabe 1 (Schleife + Bedingung + Zählen):
#   Wie viele Zahlen zwischen 50 und 500 (beide inklusive) sind durch 9,
#   aber NICHT durch 4 teilbar? → anzahl1, ausgeben.
#
# Aufgabe 2 (Funktion + if + return):
#   Funktion 'tarif' mit drei Inputs (a, b, c). Ist die Summe von a und b
#   kleiner als c, wird das Produkt von a und b zurückgegeben, sonst c
#   minus a. Welche Werte geben tarif(3, 4, 10) und tarif(6, 5, 10) zurück?
#
# Aufgabe 3 (String-Methoden):
#   Erstelle das String-Literal 'datenbanksystem' und weise es der
#   Variablen y zu. Ersetze alle 'a' durch 'e' und zähle danach alle 'e'
#   → anzahl_e, ausgeben.
#
# Aufgabe 4 (Liste):
#   zahlen = [5, 12, 7, 3, 12, 9]
#   Entferne den Wert 12 (nur das erste Vorkommen), füge 20 an Index 1 ein
#   und sortiere absteigend. Welches ist danach das dritte Element?
#   → drittes, ausgeben.
#
# Aufgabe 5 (Dictionary):
#   preise = {'Apfel': 0.5, 'Brot': 2.2, 'Milch': 1.1}
#   Ändere Milch auf 1.3, füge 'Käse': 3.0 hinzu, entferne 'Brot'.
#   Summe aller Preise (auf 2 Nachkommastellen gerundet) → summe_preise.
#
# Aufgabe 6 (Menge):
#   a = {2, 4, 6, 8, 10}, b = {3, 6, 9}
#   schnitt = Schnittmenge, nur_a = was nur in a ist,
#   anzahl_vereinigung = Anzahl Elemente der Vereinigung. Alle ausgeben.
#
# Aufgabe 7 (Zeitstempel):
#   Parse den String '15.03.2027 14:45' in ein datetime → termin.
#   tage = ganze Tage von termin bis 01.05.2027 00:00 (int).
#   text = termin als String im Format TT.MM.JJJJ. Beides ausgeben.
#
# Aufgabe 8 (numpy, bedingte Auswahl):
#   x = NumPy-Array mit den Zahlen 1 bis 50.
#   mittel3 = Mittelwert aller durch 3 teilbaren Elemente,
#   anzahl_gross = Anzahl der Elemente größer als 40. Beides ausgeben.
#
# Aufgabe 9 (numpy, Vorklausur-Typ):
#   Berechne Mittelwert und Standardabweichung aller GERADEN Zahlen von
#   2 bis 100 → mittel_g, std_g (std_g auf 2 Nachkommastellen runden).
#   Welche Werte kommen heraus?
#
# Aufgabe 10 (pandas):
#   DataFrame df mit den Spalten
#     Produkt:   Maus, Tastatur, Monitor, Kabel
#     Kategorie: Zubehör, Zubehör, Display, Zubehör
#     Preis:     25, 45, 180, 8
#     Menge:     4, 2, 1, 10
#   a) Neue Spalte 'Umsatz' = Preis mal Menge.
#   b) teuerstes = Name des Produkts mit dem höchsten Preis.
#   c) umsatz_kat = durchschnittlicher Umsatz pro Kategorie (groupby).
#   d) Danach die Zeile mit Index 3 entfernen. df ausgeben.
#
# Aufgabe 11 (random + Seed):
#   Setze den Seed auf 7 und würfle 5-mal (ganze Zahl 1 bis 6), die Würfe
#   in einer Liste wuerfe sammeln. summe_wuerfe = Summe der Würfe.
#   Welche Summe kommt heraus? Warum ist sie bei jedem Lauf gleich?
#
# Aufgabe 12 (random + Schleife):
#   Setze den Seed auf 1 und erzeuge 1000 float-Zufallszahlen zwischen
#   10 und 20 in der Liste werte. mittel_w = Mittelwert (auf 1 Nach-
#   kommastelle runden). Welchen Wert erwartest du ungefähr – und warum?
# ────────────────────────────────────────────────────────────────

# DEIN CODE:




# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    variablen={"anzahl1": 38, "anzahl_e": 4, "drittes": 9, "summe_preise": 4.8,
               "anzahl_vereinigung": 7, "tage": 46, "text": "15.03.2027",
               "anzahl_gross": 10, "teuerstes": "Monitor", "summe_wuerfe": 16},
    aufrufe={"tarif(3, 4, 10)": 12, "tarif(6, 5, 10)": 4,
             "y": "detenbenksystem", "zahlen": [20, 12, 9, 7, 5, 3],
             "preise": {"Apfel": 0.5, "Milch": 1.3, "Käse": 3.0},
             "schnitt": {6}, "nur_a": {2, 4, 8, 10},
             "float(mittel3)": 25.5, "float(mittel_g)": 51.0, "float(std_g)": 28.86,
             "umsatz_kat.to_dict()": {"Display": 180.0, "Zubehör": 90.0},
             "df['Umsatz'].tolist()": [100, 90, 180],
             "wuerfe": [3, 2, 4, 6, 1], "float(mittel_w)": 15.1},
)
