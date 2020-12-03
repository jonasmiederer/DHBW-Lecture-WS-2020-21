"""
Mathematische Formel

Der Nutzer kann eine Ganzzahl k >= 1 eingeben. Anschließend soll der Wert der in der 
Aufgabenstellung gegebenen Formel berechnet und ausgegeben werden.

Formel in LaTex-Schreibweise:
$\prod_{i=1}^{k}{i^{\dfrac{1}{i+0.5}} + log_{e}{i} - cos(2i)}$

"""

# Importieren der eingebauten math-Bibliothek, um die Logarithmus und cosinus-Funktionen zu nutzen
import math

# Einlesen von k
k = int(input("Bitte Wert für k eingeben (>= 1): "))

if k < 1:
    print("Bitte gültigen Wert für k eingeben")
else:
    """
    Abbilden der Formel.

    Grundsätzlich handelt es sich bei der Formel um ein Produkt, dessen Faktoren sich in der Belegung
    des Wertes i unterscheiden.
    """

    # In der Variablen product wird jeweils das Zwischenergebnis nach der Multiplikation mit den Faktoren gespeichert.
    # Initial wird die Variable mit dem neutralen Element der Multiplikation (1) belegt.    
    product = 1

    # Iteriere über jeden Wert für i über i=1 bis k
    for i in range(1, k+1):
        # Berechnung des Faktors
        factor  = i**(1 / (i + 0.5)) + math.log(i) - math.cos(2*i)

        # Multipliziere den Wert des Faktors zum Zwischenprodukt hinzu
        product = product * factor
    
    # Nachdem alle Werte der Schleife durchlaufen wurden ist in product das Endergebnis gespeichert.
    print(f"Das Ergebnis ist {product}")

