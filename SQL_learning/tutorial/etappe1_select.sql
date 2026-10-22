-- ════════════════════════════════════════════════════════════════
-- ETAPPE 1: Daten lesen – SELECT, WHERE, ORDER BY
-- ════════════════════════════════════════════════════════════════
--
-- WAS WIR ÜBEN
--   Wie eine Abfrage aufgebaut ist und in welcher Reihenfolge
--   die Datenbank sie abarbeitet:
--
--      FROM movies        → 1. aus welcher Tabelle?
--      WHERE …            → 2. welche Zeilen behalten?
--      SELECT …           → 3. welche Spalten zeigen?
--      ORDER BY …         → 4. in welcher Reihenfolge?
--
--   Geschrieben wird SELECT zuerst – ausgeführt wird FROM zuerst.
--
-- BEDIENUNG
--   - Datenquelle oben rechts: "bond"
--   - Cursor in EIN Statement → Cmd+Enter
--   - Erst die FRAGE beantworten (als Kommentar unter "MEINE ANTWORT"),
--     dann ausführen und vergleichen.
--   - Diese Datei liest nur – an bond.db ändert sich nichts.
-- ════════════════════════════════════════════════════════════════


-- ── TEIL A: Vorgemacht – lesen, vorhersagen, ausführen ──────────

-- A1: Alles
-- * heißt "alle Spalten"
-- FRAGE: Wie viele Zeilen und wie viele Spalten?
-- MEINE ANTWORT:
SELECT * FROM movies;


-- A2: Nur bestimmte Spalten
-- FRAGE: Wie viele Zeilen und Spalten jetzt?
-- MEINE ANTWORT:
SELECT title, released FROM movies;


-- A3: Zeilen filtern mit WHERE (Zahlen)
-- FRAGE: Welche Filme kommen heraus?
-- MEINE ANTWORT:
SELECT title, box_office FROM movies WHERE box_office > 300;


-- A4: Zeilen filtern mit WHERE (Text)
-- Text steht in 'einfachen' Anführungszeichen.
-- FRAGE: Welche Filme kommen heraus?
-- MEINE ANTWORT:
SELECT title FROM movies WHERE actor = 'SEAN CONNERY';


-- A5: Sortieren
-- ASC = aufsteigend (Standard), DESC = absteigend
-- FRAGE: Welcher Film steht ganz oben?
-- MEINE ANTWORT:
SELECT title, box_office FROM movies ORDER BY box_office DESC;


-- A6: Alles kombiniert
-- FRAGE: Welche Filme in welcher Reihenfolge?
-- MEINE ANTWORT:
SELECT title, released
FROM movies
WHERE released < 2000
ORDER BY released DESC;


-- ── TEIL B: Selbst schreiben ────────────────────────────────────
-- Schreib deine Abfrage unter die Aufgabe und führe sie aus.

-- B1: Zeige title und actor aller Filme.
-- MEINE ABFRAGE:
SELECT title, actor FROM movies;


-- B2: Zeige alle Filme, die NACH 1990 erschienen sind.
-- MEINE ABFRAGE:
SELECT title FROM movies WHERE released > 1990

-- B3: Zeige title und box_office, sortiert vom
--     kleinsten zum größten Einspielergebnis.
-- MEINE ABFRAGE:
SELECT title, box_office FROM movies
ORDER BY box_office ASC

-- B4: Zeige die Filme von SEAN CONNERY, neuester zuerst.
-- MEINE ABFRAGE:
SELECT title FROM movies WHERE actor = 'SEAN CONNERY'
ORDER BY released desc


-- B5: Zeige title und box_office aller Filme, die MEHR als 100
--     UND WENIGER als 400 eingespielt haben.
--     Neu: Zwei Bedingungen verbindest du mit AND –
--     jede Bedingung braucht dabei ihre eigene Spalte.
-- MEINE ABFRAGE:
SELECT title, box_office
FROM movies
WHERE box_office > 100 AND box_office < 400
-- uberlegung war dass mit where ohne not ja beide konditions immer erfullt sind, also groesser 100 und kleiner 400, ka ob sich das dann gegenseitig ausschliesst


-- B6: Zeige title, released und box_office aller Filme vor 2000,
--     sortiert nach Einspielergebnis, größtes zuerst.
--     Bonus: Schreib sie über mehrere Zeilen (eine Zeile pro Klausel).
-- MEINE ABFRAGE:
SELECT title, released, box_office
FROM movies
WHERE released < 2000
ORDER BY box_office DESC


-- ── TEIL C: Fehler finden (Review-Training) ─────────────────────
-- Jede Abfrage hat EINEN Fehler. Erst finden, dann ausführen.
-- Achtung: Nicht jeder Fehler erzeugt eine Fehlermeldung!
-- Manche liefern still ein falsches oder leeres Ergebnis –
-- genau die sind beim Review gefährlich. Was ist falsch?

-- C1: MEINE ANTWORT:
SELECT title FROM movies WHERE actor = 'DANIEL CRAIG';
-- ''

-- C2: MEINE ANTWORT:
SELECT title FROM movies WHERE actor = 'Daniel Craig';
-- richtig

-- C3: MEINE ANTWORT:
SELECT title FROM movies ORDER BY released WHERE released > 1990;
-- falsche reihenfolge
SELECT title FROM movies where released > 1990 -- ORDER BY asc or desc

-- C4: Gewollt: zwei Spalten, title UND released.
-- MEINE ANTWORT:
SELECT title, released FROM movies;

-- C5: Gewollt: Filme mit box_office zwischen 100 und 400.
-- MEINE ANTWORT:
SELECT title FROM movies WHERE box_office > 100 AND < 400;
-- frage ob man bei so einem case nicht mit not arbeitet keine ahnung

-- C6: Gewollt: alle Filme, die VOR 1995 erschienen sind.
-- MEINE ANTWORT:
SELECT title, released FROM movies WHERE released < 1995;
