"""
Fizz Buzz

Für jede Zahlen zwischen start und stop sollen folgende Regeln angewendet werden:

* Falls die Zahl durch `div1` und `div2` teilbar ist, soll "fizzbuzz" ausgegeben werden
* Falls die Zahl nur durch `div1` teilbar ist, soll "fizz" ausgegeben werden
* Falls die Zahl nur durch `div2` teilbar ist, soll "buzz" ausgegeben werden
* Andernfalls soll einfach die Zahl ausgegeben werden

"""

# Einlesen der Werte und Umwandlung in Integer
start = int(input("Bitte Startwert eingeben: "))
stop = int(input("Bitte Stopwert eingeben: "))
div1 = int(input("Bitte 1. Dividend eingeben: "))
div2 = int(input("Bitte 2. Dividend eingeben: "))

# Iteriere über alle Werte zwischen start und stop
for current_number in range(start, stop):    
    if current_number % div1 == 0 and current_number % div2 == 0:
        # Falls aktuelle Zahl durch div1 und div2 teilbar ist, gebe fizzbuzz aus
        print("fizzbuzz")    
    elif current_number % div1 == 0:
        # Falls aktuelle Zahl nur durch div1 teilbar ist, gebe fizz aus
        print("fizz")    
    elif current_number % div2 == 0:
        # Falls aktuelle Zahl nur durch div2 teilbar ist, gebe buzz aus
        print("buzz")
    else:
        # Falls keine der Bedingungen zutrifft, gebe aktuelle Zahl aus.
        print(current_number)