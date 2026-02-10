# Smart Parking System (CPS)

### Projektbeschreibung

Dieses Projekt simuliert ein intelligentes Parkhaus (Smart Parking System) in Python. Es modelliert realistische Abläufe wie Einfahren, Parken, Bezahlen und Ausfahren von Fahrzeugen sowie Wartungsfunktionen.​

### Cyber-physisches System

Das Parkhaus ist ein cyber-physisches System (CPS), da die physische Ebene begrenzte Parkplätze und Einnahmen (Geld) umfasst, während die cyber-Ebene diese Zustände überwacht, Entscheidungen trifft (z. B. Platz prüfen, Gebühren berechnen) und den Ablauf steuert.​

### Projektstruktur

    config.py: Feste Werte wie Anzahl Parkplätze (z. B. 10), Gebühr (2 €/Stunde), erlaubte Münzen (0,50 €, 1 €, 2 €), optionales Wartungscodewort.​

    storage.py: Funktionen zum Speichern/Laden des Zustands (belegte Plätze, Einnahmen) in CSV-Datei; lädt beim Start, speichert beim Beenden.​

    payment.py: Bezahlvorgang mit Münzeingabe, Prüfung auf ausreichend Zahlung und Wechselgeld-Ausgabe (unendlich verfügbar).​

    parking.py: Logik für Ein-/Ausfahren, Zeitstempel-Speicherung, Parkdauer-Berechnung (angebrochene Stunden voll), Platzprüfung ("Parkhaus voll" bei Vollauslastung).​

    utils.py: Hilfsfunktionen wie Statusbericht (freie/belegte Plätze, Einnahmen), Menüausgaben.​

    main.py: Hauptprogramm mit Menü (enter, exit, status, maintenance, off), Wartungsmodus (empty, take money, report, exit).​

### Startanleitung

    Repository klonen: git clone <repo-url>.

    In Verzeichnis wechseln: cd smart-parking-cps.

    Programm starten: python main.py.
    Das System lädt automatisch den gespeicherten Zustand und zeigt das Hauptmenü.