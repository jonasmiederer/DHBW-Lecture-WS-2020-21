"""
Heron-Verfahren

Der Nutzer soll eine positive Integerzahl eingeben können.

Von dieser Zahl soll mithilfe des Annäherungsalgorithmus der Wert der Quadratwurzel bestimmt werden.

Der Algorithmus ist beendet, sofern die Differenz der beiden Näherungswerte < 0.001 beträgt, oder nach spätestens 15 Iterationen.

Schlussendlich sollen beide Näherungswerte sowie die Differenz zum tatsächlichen exakten Wert ausgegeben werden.
"""

# Einlesen des Wertes, von dem die Quadratwurzel berechnet werden soll
value = input("Bitte Wert eingeben, von dem die Quadratwurzel ermittelt werden soll: ")

# Umwandlung von String in Integer
value = int(value)

# Es sind lediglich ganzzahlige positive Wert erlaubt
if value <= 0:
    print("Es sind lediglich ganzzahlige positive Werte erlaubt")
else:
    # Festlegen von a und b
    a, b = 1, value

    for i in range(15): # Maximal 15 Iterationen
        new_a = (a + b) / 2
        new_b = value / a

        # Zuweisung der berechneten Werte 
        a = new_a
        b = new_b

        # Überprüfung des Abbruchkriteriums
        if abs(new_a - new_b) <= 0.001:
            # Falls die Bedingung erfüllt ist, wird durch 'break' die Schleife abgebrochen,
            # da weitere Schleifendurchläufe nicht nötig sind.
            # Ist die Bedingung nicht erfüllt, so läuft die Schleife ganz normal weiter.
            break
    
    # Schleife ist beendet, entweder weil die Differenz der beiden Zahlen < 0.001 ist oder weil 15 
    # Iterationsdurchläufe erreicht wurden.

    # Ausgabe der Ergebnisse:
    print(f"Annäherungsberchnung der Quadratwurzel nach {i+1} Iterationen beendet.")
    print(f"Die beiden ermittelten Werte sind {a} und {b}")
    print(f"Die Differenz zur tatsächlichen Qudratwurzel beträgt {abs(value - (a*b))}")