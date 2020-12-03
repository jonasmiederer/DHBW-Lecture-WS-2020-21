"""
Das 1x1

Der Nutzer kann 2 Ganzzahlen eingeben.

Die erste Zahl beschreibt den Multiplikanden ("welches 1x1?")
Die zweite Zahl beschreibt den Multiplikator ("bis zu welcher Zahl?")

Ausgabe ist die entsprechende Multiplikationstabelle in der korrekten Formatierung
"""

# Einlesen der beiden Zahlen
multiplicand = input("Bitte geben Sie den Multiplikanden ein: ")
multiplicator = input("Bitte geben Sie den Multiplikator ein: ")

# Umwandlung in Integer-Werte
multiplicand = int(multiplicand)

# Wurde für den Multiplikator eine Zahl eingegeben? Falls nicht, wähle standardmäßig die Zahl 10.
if multiplicator == "":
    multiplicator = 10
else:
    multiplicator = int(multiplicator)


# Ausgagbe der Multiplikationstabelle in einer Schleife
# Für jede Zahl von 0 bis multiplicator soll das entsprechende Produkt ausgegeben werden
# Achtung: Ausgabe soll bei 1 beginnen und den eingegebenen Multiplikator inkludieren, daher range(1, multiplicator +1)
for current_multiplicator in range(1, multiplicator +1):
    print(f"{current_multiplicator} x {multiplicand} = {current_multiplicator * multiplicand}")


# Entsprechende Funktionalität mit einer while-Schleife:

"""
current_multiplicator = 1
while current_multiplicator <= multiplicator:
    print(f"{current_multiplicator} x {multiplicand} = {current_multiplicator * multiplicand}")
    current_multiplicator += 1
"""