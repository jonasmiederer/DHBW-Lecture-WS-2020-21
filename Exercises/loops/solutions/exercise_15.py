"""
Teilbarkeit

Es wird über die Zahlen von 0 bis 100 iteriert.
Entsprechend der Teilbarkeit mit den Ziffern von 1-9 werden die Zahlen in einem Dictionary gespeichert.

"""

# Anlegen des Dictionaries mit den Teilern als Keys
dictionary = {}

# Iteriere über die Zahlen von 0 bis 100
for number in range(1, 101):
    
    # Iteriere über die Teiler von 1 bis 9
    for divisor in range(1, 10):

        # Überprüfe für jede Zahl von 1 bis 100, ob diese für alle Ziffern von 1 bis 9 teilbar ist.
        if number % divisor == 0:
            # number ist durch divisor teilbar.
            # Füge number dem Dictionary unter dem Key divisor hinzu

            # Überprüfe zunächst, ob der Key divisor schon im Dictionary existiert
            # Falls nicht, füge dem Dictionary unter dem Key divisor eine leere Liste als Value hinz
            if divisor not in dictionary:
                dictionary[divisor] = []
            
            # Da nun sichergestellt ist, dass der Key existiert und der Value eine Liste ist, kann die Zahl dieser Liste hinzugefügt werden 
            dictionary[divisor].append(number)

# Ausgeben des Dictionaries
print(dictionary)

# Um Ausgabe zu verschönern:

# import pprint # Import von pprint (pretty print)
# pprint.pprint(dictionary)
