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
-- Schreib deine Abfrage unter die Aufgabe, mit ; am Ende,
-- und führe sie aus.

-- B1: Zeige title und actor aller Filme.
-- MEINE ABFRAGE:


-- B2: Zeige alle Filme, die NACH 1990 erschienen sind.
-- MEINE ABFRAGE:


-- B3: Zeige title und box_office, sortiert vom
--     kleinsten zum größten Einspielergebnis.
-- MEINE ABFRAGE:


-- B4: Zeige die Filme von SEAN CONNERY, neuester zuerst.
-- MEINE ABFRAGE:


-- B5: Zeige title und box_office aller Filme, die MEHR als 100
--     UND WENIGER als 400 eingespielt haben.
--     Neu: Zwei Bedingungen verbindest du mit AND –
--     jede Bedingung braucht dabei ihre eigene Spalte.
-- MEINE ABFRAGE:


-- B6: Zeige title, released und box_office aller Filme vor 2000,
--     sortiert nach Einspielergebnis, größtes zuerst.
--     Bonus: Schreib sie über mehrere Zeilen (eine Zeile pro Klausel).
-- MEINE ABFRAGE:


-- ── TEIL C: Fehler finden (Review-Training) ─────────────────────
-- Jede Abfrage hat EINEN Fehler. Erst finden, dann ausführen.
-- Achtung: Nicht jeder Fehler erzeugt eine Fehlermeldung!
-- Manche liefern still ein falsches oder leeres Ergebnis –
-- genau die sind beim Review gefährlich. Was ist falsch?
-- Schreib deine Antwort als Kommentar – die Abfrage selbst
-- bleibt unverändert, damit der Fehler sichtbar bleibt.

-- C1: Gewollt: die Filme von DANIEL CRAIG.
-- MEINE ANTWORT:
SELECT title FROM movies WHERE actor = "DANIEL CRAIG";

-- C2: Gewollt: die Filme von DANIEL CRAIG.
-- MEINE ANTWORT:
SELECT title FROM movies WHERE actor = 'Daniel Craig';

-- C3: Gewollt: Filme nach 1990, nach Erscheinungsjahr sortiert.
-- MEINE ANTWORT:
SELECT title FROM movies ORDER BY released WHERE released > 1990;

-- C4: Gewollt: zwei Spalten, title UND released.
-- MEINE ANTWORT:
SELECT title released FROM movies;

-- C5: Gewollt: Filme mit box_office zwischen 100 und 400.
-- MEINE ANTWORT:
SELECT title FROM movies WHERE box_office > 100 AND < 400;

-- C6: Gewollt: alle Filme, die VOR 1995 erschienen sind.
-- MEINE ANTWORT:
SELECT title, released FROM movies WHERE released <= 1995;
