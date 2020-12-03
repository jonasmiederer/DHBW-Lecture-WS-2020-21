"""
Begrüßung

Der Nutzer wird nach seinen Namen gefragt und wird anschließend gegrüßt
"""

# Abfrage des Namens des Nutzers mit der eingebauten input()-Funktion
# In den Klammern der input()-Funktion kann ein String übergeben werden, der zusätzlich 
# ausgegeben wird, bevor der Nutzer seine Eingabe tätigen kann.
# Die Eingabe wird der Variablen `name` zugewiesen:

name = input("Bitte Namen eingeben: ")

# Anschließend wird der Nutzer mit seinem Namen gegrüßt.
# Hierzu steht die print()-Funktion zur Verfügung, um Ausgaben anzuzeigen.

# Die Ausgabe soll den eingegebenen Namen enthalten. Dieser kann mit einem 
# formatierten String "injeziert" werden, indem dem String ein `f` vorangestellt wird
# und die entsprechende Variable in geschweiften Klammern innerhalb des Strings referenziert wird:

print(f"Guten Tag, {name}")

# Alternativ kann der Name dem String auch mit einem + -Zeichen angehangen werden:
# print("Guten Tag, " + name )