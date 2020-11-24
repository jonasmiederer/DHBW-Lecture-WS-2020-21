"""
Luhn-Algorithmus

Es soll eine Funktion implementiert werden, die die Prüfziffer einer Zahl ermittelt bzw. validiert.
Der Luhn-Algorithmus ist hierfür in der Aufgabenstellung beschrieben.

Entsprechend der Integrität der Zahl soll die Funktion einen booleschen Wert zurückliefern.
Außerhalb der Funktion wird das Ergebnis ausgegeben.
"""

# Definition der Funktion
def is_luhn_valid(number):
    # Die Funktion is_luhn_valid erwartet ein Argument: number
    # Dieser Variable entspricht die Zahl, die gemäß des Luhn-Algorithmus überprüft werden soll.

    # Anlegen der sum Variable, in der die aktuelle Summe der Ziffern gespeichert wird
    sum = 0

    # Die Ziffer soll von rechts nach links durchlaufen werden.
    # Hierfür bietet sich eine Iteration über die String-Darstellung der Zahl an
    number = str(number)

    # Mithilfe der Laufvariablen i wird mithilfe des for-Loops wird rückwärts von der Länge des Strings (Anzahl der Ziffern der Zahl) bis 0 iteriert.
    for i in range(len(number)-1, -1, -1):
        # Auslesen der Ziffer an Stelle number[i]
        value = int(number[i])

        # Überprüfe ob es sich um eine Ziffer handelt, die Verdoppelt werden muss
        # (jede 2. Ziffer)
        if i % 2 == 0:
            # Ziffer muss verdoppelt werden
            value = 2 * value

            # Falls Wert > 9: Subtrahiere 9
            if value > 9:
                value -= 9

        # Addiere den Wert zur bisherigen Summe
        sum += value
    
    # Alle Ziffern sind durchlaufen, in sum ist nun die komplette "Luhn-Summe" gespeichert.
    # Nur wenn die Summe als letzte Ziffer eine 0 besitzt, ist die Zahl valide.
    # Die ist dann gegeben, wenn die Zahl restlos durch 10 teilbar ist

    if sum % 10 == 0:
        # Zahl ist valide
        return True
    else:
        # Zahl ist invalide
        return False

# Einlesen der Zahl, die geprüft werden soll
number = int(input("Bitte Zahl eingeben, die anhand des Luhn-Algorithmus geprüft werden soll: "))

# Aufrufen der is_luhn_valid Funktion und Ausgabe des Ergebnisses
if is_luhn_valid(number):
    print(f"Die Zahl {number} entspricht einer gültigen Zahl mit valider Luhn-Prüfziffer")
else:
    print(f"Die Zahl {number} entspricht keiner gültigen Zahl nach Luhn-Algorithmus")
            