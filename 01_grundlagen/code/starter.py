"""
Baustein 01 – Grundlagen der Softwaretests
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Fehlerhafte Funktion
# ============================================================

def berechne_rabatt(preis: float, prozent: float) -> float:
    """
    Berechnet den Preis nach Rabattabzug.

    Beispiel:
        berechne_rabatt(100.0, 20) soll 80.0 zurückgeben.
    """
    # Hier ist ein Defekt eingebaut – findest du ihn?
    rabatt = preis * prozent  # <-- Zeile mit Defekt
    return preis - rabatt


# Aufgabe 1a): Beantworte folgende Fragen als Kommentar:

# Error (falsche Handlung des Entwicklers):
# Die Formel ist falsch, da sie den Rabatt nicht korrekt berechnet (preis*(prozent/100) wäre korrekt).

# Defect (fehlerhafte Stelle im Code):
# Die Zeile "rabatt = preis * prozent" ist fehlerhaft, da sie den Rabatt als einen Bruchteil des Preises berechnet, anstatt den Prozentsatz korrekt zu berücksichtigen.

# Failure (was der Benutzer bemerken würde):
# Der Benutzer würde einen viel zu hohen Rabatt erhalten, z.B. 2000.0 statt 80.0 bei einem Preis von 100.0 und 20% Rabatt.


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    rabatt = preis * (prozent / 100)  # Korrekte Berechnung des Rabatts
    return preis - rabatt   


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze print()-Ausgaben, um deine korrigierte Funktion zu testen
    # Erwartete Ergebnisse:
    #   berechne_rabatt_korrigiert(100.0, 20) -> 80.0
    #   berechne_rabatt_korrigiert(200.0, 10) -> 180.0
    #   berechne_rabatt_korrigiert(50.0, 0)   -> 50.0

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    print(berechne_rabatt_korrigiert(100.0, 20))  # Erwartet: 80.0
    print(berechne_rabatt_korrigiert(200.0, 10))  # Erwartet: 180.0
    print(berechne_rabatt_korrigiert(50.0, 0))    # Erwartet: 50.0

# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    | X     | -      |
# | Programm mit Testdaten ausführen    | -     | X      |
# | Syntaxprüfung durch den Editor      | -     | X      |
# | Walkthroughs im Team                | X     | -      |
# | Unit-Tests laufen lassen            | -     | X      |
# | Checklisten für Codestruktur        | X     | -      |
#
# Warum reicht statisches Testen allein nicht aus?
# Die Zeit und Ressourcen, die für das Testen zur Verfügung stehen, sind begrenzt. Statisches Testen kann viele 
# Fehler erkennen, aber es kann nicht alle möglichen Laufzeitfehler oder Interaktionen zwischen Komponenten 
# abdecken. Dynamisches Testen ist notwendig, um sicherzustellen, dass die Software unter realen Bedingungen 
# funktioniert und um Fehler zu entdecken, die durch statische Analyse nicht erkannt werden können.


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# Ein Software-Entwickler kann nicht alle möglichen Eingabekombinationen und Szenarien testen, daher ist 
# vollständiges Testen unrealistisch.

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# Fehler tendieren dazu, in bestimmten Bereichen des Codes zu konzentrieren. Zum Beispiel könnte ein 
# bestimmtes Modul oder eine Funktion besonders fehleranfällig sein, während andere Teile des Codes relativ 
# fehlerfrei sind.

# Welches Prinzip überrascht dich? Warum?
# Prinzip 2 überrascht mich, weil es zeigt, dass es immer eine gewisse Unsicherheit in der 
# Softwareentwicklung gibt. Es ist eine Herausforderung zu akzeptieren, dass man nicht alle Fehler finden kann, 
# aber es betont die Bedeutung von Priorisierung und Risikomanagement im Testprozess.


# das ist ein Test für den Pull Request – bitte nicht löschen