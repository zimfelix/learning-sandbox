// Einwand-Matrix für den Tab „Leitfaden“ (Entwurf, noch nicht abgestimmt). Quelle: sales_learning/einwand-sammlung.md
// Je Zeile: k = Kern-Einwand, sag = so sagt es der Kunde, a = Antwort (① Reframing bzw. Sonderweg), z = ② Zusatz (optional),
// q = Quellen, x = true → kein Reframing (Sonderweg). 🛠 = eigener Vorschlag. youtu.be-Links machen Videos zu 📌.
// Ausgangslage Felix: Jeder Angerufene HAT eine Website, meist veraltet, zeigt die Projekte nicht. Darum Ersetzen statt Ergänzen
// (anders als Julian, der laufende Dienstleistungen verkauft). Ergänzung nur, wenn jemand wirklich zufrieden ist.
window.EINWAENDE = {
"formel": "① „Verstanden, das heißt nur, wenn [Lösung für genau sein Problem] – nur dann lohnt sich ein Gespräch für Sie, oder?“",
"rueck": "„Was kostet das?“ / „Wie machen Sie das?“ = Rückfrage, kein Einwand: in den Termin überleiten – „Den Preis sage ich Ihnen gleich in den ersten 10 Minuten. Passt er nicht, beenden wir das Gespräch einfach.“ Keine Zahl am Telefon.",
"merk": "Das Bild im Wenn-Teil macht den Satz stark, nicht die Formel. Wo es passt: kostenloser Entwurf + Zahlung erst am Ende.",
"kette": "Kommt danach ein neuer Einwand: einfach den nächsten genauso reframen – höchstens 1–2 Runden, dann lockerlassen.",
"varianten": [
 ["Einstieg", ["„Verstanden, das heißt nur, wenn …“ (Hauptformulierung)", "„Verstanden, das bedeutet nur, wenn …“", "„Verstanden, das heißt, unser Gespräch macht nur unter der Voraussetzung Sinn, wenn …“", "„Wenn ich Sie richtig verstehe, …“"]],
 ["Schluss", ["„… nur dann lohnt sich ein Gespräch für Sie, oder?“", "„… nur dann lohnt es sich, dass wir kurz sprechen, oder?“", "„… nur dann lohnt sich ein Vergleich für Sie.“"]],
 ["Rückfrage", "„Stimmt's?“ · „Richtig?“ · „Oder?“ · „Habe ich Sie da richtig verstanden?“"]
],
"weiter": "③ Nach dem Ja: „Sehr gut, dann lassen Sie uns direkt schauen, wann es passt – dann zeige ich Ihnen, wie wir [die Bedingung] für Sie hinbekommen. Wie sieht's spontan morgen aus?“",
"rows": [
{"k": "Kein Bedarf",
 "sag": ["Bekomme alles über Empfehlung, Internet brauche ich nicht", "Wir haben genug zu tun", "Läuft gut bei uns", "Kein Interesse, brauchen wir nicht"],
 "a": "„Verstanden, das heißt nur, wenn jemand, der Sie empfohlen bekommt und kurz googelt, sofort Ihre besten Projekte sieht und merkt ‚Hier bin ich richtig‘ – nur dann lohnt sich ein Gespräch für Sie, oder?“",
 "z": "Bei „genug zu tun“: „Dann kommen nicht mehr Anfragen, sondern die richtigen.“",
 "q": "Nr. 14 @19:01 (alles derselbe Einwand) · Nr. 182 @8:02 · Vorwegnahme Schritt 4"},
{"k": "Seite reicht / bringt nix", "o": "Entwurf: Nr. 2 und 3 zusammengelegt – noch abstimmen",
 "sag": ["Wir haben eine Website, die reicht völlig", "Hab ich schon gehabt, hat nichts gebracht", "Die Website bringt eh nix", "Über die Seite kommen nur Schein-Anfragen", "Lege da keinen Wert drauf"],
 "a": "Erst klären: „Alles klar – wenn ich Sie richtig verstehe, geht es Ihnen darum, ob sich so eine Seite finanziell überhaupt lohnt, richtig?“ → „Verstanden, das heißt nur, wenn über Ihre Seite Aufträge reinkommen, die Ihnen mehr einbringen, als die Seite kostet – nur dann lohnt sich ein Gespräch für Sie, oder?“ 🛠",
 "z": "Sagt er „reicht völlig“ (zufrieden): „Verstanden, das heißt nur, wenn Ihre fertigen Projekte auf der Seite so aussehen, dass Kunden sofort sagen ‚Genau so will ich das auch‘ – nur dann lohnt sich ein Gespräch für Sie, oder?“ (Felix) + „Ihre jetzige Seite bleibt, wie sie ist – Sie sehen nur einen kostenlosen Entwurf als Vergleich.“ · Fragt er nach dem Warum: „Woran das liegt, zeige ich Ihnen im Termin.“",
 "q": "Nr. 28 @6:01 (echtes Webdesign-Telefonat) · erst verstehen: Nr. 167 @1:01 · derselbe Einwand, andere Begründung: Nr. 14 @19:01"},
{"k": "Macht schon jemand",
 "sag": ["Ich hab da schon jemanden, der macht mir das", "Haben schon eine Agentur", "Macht mein Neffe", "Haben einen Vertrag"],
 "a": "„Verstanden, das heißt nur, wenn Sie an einem kostenlosen Entwurf sehen, dass es deutlich besser geht als jetzt – ohne etwas zu riskieren – nur dann lohnt sich ein Vergleich für Sie, oder?“",
 "z": "„Sie sehen nur, was möglich ist, und entscheiden danach.“ · Bei Neffe/Mitarbeiter: „… und Ihr [Neffe] kann die Seite danach gerne weiter pflegen.“",
 "q": "Nr. 53 @7:03 · Nr. 73 @2:00 · Nr. 2 @4:02 (nicht rauskegeln)"},
{"k": "Schlechte Erfahrung",
 "sag": ["Der hat mich über den Tisch gezogen, mit so was arbeite ich nicht mehr", "Haben uns schon die Finger verbrannt", "Schon mal Geld bei einer Agentur versenkt"],
 "a": "„Verstanden, das heißt nur, wenn Sie vorher an einem kostenlosen Entwurf sehen, was Sie bekommen, und erst am Ende zahlen – nur dann lohnt sich ein Gespräch für Sie, oder?“",
 "z": "„Sie entscheiden erst, wenn Sie den Entwurf gesehen haben.“ · ❌ „… wenn wir Sie überzeugen, dass wir besser sind“ – trifft den Kern nicht.",
 "q": "Nr. 53 @6:01 (sicherstellen, dass es sich nicht wiederholt) · Nr. 59 @25:00 · Risikoumkehr: Nr. 146 @5:00"},
{"k": "Keine Zeit",
 "sag": ["Keine Zeit, zu viel zu tun", "Ich bin auf der Baustelle", "Hab gleich Kunden da", "Diesen Monat geht gar nichts"],
 "a": "„Verstanden, das heißt nur, wenn wir einen Termin finden, der gut in Ihren Tag passt – Mittagspause oder nach Feierabend – und es bei 15 Minuten bleibt – nur dann lohnt es sich für Sie, oder?“",
 "z": "Gerade jetzt (Baustelle, Kunde da): kein Reframing – „Ich hör's raus. Wann passt es besser?“ → feste Uhrzeit. · Später: zwei, drei Terminvorschläge per Mail. · „Machen Sie's kurz“ → Schritt 2.",
 "q": "Nr. 53 @7:03 · Nr. 420 @1:00 · Nr. 73 @3:02 (Mini-Termin) · Nr. 428 @6:00"},
{"k": "Unterlagen",
 "sag": ["Schicken Sie mir einfach was per Mail", "Schicken Sie Infos, ich melde mich", "Schicken Sie einen Link"],
 "a": "„Wenn ich Sie richtig verstehe, wollen Sie erst schwarz auf weiß sehen, ob sich so etwas für Sie lohnen kann, richtig?“ (Felix)",
 "z": "„Dann schicke ich Ihnen gleich zwei, drei Beispielseiten – und den Entwurf mit Ihren Projekten zeige ich Ihnen morgen in 15 Minuten. Der Termin gilt nur, wenn Ihnen die Beispiele zusagen. Wie sieht's um 13 Uhr aus?“ (Bleistifttermin; Entwurf nicht per Mail, sonst schaut er allein)",
 "q": "Nr. 167 @1:01 (3 Schritte) · Nr. 73 @3:02 · Nr. 130 @4:01"},
{"k": "Misstrauen",
 "sag": ["Woher haben Sie meine Nummer? Wer sind Sie überhaupt?", "Sie sind schon der Zehnte", "Glaub ich Ihnen nicht", "Das sagen alle"],
 "a": "Bei „Wer sind Sie?“ erst kurz und wahr beantworten. Dann: „Offen gesagt, Sie kennen mich nicht, und am Telefon kann ich viel versprechen. Das heißt nur, wenn ich es Ihnen zeige, statt es zu behaupten – nur dann lohnt sich ein Gespräch für Sie, oder?“",
 "z": "„Mit einem kostenlosen Entwurf – und Sie entscheiden danach.“",
 "q": "Nr. 188 @19:00 · Nr. 130 @2:07 (Firma nennen) · Nr. 53 @11:00 / @12:02"},
{"k": "Frau / Partner",
 "sag": ["Das muss ich mit meiner Frau / meinem Mann besprechen", "Muss ich mit meinem Teilhaber klären"],
 "a": "„Verstanden, das heißt nur, wenn Sie beide den Entwurf gemeinsam sehen – nur dann lohnt sich ein Gespräch für Sie, oder?“",
 "z": "„Dann müssen Sie nichts weitergeben. Wann sind Sie beide da – wie sieht's morgen um 18 Uhr aus?“",
 "q": "Nr. 181 @10:00 (zu dritt, Druck raus)"},
{"k": "Zu teuer",
 "sag": ["Das ist mir zu teuer", "Haben kein Budget dafür", "Warum so teuer, Websites sind alle gleich"],
 "a": "„Verstanden, das heißt nur, wenn es zu Ihrem Budget passt und ich Ihnen zeigen kann, dass dadurch tatsächlich mehr Aufträge reinkommen, die Sie wirklich haben wollen – nur dann lohnt sich ein Gespräch für Sie, oder?“ (Felix)",
 "z": "„Der Entwurf kostet nichts. Den Preis sage ich Ihnen gleich in den ersten 10 Minuten – passt er nicht, beenden wir das Gespräch einfach.“",
 "q": "Nr. 17 @8:01 (passt ins Budget) · Nr. 69 @8:00 (keine Zahl am Telefon)"}


],
"ton": "Ruhig, verständnisvolles „Verstanden“ – nicht rechtfertigen, nicht schneller werden, kein Konjunktiv. Wirkt nur, wenn Schritt 1–4 entspannt waren.",
"no": "Argumentieren („Wir sind besser/günstiger“) · „Sie kennen unser Angebot ja gar nicht“ · Einwand loben („Danke, dass Sie das offen sagen“) · „aber“ · Suggestivfragen.",
"videos": [
 ["Nr. 53 💎 @6:01 – die Formel plus alle Klassiker", "https://youtu.be/639wCGS1SA4?t=361"],
 ["Nr. 2 @2:01 – live „machen wir intern“", "https://youtu.be/KKvUr--VrQE?t=121"],
 ["Nr. 73 @2:00 – Kette und Unterlagen live", "https://youtu.be/eCUNXUw6EZ8?t=120"],
 ["Nr. 130 @4:01 – live Bleistifttermin", "https://youtu.be/bwSFCibBhLg?t=241"],
 ["Nr. 420 @1:00 – live „keine Zeit, gleich Meeting“", "https://youtu.be/F_RgIbBdiyE?t=60"]
]
};
