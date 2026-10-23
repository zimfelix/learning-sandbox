-- ════════════════════════════════════════════════════════════════
-- ETAPPE 2 – EXTRA: Lesetraining (Niveau A4–A6, etwas kniffliger)
-- ════════════════════════════════════════════════════════════════
--
-- SO GEHST DU VOR (bei jeder Aufgabe)
--   1. SELECT kurz ansehen:  Was soll herauskommen?
--   2. Dann in Ausführungsreihenfolge durchgehen:
--        FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
--      Fehlt eine Klausel, überspringst du sie.
--   3. Zwischenstände notieren: wie viele Zeilen / welche Stapel?
--   4. Erst DANN ausführen (Cursor ins Statement, Cmd+Enter).
--
-- Zum Nachschlagen – die Tabelle movies:
--   DR.NO          SEAN CONNERY    1962   59.5
--   GOLDFINGER     SEAN CONNERY    1964  124.9
--   GOLDENEYE      PIERCE BROSNAN  1995  352.0
--   CASINO ROYALE  DANIEL CRAIG    2006  594.2
--
-- Diese Datei liest nur – an bond.db ändert sich nichts.
-- ════════════════════════════════════════════════════════════════


-- X1: Erst filtern, dann gruppieren
-- FRAGE: Wie viele Ergebniszeilen? Was steht bei CONNERY?
-- ZWISCHENSTAND nach WHERE:
-- MEINE ANTWORT:

SELECT actor, COUNT(*) AS filme
FROM movies
WHERE released < 1990
GROUP BY actor;


-- X2: WHERE und HAVING in einer Abfrage
-- FRAGE: Welche Gruppe(n) bleiben übrig – und warum fällt CONNERY raus?
-- ZWISCHENSTAND nach WHERE:
-- ZWISCHENSTAND nach GROUP BY:
-- MEINE ANTWORT:

SELECT actor, SUM(box_office) AS gesamt
FROM movies
WHERE released > 1960
GROUP BY actor
HAVING SUM(box_office) > 200;


-- X3: Sortieren nach einem alias
-- FRAGE: In welcher Reihenfolge erscheinen die Schauspieler?
-- MEINE ANTWORT:

SELECT actor, AVG(box_office) AS schnitt
FROM movies
GROUP BY actor
ORDER BY schnitt;


-- X4: HAVING mit einer anderen Aggregatfunktion als im SELECT
-- FRAGE: Welche Zeile(n) kommen heraus? Achtung: HAVING prüft MIN,
--        angezeigt wird COUNT.
-- MEINE ANTWORT:

SELECT actor, COUNT(*) AS filme
FROM movies
GROUP BY actor
HAVING MIN(box_office) > 100;


-- X5: Eine Bedingung, die niemand erfüllt
-- FRAGE: Wie viele Ergebniszeilen? Fehler oder leeres Ergebnis?
-- MEINE ANTWORT:

SELECT actor, COUNT(*) AS filme
FROM movies
WHERE released > 1990
GROUP BY actor
HAVING COUNT(*) > 1;


-- X6: Alles zusammen
-- FRAGE: Welche Zeilen in welcher Reihenfolge? Schreib die
--        Zwischenstände nach jeder Klausel auf.
-- ZWISCHENSTAND nach WHERE:
-- ZWISCHENSTAND nach GROUP BY:
-- ZWISCHENSTAND nach HAVING:
-- MEINE ANTWORT:

SELECT actor,
       COUNT(*) AS filme,
       MAX(box_office) AS bester
FROM movies
WHERE box_office > 100
GROUP BY actor
HAVING COUNT(*) >= 1
ORDER BY bester DESC;
