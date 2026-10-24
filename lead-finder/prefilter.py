"""Cheap keyword score: which postings are worth sending to the model first."""

HANDWERK_WORDS = [
    "handwerk", "elektro", "sanitär", "heizung", "shk", "klima", "dach", "bedach",
    "maler", "lackier", "tischler", "schreiner", "zimmer", "metallbau", "schlosser",
    "bau", "fliesen", "estrich", "trockenbau", "stuck", "gerüst", "glaser", "garten",
    "landschaft", "kfz", "autohaus", "karosserie", "werkstatt", "installation",
    "haustechnik", "gebäudetechnik", "fenster", "rolladen", "boden", "parkett",
    "steinmetz", "schornstein", "kälte", "bäckerei", "fleischerei", "meisterbetrieb",
]

NOT_HANDWERK_WORDS = [
    "praxis", "kanzlei", "steuerber", "rechtsanw", "notar", "klinik", "krankenhaus",
    "pflege", "therapie", "physio", "logopäd", "versicherung", "bank", "sparkasse",
    "schule", "nachhilfe", "hotel", "stadt ", "landkreis", "landratsamt", "verband",
    "e.v.", "universität", "personal", "vermittlung", "immobilien",
]


def score(firma: str, titel: str, berufe: str) -> int:
    """+2 per Handwerk word in the company name, +1 in title/jobs, -3 per counter word."""
    firma, rest = firma.lower(), f"{titel} {berufe}".lower()
    points = sum(2 for word in HANDWERK_WORDS if word in firma)
    points += sum(1 for word in HANDWERK_WORDS if word in rest)
    points -= sum(3 for word in NOT_HANDWERK_WORDS if word in firma)
    return points
