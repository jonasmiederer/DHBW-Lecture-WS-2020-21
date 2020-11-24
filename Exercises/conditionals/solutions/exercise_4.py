"""
Schaltjahr

Der Nutzer gibt eine Jahreszahl ein.
Es soll ermittelt und ausgegeben werden, ob es sich dabei um ein Schaltjahr handelt.

Hierbei greifen die Regeln, die in der Aufgabenstellung beschrieben wurden.
"""

# Einlesen der vom Nutzer eingegebenen Jahreszahl 
year = input("Bitte Jahreszahl eingeben: ")

# Umwandlung in Integer-Wert
year = int(year)

if year % 400 == 0:
    print(f"Das Jahr {year} ist ein Schaltjahr, da es durch 400 teilbar ist.")
elif year % 100 == 0:
    print(f"Das Jahr {year} ist kein Schaltjahr, da es durch 100 teilbar ist.")
elif year % 4 == 0:
    print(f"Das Jahr {year} ist ein Schaltjahr, da es durch 4 teilbar ist.")
else:
    print(f"Das Jahr {year} ist kein Schlatjahr")

#Alternativ:
"""
if year % 4 == 0:
    if year % 400 == 0:
        print(f"Das Jahr {year} ist ein Schaltjahr, da es durch 400 teilbar ist.")
    elif year % 100 == 0:
        print(f"Das Jahr {year} ist kein Schaltjahr, da es durch 100 teilbar ist.")
    else:
        print(f"Das Jahr {year} ist ein Schaltjahr, da es durch 400 teilbar ist.")
else:
    print(f"Das Jahr {year} ist kein Schlatjahr")
"""