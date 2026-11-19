"""Mini-Testhelfer für die Übungsdateien.

Nutzung in einer Übungsdatei:
    import check            # ganz oben: zeichnet ab hier alle print-Ausgaben auf
    ...dein Code...
    check.ende(globals(), variablen={...}, aufrufe={...}, ausgabe=[...])
"""
import io
import sys

_FEHLT = object()


class _Tee:
    """Schreibt Ausgaben normal in die Konsole und merkt sie sich zusätzlich."""

    def __init__(self, original):
        self.original = original
        self.puffer = io.StringIO()

    def write(self, text):
        self.original.write(text)
        self.puffer.write(text)
        return len(text)

    def flush(self):
        self.original.flush()


_tee = _Tee(sys.stdout)
sys.stdout = _tee


def _zeile(ok, text):
    print(("✅ " if ok else "❌ ") + text)
    return ok


def _pruefe_variablen(g, variablen):
    ergebnisse = []
    for name, erwartet in variablen.items():
        wert = g.get(name, _FEHLT)
        if wert is _FEHLT:
            ergebnisse.append(_zeile(False, f"{name} fehlt"))
        elif wert == erwartet and type(wert) is type(erwartet):
            ergebnisse.append(_zeile(True, f"{name} = {wert!r}"))
        else:
            ergebnisse.append(_zeile(False, f"{name} = {wert!r}, erwartet {erwartet!r}"))
    return ergebnisse


def _pruefe_aufrufe(g, aufrufe):
    ergebnisse = []
    for ausdruck, erwartet in aufrufe.items():
        try:
            wert = eval(ausdruck, g)
        except Exception as fehler:
            ergebnisse.append(_zeile(False, f"{ausdruck} → {type(fehler).__name__}: {fehler}"))
            continue
        ok = wert == erwartet and type(wert) is type(erwartet)
        text = f"{ausdruck} → {wert!r}" + ("" if ok else f", erwartet {erwartet!r}")
        ergebnisse.append(_zeile(ok, text))
    return ergebnisse


def _pruefe_ausgabe(text, ausgabe):
    """Sucht die erwarteten Textstücke der Reihe nach in der Ausgabe."""
    position = 0
    for stueck in ausgabe:
        fund = text.find(stueck, position)
        if fund == -1:
            return [_zeile(False, f"Ausgabe: {stueck!r} fehlt (oder falsche Reihenfolge)")]
        position = fund + len(stueck)
    return [_zeile(True, f"Ausgabe: alle {len(ausgabe)} erwarteten Werte in richtiger Reihenfolge")]


def ende(g, variablen=None, aufrufe=None, ausgabe=None):
    sys.stdout = _tee.original
    text = _tee.puffer.getvalue()
    print("\n" + "─" * 50 + "\nTEST")
    ergebnisse = []
    ergebnisse += _pruefe_ausgabe(text, ausgabe) if ausgabe else []
    ergebnisse += _pruefe_variablen(g, variablen or {})
    ergebnisse += _pruefe_aufrufe(g, aufrufe or {})
    print(f"→ {sum(ergebnisse)}/{len(ergebnisse)} bestanden")
