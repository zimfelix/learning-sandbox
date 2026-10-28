// Einwand-Matrix für den Tab „Leitfaden“ (Entwurf, noch nicht abgestimmt). Quelle: sales_learning/einwand-sammlung.md
// Je Zeile: k = Kern-Einwand, sag = so sagt es der Kunde, a = Antwort (① Reframing bzw. Sonderweg), z = ② Zusatz (optional),
// q = Quellen, x = true → kein Reframing (Sonderweg). 🛠 = eigener Vorschlag. youtu.be-Links machen Videos zu 📌.
// Ausgangslage Felix: Jeder Angerufene HAT eine Website, meist veraltet, zeigt die Projekte nicht. Darum Ersetzen statt Ergänzen
// (anders als Julian, der laufende Dienstleistungen verkauft). Ergänzung nur, wenn jemand wirklich zufrieden ist.
window.EINWAENDE = {
"formel": "① „Okay, das heißt nur, wenn [Lösung für genau sein Problem] – nur dann macht es Sinn, dass wir kurz sprechen. Stimmt's?“",
"rueck": "„Was kostet das?“ · „Wie machen Sie das?“ = Rückfrage, kein Einwand → Schritt 4, Mini-Thema Rückfrage. Keine Zahl am Telefon.",
"kette": "Kommt danach ein neuer Einwand: einfach den nächsten genauso reframen – höchstens 1–2 Runden, dann lockerlassen.",
"varianten": [
 ["Einstieg", ["„Okay, das heißt nur, wenn …“", "„Okay, das heißt, unser Gespräch macht nur unter der Voraussetzung Sinn, wenn …“", "„Wenn ich Sie richtig verstehe, …“"]],
 ["Schluss", ["„… nur dann macht es Sinn, dass wir kurz sprechen.“", "„… nur dann lohnt sich ein Vergleich für Sie.“"]],
 ["Rückfrage", "„Stimmt's?“ · „Richtig?“ · „Oder?“ · „Habe ich Sie da richtig verstanden?“"]
],
"weiter": "③ Nach dem Ja: „Sehr gut, dann lassen Sie uns direkt schauen, wann es passt – dann zeige ich Ihnen, wie wir [die Bedingung] für Sie hinbekommen. Wie sieht's spontan morgen aus?“",
"rows": [
{"k": "Kein Bedarf",
 "sag": ["Kein Interesse, brauchen wir nicht", "Läuft gut bei uns", "Läuft alles über Empfehlungen", "Sind voll ausgelastet", "Haben genug Aufträge"],
 "a": "„Okay, das heißt nur, wenn jeder, der von Ihnen hört, online sofort Ihre besten Projekte sieht und merkt ‚Hier bin ich richtig‘ – nur dann macht es Sinn, dass wir kurz sprechen. Stimmt's?“ 🛠 (greift den Nutzen aus Schritt 4 auf)",
 "z": "Worst-Case: „Was kann im schlimmsten Fall passieren, wenn ich Ihnen am [Tag] kurz zeige, wie das bei Ihnen aussehen kann?“",
 "q": "Nr. 14 @19:01 (alles derselbe Einwand) · Nr. 182 @8:02 · Nr. 181 @2:00"},
{"k": "Website bringt nix",
 "sag": ["Die Website bringt eh nix", "Haben Stammkunden, brauchen keine Seite", "Über die Seite kommen nur Schein-Anfragen", "Lege da keinen Wert drauf"],
 "a": "„Okay, das heißt nur, wenn Ihre Seite Ihnen endlich etwas bringt – also Ihre Projekte so zeigt, dass Besucher anfragen statt abspringen – nur dann macht es Sinn, dass wir kurz sprechen. Stimmt's?“ 🛠",
 "z": "Sagt er „nur Schein-Anfragen“, seine Worte aufgreifen: „… wenn über Ihre Seite endlich echte Anfragen kommen statt Schein-Anfragen …“",
 "q": "Einwand: Nr. 28 @6:01 (echtes Webdesign-Telefonat) · seine eigenen Worte = Kern treffen: Nr. 59 @25:00"},
{"k": "Haben schon eine Website",
 "sag": ["Haben schon eine Seite", "Unsere Seite reicht doch", "Haben wir erst neu gemacht", "Sind mit unserer Seite zufrieden"],
 "a": "„Okay, das heißt nur, wenn eine neue Seite Ihnen deutlich mehr bringt als die jetzige – also Ihre Projekte so zeigt, dass Kunden sofort sagen ‚genau so will ich das auch‘ – nur dann macht es Sinn, dass wir kurz sprechen. Stimmt's?“ 🛠 (Ersetzen – Normalfall)",
 "z": "Nur wenn er wirklich rundum zufrieden ist: Ergänzung – „… wenn wir Ihre Seite um sinnvolle Bausteine ergänzen, zum Beispiel, dass darüber mehr passende Anfragen reinkommen …“ (Felix)",
 "q": "Ersetzen-Logik wie Partner-Vergleich: Nr. 53 @7:03 · Ergänzung: Nr. 2 @3:02, Nr. 428 @5:02"},
{"k": "Macht schon jemand",
 "sag": ["Haben schon eine Agentur", "Macht mein Neffe", "Macht ein Mitarbeiter", "Machen wir selbst", "Haben einen Vertrag", "Sind gerade erst mit jemandem gestartet"],
 "a": "„Okay, das heißt nur, wenn wir Ihnen etwas deutlich Besseres zeigen als das, was Sie jetzt haben – nur dann lohnt sich ein Vergleich für Sie. Stimmt's?“ → nach dem Ja: „… wir legen das mal nebeneinander, und Sie entscheiden.“",
 "z": "Bei Neffe/Mitarbeiter vorsichtig: niemand will die eigenen Leute „rauskegeln“ – „… und Ihr [Neffe] kann die Seite danach gerne weiter pflegen“ 🛠 · Bei laufendem Vertrag: Kontakt halten – „… dass Sie uns schon mal in der Schublade haben, wenn es so weit ist.“",
 "q": "Nr. 53 @7:03 · Nr. 73 @2:00 · Nr. 4 @6:01 · Nr. 2 @4:02 (rauskegeln) · Nr. 403 @2:23"},
{"k": "Schlechte Erfahrung", "sag": ["Haben uns schon die Finger verbrannt", "Schon mal Geld bei einer Agentur versenkt", "Agenturen versprechen viel"],
 "a": "„Okay, das heißt nur, wenn wir sicherstellen, dass sich die schlechte Erfahrung nicht wiederholt – nur dann macht es Sinn, dass wir kurz sprechen. Stimmt's?“",
 "z": "❌ „… wenn wir Sie überzeugen, dass wir besser sind“ – trifft den Kern nicht, das hat der andere auch behauptet.",
 "q": "Nr. 53 @6:01 · Nr. 59 @25:00"},
{"k": "Keine Zeit", "sag": ["Keine Zeit, zu viel zu tun", "Bin gerade auf der Baustelle", "Heute brennt die Bude", "Bin momentan ziemlich eingespannt", "Hab gleich Kunden da", "Diesen Monat geht gar nichts", "Rufen Sie nächstes Jahr wieder an"],
 "a": "„Okay, das heißt nur, wenn wir einen Zeitpunkt finden, der gut reinpasst, und es kurz halten – nur dann macht es Sinn, dass wir in den Kalender schauen. Stimmt's?“",
 "z": "Gerade jetzt (Baustelle, Kunde da): kein Reframing, sondern „Ich hör's raus. Wann passt es besser?“ → feste Uhrzeit. · Mini-Termin: „Wir machen 15 Minuten. Wenn Sie nach 5 Minuten merken, das passt nicht, brechen wir ab – Zeit zu verschwenden haben wir beide nicht.“ · Später (diesen Monat nicht): „Alles klar, dann schicke ich Ihnen gleich zwei, drei Terminvorschläge per Mail.“ · Bei „Machen Sie's kurz“ → Schritt 2.",
 "q": "Nr. 53 @7:03 · Nr. 4 @5:00 · Nr. 420 @1:00 · Nr. 73 @3:02 · Nr. 428 @6:00"},
{"k": "Unterlagen", "sag": ["Schicken Sie mir was per Mail", "Schicken Sie Infos, ich melde mich", "Schicken Sie einen Link oder Flyer"],
 "a": "„Wenn ich Sie richtig verstehe, wollen Sie schwarz auf weiß sehen, ob sich der Termin für Sie lohnt, richtig?“",
 "z": "Bleistifttermin: „Schicke ich Ihnen gleich – ein paar Beispielseiten. Lassen Sie uns trotzdem schon einen Bleistifttermin machen, der findet nur statt, wenn Ihnen die Beispiele zusagen. Wie sieht's morgen um 13 Uhr aus?“ – die „Unterlagen“ sind die Kalendereinladung mit Link.",
 "q": "Nr. 167 @1:01 (3 Schritte) · Nr. 73 @3:02 · Nr. 130 @4:01 · Nr. 186 @1:00"},
{"k": "Misstrauen", "sag": ["Sie sind schon der Zehnte", "Glaub ich Ihnen nicht", "Das sagen alle", "Müsste schon herausragend sein"],
 "a": "„Okay, das heißt nur, wenn wir endlich mal die Ersten sind, die Ihnen wirklich etwas Interessantes zeigen – nur dann macht es Sinn, dass wir weitersprechen, oder?“ · bei „glaub ich nicht“: „… wenn ich es nicht nur behaupte, sondern Ihnen an echten Seiten zeige …“",
 "z": "Offen zugeben: „Sie kennen mich ja nicht, und am Telefon kann ich viel versprechen – deshalb zeige ich es Ihnen lieber.“",
 "q": "Nr. 53 @11:00 / @12:02 · Nr. 188 @19:00"},
{"k": "Frau / Partner", "x": true, "sag": ["Muss ich mit meiner Frau besprechen", "Entscheidet mein Partner mit"],
 "a": "„Im Termin geht's gar nicht darum, gleich etwas zu entscheiden – und über den Kopf Ihrer Frau hinweg wollen Sie das ja auch nicht. Lassen Sie uns schauen, wann es Ihnen beiden passt. Merken Sie vorher, es passt doch nicht, sagen wir einfach ab.“",
 "q": "Nr. 181 @10:00 – „Druck rausnehmen“"}


],
"ton": "Ruhig, verständnisvolles „Okay“ – nicht rechtfertigen, nicht schneller werden, kein Konjunktiv. Wirkt nur, wenn Schritt 1–4 entspannt waren.",
"no": "Argumentieren („Wir sind besser/günstiger“) · „Sie kennen unser Angebot ja gar nicht“ · Einwand loben („Danke, dass Sie das offen sagen“) · „aber“ · Suggestivfragen.",
"videos": [
 ["Nr. 53 💎 @6:01 – die Formel plus alle Klassiker", "https://youtu.be/639wCGS1SA4?t=361"],
 ["Nr. 2 @2:01 – live „machen wir intern“", "https://youtu.be/KKvUr--VrQE?t=121"],
 ["Nr. 73 @2:00 – Kette und Unterlagen live", "https://youtu.be/eCUNXUw6EZ8?t=120"],
 ["Nr. 130 @4:01 – live Bleistifttermin", "https://youtu.be/bwSFCibBhLg?t=241"],
 ["Nr. 420 @1:00 – live „keine Zeit, gleich Meeting“", "https://youtu.be/F_RgIbBdiyE?t=60"]
]
};
