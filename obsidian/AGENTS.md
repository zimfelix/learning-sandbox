# Obsidian – vorhabensbezogene Agentenanweisungen

## Geltungsbereich

Diese Regeln ergänzen die repositorybezogene `../AGENTS.md` für das Vorhaben `obsidian/`. Sie gelten nicht automatisch für `SQL_learning/` oder andere Lernvorhaben. Lernkarten zu anderen Vorhaben werden nur nach ausdrücklicher Absprache erstellt; dadurch werden die Vorhaben nicht zu einer gemeinsamen Anwendung.

## Lernkarten und Freigaben

- Lernkarten sind eine optionale Nachschlagehilfe, keine automatische Mitschrift. Bei einem passenden neuen Thema nur anbieten, wenn eine kurze Karte beim Verstehen oder Nachschlagen hilft; Freigabe abwarten.
- Nach Freigabe den Workflow unter `obsidian/README.md` und die Vorlage `obsidian/templates/learning-card.md` nutzen (Pfade relativ zu diesem Ordner).
- Merkregel und konkretes Beispiel festhalten: scharfes SVG oben, editierbarer Text darunter, Dateiname = Haupttitel, Bilder separat, keine Properties im Hover. Themen passend verlinken; keine leeren Übersichten.
- Passende Obsidian-Skills laden. Vor Vault-Aktionen den Ziel-Vault bestätigen; bevorzugt die offizielle Obsidian-CLI nutzen und den Vault explizit angeben. Kein Community-Plugin ohne Auftrag.
- Nach Änderungen Bild/Text-Konsistenz, Links und Vorschau prüfen. Bestehende Inhalte vorher lesen; private oder fachfremde Vault-Inhalte nicht ungefragt ins Repository übernehmen.

## Export und Ablage

- `obsidian/vault-export/` ist eine gezielte Momentaufnahme, kein automatisch synchronisierter Vault. Export nur auf ausdrücklichen Auftrag aktualisieren.
- Während der Vault-Arbeit ist der lokale Vault die aktuelle Fassung. Export und SVG-Quelldaten nur im beauftragten Schritt nachziehen.
- Vorhandene Vault-Inhalte und persönliche Einstellungen nicht blind überschreiben. Export, Commit und Push sind jeweils gesondert freizugeben.
- Lernstand nur auf Wunsch festhalten; vor dem Anlegen einer fehlenden `learning-state.md` den Ablageort klären. Keine automatische Übernahme in globale Anweisungsdateien.
