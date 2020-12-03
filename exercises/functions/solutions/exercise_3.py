"""
Teilbarkeit

Der Nutzer kann 2 Zahlen eingeben, mit der is_divisible()-Funktion wird überprüft, ob die Zahlen 
miteinander teilbar sind. Die Funktion gibt entsprechend einen booleschen Wert zurück.
"""

def is_divisible(dividend, divisor):
    # Die Funktion liefert True zurück, wenn dividend und divisor restlos teilbar sind.
    # Andernfalls False.

    if dividend % divisor == 0:
        return True
    else:
        return False

    # Die 4 Codezeilen können auch kompakter in nur einer Zeile geschrieben werden:
    # return dividend % divisor == 0:


# Einlesen der beiden Zahlen
zahl_1 = int(input("Bitte 1. Zahl eingeben: "))
zahl_2 = int(input("Bitte 2. Zahl eingeben: "))

if is_divisible(dividend=zahl_1, divisor=zahl_2): # äquivalent zu if is_divisible(dividend=zahl_1, divisor=zahl_2) == True:
    print(f"Die Zahlen {zahl_1} und {zahl_2} sind restlos teilbar")
else:
    print(f"Die Zahlen {zahl_1} und {zahl_2} sind nicht restlos teilbar")