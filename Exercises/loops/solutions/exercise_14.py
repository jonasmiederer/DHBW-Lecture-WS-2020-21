"""
Vokabel-Tainer

Der Nutzer wird nach der Übersetzung der zufällig gemischten Vokabeln gefragt, entsprechend der Eingabe soll eine Ausgabe erfolgen.
Zuletzt soll auch eine Auswertung ausgegeben werden
"""

# Importieren der random-Bibliothek, die für das Mischen der Liste und dem Erzeugen von Zufallszahlen benötigt wird
import random

# Zählvariable, wie viele Übersetzungen korrekt sind
correct_translations_count = 0

# Anlegen der Vokabelliste
vocabulary = [
    {"de": "Pferd", "en": "horse"},
    {"de": "Kuh", "en": "cow"},
    {"de": "Hund", "en": "dog"},
    {"de": "Katze", "en": "cat"},
    {"de": "Banane", "en": "banana"},
    {"de": "Erdbeere", "en": "strawberry"},
    {"de": "Apfel", "en": "apple"}
]

# Mischen der Vokabelliste:
random.shuffle(vocabulary)

# Nun wird über jeden Eintrag der Vokabelliste iteriert:
for vocab in vocabulary:
    # Jeder Eintrag stellt dabei ein Dictionary dar

    # Es soll zufällig entweder das deutsche oder das englische Wort abgefragt werden. Hierzu wird eine Zufallszahl zwischen 0 und 1 erzeugt.
    # Ist diese Zufallszahl >= 0.5, wird die deutsche Übersetzung abgefragt, andernfalls die englische.

    random_float = random.random()
    if random_float >= 0.5:
        # Abfrage der deutschen Vokabel
        translation = input(f"{vocab['en']} auf deutsch?: ")
        if translation == vocab['de']:
            print("Übersetzung ist korrekt!")
            
            # Erhöhe correct_translations_count um 1
            correct_translations_count += 1
        else:
            print(f"Übersetzung ist nicht korrekt! Richtige Übersetzung: {vocab['de']}")
    else:
        # Abfrage der englischen Vokabel
        translation = input(f"{vocab['de']} auf englisch?: ")
        if translation == vocab['en']:
            print("Übersetzung ist korrekt!")
            
            # Erhöhe correct_translations_count um 1
            correct_translations_count += 1
        else:
            print(f"Übersetzung ist nicht korrekt! Richtige Übersetzung: {vocab['en']}")

# Schleife ist beendet, alle Vokabeln wurden abgefragt.
# Ausgabe der Auswertung

print("Vokabeltest beendet")
print() # Leerzeile

print("Auswertung:")
print(f"Es wurden {correct_translations_count} von {len(vocabulary)} Vokabeln korrekt übersetzt")
print(f"Es wurden {100*correct_translations_count/len(vocabulary)} % der Vokabeln korrekt übersetzt")