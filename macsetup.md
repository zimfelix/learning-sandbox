# Mac-Setup: Test nach der Migration

**Wo liegt das?** Diese Datei liegt im Repo `learning-sandbox` (GitHub: zimfelix/learning-sandbox). Nach der Migration ist sie auf dem neuen Mac automatisch unter `~/Code/python/learning-sandbox/macsetup.md` – nichts extra kopieren.

**Wo abspielen?**

1. Auf dem **neuen MacBook** ein Terminal öffnen (Warp oder Terminal).
2. `cd ~` (Benutzerordner, nicht in einem Projekt starten)
3. `claude` starten.
4. Den Prompt unten (alles zwischen den Linien) hineinkopieren und abschicken.

Claude Code arbeitet die Liste ab, ändert nichts ohne Rückfrage und gibt am Ende eine Tabelle ✅ / ⚠️ / ❌ mit dem, was du noch von Hand erledigen musst.

**Ausgangslage (Stand 18.10.2026):** altes MacBook mit Apple M4, macOS 27.0.1, neues ebenfalls mit M-Chip. Homebrew unter `/opt/homebrew`. Migration per Migrationsassistent bei der Ersteinrichtung, Benutzername `felix`.

---

## Prompt

```text
Ich habe gerade mit dem Migrationsassistenten von meinem alten MacBook (Apple M4) auf dieses neue MacBook (ebenfalls M-Chip) migriert. Prüfe bitte, ob alles 1:1 übernommen wurde und funktioniert.

Regeln:
- Nur prüfen und lesen. Nichts installieren, löschen oder umkonfigurieren, ohne mich vorher zu fragen.
- Keine Secrets ausgeben (keine Schlüssel, Tokens, Passwörter, Inhalte von ~/.ssh).
- Wenn macOS eine Berechtigung verweigert, nicht umgehen, sondern notieren, welche Berechtigung ich wo erteilen muss.
- Arbeite die Punkte der Reihe nach ab und fasse am Ende alles in einer Tabelle zusammen: Bereich | Status (✅/⚠️/❌) | Was ich tun muss.

1. System
   - macOS-Version, Chip, Benutzername (soll `felix` sein), Home-Pfad `/Users/felix`.
   - Gibt es mehr als ein Benutzerkonto (Hinweis auf doppelte Kontoanlage)?

2. Kommandozeilen-Werkzeuge
   - Xcode Command Line Tools vorhanden (`xcode-select -p`)?
   - Homebrew unter `/opt/homebrew`, `brew doctor` ohne ernste Fehler.
   - Versionen prüfen: git, gh, node, npm, python3, uv/uvx, pi, claude, obsidian-CLI.
   - `gh auth status`: angemeldet? (nur Status, kein Token anzeigen)
   - Git-Identität: `git var GIT_AUTHOR_IDENT` soll meine GitHub-verifizierte Mail zeigen.
   - SSH: existiert ~/.ssh mit Schlüsseldateien? Nur Dateinamen und Rechte (600) prüfen, keinen Inhalt.

3. Claude Code und Pi
   - ~/.claude/CLAUDE.md und ~/.pi/agent/AGENTS.md vorhanden.
   - Skills unter ~/.claude/skills vorhanden, Symlinks auf ~/.local/share/agent-skills/... nicht kaputt.
   - `claude mcp list`: verbinden sich alle MCP-Server (z. B. sitegeist)?

4. Projekte
   - ~/Code vorhanden. In jedem Git-Repo darunter (bis Tiefe 3): `git status` sauber oder bekannte Änderungen, Remote erreichbar (`git fetch --dry-run`).
   - Python-Projekte mit .venv: funktioniert `.venv/bin/python --version`? Falls nicht, nur melden (venv neu anlegen, nicht selbst machen).
   - Projekt projektmanagement-oberfranken: startet der lokale Server laut AGENTS.md/README? Nur kurz starten, prüfen, wieder beenden.

5. Hintergrunddienste
   - ~/Library/LaunchAgents: com.felix.codexbar-keepalive, com.felix.flowscale-vorschau, com.felix.keep-wispr-flow-running vorhanden und geladen (`launchctl list | grep com.felix`)?
   - Zeigen die Pfade in den .plist-Dateien auf existierende Programme/Skripte?

6. Apps
   - In /Applications vorhanden und startbar (nur prüfen, nicht nach vorne holen): Brave Browser, Obsidian, PyCharm, Warp, Claude, CodexBar, Wispr Flow, RoboForm, Antinote, CotEditor, LM Studio, MenuBarUSB, DaisyDisk, WhatsApp, Discord, Microsoft Word/Excel/PowerPoint/Teams, Google Drive.
   - Brave: Profilordner unter ~/Library/Application Support/BraveSoftware vorhanden (Lesezeichen, Erweiterungen)?
   - Obsidian: Vault "Obsidian Vault" unter ~/Documents/Obsidian Vault vorhanden, `obsidian help` funktioniert (CLI in Obsidian unter Settings → General → Advanced aktiviert?).

7. Browser-Steuerung
   - Sitegeist-Verbindung zu Brave testen: einen Hintergrund-Tab öffnen, example.com laden, Titel lesen, Tab schließen.

8. Berechtigungen (macOS Datenschutz & Sicherheit)
   - Prüfe, soweit möglich, ob Terminal/Warp Festplattenvollzugriff hat (z. B. Lesen von ~/Library/Mail oder ~/.Trash).
   - Liste mir auf, welche Apps ich unter Datenschutz & Sicherheit wahrscheinlich neu freigeben muss: Festplattenvollzugriff, Bedienungshilfen, Bildschirmaufnahme, Automation, Mikrofon (Wispr Flow).

9. Was du nicht prüfen kannst – als Checkliste für mich ausgeben
   - Touch ID neu einrichten, Apple Pay, Entsperren mit Apple Watch
   - Bluetooth-Geräte koppeln
   - iCloud / Nachrichten / FaceTime bestätigen
   - WhatsApp, Banking-Apps neu anmelden
   - Externe Monitore anordnen
   - Dock, Schreibtisch, Finder-Seitenleiste optisch kurz kontrollieren
   - Altes MacBook erst zurücksetzen, wenn alles läuft (vorher iCloud und „Wo ist?“ abmelden)

Am Ende: Tabelle plus die drei wichtigsten nächsten Schritte.
```

---

## Notizen nach dem Test

_(hier eintragen, was gefehlt hat oder angepasst werden musste)_
