# ════════════════════════════════════════════════════════════════
# Meine Lösungen zu den Uni-Übungen (Grundlagen der Programmierung)
# Stand 2026-11-13 – gesichert aus der Session, inkl. Korrekturen aus dem Review
# Aufgabentexte: uni_material/Grundlagen_der_Programmierung_Uebung.ipynb
# ════════════════════════════════════════════════════════════════


# ── 2.1 Variable und Datentyp ───────────────────────────────────
a = None
b = True
c = 42
d = 3.14
e = 'Hello World'          # Uni-Vorgabe 'Hello, 'World!' wäre ein SyntaxError

print(a, b, c, d, e)
print(type(a), type(b), type(c), type(d), type(e))

b_int = int(b)             # True → 1
c_float = float(c)         # 42 → 42.0
d_str = str(d)             # 3.14 → '3.14'
e_upper = e.upper()        # () nicht vergessen: sonst nur die Methode, kein Ergebnis

print(b_int, c_float, d_str, e_upper)
print(type(b_int), type(c_float), type(d_str), type(e_upper))


# ── 2.2 Operator ────────────────────────────────────────────────
# 1 – OFFEN: x und y verwenden (nicht a und b)
x = 10
y = 3
# TODO: + - * / % ** mit x und y ausgeben

# 2
str1 = 'Hello '
str2 = 'World'
greeting = str1 + str2
print(greeting)

# 3 – OFFEN: z selbst verändern mit += -= *= /=, nach jedem Schritt print(z)
z = 5
# TODO

# 4
print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False

# 5 – OFFEN: a = True, b = False, dann and / or / not ausgeben
# TODO

# 6
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True
print(6 in my_list)  # False


# ── 2.3 Kontrollstruktur ────────────────────────────────────────
# 1
number = 5
if number > 0:
    print("Die Zahl ist positiv")
elif number == 0:
    print("Die Zahl ist null")
else:
    print("Die Zahl ist negativ")

# 2
for x in range(1, 11):
    print(x)

counter = 0
while counter < 5:
    counter += 1
    print(counter)

# 3 – erst prüfen (continue/break), dann ausgeben → 1 3 5
for x in range(1, 11):
    if x % 2 == 0:
        continue
    if x == 7:
        break
    print(x)


# ── 2.4 Funktion ────────────────────────────────────────────────
# 1
def addiere(a, b):
    c = a + b
    return c

def ist_gerade(n):
    return n % 2 == 0      # Vergleich direkt zurückgeben

print(addiere(2, 3))       # 5
print(ist_gerade(4))       # True
print(ist_gerade(3))       # False

# 2
global_var = 10

def multipliziere_mit_global_var(x):
    local_var = x * global_var
    print(local_var)

multipliziere_mit_global_var(5)   # 50
print(global_var)                 # 10 – unverändert

# 3
def aufrufe_funktion():
    def innere_funktion(y):
        i = y ** 2
        return i

    ergebnis = innere_funktion(5)
    print(ergebnis)

aufrufe_funktion()                # 25


# ── 2.4 Zusatzaufgaben ──────────────────────────────────────────
def subtrahiere(a, b):
    return a - b

def ist_positiv(n):
    return n > 0

def bewerte_note(note):
    if note <= 1.5:
        return 'sehr gut'
    elif note <= 4.0:
        return 'bestanden'
    else:
        return 'nicht bestanden'

def summe_bis(n):
    gesamt = 0                    # Accumulator: vorher starten
    for x in range(1, n + 1):     # + 1, weil range vor dem Stopp aufhört
        gesamt += x               # drin sammeln
    return gesamt                 # danach zurückgeben
    # Kurzform: return sum(range(1, n + 1))

print(subtrahiere(10, 4), ist_positiv(-2))          # 6 False
print(bewerte_note(1.3), bewerte_note(3.7), bewerte_note(5.0))
print(summe_bis(4), summe_bis(10))                  # 10 55

# OFFEN: Zusatz 4 (zaehle_gerade), 5 (global/lokal mit bonus), 6 (Default-Wert potenz)
