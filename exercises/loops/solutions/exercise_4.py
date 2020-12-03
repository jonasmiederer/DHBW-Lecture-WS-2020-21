"""
Fakultät

Der Nutzer gibt eine Zahl ein, von der die Fakultät berechnet und ausgegeben wird
"""

# Einlesen der Zahl und Umwandlung in Integer
zahl = int(input("Bitte Zahl eineben, von der die Fakultät berechnet werden soll: "))

if zahl < 1:
    print("Bitte gültige Zahl eingeben")
else:
    # Für die Fakultät sollen alle Zahlen von 1 bis x multipliziert werden.
    # Dies kann mit einer for-Schleife in Verbindung mit range() abgebildet werden.
    # Da die Zahl selbst mit eingeschlossen werden soll, muss der Endwert der range zahl+1 sein.

    # Es wird eine Variable erzeugt, in der jeweils das aktuelle Ergebnis des Produkts gespeichert wird.
    # Da bei einer Multiplikation die Zahl 1 das neutrale Element ist, wird die Variable initial auf 1 gesetzt.
    fakultaet = 1
    
    for current_number in range(1, zahl+1):
        # Der neue Wert des Produkts ist der alte Wert des Produkts multipliziert mit dem neuen Faktor (aktuelle Zahl)
        fakultaet = fakultaet * current_number # Alternativ: fakultaet *= current_number
    
    # Nachdem die Schleife durchlaufen wurde ist in der Variable fakultaet das Ergebnis der Fakultätberechnung gespeichert
    print(f"Das Ergebnis von {zahl}! ist {fakultaet}")