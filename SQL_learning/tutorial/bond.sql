CREATE table movies (
    id          INTEGER PRIMARY KEY,
    title       TEXT NOT NULL,
    released    INTEGER NOT NULL,
    actor       TEXT NOT NULL,
    box_office  REAL NOT NULL
);

INSERT INTO movies (id, title, released, actor, box_office) VALUES
    (1, 'DR.NO',         1962, 'SEAN CONNERY',   59.5),
    (2, 'GOLDFINGER',    1964, 'SEAN CONNERY',  124.9),
    (3, 'GOLDENEYE',     1995, 'PIERCE BROSNAN', 352.0),
    (4, 'CASINO ROYALE', 2006, 'DANIEL CRAIG',  594.2);
