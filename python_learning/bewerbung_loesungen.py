# Lösungen zu bewerbung_basics.py – erst selbst probieren!

# 1. Liste
staedte = ["Berlin", "Hamburg", "München"]
staedte.append("Köln")
print(len(staedte))
for stadt in staedte:
    print(stadt)

# 2. if
alter = 17
if alter >= 18:
    print("volljährig")
else:
    print("minderjährig")

# 3. Funktion
def brutto(netto):
    return netto * 1.19

print(brutto(100))

# 4. Dictionary
kunde = {"name": "Müller", "ort": "Berlin", "offen": 250}
print(kunde["name"])
kunde["offen"] = 0
kunde["email"] = "mueller@example.com"
for key, wert in kunde.items():
    print(f"{key}: {wert}")

# 5. Filtern (Accumulator mit Liste)
zahlen = [3, 8, 12, 5, 7, 20]
gross = []
for z in zahlen:
    if z > 6:
        gross.append(z)
print(gross)

# 6. Maximum ohne max()
preise = [19.99, 5.49, 42.0, 13.5]
hoechster = preise[0]          # mit dem ersten Wert starten, nicht mit 0
for p in preise:
    if p > hoechster:
        hoechster = p
print(hoechster)

# 7. Code lesen: summiert die ungeraden Zahlen 1 + 3 + 5
werte = [1, 2, 3, 4, 5]
ergebnis = 0
for w in werte:
    if w % 2 == 1:
        ergebnis += w
print(ergebnis)               # 9

# BONUS – FizzBuzz: die Prüfung auf 15 (3 UND 5) muss zuerst kommen
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
