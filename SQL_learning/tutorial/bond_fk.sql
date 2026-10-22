-- ════════════════════════════════════════════════════════════════
-- LEKTION 3: Zwei Tabellen verbinden – Foreign Key und JOIN
-- ════════════════════════════════════════════════════════════════
--
-- WAS WIR ÜBEN
--   1. Daten auf zwei Tabellen aufteilen (Schauspieler nur EINMAL speichern)
--   2. Foreign Key: movies zeigt per Nummer auf actors
--   3. JOIN: beide Tabellen für die Anzeige wieder zusammensetzen
--   4. Was der Foreign Key verhindert (falsche Nummern, Löschen)
--
-- BEDIENUNG (PyCharm)
--   - Oben rechts im Editor als Datenquelle "bond" wählen.
--   - Cursor in EIN Statement setzen → Cmd+Enter → Ergebnis erscheint unten.
--   - Immer ERST die Frage beantworten (im Kopf oder als Kommentar),
--     DANN ausführen und vergleichen.
--   - Etwas kaputt? Schritt 0 nochmal komplett ausführen.
--   - Zurück zur alten Ein-Tabellen-Version: bond.sql komplett ausführen.
-- ════════════════════════════════════════════════════════════════


-- ── SCHRITT 0: Aufbau ────────────────────────────────────────────
-- Ganzen Block markieren (von PRAGMA bis COMMIT) → Cmd+Enter.
-- PRAGMA schaltet die Foreign-Key-Prüfung ein. In SQLite ist sie
-- standardmäßig AUS und gilt nur für die aktuelle Verbindung.

PRAGMA foreign_keys = ON;

BEGIN;

DROP TABLE IF EXISTS movies;   -- zuerst movies löschen: sie zeigt auf actors
DROP TABLE IF EXISTS actors;

CREATE TABLE actors (
    id    INTEGER PRIMARY KEY,   -- Primary Key: "Wer bin ich?"
    name  TEXT NOT NULL UNIQUE   -- jeder Name nur einmal
);

CREATE TABLE movies (
    id          INTEGER PRIMARY KEY,
    title       TEXT NOT NULL,
    released    INTEGER NOT NULL,
    actor_id    INTEGER NOT NULL REFERENCES actors(id),  -- Foreign Key: "Auf wen zeige ich?"
    box_office  REAL NOT NULL
);

INSERT INTO actors (id, name) VALUES
    (1, 'SEAN CONNERY'),
    (2, 'PIERCE BROSNAN'),
    (3, 'DANIEL CRAIG');

INSERT INTO movies (id, title, released, actor_id, box_office) VALUES
    (1, 'DR.NO',         1962, 1,  59.5),
    (2, 'GOLDFINGER',    1964, 1, 124.9),
    (3, 'GOLDENEYE',     1995, 2, 352.0),
    (4, 'CASINO ROYALE', 2006, 3, 594.2);

COMMIT;


-- ── SCHRITT 1: Beide Tabellen ansehen ────────────────────────────
-- FRAGE: Wo steht jetzt "SEAN CONNERY" – und wie oft?
SELECT * FROM actors;

-- FRAGE: Was steht in movies statt des Namens?
SELECT * FROM movies;


-- ── SCHRITT 2: JOIN – wieder zusammensetzen ──────────────────────
-- Lies es so: "Nimm jeden Film, suche den Schauspieler mit
--             passender Nummer und zeige den Namen daneben."
-- ERWARTUNG: 4 Zeilen, wie die alte Ein-Tabellen-Version.
SELECT movies.title, actors.name
FROM movies
JOIN actors ON movies.actor_id = actors.id;


-- ── SCHRITT 3: Was der Foreign Key verhindert (1) ────────────────
-- Schauspieler Nummer 99 gibt es nicht.
-- FRAGE: Klappt das? Was erwartest du?
INSERT INTO movies (id, title, released, actor_id, box_office)
VALUES (5, 'TEST FILM', 2030, 99, 1.0);


-- ── SCHRITT 4: Was der Foreign Key verhindert (2) – DEINE AUFGABE ─
-- Wir löschen Sean Connery aus actors.
-- FRAGE: Was passiert – und warum?
--        Tipp: Worauf würden DR.NO und GOLDFINGER danach zeigen?
-- DEINE VERMUTUNG:
--
DELETE FROM actors WHERE id = 1;


-- ── SCHRITT 5: Selbst schreiben ──────────────────────────────────
-- AUFGABE: Zeige nur die Filme von SEAN CONNERY (title und name).
-- Tipp: Nimm die Abfrage aus Schritt 2 und ergänze ein WHERE.
-- DEINE ABFRAGE:

