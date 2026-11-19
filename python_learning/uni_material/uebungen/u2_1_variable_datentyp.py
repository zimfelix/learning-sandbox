import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── 2.1 Variable und Datentyp ───────────────────────────────────
#
# 1. Erstellen von Variablen:
#    - a = None
#    - b = True
#    - c = 42
#    - d = 3.14
#    - e = 'Hello, World!'   (Uni-Vorgabe 'Hello, 'World!' ist ein SyntaxError)
#
# 2. Ausgabe: Gib a, b, c, d und e auf der Konsole aus.
#
# 3. Typüberprüfung: Gib den Datentyp jeder Variable mit type() aus.
#
# 4. Umwandlungen (jeweils in neuer Variable speichern):
#    - b als Integer        → b_int
#    - c als Float          → c_float
#    - d als String         → d_str
#    - e in Großbuchstaben  → e_upper
#
# 5. Gib b_int, c_float, d_str und e_upper aus.
# ────────────────────────────────────────────────────────────────

# DEIN CODE:

a = None
b = True
c = 42
d = 3.14
e = "Hello, World!"

print(a, b, c, d, e)

print(type(a), type(b), type(c), type(d), type(e))

b_int = int(b)
c_float = float(c)
d_str = str(d)
e_upper = e.upper()

print(b_int, c_float, d_str, e_upper)


# ── Test (nicht ändern) ─────────────────────────────────────────
check.ende(
    globals(),
    ausgabe=["None", "True", "42", "3.14", "Hello, World!",
             "NoneType", "bool", "int", "float", "str",
             "1", "42.0", "3.14", "HELLO, WORLD!"],
    variablen={"a": None, "b": True, "c": 42, "d": 3.14, "e": "Hello, World!",
               "b_int": 1, "c_float": 42.0, "d_str": "3.14", "e_upper": "HELLO, WORLD!"},
)
