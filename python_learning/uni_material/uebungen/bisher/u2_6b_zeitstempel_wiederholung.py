import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import check  # nicht löschen: zeichnet die Ausgabe für den Test auf

# ── 2.6b Zeitstempel – Wiederholung ─────────────────────────────
# Thema: Wie lange lebst du schon?
#
# 1. Jetzt:
#    - Importiere datetime aus der Bibliothek datetime.
#    - jetzt = aktueller Zeitpunkt
#    - ausgeben
#
# 2. Anzeigen:
#    - jetzt als String im Format JJJJ/MM/TT HH:MM  (ohne Sekunden!)
#    - unter jetzt_text speichern und ausgeben
#
# 3. Einlesen:
#    - geburtstag_string = '24.12.2003 18:45'
#    - in ein datetime-Objekt umwandeln → geburtstag
#    - ausgeben
#
# 4. Rechnen:
#    - lebenszeit = jetzt - geburtstag
#    - ausgeben: "Du lebst seit X Tagen und Y Stunden."
# ────────────────────────────────────────────────────────────────

# DEIN CODE:

from datetime import datetime

jetzt = datetime.now()
print(jetzt)

#2
jetzt_string = jetzt.strftime('%Y/%m/%d %H:%M')
print(jetzt_string)

#3
geburtstag_string = '24.12.2003 18:45'
#jetzt brauchen wir die zuweisung wo was steht fuer strptime
geburtstag = datetime.strptime(geburtstag_string, '%d.%m.%Y %H:%M')
print(geburtstag)

#4
lebenszeit = jetzt - geburtstag
tage = lebenszeit.days
stunden = lebenszeit.seconds // 3600
