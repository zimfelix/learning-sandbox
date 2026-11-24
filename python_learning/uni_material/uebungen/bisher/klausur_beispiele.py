# ── Klausur-Beispiele: Original-Aufgaben aus Vorklausuren ────────
#
# Referenz für den Schwierigkeitsgrad der Papierklausur (Stand 2026-11-17).
# Neue Übungsaufgaben fürs Papier-Training an diesem Niveau ausrichten:
# kurze Aufgaben, die mehrere Grundbausteine kombinieren
# (Schleife + Bedingung + Accumulator, Funktion + if + return,
# String-Methoden).
#
# Aufgabe 1:
#   Zahlen zwischen 10 und 1000, die durch 7 und durch 2 teilbar sind.
#   Berechne die Summe dieser Zahlen.
#
# Aufgabe 2:
#   Funktion 'rechnen' mit drei Inputs (a, b, c). Falls das Produkt von
#   a und b mindestens 100 ist, soll es zu c addiert werden. Ergebnis
#   zurückgeben. Welchen Wert gibt rechnen zurück, wenn a = 4, b = 26
#   und c = 7 sind?
#
# Aufgabe 3:
#   Erstelle das String-Literal 'wirtschaftsinformatik' und weise es der
#   Variablen y zu. Ersetze alle 'i' durch 'o' und zähle danach alle 'o'.
#
# Typische Fehler beim ersten Versuch (2026-11-17):
#   - 'and if' statt 'and' in einer Bedingung
#   - np.sum(...) berechnet, aber nicht ausgegeben
#   - '>' statt '>=' bei "mindestens"
#   - return nur im if → None im anderen Fall
#   - c + b statt c + x (Variablen verwechselt)
#   - Funktion definiert, aber nicht aufgerufen
# ────────────────────────────────────────────────────────────────


# ── Musterlösungen (erst nach eigenem Versuch ansehen) ──────────

# Aufgabe 1 → 35784
summe = 0
for x in range(10, 1001):
    if x % 7 == 0 and x % 2 == 0:
        summe += x
print(summe)


# Aufgabe 2 → 111
def rechnen(a, b, c):
    x = a * b
    if x >= 100:
        c += x
    return c


print(rechnen(4, 26, 7))

# Aufgabe 3 → 4
y = 'wirtschaftsinformatik'
y = y.replace('i', 'o')
print(y.count('o'))
