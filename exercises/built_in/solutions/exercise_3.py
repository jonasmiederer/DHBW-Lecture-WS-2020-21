"""
Bogenmaß - Winkelmaß

Der Nutzer kann eine Zahl im Bogenmaß eingeben.
Ihm wird der entsprechende Wert im Gradmaß ausgegeben
"""

# Um einen exakten Wert für PI zu verwenden kann der Wert PI aus der eingebauten math-Bibliothek genutzt werden.
# Hierfür muss die Bibliothek zunächst importiert werden
import math

# Nutzereingabe des Bogenmaß-Wertes
bogenmass = input("Bitte Bogenmaß-Wert eingeben: ")

# Umwandlung des Strings in float
bogenmass = float(bogenmass)

# Konvertierung des Wertes in Gradmass
# Formel: gradmaß = (bogenmaß / PI) * 180° 

gradmass = (bogenmass / math.pi ) * 180

# Alternativ: PI als 3.14 anstatt des "exakten" Wertes aus der math-Bibliothek
#gradmass = (bogenmass / 3.14) * 180

# Ausgabe des Ergebnisses
print(f"{bogenmass} im Bogenmaß entsprechen {gradmass}°")