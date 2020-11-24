"""
Umwandlung for-Schleife in while-Schleife 

Der folgende Code soll mit einer while-Schleife umgesetzt werden:

names = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']
for name in names:
    print(names)
"""

# Namensliste
names = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']

# Laufvariable
i = 0

# Wiederhole, solange Laufvariable noch nicht am Ende der Liste angelangt
while i < len(names):
    # Ausgabe des Namens
    print(names[i])

    # Erhöhe i um 1
    i = i + 1 # Alternativ: i += 1
    