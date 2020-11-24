"""
String Ausgabe

Nutzer kann ein Wort eingeben, von dem nur jeder 2. Buchstabe ausgegeben werden soll.

"""

# Einlesen des Wortes 
string = input("Bitte geben Sie ein Wort ein: ")

# Variable, in der die Ausgabe gespeichert wird
output = ""

# for-Schleife mit Slicing.
# string[1::2] bedeutet: Iteriere über String, beginnend bei Index 1 bis zum Ende mit einer Schrittweite von 2.
# Es wird also beim 2. Buchstaben begonnen und anschließend jeder zweite Buchstabe besucht, bis die Schleife am Ende der Liste angelangt ist.
for character in string[1::2]:
    # Falls das Zeichen direkt hier mit print(character) ausgegeben wird, wird jedes Zeichen in einer neuen Zeile ausgegeben.
    # Die Ausgabe soll aber in einer einzigen Zeile erfolgen. Daher wird das Zeichen zunächst nur an output angehangen
    output += character # äquivalent zu output = output + character

# Gebe letztendlich den Inhalt von ouput aus, um alles in einer Zeile auszugeben
print(output)