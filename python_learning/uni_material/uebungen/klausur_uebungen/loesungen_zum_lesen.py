# ── Lösungen zum Durchlesen (Klausur 26.11.2026) ─────────────────
# Typ 3 + 4 aus klausur_training.py, dann Drill 3.1 numpy,
# 3.3 pandas, 3.4 random. Hinter jeder Zeile: Signalwort → Ergebnis.
import random

import numpy as np
import pandas as pd

# ═══ Typ 3: Strings ═════════════════════════════════════════════

# Aufgabe 9: 'programmierung' groß machen, alle 'R' zählen
x = 'programmierung'
x = x.upper()                     # „Großbuchstaben“ → SPEICHERN!
print(9, x.count('R'))            # „zähle alle R“ → 3

# Aufgabe 10: 'banane', a → e ersetzen, dann 'e' zählen
y = 'banane'
y = y.replace('a', 'e')           # „ersetze“ → 'benene'
print(10, y.count('e'))           # → 3

# Aufgabe 11: 'python' zählen, durch 'java' ersetzen, Länge
satz = 'python ist toll und python ist einfach'
print(11, satz.count('python'))   # „wie oft“ bestimmter Wert → 2
satz = satz.replace('python', 'java')
print(11, len(satz))              # „Länge“ → 34

# ═══ Typ 4: Kombination (Schleife + if + Zähler) ════════════════

# Aufgabe 12: Vokale in 'hochschule' zählen (for-Schleife)
vokale = 0                        # Anzahl → Start 0
for buchstabe in 'hochschule':
    if buchstabe in 'aeiou':      # „ist ein Vokal“ → in
        vokale += 1               # Anzahl → += 1
print(12, vokale)                 # → 3

# Aufgabe 13: Summe aller Zahlen größer 10
zahlen = [12, 7, 33, 18, 5, 40]
summe = 0                         # Summe → Start 0
for z in zahlen:
    if z > 10:                    # „größer als“ → >
        summe += z                # Summe → += z (die Zahl selbst)
print(13, summe)                  # → 103


# Aufgabe 14: zaehle(text, zeichen) OHNE .count()
def zaehle(text, zeichen):
    anzahl = 0
    for buchstabe in text:
        if buchstabe == zeichen:  # == vergleicht
            anzahl += 1
    return anzahl                 # NACH der Schleife!


print(14, zaehle('mississippi', 's'))  # → 4

# ═══ Drill 3.1 numpy ════════════════════════════════════════════

# 1) Array 5, 10, … 50 · Summe, Mittel, Maximum
a = np.arange(5, 51, 5)           # Start 5, Stop 51 (exklusiv), Schritt 5
summe = np.sum(a)                 # → 275
mittel = np.mean(a)               # → 27.5
groesster = np.max(a)             # → 50
print('3.1/1', summe, mittel, groesster)

# 2) „jedes Element“ → direkt mit a rechnen, KEINE Schleife
b = a * 3                         # → [15 30 … 150]
c = a + 100                       # → [105 110 … 150]
b2 = b[2]                         # „drittes Element“ → Index 2 → 45
print('3.1/2', b, c, b2)

# 3) Slicing: Stop ist exklusiv
mitte = a[2:6]                    # „Index 2 bis 5“ → :6 → [15 20 25 30]
ende3 = a[-3:]                    # „letzte drei“ → [40 45 50]
print('3.1/3', mitte, ende3)

# 4) Masken: & statt and, jede Bedingung in Klammern
zwischen = a[(a > 12) & (a < 38)]  # → [15 20 25 30 35]
ungerade = a[a % 2 != 0]          # → [5 15 25 35 45]
anzahl_ueber_30 = len(a[a > 30])  # „Anzahl“ → len → 4
print('3.1/4', zwischen, ungerade, anzahl_ueber_30)

# 5) Elemente ersetzen
d = np.arange(5, 51, 5)
d[0:3] = 0                        # „Index 0 bis 2“ → :3
summe_neu = np.sum(d)             # → 245
print('3.1/5', d, summe_neu)

# 6) Mittelwert + Standardabweichung von 1 bis 50
zahlen50 = np.arange(1, 51)       # „1 bis 50“ → Stop 51
m50 = np.mean(zahlen50)           # → 25.5
s50 = round(np.std(zahlen50), 2)  # „2 Stellen“ → round(…, 2) → 14.43
print('3.1/6', m50, s50)

# ═══ Drill 3.3 pandas ═══════════════════════════════════════════

# 1) DataFrame = Dict: Spaltenname → Liste
df = pd.DataFrame({
    'Name': ['Lena', 'Tom', 'Mia', 'Ali', 'Eva'],
    'Alter': [21, 25, 22, 30, 24],
    'Stadt': ['Kronach', 'Coburg', 'Kronach', 'Bamberg', 'Coburg'],
    'Note': [1.7, 2.3, 1.3, 3.0, 2.0],
})
print(df)

# 2) „neue Spalte“ → df['Neu'] = Rechnung mit anderer Spalte
df['Jahrgang'] = 2026 - df['Alter']

# 3) „höchstens“ → <= · True zählt als 1 → .sum() = Anzahl
df['Gut'] = df['Note'] <= 2.0
anzahl_gut = df['Gut'].sum()      # → 3
print('3.3/3', anzahl_gut)

# 4) Einzelnen Wert ändern: df.loc[Zeile, Spalte]
df.loc[df['Name'] == 'Tom', 'Note'] = 1.7
schnitt = round(df['Note'].mean(), 2)  # → 1.94
print('3.3/4', schnitt)           # 'Gut' ändert sich NICHT automatisch

# 5) Name der ältesten Person: idxmax = Zeile des Maximums
aeltester = df.loc[df['Alter'].idxmax(), 'Name']  # → 'Ali'
print('3.3/5', aeltester)

# 6) „pro Stadt“ → groupby
alter_stadt = df.groupby('Stadt')['Alter'].mean()
print('3.3/6', alter_stadt)       # Bamberg 30.0, Coburg 24.5, Kronach 21.5

# 7) Zeilen filtern + zählen
nur_kronach = df[df['Stadt'] == 'Kronach']
anzahl_kronach = len(nur_kronach)  # → 2
print('3.3/7', anzahl_kronach)

# 8) Zeile löschen, CSV speichern + laden
df = df.drop(3)                   # Index 3 = Ali → SPEICHERN!
zeilen = len(df)                  # → 4
df.to_csv('drill.csv', index=False)
df2 = pd.read_csv('drill.csv')
print('3.3/8', zeilen)
print(df2)

# ═══ Drill 3.4 random ═══════════════════════════════════════════

# 1) seed → danach immer dieselben „Zufalls“zahlen
random.seed(3)
wurf = random.randint(1, 6)       # ganze Zahl, 6 INKLUSIVE → 2
temp = round(random.uniform(-5, 30), 1)  # Kommazahl → 15.7
farbe = random.choice(['rot', 'gruen', 'blau'])  # ein Element → 'rot'
print('3.4/1', wurf, temp, farbe)

# 2) 8-mal würfeln, sammeln, 4en zählen
random.seed(10)
wuerfe = []
for i in range(8):
    wuerfe.append(random.randint(1, 6))
vieren = wuerfe.count(4)          # bestimmter Wert → .count(4) → 3
print('3.4/2', wuerfe, vieren)

# 3) „verschiedene“ / „ohne Zurücklegen“ → sample
random.seed(5)
lotto = random.sample(range(1, 50), 6)  # 1–49 → Stop 50
lotto.sort()                      # NICHT lotto = lotto.sort()
print('3.4/3', lotto)             # → [17, 23, 34, 40, 42, 45]

# 4) mischen: shuffle ändert die Liste selbst, gibt None zurück
random.seed(0)
karten = ['A', 'K', 'D', 'B', '10']
random.shuffle(karten)
erste = karten[0]                 # → 'D'
print('3.4/4', karten, erste)


# 5) Funktion mit seed
def zufall_liste(n, s):
    random.seed(s)
    liste = []
    for i in range(n):
        liste.append(random.randint(1, 100))
    return liste


gleich = zufall_liste(5, 1) == zufall_liste(5, 1)
print('3.4/5', gleich)            # True: gleicher Seed → gleiche Folge
