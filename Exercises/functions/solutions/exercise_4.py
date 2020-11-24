"""
Primzahl

Nutzer gibt positive Ganzzahl ein. 
Funktion is_prime() überprüft, ob diese Zahl eine Primzahl ist und gibt abhängig davon einen booleschen Wert zurück.

Anschließend soll eine entsprechende Ausgabe erfolgen
"""
import math 

# Definition der is_divisible Funktion aus Aufgabe 3
def is_divisible(dividend, divisor):
    # Die Funktion liefert True zurück, wenn dividend und divisor restlos teilbar sind.
    # Andernfalls False.

    if dividend % divisor == 0:
        return True
    else:
        return False


# Definition der is_prime Funktion
def is_prime(number):
    # Eine Zahl ist eine Primzahl, wenn sie nur durch sich selbst und durch 1 restlos teilbar ist.
    # Es müssen alle Zahlen von 2 bis zur Quadratwurzel der Zahl überprüft werden, ob diese mit nubmer restlos teilbar sind.    
    for i in range(2, int(math.ceil(number**0.5) +1)):
        if is_divisible(number, i):
            # Sobald die Zahl durch i restlos teilbar ist steht fest, dass Zahl keine Primzahl ist, die Schleife kann daher
            # vorzeitig beendet werden. Durch return wird immer unmittelbar aus der Funktion ausgestiegen
            return False
        # Falls die Zahl nicht durch i restlos teilbar ist, wird die Schleife ganz normal fortgesetzt
    
    # Nachdem alle Zahlen von 2 bis zur Qudratwurzel von number durchlaufen wurden und keine Teilbarkeit festgestellt wurde,
    # steht fest, dass number eine Primzahl sein muss, daher wird True zurückgegeben

    return True

# Eingabe der Zahl
number = int(input("Bitte positive Ganzzahl eingeben: "))

if is_prime(number):
    print(f"{number} ist eine Primzahl")
else:
    print(f"{number} ist keine Primzahl")

