"""
Mathe Trainer

Dem Nutzer sollen mind. 5 Rechenaufgaben präsentiert werden.
Der Nutzer kann jede der Fragen beantworten, dementsprechend erfolgt eine Ausgabe.

Am Ende erfolgt eine Auswertung der Ergebnisse.

Hierbei sollen die Fragen dynamisch und zufällig generiert werden.
"""

# Import der benötigten random Bibliothek
import random 

# Zählvariable, wie viele Fragen korrekt beantwortet wurden
correct_answers_count = 0

"""
Frage 1
"""
# Erzeugen der Zufallszahlen zwischen 0 und 100
value_1 = random.randint(0,100)
value_2 = random.randint(0,100)

# Zufällige Wahl der Rechenoperation
# Falls die erzeugte Zufallszahl zwischen 0 und 1 größer ist als 0,5 => wähle "+", andernfalls wähle "-"
random_float = random.random()
if random_float >= 0.5:
    # Bilde Summe
    correct_answer_1 = value_1+value_2
    answer_1 = int(input(f"Frage 1: {value_1}+{value_2} = "))
else:
    # Bilde Differenz
    correct_answer_1 = value_1-value_2
    answer_1 = int(input(f"Frage 1: {value_1}-{value_2} = "))

if answer_1 == correct_answer_1:
    print("Das Ergebnis ist korrekt!")
    
    # Inkrementiere (Erhöhe) correct_answers_count um 1
    correct_answers_count = correct_answers_count +1
else:
    print(f"Das Ergebnis ist nicht korrekt! Richtiges Ergebnis: {correct_answer_1}")

"""
Frage 2
"""
# Erzeugen der Zufallszahlen zwischen 0 und 100
value_1 = random.randint(0,100)
value_2 = random.randint(0,100)

# Zufällige Wahl der Rechenoperation
# Falls die erzeugte Zufallszahl zwischen 0 und 1 größer ist als 0,5 => wähle "+", andernfalls wähle "-"
random_float = random.random()
if random_float >= 0.5:
    # Bilde Summe
    correct_answer_2 = value_1+value_2
    answer_2 = int(input(f"Frage 2: {value_1}+{value_2} = "))
else:
    # Bilde Differenz
    correct_answer_2 = value_1-value_2
    answer_2 = int(input(f"Frage 2: {value_1}-{value_2} = "))

if answer_2 == correct_answer_2:
    print("Das Ergebnis ist korrekt!")
    
    # Inkrementiere (Erhöhe) correct_answers_count um 1
    correct_answers_count = correct_answers_count +1
else:
    print(f"Das Ergebnis ist nicht korrekt! Richtiges Ergebnis: {correct_answer_2}")

"""
Frage 3
"""
# Erzeugen der Zufallszahlen zwischen 0 und 100
value_1 = random.randint(0,100)
value_2 = random.randint(0,100)

# Zufällige Wahl der Rechenoperation
# Falls die erzeugte Zufallszahl zwischen 0 und 1 größer ist als 0,5 => wähle "+", andernfalls wähle "-"
random_float = random.random()
if random_float >= 0.5:
    # Bilde Summe
    correct_answer_3 = value_1+value_2
    answer_3 = int(input(f"Frage 3: {value_1}+{value_2} = "))
else:
    # Bilde Differenz
    correct_answer_3 = value_1-value_2
    answer_3 = int(input(f"Frage 3: {value_1}-{value_2} = "))

if answer_3 == correct_answer_3:
    print("Das Ergebnis ist korrekt!")
    
    # Inkrementiere (Erhöhe) correct_answers_count um 1
    correct_answers_count = correct_answers_count +1
else:
    print(f"Das Ergebnis ist nicht korrekt! Richtiges Ergebnis: {correct_answer_3}")


"""
Frage 4
"""
# Erzeugen der Zufallszahlen zwischen 0 und 100
value_1 = random.randint(0,100)
value_2 = random.randint(0,100)

# Zufällige Wahl der Rechenoperation
# Falls die erzeugte Zufallszahl zwischen 0 und 1 größer ist als 0,5 => wähle "+", andernfalls wähle "-"
random_float = random.random()
if random_float >= 0.5:
    # Bilde Summe
    correct_answer_4 = value_1+value_2
    answer_4 = int(input(f"Frage 4: {value_1}+{value_2} = "))
else:
    # Bilde Differenz
    correct_answer_4 = value_1-value_2
    answer_4 = int(input(f"Frage 4: {value_1}-{value_2} = "))

if answer_4 == correct_answer_4:
    print("Das Ergebnis ist korrekt!")
    
    # Inkrementiere (Erhöhe) correct_answers_count um 1
    correct_answers_count = correct_answers_count +1
else:
    print(f"Das Ergebnis ist nicht korrekt! Richtiges Ergebnis: {correct_answer_4}")

"""
Frage 5
"""
# Erzeugen der Zufallszahlen zwischen 0 und 100
value_1 = random.randint(0,100)
value_2 = random.randint(0,100)

# Zufällige Wahl der Rechenoperation
# Falls die erzeugte Zufallszahl zwischen 0 und 1 größer ist als 0,5 => wähle "+", andernfalls wähle "-"
random_float = random.random()
if random_float >= 0.5:
    # Bilde Summe
    correct_answer_5 = value_1+value_2
    answer_5 = int(input(f"Frage 5: {value_1}+{value_2} = "))
else:
    # Bilde Differenz
    correct_answer_5 = value_1-value_2
    answer_5 = int(input(f"Frage 5: {value_1}-{value_2} = "))

if answer_5 == correct_answer_5:
    print("Das Ergebnis ist korrekt!")
    
    # Inkrementiere (Erhöhe) correct_answers_count um 1
    correct_answers_count = correct_answers_count +1
else:
    print(f"Das Ergebnis ist nicht korrekt! Richtiges Ergebnis: {correct_answer_5}")



"""
Auswertung
"""
print("Alle Fragen wurden beantwortet")
print("Ergebnisse: ")
print(f"{correct_answers_count} von 5 Fragen korrekt beantwortet")
print(f"{100*correct_answers_count/5}% korrekt beantwortet")