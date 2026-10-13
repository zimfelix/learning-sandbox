-- RESET-SKRIPT für bond.db
-- Stellt die Tabelle movies im Originalzustand (26 Bond-Filme) wieder her.
-- Ausführen: ganze Datei markieren (Cmd+A) und Cmd+Enter – oder im Terminal:
--   sqlite3 SQL_learning/tutorial/bond.db < SQL_learning/tutorial/bond.sql
-- Achtung: DROP löscht alles, was du in movies geändert hast.

DROP TABLE IF EXISTS movies;

CREATE TABLE movies (
    id         INTEGER PRIMARY KEY,
    title      TEXT NOT NULL,
    released   INTEGER NOT NULL,
    actor      TEXT NOT NULL,
    director   TEXT NOT NULL,
    box_office REAL NOT NULL
);

INSERT INTO movies (id, title, released, actor, director, box_office) VALUES
    (1,  'DR.NO',                           1962, 'SEAN CONNERY',   'Terence Young',        59.5),
    (2,  'FROM RUSSIA WITH LOVE',           1963, 'SEAN CONNERY',   'Terence Young',        78.9),
    (3,  'GOLDFINGER',                      1964, 'SEAN CONNERY',   'Guy Hamilton',        124.9),
    (4,  'THUNDERBALL',                     1965, 'SEAN CONNERY',   'Terence Young',       141.2),
    (5,  'YOU ONLY LIVE TWICE',             1967, 'SEAN CONNERY',   'Lewis Gilbert',       111.6),
    (6,  'ON HER MAJESTY''S SECRET SERVICE', 1969, 'GEORGE LAZENBY', 'Peter R. Hunt',        64.6),
    (7,  'DIAMONDS ARE FOREVER',            1971, 'SEAN CONNERY',   'Guy Hamilton',        116.0),
    (8,  'LIVE AND LET DIE',                1973, 'ROGER MOORE',    'Guy Hamilton',        126.4),
    (9,  'THE MAN WITH THE GOLDEN GUN',     1974, 'ROGER MOORE',    'Guy Hamilton',         97.6),
    (10, 'THE SPY WHO LOVED ME',            1977, 'ROGER MOORE',    'Lewis Gilbert',       185.4),
    (11, 'MOONRAKER',                       1979, 'ROGER MOORE',    'Lewis Gilbert',       210.3),
    (12, 'FOR YOUR EYES ONLY',              1981, 'ROGER MOORE',    'John Glen',           194.9),
    (13, 'OCTOPUSSY',                       1983, 'ROGER MOORE',    'John Glen',           183.7),
    (14, 'NEVER SAY NEVER AGAIN',           1983, 'SEAN CONNERY',   'Irvin Kershner',      160.0),
    (15, 'A VIEW TO A KILL',                1985, 'ROGER MOORE',    'John Glen',           152.4),
    (16, 'THE LIVING DAYLIGHTS',            1987, 'TIMOTHY DALTON', 'John Glen',           191.2),
    (17, 'LICENCE TO KILL',                 1989, 'TIMOTHY DALTON', 'John Glen',           156.2),
    (18, 'GOLDENEYE',                       1995, 'PIERCE BROSNAN', 'Martin Campbell',     352.0),
    (19, 'TOMORROW NEVER DIES',             1997, 'PIERCE BROSNAN', 'Roger Spottiswoode',  333.0),
    (20, 'THE WORLD IS NOT ENOUGH',         1999, 'PIERCE BROSNAN', 'Michael Apted',       361.8),
    (21, 'DIE ANOTHER DAY',                 2002, 'PIERCE BROSNAN', 'Lee Tamahori',        432.0),
    (22, 'CASINO ROYALE',                   2006, 'DANIEL CRAIG',   'Martin Campbell',     594.2),
    (23, 'QUANTUM OF SOLACE',               2008, 'DANIEL CRAIG',   'Marc Forster',        586.1),
    (24, 'SKYFALL',                         2012, 'DANIEL CRAIG',   'Sam Mendes',         1108.6),
    (25, 'SPECTRE',                         2015, 'DANIEL CRAIG',   'Sam Mendes',          880.7),
    (26, 'NO TIME TO DIE',                  2021, 'DANIEL CRAIG',   'Cary Joji Fukunaga',  774.2);

-- Kontrolle: muss 26 ergeben
SELECT COUNT(*) FROM movies;
