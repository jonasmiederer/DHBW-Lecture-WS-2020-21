"""
Speichern der 52 Spielkarten eines französischen Blatts in einer Listen.
Zufälliges Durchmischen der Liste und Ausgabe der gewählten Karte entsprechend der Nutzereingabe
"""

# Imoprtieren der random Bibliothek zum zufälligen Durchmischen der Liste
import random

# Anlegen der Listen für Farben ("suits") und Werte der Karten
suits = ["♥", "♦", "♣", "♠"]
values = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]

# Erzeugen einer leeren Liste, die anschließend befüllt wird
cards = []

# Befüllen der Liste
for suit in suits:
    for value in values:
        cards.append(f"{suit}{value}")

# Durchmischen der Liste
# Hierfür steht die shuffle()-Funktion aus der random-Bibliothek zur Verfügung
random.shuffle(cards)

# Abfrage des Nutzers, welche Karte gezogen werden soll (+ Umwandlung in Integer-Wert)
draw_index = int(input("Welche Karte soll gezogen werden?: "))

# Die gewählte Karte muss zwischen Index 0 und 51 liegen
if draw_index < 0 or draw_index > 51:
    print("Ungültige Wahl")
else:
    card = cards[draw_index]
    print(f"Gezogene Karte: {card}")