-- ÜBUNGEN mit der Bond-Datenbank
-- Oben im Editor: Connection = bond, Dialekt = SQLite.
-- Bedienung: Cursor in EIN Statement setzen, Cmd+Enter → Ergebnis erscheint unten.
-- Etwas kaputt gemacht? bond.sql komplett ausführen = Originalzustand.
-- Tipp: Erst überlegen, was herauskommen sollte – dann ausführen und vergleichen.


-- ── 1. Alles ansehen ─────────────────────────────────────────────
-- Erwartung: 26 Zeilen, 6 Spalten
SELECT * FROM movies;


-- ── 2. Nur bestimmte Spalten ─────────────────────────────────────
SELECT title, released FROM movies;


-- ── 3. Filtern mit WHERE ─────────────────────────────────────────
-- Gleichheit (Text in einfachen Anführungszeichen, Groß/klein zählt!)
SELECT title FROM movies WHERE actor = 'DANIEL CRAIG';

-- Vergleich mit Zahlen
SELECT title, box_office FROM movies WHERE box_office > 500;

-- AND / OR: beide Bedingungen bzw. eine von beiden
SELECT title FROM movies WHERE actor = 'ROGER MOORE' AND released > 1980;
SELECT title FROM movies WHERE actor = 'GEORGE LAZENBY' OR actor = 'TIMOTHY DALTON';

-- IN: mehrere exakte Werte (kürzer als viele OR)
SELECT title, actor FROM movies WHERE actor IN ('GEORGE LAZENBY', 'TIMOTHY DALTON');

-- BETWEEN: Bereich inklusive beider Grenzen
SELECT title, released FROM movies WHERE released BETWEEN 1970 AND 1979;

-- LIKE: Muster. % = beliebig viele Zeichen, _ = genau ein Zeichen
SELECT title FROM movies WHERE title LIKE '%GOLD%';
SELECT title FROM movies WHERE title LIKE 'S______';  -- S + genau 6 Zeichen


-- ── 4. Sortieren mit ORDER BY ────────────────────────────────────
SELECT title, box_office FROM movies ORDER BY box_office DESC;   -- DESC = absteigend
SELECT actor, title FROM movies ORDER BY actor, released;        -- erst actor, dann Jahr


-- ── 5. Begrenzen mit LIMIT ───────────────────────────────────────
-- Die 3 erfolgreichsten Filme
SELECT title, box_office FROM movies ORDER BY box_office DESC LIMIT 3;


-- ── 6. Zusammenfassen: Aggregatfunktionen ────────────────────────
SELECT COUNT(*) FROM movies;
SELECT SUM(box_office), AVG(box_office), MIN(released), MAX(released) FROM movies;


-- ── 7. Gruppieren mit GROUP BY (+ HAVING) ────────────────────────
-- Pro Darsteller: Anzahl Filme und Gesamt-Einspielergebnis
SELECT actor, COUNT(*) AS filme, SUM(box_office) AS gesamt
FROM movies
GROUP BY actor
ORDER BY gesamt DESC;

-- HAVING filtert NACH dem Gruppieren (WHERE filtert VORHER)
SELECT actor, COUNT(*) AS filme
FROM movies
GROUP BY actor
HAVING COUNT(*) >= 5;


-- ── 8. Daten ändern (danach ggf. Commit-Button drücken) ─────────
INSERT INTO movies VALUES (27, 'TEST FILM', 2030, 'TEST ACTOR', 'TEST DIRECTOR', 1.0);
UPDATE movies SET box_office = 2.0 WHERE id = 27;
DELETE FROM movies WHERE id = 27;


-- ── Eigene Experimente ab hier ───────────────────────────────────
