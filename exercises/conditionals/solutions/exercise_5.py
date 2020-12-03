"""
Alter & Gesetze

In den USA, UK und DE gilt ein Mindestwahlalter von 18.
Der Erwerb von Alkohol ist in DE ab 16 Jahren gestattet, in UK ab 18 und in US ab 21.

Der Nutzer soll nach seinem Herkunftsland und Alter gefragt werden und entsprechend darauf hingewiesen werden, 
ob er wählen sowie legal Alkohol konsumieren darf.
"""

# Abfrage des Herkunfslands & Alters
age = input("Wie alt sind Sie?: ")
country = input("Woher kommen Sie (DE/UK/US)?: ")

# Umwandlung des Alters von String in Integer
age = int(age)

# Überprüfung der Eingabe des Herkunftslandes
if country != "DE" and country != "UK" and country != "US": # oder kürzer: if country not in ["DE", "UK", "US"]: 
    print(f"Das Land {country} ist nicht bekannt")
else:
    # Falls Nutzer mind. (>=) 18 Jahre alt ist, darf er wählen
    if age >= 18:
        print("Sie dürfen wählen")
    else: 
        print("Sie dürfen nicht wählen")
    
    # Je nachdem aus welchem Land der Nutzer kommt gelten unterschiedliche Altersregelungen hinsichtlich Alkoholkonsum
    if country == "DE" and age >= 16:
        print("Sie dürfen Alkohol konsumieren")
    elif country == "UK" and age >= 18:
        print("Sie dürfen Alkohol konsumieren")
    elif country == "US" and age >= 21:
        print("Sie dürfen Alkohol konsumieren")
    else:
        # Falls keine der vorherigen Regeln greift bedeutet das, dass der Nutzer keinen Alkohol trinken darf.
        print("Sie dürfen keinen Alkohol konsumieren")
