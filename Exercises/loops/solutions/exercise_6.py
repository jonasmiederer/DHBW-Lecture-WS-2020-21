"""
String Ausgabe II

Nutzer kann mehrere Wörter eingeben, von dem nur jedes 2. Wort ausgegeben werden soll.

"""

# Einlesen des Strings 
word_string = input("Bitte geben Sie mehrere Wörter ein: ")

# Variable, in der die Ausgabe gespeichert wird
output = ""

# Wörter sind durch Leerzeichen getrennt. Um einen String anhand eines bestimmten Zeichens zu trennen gibt es in Python die split()-Funktion.
# Falls der Funktion kein Argument übergeben wird (siehe Funktionen), wird automatisch anhand von Leerzeichen getrennt.
# Das Ergebnis ist eine Liste der getrennten Satzteile.
# Die Variable words enthält also alle einzelnen Wörter
words = word_string.split()

# for-Schleife mit Slicing.
# words[1::2] bedeutet: Iteriere über die Wort-Liste, beginnend bei Index 1 bis zum Ende mit einer Schrittweite von 2.
# Es wird also beim 2. Wort begonnen und anschließend jedes zweite Wort besucht, bis die Schleife am Ende der Liste angelangt ist.
for word in words[1::2]:
    # Falls das Wort direkt hier mit print(word) ausgegeben wird, wird jedes Wort in einer neuen Zeile ausgegeben.
    # Die Ausgabe soll aber in einer einzigen Zeile erfolgen. Daher wird das Wort zunächst nur an output angehangen.
    # Außerdem wird ein Leerzeichen angehangen, da diese zuvor entfernt wurden
    output += f"{word} " # äquivalent zu output = output + f"{word} "

# Gebe letztendlich den Inhalt von ouput aus, um alles in einer Zeile auszugeben
print(output)