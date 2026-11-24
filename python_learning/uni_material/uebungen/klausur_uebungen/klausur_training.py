# ── Klausur-Training: neue Aufgaben im Stil der Vorklausuren ─────
#
# Gleicher Schwierigkeitsgrad wie klausur_beispiele.py (Stand 2026-11-19).
# Auf Papier lösen, dann abtippen und mit der Musterlösung unten prüfen.
#
# ── Typ 1: Schleife + Bedingung + Accumulator ────────────────────
#
# Aufgabe 1:
#   Zahlen zwischen 1 und 500, die durch 3 und durch 5 teilbar sind.
#   Berechne die Summe dieser Zahlen.
#
# Aufgabe 2:
#   Zahlen zwischen 100 und 300, die durch 4, aber NICHT durch 6
#   teilbar sind. Wie viele Zahlen sind das?
#
# Aufgabe 3:
#   Berechne das Produkt aller geraden Zahlen von 1 bis 10.
#
# Aufgabe 4:
#   Addiere 1 + 2 + 3 + ... so lange, bis die Summe größer als 1000 ist.
#   Bei welcher Zahl n ist das zum ersten Mal der Fall? (while-Schleife)
#
# ── Typ 2: Funktion + if + return ────────────────────────────────
#
# Aufgabe 5:
#   Funktion 'rabatt' mit zwei Inputs (preis, menge). Ist der Gesamtpreis
#   (preis mal menge) größer als 200, werden 10 % abgezogen. Gesamtpreis
#   zurückgeben. Was gibt rabatt(15, 20) zurück?
#
# Aufgabe 6:
#   Funktion 'pruefen' mit drei Inputs (a, b, c). Falls die Summe von a
#   und b größer als c ist, soll c davon abgezogen werden und das
#   Ergebnis zurückgegeben werden; sonst wird c zurückgegeben.
#   Welchen Wert gibt pruefen(12, 9, 25) zurück?
#
# Aufgabe 7:
#   Funktion 'note' mit einem Input (punkte):
#   mindestens 90 → 'sehr gut', mindestens 75 → 'gut',
#   mindestens 50 → 'bestanden', sonst → 'nicht bestanden'.
#   Was gibt note(75) zurück?
#
# Aufgabe 8:
#   Funktion 'maximum' mit drei Inputs (a, b, c), die die größte Zahl
#   zurückgibt, OHNE max() zu verwenden. Was gibt maximum(7, 19, 3) zurück?
#
# ── Typ 3: String-Methoden ───────────────────────────────────────
#
# Aufgabe 9:
#   Erstelle das String-Literal 'programmierung' und weise es der
#   Variablen x zu. Wandle es in Großbuchstaben um und zähle alle 'R'.
#
# Aufgabe 10:
#   Erstelle das String-Literal 'banane' und weise es der Variablen y zu.
#   Ersetze alle 'a' durch 'e' und zähle danach alle 'e'.
#
# Aufgabe 11:
#   satz = 'python ist toll und python ist einfach'
#   Zähle, wie oft 'python' vorkommt. Ersetze dann 'python' durch 'java'
#   und gib die Länge des neuen Strings aus.
#
# ── Typ 4: Kombination ───────────────────────────────────────────
#
# Aufgabe 12:
#   Zähle mit einer for-Schleife die Vokale (a, e, i, o, u) im String
#   'hochschule'.
#
# Aufgabe 13:
#   zahlen = [12, 7, 33, 18, 5, 40]
#   Berechne die Summe aller Zahlen, die größer als 10 sind.
#
# Aufgabe 14:
#   Funktion 'zaehle' mit zwei Inputs (text, zeichen), die zurückgibt,
#   wie oft zeichen in text vorkommt, OHNE .count() zu verwenden.
#   Was gibt zaehle('mississippi', 's') zurück?
#
# Achte auf die typischen Fehler aus klausur_beispiele.py:
#   '>=' bei "mindestens", return in jedem Fall, Ergebnis ausgeben,
#   Funktion auch aufrufen.
# ────────────────────────────────────────────────────────────────


# ── Musterlösungen (erst nach eigenem Versuch ansehen) ──────────

# Aufgabe 1 → 8415
summe = 0
for x in range(1, 501):
    if x % 3 == 0 and x % 5 == 0:
        summe += x
print(1, summe)

# Aufgabe 2 → 34
anzahl = 0
for x in range(100, 301):
    if x % 4 == 0 and x % 6 != 0:
        anzahl += 1
print(2, anzahl)

# Aufgabe 3 → 3840
produkt = 1
for x in range(2, 11, 2):
    produkt *= x
print(3, produkt)

# Aufgabe 4 → 45
n = 0
summe = 0
while summe <= 1000:
    n += 1
    summe += n
print(4, n)


# Aufgabe 5 → 270.0
def rabatt(preis, menge):
    gesamt = preis * menge
    if gesamt > 200:
        gesamt = gesamt * 0.9
    return gesamt


print(5, rabatt(15, 20))


# Aufgabe 6 → 25
def pruefen(a, b, c):
    if a + b > c:
        return a + b - c
    return c


print(6, pruefen(12, 9, 25))


# Aufgabe 7 → 'gut'
def note(punkte):
    if punkte >= 90:
        return 'sehr gut'
    elif punkte >= 75:
        return 'gut'
    elif punkte >= 50:
        return 'bestanden'
    else:
        return 'nicht bestanden'


print(7, note(75))


# Aufgabe 8 → 19
def maximum(a, b, c):
    groesste = a
    if b > groesste:
        groesste = b
    if c > groesste:
        groesste = c
    return groesste


print(8, maximum(7, 19, 3))

# Aufgabe 9 → 3
x = 'programmierung'
x = x.upper()
print(9, x.count('R'))

# Aufgabe 10 → 3
y = 'banane'
y = y.replace('a', 'e')
print(10, y.count('e'))

# Aufgabe 11 → 2 / 34
satz = 'python ist toll und python ist einfach'
print(11, satz.count('python'))
satz = satz.replace('python', 'java')
print(11, len(satz))

# Aufgabe 12 → 3
vokale = 0
for buchstabe in 'hochschule':
    if buchstabe in 'aeiou':
        vokale += 1
print(12, vokale)

# Aufgabe 13 → 103
zahlen = [12, 7, 33, 18, 5, 40]
summe = 0
for z in zahlen:
    if z > 10:
        summe += z
print(13, summe)


# Aufgabe 14 → 4
def zaehle(text, zeichen):
    anzahl = 0
    for buchstabe in text:
        if buchstabe == zeichen:
            anzahl += 1
    return anzahl


print(14, zaehle('mississippi', 's'))
