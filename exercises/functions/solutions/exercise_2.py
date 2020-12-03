"""
Umgekehrter Satz

Der Nutzer gibt einen Satz ein.
Dieser String wird an eine Funktion übergeben, die die Reihenfolge der Wörter umkehrt
und diesen umgekehrten Satz zurückgibt. 

Dieser Satz soll dann ausgegeben werden
"""

# Definition der Funktion
def reverse_sentence(sentence):
    # Die reverse_sentence Funktion akzeptiert einen Parameter, also den eingegeben Satz

    # Trenne den Satz anhand der Leerzeichen, um die einzelnen Wörter zu erhalten
    words = sentence.split()

    # Erzeuge reversed_sentence Variable, in der der umgekehrte Satz gespeichert wird
    reversed_sentence = ""

    # Iteriere rückwärts über alle Wörter und hänge diese der reversed_sentence Variable an (sowie jeweils ein Leerzeichen)
    for word in words[::-1]:
        reversed_sentence += (word + " ")
    
    # Gebe Inhalt von reversed_sentence zurück
    return reversed_sentence


# Einlesen des Satzes
sentence = input("Bitte geben Sie einen Satz ein: ")

# Aufruf der reverse_sentence Funktion
reversed_sentence = reverse_sentence(sentence)

# Ausgabe des umgekehrten Satzes
print("Rückwärts: ")
print(reversed_sentence)