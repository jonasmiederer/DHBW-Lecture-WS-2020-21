"""
Mathe Trainer

Dem Nutzer sollen mind. 5 Rechenaufgaben präsentiert werden.
Der Nutzer kann jede der Fragen beantworten, dementsprechend erfolgt eine Ausgabe.

Am Ende erfolgt eine Auswertung der Ergebnisse.
"""

# Zählvariable, wie viele Fragen korrekt beantwortet wurden
correct_answers_count = 0

"""
Frage 1
"""
answer_1 = input("Frage 1: 53+12 = ")
correct_answer_1 = 53+12

# Umwandlung in Integer
answer_1 = int(answer_1)

if answer_1 == correct_answer_1:
    print("Das Ergebnis ist korrekt!")
    
    # Inkrementiere (Erhöhe) correct_answers_count um 1
    correct_answers_count = correct_answers_count +1
else:
    print(f"Das Ergebnis ist nicht korrekt! Richtiges Ergebnis: {correct_answer_1}")


"""
Frage 2
"""
answer_2 = input("Frage 2: 34-19 = ")
correct_answer_2 = 34-19

# Umwandlung in Integer
answer_2 = int(answer_2)

if answer_2 == correct_answer_2:
    print("Das Ergebnis ist korrekt!")
    
    # Inkrementiere (Erhöhe) correct_answers_count um 1
    correct_answers_count = correct_answers_count +1
else:
    print(f"Das Ergebnis ist nicht korrekt! Richtiges Ergebnis: {correct_answer_2}")


"""
Frage 3
"""
answer_3 = input("Frage 3: 99-57 = ")
correct_answer_3 = 99-57

# Umwandlung in Integer
answer_3 = int(answer_3)

if answer_3 == correct_answer_3:
    print("Das Ergebnis ist korrekt!")
    
    # Inkrementiere (Erhöhe) correct_answers_count um 1
    correct_answers_count = correct_answers_count +1
else:
    print(f"Das Ergebnis ist nicht korrekt! Richtiges Ergebnis: {correct_answer_3}")


"""
Frage 4
"""
answer_4 = input("Frage 4: 51+42 = ")
correct_answer_4 = 51+42

# Umwandlung in Integer
answer_4 = int(answer_4)

if answer_4 == correct_answer_4:
    print("Das Ergebnis ist korrekt!")
    
    # Inkrementiere (Erhöhe) correct_answers_count um 1
    correct_answers_count = correct_answers_count +1
else:
    print(f"Das Ergebnis ist nicht korrekt! Richtiges Ergebnis: {correct_answer_4}")

"""
Frage 5
"""
answer_5 = input("Frage 5: 10+57 = ")
correct_answer_5 = 10+57

# Umwandlung in Integer
answer_5 = int(answer_5)

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