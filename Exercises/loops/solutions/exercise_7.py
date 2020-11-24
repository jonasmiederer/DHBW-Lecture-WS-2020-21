"""
Quersumme

Der Nutzer gibt eine beliebige Ganzzahl ein. Von dieser Zahl wird die Quersumme
berechnet und ausgegeben.

Die Quersumme entspricht der Summe aller Ziffern der jeweiligen Zahl
"""

# Einlesen der Zahl
number = input("Bitte geben Sie eine Zahl ein, von der die Quersumme berechnet werden soll: ")

# Die Zahl wird nicht in Integer umgewandelt.
# Es ist einfacher, die Quersumme einer Zahl zu berechnen, wenn diese als String vorliegt, als wenn sie als int dargestellt wird.

# Erstelle Variable, in der die Quersumme gespeichert wird
sum = 0

# Um die Quersumme zu berechnen muss nun jede Ziffer eingelesen und aufaddiert werden.
# Falls die eingegebene Zahl als String vorliegt, kann ganz einfach über diesen String iteriert werden.
# Dabei stellt jedes "Zeichen" dieses String eine Ziffer dar. 

for digit in number:
    # Diese Ziffer liegt noch im String-Format vor. Um sie aber zur Quersumme addieren zu können, muss sie nun in den Integertyp konvertiert werden
    int_digit = int(digit)

    # Addiere Ziffer zur Quersumme
    sum += int_digit

print(f"Die Quersumme von {number} ist {sum}")