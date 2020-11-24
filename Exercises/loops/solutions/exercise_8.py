"""
Einkaufsliste

Der Nutzer wird wiederholt nach Produkten gefragt, die in die Einkaufsliste aufgenommen werden sollen.

Gibt der Nutzer ein "X" ein wird die Abfrage beendet und die Liste ausgegeben
"""

# Erzeuge leere Liste, in der die Items gespeichert werden
items = []

# Erzeuge Endlosschleife, die erst durch die Eingabe von "X" beendet wird (break)
while True:
    eingabe = input("Was soll zur Einkaufsliste hinzugefügt werden? (oder 'X' für Abbruch): ")

    if eingabe == "X":
        # Abbruch der Schleife
        break
    else:
        # Füge die Eingabe der Liste hinzu
        items.append(eingabe)

# Falls die Schleife durch "X" beendet wurde, gebe die komplette Liste aus

print("Die Einkaufsliste enthält folgende Items: ")
print() # Leerzeile

for item in items:
    print(item)