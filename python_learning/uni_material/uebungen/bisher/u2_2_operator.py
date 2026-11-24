import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── 2.2 Operator ────────────────────────────────────────────────
#
# 1. Arithmetische Operatoren:
#    - x = 10, y = 3
#    - Gib aus: Addition, Subtraktion, Multiplikation, Division, Modulo, Potenz
#
# 2. String-Verkettung:
#    - str1 = 'Hello', str2 = 'World'
#    - Verkette beide in greeting und gib greeting aus.
#
# 3. Zuweisungsoperatoren:
#    - z = 5
#    - Ändere z nacheinander und gib jedes Mal z aus:
#      +2, dann -3, dann *4, dann /2
#
# 4. Vergleichsoperatoren:
#    - Vergleiche x und y mit ==, !=, >, <, >=, <= und gib die Ergebnisse aus.
#
# 5. Logische Operatoren:
#    - a = True, b = False
#    - Prüfe Kombinationen mit and, or und not und gib die Ergebnisse aus.
#
# 6. Membership-Operatoren:
#    - my_list = [1, 2, 3, 4, 5]
#    - Prüfe, ob 3 und ob 6 in my_list enthalten sind, und gib das aus.
# ────────────────────────────────────────────────────────────────

# DEIN CODE:

x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)

str1 = 'Hello '
str2 = 'World'
print(str1 + str2)

#Alternative oder?
str3 = 'Hello'
print(str3 + '' + str2)

z = 5
print(z + 2)
print(z - 3)
print(z * 4)
print(z / 2)

print(x == y, x != y, x > y, x < y, x >= y, x <= y)

a = True
b = False

# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    ausgabe=["13", "7", "30", "3.3333333333333335", "1", "1000",
             "HelloWorld",
             "7", "4", "16", "8.0",
             "False", "True", "True", "False", "True", "False",
             "True", "False"],
    variablen={"x": 10, "y": 3, "greeting": "HelloWorld", "z": 8.0,
               "a": True, "b": False, "my_list": [1, 2, 3, 4, 5]},
)
