import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── 2.3 Kontrollstruktur ────────────────────────────────────────
#
# 1. Entscheidungsanweisungen:
#    - number mit beliebigem Wert anlegen
#    - if-elif-else:
#      > 0  → 'Die Zahl ist positiv'
#      == 0 → 'Die Zahl ist null'
#      < 0  → 'Die Zahl ist negativ'
#
# 2. Schleifen:
#    - for-Schleife, die die Zahlen 1 bis 10 ausgibt
#    - while-Schleife, die läuft, bis counter den Wert 5 erreicht;
#      counter jedes Mal um 1 erhöhen und ausgeben
#
# 3. Sprunganweisungen:
#    - for-Schleife über 1 bis 10
#    - gerade Zahl → mit continue überspringen
#    - bei 7 → mit break beenden
#    - sonst die aktuelle Zahl ausgeben
# ────────────────────────────────────────────────────────────────

# DEIN CODE:

number = 10

if number > 0:
    print('positiv')
elif number == 0:
    print('gleich null')
else:
    print('negativ')

#2
for zahl in range(1, 11):
    print(zahl)

counter = 0
while counter < 5:
    for zahl in range(1, 11):
        counter += 1
        print(counter)

#3
for zahl in range(1, 11):
    if zahl % 2 == 0:
        continue

    if zahl == 7:
        break

    print(zahl)



# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    ausgabe=["Die Zahl ist",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "1", "2", "3", "4", "5",
             "1", "3", "5"],
    variablen={"counter": 5},
)
