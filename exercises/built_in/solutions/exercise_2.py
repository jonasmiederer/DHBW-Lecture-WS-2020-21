"""
Taschenrechner

Der Nutzer kann zwei Zahlen eingeben.

Anschließend wird die Summe berechnet und dem Nutzer präsentiert
"""

# Einlesen der 1. Zahl
summand_1 = input("Bitte 1. Zahl eingeben: ")
# Einlesen der 2. Zahl
summand_2 = input("Bitte 2. Zahl eingeben: ")

# Mithilfe von input() werden stets Strings eingelesen, unabhängig davon, was der Nutzer eingegeben hat.
# Da hier Zahlen erwartet werden, müssen diese Strings in das entsprechende Datenformat konvertiert werden.
# Wenn lediglich mit Ganzzahlen gerechnet werden soll bietet sich eine Konvertierung in Integer an, für Fließkommazahlen in float.

summand_1 = float(summand_1)
summand_2 = float(summand_2)

# Nun kann die Summe gebildet werden
sum = summand_1 + summand_2

# Ausgabe der Ergebnisse:
print(f"Die Summe aus {summand_1} und {summand_2} ist  {sum}")