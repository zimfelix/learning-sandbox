-- ════════════════════════════════════════════════════════════════
-- ETAPPE 2: Zählen und Zusammenfassen – COUNT, SUM, GROUP BY
-- ════════════════════════════════════════════════════════════════
--
-- WAS WIR ÜBEN
--   aggregate function (Aggregatfunktion): macht aus VIELEN Zeilen
--   EINEN Wert.
--
--      COUNT(*)      → Anzahl Zeilen
--      SUM(spalte)   → Summe
--      AVG(spalte)   → Durchschnitt (average)
--      MIN / MAX     → kleinster / größter Wert
--
--   GROUP BY bildet Gruppen – die Aggregatfunktion rechnet dann
--   PRO GRUPPE statt über die ganze Tabelle:
--
--      ohne GROUP BY:  4 Filme ──────────────▶ 1 Ergebnis
--      GROUP BY actor: CONNERY  (2 Filme) ──▶ 1 Ergebnis
--                      BROSNAN  (1 Film)  ──▶ 1 Ergebnis
--                      CRAIG    (1 Film)  ──▶ 1 Ergebnis
--
--   Ausführungsreihenfolge (neu: GROUP BY und HAVING):
--      FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
--             Zeilen   Gruppen    Gruppen
--             filtern  bilden     filtern
--
-- BEDIENUNG
--   - Datenquelle oben rechts: "bond"
--   - Cursor in EIN Statement → Cmd+Enter
--   - Erst FRAGE beantworten, dann ausführen und vergleichen.
--   - Diese Datei liest nur – an bond.db ändert sich nichts.
-- ════════════════════════════════════════════════════════════════


-- ── TEIL A: Vorgemacht – lesen, vorhersagen, ausführen ──────────
-- Rechts neben jeder Zeile steht, was genau sie tut.


-- A1: Zählen
-- FRAGE: Welche Zahl kommt heraus?
-- MEINE ANTWORT: 4

SELECT COUNT(*)          -- zähle die Zeilen (ohne GROUP BY: die ganze Tabelle = 1 Gruppe)
FROM movies;             -- aus der Tabelle movies


-- A2: Summe mit alias (Ersatzname)
-- FRAGE: Wie viele Zeilen hat das Ergebnis? Ungefähr welche Zahl?
-- MEINE ANTWORT: gesamt: 800 ca -- auch hier wo kommt gesamt hin in der antwort??

SELECT SUM(box_office)   -- addiere alle Werte der Spalte box_office
       AS gesamt         -- nenne die Ergebnisspalte "gesamt" (nur der Name)
FROM movies;             -- aus der Tabelle movies

-- Hinweis: Kommazahlen (REAL) sind intern nicht ganz exakt,
-- deshalb erscheinen   evtl. viele Nachkommastellen. ROUND rundet:
SELECT ROUND(SUM(box_office), 1)   -- erst summieren, dann auf 1 Nachkommastelle runden
       AS gesamt                   -- Ergebnisspalte heißt "gesamt"
FROM movies;


-- A3: Mehrere Aggregatfunktionen auf einmal
-- FRAGE: Welcher Wert ist MIN, welcher MAX?
-- MEINE ANTWORT: 250 / 59.5 / 594.2

SELECT AVG(box_office),  -- Durchschnitt (average) aller Einspielergebnisse
       MIN(box_office),  -- kleinster Wert
       MAX(box_office)   -- größter Wert
FROM movies;             -- alle drei rechnen über dieselben 4 Zeilen → 1 Ergebniszeile


-- A4: Erst filtern, dann zählen
-- FRAGE: Welche Zahl kommt heraus?
-- MEINE ANTWORT: 2

SELECT COUNT(*)                  -- 3. zähle die Zeilen, die übrig geblieben sind
FROM movies                      -- 1. nimm die Tabelle movies (4 Zeilen)
WHERE actor = 'SEAN CONNERY';    -- 2. behalte nur Zeilen von Connery (2 Zeilen)


-- A5: Gruppieren
-- FRAGE: Wie viele Zeilen hat das Ergebnis – und warum genau so viele?
-- MEINE ANTWORT:

SELECT actor,                    -- zeige die Beschriftung jeder Gruppe (den Namen)
       COUNT(*) AS filme,        -- zähle die Zeilen PRO GRUPPE, Spaltenname "filme"
       SUM(box_office) AS gesamt -- addiere box_office PRO GRUPPE, Spaltenname "gesamt"
FROM movies                      -- aus der Tabelle movies
GROUP BY actor;                  -- bilde eine Gruppe (einen "Stapel") pro Schauspieler


-- A6: Gruppen filtern mit HAVING
-- WHERE  filtert ZEILEN  (vor dem Gruppieren)
-- HAVING filtert GRUPPEN (nach dem Gruppieren)
-- FRAGE: Welche Gruppe bleibt übrig?
-- MEINE ANTWORT:

SELECT actor,                    -- 4. zeige den Namen der Gruppe …
       COUNT(*) AS filme         --    … und ihre Anzahl Zeilen, Spaltenname "filme"
FROM movies                      -- 1. nimm die Tabelle movies (4 Zeilen)
GROUP BY actor                   -- 2. bilde Stapel: CONNERY (2), BROSNAN (1), CRAIG (1)
HAVING COUNT(*) >= 2;            -- 3. behalte nur Stapel mit mindestens 2 Zeilen


-- ── TEIL B: Selbst schreiben ────────────────────────────────────
-- Schreib deine Abfrage unter die Aufgabe, mit ; am Ende.
-- Ab 3 Klauseln: eine Klausel pro Zeile.

-- B1: Wie viele Filme sind NACH 1990 erschienen?
-- MEINE ABFRAGE:
SELECT COUNT(*) as filme
FROM movies
WHERE released > 1990

-- B2: Was ist das höchste Einspielergebnis?
-- MEINE ABFRAGE:

SELECT title, MAX(box_office)
FROM movies

-- B3: Wie hoch ist das durchschnittliche Einspielergebnis
--     der Filme von SEAN CONNERY?
-- MEINE ABFRAGE:

SELECT actor, AVG(box_office) AS schnitt
FROM movies
WHERE actor = 'SEAN CONNERY'

-- oder:
SELECT AVG(box_office)
FROM movies
GROUP by actor
HAVING > 1


-- B4: Wie viele Filme hat jeder Schauspieler?
--     Zeige actor und die Anzahl (alias: filme),
--     meiste Filme zuerst.
-- MEINE ABFRAGE:


-- B5: Wie viel hat jeder Schauspieler insgesamt eingespielt?
--     Zeige actor und die Summe (alias: gesamt), größte zuerst.
-- MEINE ABFRAGE:


-- B6: Wie B5 – aber nur Schauspieler, die insgesamt
--     MEHR als 300 eingespielt haben.
-- MEINE ABFRAGE:


-- ── TEIL C: Fehler finden (Review-Training) ─────────────────────
-- Jede Abfrage hat EINEN Fehler. Erst finden, dann ausführen.
-- Manche Fehler melden sich laut, manche liefern still ein
-- falsches Ergebnis. Vergleiche immer mit dem "Gewollt".

-- C1: Gewollt: Schauspieler mit mindestens 2 Filmen.
-- MEINE ANTWORT:
SELECT actor, COUNT(*) FROM movies WHERE COUNT(*) >= 2 GROUP BY actor;

-- C2: Gewollt: Anzahl Filme PRO Schauspieler.
-- MEINE ANTWORT:
SELECT actor, COUNT(*) FROM movies;

-- C3: Gewollt: Gesamt-Einspielergebnis aller Filme.
-- MEINE ANTWORT:
SELECT COUNT(box_office) FROM movies;

-- C4: Gewollt: Schauspieler mit mindestens 2 Filmen.
-- MEINE ANTWORT:
SELECT actor, COUNT(*) FROM movies HAVING COUNT(*) >= 2 GROUP BY actor;

-- C5: Gewollt: EIN Wert – der Durchschnitt aller Filme nach 1990.
-- MEINE ANTWORT:
SELECT AVG(box_office) FROM movies WHERE released > 1990 GROUP BY actor;

-- C6: Gewollt: Schauspieler mit mehr als einem Film.
-- MEINE ANTWORT:
SELECT title, COUNT(*) FROM movies GROUP BY title HAVING COUNT(*) > 1;
