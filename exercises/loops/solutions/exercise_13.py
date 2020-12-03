"""
Fibonacci

Der Nutzer gibt eine Zahl ein. Anschließend werden alle Fibonacci-Zahlen von 0 bis zur jeweiligen Zahl ausgegeben

"""

# Einlesen der Zahl und Konvertierung in int
fibonacci_end = int(input("Bitte Zahl eingeben, bis zu der die Fibonacci-Zahlen ausgegeben werden sollen: "))

# Liste, in der die Fibonacci-Zahlen gespeichert werden
fibonacci = []

# Erzeuge Endlos-Schleife, die solange durchlaufen wird, bis sie durch break beendet wird.
while True:
    if len(fibonacci) == 0:
        # Liste ist noch leer. Füge die Zahl 0 hinzu
        fibonacci.append(0)
    elif len(fibonacci) == 1:
        # Liste enthält lediglich die Zahl 0. Füge 1 hinzu
        fibonacci.append(1)
    else:
        # Die Liste enthält mindestens 2 Einträge.
        # Die neue Zahl ist eine Summe der beiden vorhergehenden Zahlen
        new_number = fibonacci[-1] + fibonacci[-2]

        # Überprüfe, ob neue Zahl größer ist als vom Nutzer eingegebene Zahl
        if new_number > fibonacci_end:
            # Das Abbruchkriterium wurde erreicht. Die Schleife kann beendet werden.
            # Da der neue Wert größer ist als der vom Nutzer eingegebene Wert, wird dieser nicht der Liste angehangen.
            break
        else:
            fibonacci.append(new_number)

print(f"Die Fibonacci-Zahlen von 0 bis {fibonacci_end} sind: {fibonacci}")