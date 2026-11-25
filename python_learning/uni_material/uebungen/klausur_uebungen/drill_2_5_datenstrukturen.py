


# ── Funktion + Datenstruktur (Vorklausur-Stil) ───────────────────
# Aufgabe 13:
#   Funktion 'filter_gross' mit zwei Inputs (werte, grenze). Gibt eine
#   Liste aller Werte zurück, die mindestens so groß wie grenze sind.
#   Was gibt filter_gross([5, 12, 7, 20], 7) zurück?

liste = []
def filter_gross(werte, grenze):
    if werte >= grenze:
        liste.append(werte)
filter_gross([5, 12, 7, 20], 7)


# Aufgabe 14 (Bonus, schwerer):
#   Funktion 'zaehle_woerter' mit einem Input (text). Gibt ein Dictionary
#   zurück: Wort → wie oft es vorkommt. Was gibt
#   zaehle_woerter('a b a c b a') zurück?
