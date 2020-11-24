"""
Temperaturen

Der Nutzer kann eine Temperatur sowie einen Buchstaben (C für Celsius oder F für Fahrenheit) eingeben.
Entsprechend der Eingabe sollen die Temperaturen umgewandelt und ausgegeben werden
"""

# Einlesen und Konvertierung der Temperatur
temperature = float(input("Bitte Temperatur eingeben: "))

# Ziel-Einheit
unit = input("In welche Einheit soll konvertiert werden (F/C)?: ")

# Überprüfen, ob gültige Einheit eingegeben wurde
if unit != "C" and unit != "F":
    print("Ungültige Einheit eingegeben")
else:
    if unit == "C":
        # Umwandlung von Fahrenheit in Celsius
        # Celsius = (Fahrenheit − 32) × 5/9
        converted_temperature = (temperature - 32) * (5/9)
        print(f"{temperature}° Fahrenheit entsprechen {converted_temperature}° Celsius")
    else:
        # Umwandlung von Celsius in Fahrenheit
        # Fahrenheit = (Celsius * 9/5) + 32
        converted_temperature = (temperature * (9/5)) + 32
        print(f"{temperature}° Celsius entsprechen {converted_temperature}° Fahrenheit")