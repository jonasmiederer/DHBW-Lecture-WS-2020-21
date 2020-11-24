"""
Altersberechnung

Der Nutzer gibt sein Geburtsjahr ein.
Das Programm berechnet sein Alter und gibt dieses aus.

"""

# Eingabe des Geburtsjahrs
year_of_birth = input("Bitte Geburtsjahr eingeben: ")

# Umwandlung in Integer-Wert
year_of_birth = int(year_of_birth)

# Berechnung des Alters
age = 2020 - year_of_birth

# Ausgabe
print(f"Sie sind {age} Jahre alt")