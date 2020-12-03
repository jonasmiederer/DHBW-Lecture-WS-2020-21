"""
Größte eingegebene Zahl

Der Nutzer kann wiederholt Zahlen eingeben.
Gibt er 'X' ein wird die Abfrage beendet und die Zahlen in Form einer Liste an eine Funktion übergeben,
die die größte Zahl dieser Liste ermittelt und zurückgibt.
Diese Zahl wird ausgegeben
"""

# Erstelle Funktion, die die größte Zahl einer Liste ermittelt und zurückgibt
def find_largest_number(list_of_numbers):
    # list_of_numbers ist die Variable, der die Parameter übergeben wurden
    
    # Erzeuge Variable, in der die größte bisher gefundene Zahl gespeichert wurde
    largest_number = None

    # Iteriere über alle Zahlen und überprüfe, ob diese > largest_number ist. 
    # Falls ja, überschreibe den aktuellen Wert von largest_number mit der Zahl
    for number in list_of_numbers:
        if largest_number is None or number > largest_number:
            largest_number = number
    
    # Die komplette Liste aller Zahlen wurde nun durchlaufen, gebe die größte gefundene Zahl zurück
    return largest_number

# Erzeuge leere Liste, in der die eingegebenen Zahlen gespeichert werden
numbers = []

# Starte while Loop, der solange läuft, bis "X" eingegeben wurde
while True:
    user_input = input("Bitte Zahl eingeben (oder 'X' zum Fortfahren): ")
    
    if user_input == "X":
        # User hat X eingegben. Beende Loop
        break
    else:
        # Nutzer hat eine Zahl eingegeben
        number = int(user_input)
        
        # Füge Zahl der Liste hinzu
        numbers.append(number)

# Alle gewünschten Zahlen wurden eingelesen. 
# Rufe nun die Funktion find_largest_number mit der Liste aller Zahlen als Argument auf
largest_number = find_largest_number(numbers)

# Gebe Ergebnis aus
print(f"Die größte eingegebene Zahl ist {largest_number}")