// Auswertung pro Video. Schema siehe sales_learning/README.md.
// p = Phase: K = Kaltakquise (Anruf bis Termin) · T = Termin/Verkaufsgespräch · A = andere Verkaufsform
// y = Typ: Sekretärin · Opener · Bedarfsfrage · Einwand · Terminvereinbarung · Leitfaden · Prinzip
// s = sinngemäß (schlechte Untertitel) · t = Zeitstempel
window.NOTES = {
// ── Paket 1 ──
"aaWn8bLoCQg": {target: "Industrie (Produktionsleiter), Software", watch: true, why: "Bestes Beispiel: kompletter Ablauf Sekretärin → Opener → Bedarfsfrage → Termin, guter Ton", items: [
  {p:"K", y:"Sekretärin", t:"1:30", x:"„Wenn Sie mich gleich einmal weiterstellen, dann richten Sie gerne aus, der Julian Mahnken ist dran. Ich bleibe so lange in der Leitung.“"},
  {p:"K", y:"Opener", t:"2:13", x:"„Jetzt können Sie mit meinem Namen vermutlich erst mal nichts anfangen, oder?“ … „Darf ich gleich mal sagen, warum ich anrufe?“"},
  {p:"K", y:"Opener", t:"2:13", x:"„Wir möchten den Kontakt, der bisher eher virtuell stattgefunden hat, gerne mal persönlich machen. Es macht aber nur Sinn, wenn wir ein gemeinsames Thema haben, und deshalb habe ich eine kurze Frage. Ist das okay?“"},
  {p:"K", y:"Bedarfsfrage", t:"3:00", x:"„Mal angenommen, Sie würden sich mit [X] befassen, die Sie sofort warnt, wenn … – was müsste so eine Lösung können, damit das für Sie interessant wird?“"},
  {p:"K", y:"Einwand", e:"Haben wir schon", t:"3:00", x:"„Sie haben so eine Software bereits im Einsatz – super, perfekt. Vor dem Hintergrund, dass nichts auf dieser Welt perfekt ist: Wenn Sie über den Alltag nachdenken, was man noch besser machen könnte oder was fehlt – was fällt Ihnen spontan ein?“"},
  {p:"K", y:"Einwand", e:"Haben wir schon", t:"4:00", x:"Lücke prüfen: „Ist dieses System auch in der Lage, Ihnen Ausfälle anzuzeigen, bevor etwas passiert?“ → „Was würde es für Sie bedeuten, wenn wir das bestehende System nicht ersetzen, sondern um diese Funktion ergänzen?“"},
  {p:"K", y:"Terminvereinbarung", t:"5:02", x:"„Mein Vorschlag wäre, dass wir erst mal eine Web-Präsentation machen … da nehmen wir uns ganz entspannt beim Kaffee 20 Minuten. Wie klingt das für Sie?“"},
  {p:"K", y:"Einwand", e:"Rufen Sie später wieder an", t:"6:00", x:"„Können wir gerne so machen. Ich würde Ihnen sonst aber, weil mein Kalender sehr schnell für zwei Wochen ausgeplant ist und wir es sonst ewig vor uns herschieben, gleich zwei, drei Terminvorschläge per E-Mail schicken. Dann können wir den schon mal reservieren. Wollen wir das so machen?“"},
  {p:"K", y:"Prinzip", t:"7:03", x:"Bei „haben wir schon“ nicht argumentieren, sondern nachfragen, was darüber hinaus interessant wäre."}]},
"tluPk9kCpkU": {target: "", watch: false, why: "", items: [], skip: "Doppelt: dasselbe Gespräch wie aaWn8bLoCQg"},
"F_RgIbBdiyE": {target: "Marketingagenturen (Dienstleistung Telefonakquise)", watch: true, why: "Einwand „keine Zeit“ charmant gedreht, 4 min", items: [
  {p:"K", y:"Opener", t:"1:00", x:"„Ich bin Profi in Sachen Telefonakquise. Das bedeutet, ich vereinbare für Marketingagenturen qualifizierte Termine auf Entscheiderebene. Jetzt habe ich mir gedacht, dass es vertrieblich bei Ihnen wahrscheinlich schon gut läuft. Die Frage war: Wenn man das Gute noch mal besser machen kann, ist das grundsätzlich interessant, dass wir uns die kommenden Tage mal austauschen?“"},
  {p:"K", y:"Einwand", e:"Keine Zeit / gleich Meeting", t:"1:00", x:"„Ich hör's raus. Wann passt es besser?“ → Uhrzeit festmachen"},
  {p:"K", y:"Bedarfsfrage", t:"2:01", x:"„Eine letzte Frage noch gestattet, ganz schnell: Was wäre das Wichtigste, das wir als Dienstleister einbringen müssten, damit es für Sie interessant ist?“"}]},
"wLrZYtekimY": {target: "KMU / Online-Marketing", watch: true, why: "Zwei Gespräche: falscher Geschäftsführer gibt Durchwahl des richtigen", items: [
  {p:"K", y:"Prinzip", t:"9:01", x:"Immer ganz oben anrufen (Geschäftsführer laut Impressum); bei falscher Person Durchwahl der richtigen geben lassen."},
  {p:"K", y:"Opener", t:"5:01", s:1, x:"Zweiter Anruf: „Ich hatte gerade ein Gespräch mit [Name], er hat mir direkt Ihre Nummer gegeben, weil er sagte, das ist eher Ihr Thema.“"},
  {p:"K", y:"Bedarfsfrage", t:"6:02", s:1, x:"„Was müsste Inhalt und Ergebnis eines Gesprächs mit uns sein, welche Ergebnisse müssten wir Ihnen sichern können, damit es für Sie interessant ist?“"},
  {p:"K", y:"Terminvereinbarung", t:"7:03", s:1, x:"„Sie kennen uns ja nicht, und am Telefon kann ich viel versprechen. Ich würde Ihnen gerne einmal ganz transparent aufzeigen, welche bewährten Methoden wir nutzen … 20 bis 30 Minuten.“"}]},
"H4jjJFVrCaY": {target: "KMU / Online-Marketing", watch: false, why: "", items: [
  {p:"K", y:"Opener", t:"0:01", s:1, x:"„Ich kann mir gut vorstellen, wenn ich Ihnen sage, dass ich beruflich in Sachen Online-Marketing unterwegs bin, dass Sie erst mal denken: nicht schon wieder einer von der Sorte – oder liege ich da vollkommen falsch?“"},
  {p:"K", y:"Bedarfsfrage", t:"0:01", s:1, x:"„Was müsste jemand eigentlich können und nachweislich im Ergebnis liefern, damit es für Sie überhaupt interessant wird?“"},
  {p:"K", y:"Leitfaden", t:"1:02", s:1, x:"Angebot erklären in zwei Zielen: 1. Leute, die aktiv suchen, auf die Website holen; 2. Website so gestalten, dass aus anonymen Besuchern Anfragen werden."},
  {p:"K", y:"Terminvereinbarung", t:"2:00", s:1, x:"„Es ist kein Zufall, dass ich Sie angerufen habe – ich betreue schon viele Kunden in einem ähnlichen Bereich … ich würde Ihnen gerne vorschlagen, dass wir zusammen eine Web-Session machen, eine halbe Stunde, und ich zeige Ihnen transparent, was wir bisher leisten, damit Sie selbst beurteilen können.“"}]},
"FCeUPxi_Nvg": {target: "Unternehmen mit Vertrieb (Dienstleistung Telefonakquise)", watch: false, why: "", items: [
  {p:"K", y:"Opener", t:"0:03", s:1, x:"„Ich mache es ganz offen: Ich bin Profi in Sachen Telefonakquise … ich gehe davon aus, dass es bei Ihnen vertrieblich gut läuft. Die Frage war: Wenn man das Gute noch mal besser machen kann, sind Sie da grundsätzlich offen?“"},
  {p:"K", y:"Einwand", e:"Was kostet das? / Fixum", t:"1:02", s:1, x:"„Wir bekommen kein Fixum wie bei vielen Agenturen, sondern werden provisionsbasiert pro Termin bezahlt, und nur, wenn er stattfindet.“"},
  {p:"K", y:"Prinzip", t:"5:00", x:"Bezahlung pro stattgefundenem Termin, nicht pro Auftrag – nur das, was man selbst zu 100 % beeinflusst."}]},
"anRkPyRjsp8": {target: "Mittelstand / Werbeagentur", watch: false, why: "", items: [
  {p:"K", y:"Bedarfsfrage", t:"1:01", s:1, x:"„Wenn Sie auf einen externen Dienstleister zurückgreifen würden und prüfen würden, ob wir geeignet sind – worauf würden Sie Wert legen, unter welchen Voraussetzungen wäre das überhaupt was?“"},
  {p:"K", y:"Einwand", e:"Kein Bedarf / brauchen kein Marketing", t:"3:09", s:1, x:"„Ich bin großer Fan davon, dass wir mit unserer Zeit gegenseitig respektvoll umgehen und nichts machen, was keinen Sinn macht – aber den Kontakt sinnvoll weiterführen. Ich würde mich gerne kurz mit Ihnen austauschen, damit Sie eine Bewertungsgrundlage haben, wenn es zu gegebener Zeit so weit ist.“"}]},
"u332FoQeK_M": {target: "Gebäudereinigung", watch: false, why: "", items: [
  {p:"K", y:"Einwand", e:"Haben schon einen Dienstleister / Vertrag", t:"2:23", s:1, x:"Kontakt halten statt drängen: „Dass wir uns einfach mal persönlich kennenlernen, 20 Minuten, und Sie uns schon mal in der Schublade haben, wenn es so weit ist.“"}]},
"00xJqgLwkFg": {target: "Personalberatung / Headhunter (Lackindustrie)", watch: false, why: "", items: [
  {p:"K", y:"Opener", t:"1:01", s:1, x:"Reaktivierung: „Ich bin neu hier und habe gesehen, unsere Firmen standen vor einiger Zeit in Kontakt. Vielleicht kann man das wieder intensivieren – aber natürlich nur, wenn es Sinn macht.“"},
  {p:"K", y:"Bedarfsfrage", t:"1:01", s:1, x:"„Unter welchen Voraussetzungen wäre es für Sie prinzipiell interessant und vor allem sinnvoll, dass wir den Kontakt in der Zukunft wieder aufnehmen?“"}]},
"DQJ0l_idr50": {target: "Immobilienmakler → Privatverkäufer", watch: false, why: "", items: [
  {p:"K", y:"Bedarfsfrage", t:"1:01", s:1, x:"„Angenommen, es käme ein Käufer über einen Makler, der zu Ihren Bedingungen und Ihrem Preis kauft – wäre es dann ein Ausschlusskriterium, dass ein Makler dabei ist?“"},
  {p:"K", y:"Prinzip", t:"3:02", s:1, x:"Ehrlich bleiben: „Wir kennen uns jetzt zwei Minuten, ich sage es ganz offen: Ich habe in diesem Moment noch keinen Käufer.“"}]},
// ── Paket 2 ──
"zdFAzni-M1s": {target: "B2B allgemein", watch: true, why: "4 Sekretärinnen live hintereinander, 3× sofort durchgestellt – Ton und Selbstverständlichkeit hören", items: [
  {p:"K", y:"Sekretärin", t:"1:01", x:"„Wenn Sie mich gleich einmal zum [Vorname Nachname] weiterstellen, dann richten Sie gerne aus, der [Name] ist dran. Ich bleibe so lange in der Leitung.“"},
  {p:"K", y:"Prinzip", t:"6:03", x:"Zielperson mit Vor- und Nachnamen nennen, als Bitte statt Frage; Selbstverständlichkeit in der Stimme verhindert „Worum geht es?“."},
  {p:"K", y:"Sekretärin", t:"5:03", x:"Wenn nicht im Haus: nicht pitchen, nur fragen, wann er wieder da ist, und später erneut anrufen."}]},
"vePdGc0hxew": {target: "B2B / IT (IT-Leiter)", watch: true, why: "Ab 36:00 wird ein kompletter Kaltakquise-Leitfaden (Tim Taxis) im Fließtext durchgespielt – Sekretärin bis Termin", items: [
  {p:"K", y:"Sekretärin", t:"5:00", x:"„[Name der Sekretärin], guten Morgen, Frau [Name], mein Name ist [Vorname Nachname] von der Firma [X].“ – dann PAUSE und den Gruß erwidern lassen. Kein Wortschwall: Dialog statt Verkaufsgespräch."},
  {p:"K", y:"Sekretärin", t:"6:01", x:"„Sagen Sie, Frau [Name], ist der Herr [Nachname] heute schon im Haus?“ – „Ja.“ – „Dann verbinden Sie mich bitte mit ihm, danke schön.“ Julian: Zielperson mit „Herr Nachname“ oder vollem Namen nennen, nicht „der Werner Richter“."},
  {p:"K", y:"Sekretärin", t:"12:00", x:"Variante (Kreuter) auf „Worum geht es?“: „Um seine IT-Infrastruktur, speziell die Verbesserung seiner Systemerreichbarkeit. Dazu brauche ich seine Entscheidung als IT-Chef. Bitte verbinden Sie mich mit ihm, danke schön.“ – Julian: Schulnote 3."},
  {p:"K", y:"Prinzip", t:"15:01", x:"Bei der Sekretärin inhaltlich nicht preisgeben, worum es geht – sobald „Verkäufer“ erkennbar ist, kommt „Schicken Sie eine Mail an info@“. Nicht lange erklären, kurz und mit abschließender Bitte."},
  {p:"K", y:"Prinzip", t:"14:01", x:"Bei der Sekretärin keine Vorteile nennen und nicht schmeicheln – künstliche Sympathie wirkt unecht."},
  {p:"K", y:"Opener", t:"18:01", x:"Nicht: „Hätten Sie zehn Minuten Zeit für mich?“ oder „Kennen Sie uns schon?“ – wirkt wie Betteln."},
  {p:"K", y:"Opener", t:"22:00", x:"„Herr [Nachname], darf ich gleich zum Punkt kommen?“ – Julian empfiehlt es: holt Erlaubnis ein, statt ungefragt loszureden. Wegen Bekanntheit lieber eigene Variante: „Darf ich gleich mal sagen, warum ich anrufe?“ (44:00)"},
  {p:"K", y:"Opener", t:"23:01", x:"„Wir möchten Ihr zusätzlicher strategischer [IT-]Partner werden – aber nur, wenn das für Sie auch wirklich Sinn macht. Dazu habe ich eine kurze Frage. Ist das okay für Sie?“ – Julian: „super“, nennt das Thema, argumentiert nicht, endet mit Frage."},
  {p:"K", y:"Prinzip", t:"26:00", x:"„Wer fragt, der führt“: Jede eigene Aussage mit einer Frage abschließen und den Gesprächspartner so Schritt für Schritt Richtung Termin führen."},
  {p:"K", y:"Prinzip", t:"27:02", x:"Keine zwei Argumente/Vorteile im Opener (alte Schule): Argumente erzeugen Druck → Totstellen, Flucht oder Gegenangriff. Und du weißt beim Kaltanruf nicht, welches Argument für ihn zählt – erst Bedarf ermitteln."},
  {p:"K", y:"Bedarfsfrage", t:"31:01", x:"„Wenn es eine Sache im Bereich Ihrer [IT-Infrastruktur] gibt, die nicht immer so läuft, wie Sie sich das als [IT-Leiter] wünschen – welche eine Sache ist das?“ – Julian: gut, aber oft kommt „läuft alles gut“."},
  {p:"K", y:"Bedarfsfrage", t:"36:00", x:"Vertiefen: „Wie müsste denn [die Erreichbarkeit im Bereich der Handelssysteme] bei Ihnen aussehen, damit es optimal passt?“"},
  {p:"K", y:"Terminvereinbarung", t:"37:00", x:"„Wunderbar, dann macht ein gemeinsames Gespräch auf alle Fälle Sinn. Wie Sie [die gesteigerte Erreichbarkeit auf Klasse 4] lösen, sehen Sie nächste Woche. Wann passt es denn bei Ihnen optimal?“ – dann zwei konkrete Terminvorschläge."},
  {p:"K", y:"Leitfaden", t:"36:00", x:"Gesamtablauf (Tim Taxis): Begrüßung + Name → „Darf ich gleich zum Punkt kommen?“ → Thema + „aber nur, wenn es Sinn macht – kurze Frage, okay?“ → „Welche eine Sache läuft nicht so, wie Sie es wünschen?“ → „Wie müsste es aussehen, damit es optimal passt?“ → „Dann macht ein Gespräch Sinn – wann passt es optimal?“"},
  {p:"K", y:"Prinzip", t:"41:02", x:"Sie-Formulierung („Sie sehen nächste Woche …“ statt „Ich zeige Ihnen …“) – Julian hält sie für überbewertet; wichtiger sei, dass die Worte authentisch zu dir passen."}]},
"EsK12QRwpU4": {target: "Aktien-Telefonverkauf an Privatanleger (Filmszene)", watch: false, why: "", items: [
  {p:"A", y:"Opener", t:"1:01", x:"Bedarf wecken über Problembewusstsein: „Der Trick ist, sich vorher zu positionieren – wenn es im Wall Street Journal steht, ist es zu spät.“ → Kunde erkennt, warum er zuhören sollte."},
  {p:"A", y:"Prinzip", t:"3:01", x:"Nach einer wichtigen Frage, vor allem der Abschlussfrage: schweigen und warten („Wer zuerst spricht, verliert“). Viele verquatschen den Abschluss."},
  {p:"A", y:"Prinzip", t:"4:01", x:"„Ihr einziger wirklicher Einwand ist, dass Sie mir nicht vertrauen.“ – Die meisten Einwände („Schicken Sie Unterlagen“, „Ich muss drüber schlafen“) sind Vorwände wegen fehlendem Vertrauen."},
  {p:"A", y:"Einwand", e:"Ich kenne Sie nicht / kein Vertrauen", t:"7:00", x:"Vertrauen aufbauen über Expertenstatus (Position nennen) + kurze Story, warum man sich keine Fehler leisten kann: „Ich will der Beste hier werden – das schaffe ich nicht, wenn ich mir Fehler erlaube.“"},
  {p:"A", y:"Leitfaden", t:"6:02", x:"Future Pacing: Kunden gedanklich in die Wunschsituation holen – „Wenn das so eingetreten ist, würden Sie dann nicht sagen, dass es sich gelohnt hat?“"},
  {p:"A", y:"Leitfaden", t:"9:01", x:"Kontrollfrage nach dem Nutzen: „Klingt das fair?“"}]},
"vKmkzP0565I": {target: "Verkäufer selbst (Telefonangst)", watch: false, why: "", items: [
  {p:"K", y:"Prinzip", t:"7:00", x:"Vor dem ersten Anruf: Nummer vorwählen, Handy hinlegen, Augen zu, 4 Sek. durch die Nase in den Bauch einatmen, 8 Sek. durch den Mund ausatmen, 60–90 Sek. lang. Dann ohne Nachdenken auf den grünen Hörer drücken."},
  {p:"K", y:"Prinzip", t:"9:01", x:"Nur der erste Anruf braucht Überwindung („Sprung ins kalte Wasser“) – danach direkt die nächsten Nummern wählen."}]},
"Q31kjBQP4VA": {target: "B2B allgemein", watch: false, why: "", items: [
  {p:"K", y:"Prinzip", t:"0:00", x:"Nach der Begrüßung nicht ungefragt losreden („Fußgängerzone“) – erst Erlaubnis holen, sonst kommen sofort Einwände."},
  {p:"K", y:"Prinzip", t:"2:01", x:"Nicht argumentieren: Argumente erzeugen Druck und Gegendruck („Talkshow“). Stattdessen fragen."}]},
// ── Einzelauftrag ──
"639wCGS1SA4": {target: "B2B allgemein (interne Schulung für Telefonakquise-Mitarbeiter)", watch: true, why: "Kern seiner Einwandbehandlung: Reframing-Formel erklärt und mit Mitarbeiter geübt – die Formulierungs-Feinheiten hört man am besten selbst", items: [
  {p:"K", y:"Leitfaden", t:"1:00", x:"Nach dem Interesse-Wecken gibt es nur drei Reaktionen: 1. klares Interesse → direkt Terminvereinbarung („Dann lassen Sie uns mal schauen, wann es die Tage passt“); 2. Einwand → Einwandbehandlung; 3. Rückfrage → kurz antworten, dann zur Terminvereinbarung."},
  {p:"K", y:"Prinzip", t:"2:01", x:"Rückfragen („Was kostet das?“, „Wie macht ihr das genau?“) sind Kaufsignale. Kurz und knapp beantworten, nie die Verkaufspräsentation vorwegnehmen, sofort zum Termin überleiten."},
  {p:"K", y:"Prinzip", t:"3:00", x:"In der Kaltakquise nicht argumentieren („Wir sind günstiger/besser als alle anderen“): Es fehlt das Vertrauen, Argumente verpuffen und drängen den Kunden in die Ecke."},
  {p:"K", y:"Prinzip", t:"5:00", x:"Negativbeispiel: „Sie wissen ja gar nicht, woran Sie kein Interesse haben, Sie kennen mein Angebot noch gar nicht.“ – logisch richtig, aber der Kunde muss sich rechtfertigen."},
  {p:"K", y:"Leitfaden", t:"6:01", x:"Reframing-Formel: Einwand = Problem des Kunden → Lösung als Bedingung zurückgeben: „Okay, das heißt nur, wenn [Lösung], nur dann macht es Sinn, dass wir sprechen – andernfalls nicht, oder?“"},
  {p:"K", y:"Einwand", e:"Schlechte Erfahrungen gemacht", t:"6:01", x:"„Okay, das heißt nur, wenn wir sicherstellen, dass sich die schlechte Erfahrung nicht wiederholt – nur dann macht es Sinn, dass wir sprechen. Andernfalls nicht, oder?“"},
  {p:"K", y:"Einwand", e:"Haben schon einen Partner", t:"7:03", x:"„Okay, das heißt nur, wenn ich Ihnen ein viel besseres Angebot mache als Ihr aktueller Partner – dann hätte sich ein Vergleich für Sie gelohnt. Könnte man das so sagen?“"},
  {p:"K", y:"Einwand", e:"Keine Zeit / viel zu tun", t:"7:03", x:"„Okay, das heißt nur, wenn wir noch eine kleine Lücke in Ihrem Kalender finden und es ganz kurz halten, also nicht viel mehr von Ihrer Zeit in Anspruch nehmen – nur dann macht es Sinn, dass wir in den Kalender schauen.“"},
  {p:"K", y:"Einwand", e:"Ich glaube Ihnen das nicht", t:"11:00", x:"„Das heißt nur, wenn ich es nicht nur behaupte, sondern auch beweisen kann – nur dann macht unser Gespräch Sinn. Stimmt's?“"},
  {p:"K", y:"Einwand", e:"Sie sind schon der Zehnte, der anruft", t:"12:02", x:"„Das heißt nur, wenn wir endlich mal die Ersten sind, die auch wirklich etwas Interessantes anzubieten haben – dann macht es Sinn, dass wir das Gespräch fortführen, oder?“"},
  {p:"K", y:"Prinzip", t:"8:00", x:"Immer das Kundeninteresse in den Mittelpunkt stellen statt „Ich würde Ihnen gerne zeigen …“ – Sätze so umformulieren, dass der Kunde merkt: Es geht um mich."},
  {p:"K", y:"Prinzip", t:"13:01", x:"Rapport als „Vertrauenskonto“: Jeder Widerstand hebt viel ab. Alles im Gespräch soll einzahlen, deshalb Widerstand vermeiden."}]},
// ── Paket 3 ──
"pW3HJaqKwoM": {target: "B2B allgemein", watch: false, why: "", items: [
  {p:"K", y:"Opener", t:"2:02", s:1, x:"Begrüßung: „Hallo Herr [Nachname], hier ist [Vorname Nachname], grüß Sie.“ – Name des Gesprächspartners zuerst (holt ihn wie ein Zuruf in der Fußgängerzone aus seinen Gedanken), „hier ist“ statt „mein Name ist“ (klingt vertraut), Vor- und Nachname ohne Titel."},
  {p:"K", y:"Prinzip", t:"6:01", x:"Firmennamen in der Begrüßung weglassen, außer die Firma ist weltbekannt – eine weitere fremde Information, die sich niemand merkt und die keinen Vorteil bringt."},
  {p:"K", y:"Prinzip", t:"8:01", x:"Das „grüß Sie“ am Satzende ist Antwortauslöser: Der Gesprächspartner erwidert den Gruß → von Anfang an Dialog statt Monolog."},
  {p:"K", y:"Opener", t:"15:00", x:"„Herr [Nachname], darf ich gleich mal sagen, warum ich anrufe?“ – wie vePdGc0hxew: Julians eigene Variante von Tim Taxis' „Darf ich gleich zum Punkt kommen?“; Ziel ist die aktive Zustimmung zum Gespräch statt ungefragt loszureden."},
  {p:"K", y:"Leitfaden", t:"10:00", x:"Begrüßung und Gesprächseinstieg sind Schritt 1 und 2 von fünf; die Schritte 3–5 erklärt das Video nicht."}]},
"t1y4G4gELSw": {target: "B2B (Julians eigene Akquise, Vlog)", watch: false, why: "", items: [
  {p:"K", y:"Prinzip", t:"21:01", x:"Ergebnis seiner 100-Calls-Challenge (13–17 Uhr): 77 Wählversuche → 12 Entscheidergespräche → 9 Termine. Ab ca. 40 Calls lassen Konzentration und Schlagfertigkeit in der Einwandbehandlung nach. Julian: lieber ca. 20 Wählversuche am Tag, Qualität vor Quantität."},
  {p:"K", y:"Prinzip", t:"15:02", x:"Einen Termin aus einem eigentlichen Nein herausgeholt – Julian: solche Termine sind meist schlecht qualifiziert, „da macht es häufig gar keinen Sinn, die wahrzunehmen“."},
  {p:"K", y:"Prinzip", t:"7:03", x:"Beim Energieloch kurze Pause (Bewegung, frische Luft, Kaffee) statt weiterzuwählen – die Stimme transportiert die Energie."},
  {p:"K", y:"Prinzip", t:"6:00", x:"Während des Telefonblocks nur Strichliste und Zettel (Termin, E-Mail für die Bestätigung); Bestätigungsmails abends verschicken – keine Zeit zwischen den Anrufen verlieren."},
  {p:"K", y:"Prinzip", t:"12:01", x:"Adressrecherche kostenlos über wlw.de („Wer liefert was“): Suchbegriff, dann nach Mitarbeiterzahl (z. B. 10–49) und Standort mit Umkreis filtern – statt Adressen zu kaufen."}]},
"pmVzqS9YJpE": {target: "Industrie (Produktionsleiter), Software", watch: false, why: "", items: [
  {p:"K", y:"Prinzip", t:"1:00", x:"Reaktionsvideo auf das Gespräch aus aaWn8bLoCQg – Formulierungen dort; hier nur Julians neue Erklärungen."},
  {p:"K", y:"Opener", t:"5:14", s:1, x:"Aufhänger: „Vielleicht erinnern Sie sich ganz dunkel daran, dass Sie mal ein Whitepaper zum Thema Industrie 4.0 von uns runtergeladen haben.“ – Julian gibt zu: Dieses Whitepaper gab es nicht. ⚠️ Erfundener Anknüpfungspunkt, nicht übernehmen; laut Julian ist ein Aufhänger „gar nicht notwendig“."},
  {p:"K", y:"Prinzip", t:"7:01", x:"Bedarfsfrage rückwärts bauen: zuerst überlegen, welche Antwort man vom Kunden hören möchte, dann die Frage so stellen, dass genau diese Antwort kommt (hier: Maschinenstillstand kostet Produktionsleiter viel Geld)."},
  {p:"K", y:"Einwand", e:"Haben wir schon", t:"12:01", s:1, x:"Genannte Schwäche bestätigen statt dagegen argumentieren: „Ich bin aber vollkommen bei Ihnen, wenn Sie sagen: Nur wegen des Handlings stellt man nicht gleich in einem großen Projekt alles um.“ → dann Lücke prüfen wie aaWn8bLoCQg. Julian: Das Alleinstellungsmerkmal erst bringen, wenn Vertrauen da ist."},
  {p:"K", y:"Terminvereinbarung", t:"14:01", s:1, x:"Den vom Kunden genannten Schmerz in den Terminvorschlag einbauen: „… und dann schauen Sie sich mal an, wie einfach vor allem das Handling ist.“ – Termingrund sind zwei Nutzen, die der Kunde selbst angesprochen hat."},
  {p:"K", y:"Prinzip", t:"11:00", x:"Am Telefon bewusst lächeln – hört man in der Stimme."},
  {p:"K", y:"Terminvereinbarung", t:"15:00", x:"Produktionsleiter haben den Kalender selten griffbereit → Terminvorschläge per Mail schicken und dort festmachen (Formulierung wie aaWn8bLoCQg 6:00)."}]},
"LdSGGgKC5jA": {target: "B2B allgemein", watch: true, why: "Short (unter 1 Min.): Julians Antwort auf „Worum geht's denn?“ ist in den Untertiteln unverständlich – selbst anhören", items: [
  {p:"K", y:"Sekretärin", t:"0:00", s:1, x:"„Hallo, hier ist der [Vorname Nachname], grüß Sie. … Wenn Sie mich einmal weiterstellen zum [Vorname Nachname], dann richten Sie gerne aus, der [Name] ist dran. Ich bleibe so lange in der Leitung.“ – wie zdFAzni-M1s; die Antwort auf die Rückfrage ist nicht verständlich transkribiert."}]},
"_e9NAQuvtlk": {target: "Verkäufer selbst (Motivation)", watch: false, why: "", items: [
  {p:"K", y:"Prinzip", t:"2:01", x:"Wert eines Wählversuchs ausrechnen (Beispielrechnung: 100 Wählversuche → 10 Termine → 5 Aufträge à 1.000 € = 50 € pro gewählter Nummer). Mit den eigenen Quoten rechnen – jeder Anruf ist dann „50 € in die Tasche“."},
  {p:"K", y:"Prinzip", t:"4:01", x:"Schmerz vermeiden: Tagesziel (z. B. 50 Nummern) als Bargeld links auf den Schreibtisch, pro 5 gewählte Nummern 50 € nach rechts; was abends noch links liegt, wird verbrannt. Julian: radikal, nur für Druckresistente."}]}
};
