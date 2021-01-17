"""
Mitternachtsformel (Quadratische Lösungsformel)

Mithilfe des Programms sollen Gleichungen der Form ax^2 + bx + c = 0 gelöst werden.
Der Nutzer kann hierfür die Koeffizienten a, b und c eingeben.
"""

# Importieren der math-Bibliothek zur Berechnung von Quadratwurzeln
import math

print("Lösungsfindung für quadratische Gleichungen")

# Eingabe der Koeffizienten und Konvertierung dieser in float-Werte
a = float(input("Bitte Koeffizient a eingeben: "))
b = float(input("Bitte Koeffizient b eingeben: "))
c = float(input("Bitte Koeffizient c eingeben: "))

"""
 Lösungsformel: 
 
 x1 = (-b + sqrt(b^2 - 4ac)) / (2a)
 x2 = (-b - sqrt(b^2 - 4ac)) / (2a)
"""

x1 = (-b + (math.sqrt(b**2 - 4*a*c))) / (2*a)
x2 = (-b - (math.sqrt(b**2 - 4*a*c))) / (2*a)

"""
Alternativ für math.sqrt(x) kann die Quadratwurzel auch mit x**(0.5) berechnet werden.

x1 = (-b + (b**2 - 4*a*c)**(0.5)) / (2*a)
x2 = (-b - (b**2 - 4*a*c)**(0.5)) / (2*a)

ACHTUNG: 
Während die Funktion math.sqrt(x) lediglich für reelle Zahlen definiert ist und 
daher einen Fehler liefert, sollte der Term unter der Wurzel negativ sein, liefert 
die Berechnung mithilfe der Exponenten eine komplexe Zahl, sollte der Term unter der 
Wurzel negativ sein
"""

# Ausgabe der Lösungen
print(f"Die Lösungen sind x1={x1}, x2={x2}")