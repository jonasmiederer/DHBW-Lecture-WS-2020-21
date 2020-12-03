"""
Teilibarkeit

Der Nutzer kann 2 Zahlen eingeben
Es soll überprüft werden, ob die Zahlen restlos durcheinander teilbar sind und eine entsprechende Ausgabe erfolgen
"""

# Einlesen der beiden Zahlen
zahl_1 = input("Bitte 1. Zahl eingeben: ")
zahl_2 = input("Bitte 2. Zahl eingeben: ")

# Umwandlung der Zahlen in Integer Werte
zahl_1 = int(zahl_1)
zahl_2 = int(zahl_2)

# Überprüfung der Teilbarkeit

"""
2 Zahlen sind restlos durcheinander teilbar, wenn bei einer Division kein Rest bleibt.
Dies kann bequem mit dem Modulo-Operator überprüft werden, der bei einer Division jeweils
den Restwert liefert. Falls das Ergebniss der Modulo-Operation also 0 ist, bleibt bei der
Division kein Rest, die Zahlen sind restlos teilbar. Bleibt ein Rest (Modulo != 0), sind 
die Zahlen nicht restlos teilbar
"""

if zahl_1 % zahl_2 == 0:
    print(f"Die Zahlen {zahl_1} und {zahl_2} sind restlos teilbar")
else:
    print(f"Die Zahlen {zahl_1} und {zahl_2} sind nicht restlos teilbar. Rest {zahl_1 % zahl_2}")

"""
Alternativ kann die Berechnung auch ohne Modulo-Operator durchgeführt werden.
Hierbei werden die beiden Zahlen zunächst ganz normal dividiert. 
Anschließend wird überprüft, ob das Ergebnis der Division (eine Float-Zahl) gleich dem 
Ergebnis der Division als int-Zahl ist. Nur wenn die Darstellung als Float und Integer übereinstimmen, 
sind beide Zahlen teilbar.

division = zahl_1 / zahl_2
if division == int(division):
    print(f"Die Zahlen {zahl_1} und {zahl_2} sind restlos teilbar")
else:
    print(f"Die Zahlen {zahl_1} und {zahl_2} sind nicht restlos teilbar. Rest {zahl_1 % zahl_2}")

"""