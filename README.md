# CSV Viewer – Webanwendung

Eine kompakte Webanwendung zum Hochladen, Parsen und Anzeigen von CSV-Dateien.

## Startanleitung

### Voraussetzungen
* Python 3.9+

### Installation & Start
1. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt

2. Server starten:
   ```bash
   uvicorn app:app --reload
4. Anwendung im Browser öffnen:
  http://127.0.0.1:8000


## API-Dokumentation:

- GET / : Liefert Frontend-Oberfläche aus
- POST /upload : Akzeptiert eine .csv-Datei
  - Validierung: Prüft Dateiendung (.csv) und ob die Datei leer ist (0 Bytes).
- GET /files : Liefert Liste aller hochgeladenen Dateien inklusive Originalnamen und Erstellzeitpunkt.
- GET /files/{filename}: Liest die angeforderte CSV-Datei ein und liefert Kopfzeile (headers) sowie Zeilen (data) als JSON zurück.

## Umgesetzte Funktionen
- Upload-Validierung: Schutz gegen Nicht-CSV-Dateien und leere Dateien.
- Kollisionsfreie Speicherung: Dateien werden serverseitig mit eine UUID versehen (uuid_filename.csv), um Namenskonflikte zu vermeiden.
- Automatische Trennzeichen-Erkennung: Verwendung von Pythons csv.Sniffer() zur flexiblen Erkennung von Delimitern (Komma, Semikolon etc.).
- Übersichtliche Benutzeroberfläche: Dropdown-Auswahl bereits hochgeladener Dateien. Bei mehrfach hochgeladenen Dateien mit gleichem Namen wird das Erstelldatum zur Unterscheidung im Dropdown angezeigt.
- Dynamisches Rendering: Automatischer Tabellenaufbau mit Behandlung leerer Datenfelder.

## Technische Entscheidungen
1. FastAPI: Wenig Boilerplate und einfache Frontend auslieferung
2. csv.Sniffer: Einfaches handling unteschiedlicher Typen ohne pandas
3. Dateisystem statt Datenbank: weniger Zeitbedarf und ausreichend für Komplexität
4. Vanilla HTML/Javascript

## Mehr Zeit
- Pagination für große Dateien
- Mehr Validierung
- Automatische Testsuite
- Löschung von Einträgen per API
- Frontend UI verbessern
- Filter und Sortierfunktion
