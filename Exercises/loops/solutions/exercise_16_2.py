"""
Login System

(Hinweis: Programmablaufplan im img-Ordner)

Der Nutzer wird nach seinem Nutzernamen gefragt. Ist dieser nicht in der Liste der Nutzer enthalten,
wird der Nutzer gefragt, ob er einen neuen Nutzer anlegen möchte. Falls nicht, beginnt das Programm von vorne.
Falls er dies möchte, wird er 2x nach dem entsprechenden Passwort gefragt. Dies erfolgt solange, bis die beiden Passwörter übereinstimmen.
Ist dies der Fall, wird der Nutzer der Liste der Nutzer hinzugefügt. 

Anschließend beginnt der Login-Prozess von vorne wie in Aufabe 1.
"""

# Liste aller NutzerInnen
users = [
    {
        "username": "Celina",
        "password": "111111"
    },
    {
        "username": "Patrick",
        "password": "1234567"
    },
    {
        "username": "Nina",
        "password": "qwertz"
    },
    {
        "username": "Sebastian",
        "password": "abc123"
    },
    {
        "username": "Anna-Lena",
        "password": "1122334455"
    }
]

print("Um diese Anwendung zu nutzen, müssen Sie sich zunächst authentifizieren.")

# Erzeuge user-Variable, in der der entsprechende Nutzer gespeichert wurde, sobald er gefunden wurde
user = None

# Wiederhole solange, bis ein gültiger Nutzer gefunden wurde
while not user:
    username = input("Bitte Nutzernamen eingeben: ")

    # Überprüfe, ob Nutzer in der Liste der Nutzer enthalten ist:
    for existing_user in users:
        # Innerhalb der Liste überprüfe jedes Dictionary, ob der username dem eingegebenen Nutzernamen entspricht.
        
        if existing_user["username"] == username:
            # Nutzer wurde gefunden. Speichere diesen Nutzer in der user-Variable ab
            user = existing_user
            # Außerdem kann die Schleife hier beendet werden, da der Nutzer gefunden wurde
            break
    
    # Falls der Nutzer nicht gefunden wurde, überprüfe ob der Nutzer einen neuen Nutzer anlegen möchte
    if not user:
        print(f"Der Nutzer {username} existiert nicht.")

        create_new_user_input = input("Möchten Sie einen neuen Nutzer erstellen? (Ja/Nein): ")

        if create_new_user_input == "Ja":
            # Es soll ein neuer Nutzer erzeugt werden
            # Nutzer gibt sein Passwort 2x ein. Nur wenn beide Passwörter übereinstimmen wird fortgefahren
            passwords_do_match = False
            while not passwords_do_match:
                password1 = input("Bitte Passwort eingeben: ")
                password2 = input("Bitte Passwort erneut eingeben: ")

                if password1 == password2:
                    # Setze passwords_do_match auf True, damit Schleife beendet wird
                    passwords_do_match = True
                else:
                    print("Passwörter stimmen nicht überein")

            # Nun kann der Nutzer der Liste der existierenden Nutzer hinzugefügt werden
            users.append(
                {"username": username, "password": password1}
            )

            # Neuer Nutzer wurde erzeugt, fahre mit Login fort
            print(f"Der Nutzer {username} wurde erfolgreich angelegt.")
        else:
            # Eingabe ist nicht "Ja" und wird daher als "Nein" interpretiert
            print("Es wird kein neuer Nutzer angelegt")

# Die while-Schleife wird erst dann beendet, wenn ein gültiger Nutzer gefunden wurde.
# An dieser Stelle können wir also sicher sein, dass in der Variable user ein gültiger Nutzer gespeichert wurde

# Indikator, ob der Nutzer erfolgreich authtentifiziert wurde. Dient dazu, um festzustellen, ob der Nutzer tatsächlich korrekt eingeloggt wurde oder nur sein Passwort 3x falsch eingegeben hat.  
user_authenticated = False

# Frage den Nutzer nun nach seinem Passwort. Hierfür hat der Nutzer nur 3 Versuche
for attempt in range(3):
    password = input("Bitte Passwort eingeben: ")

    # Überprüfe, ob das Passwort übereinstimmt
    if password == user["password"]:
        # Passwort stimmt überein, Nutzer ist somit erfolgreich authentifiziert.
        # Setze user_authenticated auf True, außerdem kann die Schleife hier beendet werden
        user_authenticated = True
        break
    else:
        # Passwort stimmt nicht überein, gebe Fehlermeldung aus. Anschließend beginnt der nächste Schleifendurchlauf (falls noch nicht der 3. Versuch erreicht wurde)
        print(f"Das Passwort stimmt nicht mit dem Nutzernamen {username} überein.")

# Die Schleife ist beendet. Dies kann 2 Gründe haben:
# Der Nutzer hat erfolgreich sein korrektes Passwort eingegeben oder aber er hat 3x ein falsches Passwort eingegeben.
# Um festzustellen was davon zutrifft können wir die user_authenticated Variable nutzen.

if user_authenticated:
    print(f"Der Nutzer {username} wurde erfolgreich eingeloggt. Herzlich Willkommen!")
else:
    print(f"Für den Nutzer {username} wurde 3x ein falsches Passwort eingegeben. Programm wird beendet")