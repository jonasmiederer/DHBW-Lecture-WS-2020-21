"""
Ausgabe der 52 Spielkarten eines französischen Blatts mit Listen und geschachtelten Schleifen
"""

# Anlegen der Listen für Farben ("suits") und Werte der Karten
suits = ["♥", "♦", "♣", "♠"]
values = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]

# Jede Farbe soll in Kombination mit jedem Wert ausgegeben werden. 
# Hierfür können zwei geschachtelte Schleifen verwendet werden:
# Die äußere Schleife iteriert über alle Farben, während die innere Schleife über alle Werte iteriert.
# Hierdurch werden alle Kombinationen abgedeckt

for suit in suits:
    for value in values:
        print(f"{suit}{value}") 