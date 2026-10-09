# Obsidian – Lernkarten und Vorschauen

Eigenständiges Vorhaben innerhalb der Learning Sandbox: Lernkarten, SVG-Vorschauen und deren Darstellung in Obsidian erproben. Keine Pflichtabhängigkeit des SQL-Lernens und keine automatische Mitschrift anderer Lernprojekte.

## Einstieg

- [Vorhabensbezogene Regeln](AGENTS.md): Freigaben, Vault-Arbeit und Exportgrenzen.
- [Lernkarten-Inhalte](python-basics.md): bisherige Python-Themen und Beispiele.
- [Workflow, Vorlage und Renderer](obsidian/README.md): bestätigte Gestaltung und Ablauf.
- [Gezielter Vault-Export](obsidian/vault-export/): Lernkarten, Bilder und ausgewählte Darstellungseinstellungen; keine vollständige private Notizensammlung.

## Ablage und Datenfluss

```text
Freigegebenes Thema → Markdown-Karte + JSON-Vorschau → SVG
                                  ↓                   ↓
                            Obsidian-Vault mit Bild und Text
                                  ↓ nur auf Auftrag
                            gezielter Vault-Export
```

Die vorhandene Ebene `obsidian/` innerhalb dieses Ordners bleibt erhalten. Sie enthält `templates/`, `previews/`, `render-preview.py`, CSS und `vault-export/`. Der Renderer ist ein Python-Skript; für Lernkartenarbeit gelten die Voraussetzungen im Workflow und in den passenden Obsidian-Skills.

Karten enthalten oben ein scharfes SVG und darunter editierbaren Text. Lokaler Vault und Repository-Export werden nicht automatisch synchronisiert. Vor Arbeiten am Vault muss der Ziel-Vault feststehen; Export und Vorschauänderungen erfolgen nur im vereinbarten Umfang.
