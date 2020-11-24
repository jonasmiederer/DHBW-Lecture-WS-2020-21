"""
Zahlen raten

Es soll eine ganzzahlige Zufallszahl zwischen 0 und 100 erzeugt werden.

Der Nutzer soll solange einen Tip abgeben, bis er die Zahl erraten hat.
Liegt er daneben, erhält er den Hinweis "Zu hoch" oder "Zu niedrig".

Ist die Zahl erraten, soll die Anzahl der Versuche ausgegeben werden
"""

# Importieren der random Bibliothek zum Erzeugen der Zufallszahl
import random

# Erzeugen der Zufallszahl (Integer zwischen 0 und 100)
number = random.randint(0, 100)

# Einlesen des Tipps des Nutzers
guess = int(input("Bitte Tipp abgeben: "))

# Wievielter Versuch (try ist ein reserviertes Schlüsselwort, daher try_)
try_ = 1

while guess10 != number:
    if guess > number:
        print("Zu hoch")
    elif guess < number:
        print("Zu niedrig")
    
    # Einlesen des Tipps des Nutzers
    guess = int(input("Bitte Tipp abgeben: "))
    try_ += 1

print(f"Richtig erraten nach {try_} Versuchen")
        
    