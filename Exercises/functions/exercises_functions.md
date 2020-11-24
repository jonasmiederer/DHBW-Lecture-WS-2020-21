# Übungsaufgaben: Funktionen

## 1. Größte eingegebene Zahl

**Aufgabe:**

Schreiben Sie ein Programm, bei dem der Nutzer wiederholt nach der Eingabe einer Zahl gefragt wird. Sobald "X" eingegeben wird, wird die Abfrage beendet.
Anschließend sollen die eingegebenen Zahlen, die in einer Liste gespeichert wurden, an eine Funktion übergeben werden, die die größte Zahl in dieser Liste findet und zurückgibt.

Diese Zahl soll dem Nutzer ausgegeben werden.

## 2. Umgekehrter Satz

**Aufgabe:**

Schreiben Sie ein Programm, bei dem der Nutzer einen Satz eingeben kann. Dieser Satz soll an eine Funktion übergeben werden, die einen String als Parameter akzeptiert. Innerhalb dieser Funktion soll die Reihenfolge der Wörter des Satzes umgekehrt werden und der so neu erzeugt String (umgekehrter Satz) zurückgegeben werden. 

Dieser soll schließlich ausgegeben werden.


## 3. Teilbarkeit

**Aufgabe:**

Schreiben Sie eine Funktion, bei dem der Nutzer zwei beliebige Zahlen eingeben kann. Anschließend soll mithilfe der Funktion `is_divisible`, die die zwei Argumente erwartet, überprüft werden, ob die zwei Zahlen durcheinander teilbar sind und entsprechend einen booleschen Wert zurückgeben. Anhand des Rückgabewertes soll außerhalb der Funktion ausgegeben werden: "Die Zahlen `Zahl1` und `Zahl2` sind (nicht) durcheinander teilbar"

## 4. Primzahl

**Aufgabe:**

Schreiben Sie eine Funktion, bei dem der Nutzer eine beliebige positive Ganzzahl eingeben kann. Diese Zahl soll an eine Funktion namens `is_prime` übergeben werden, in der überprüft wird, ob die übergebene Zahl eine Primzahl ist und dementsprechend einen booleschen Wert zurückgibt. Innerhalb der `is_prime`-Funktion soll die `is_divisible`-Funktion aus der Aufgabe "Teilbarkeit" verwendet werden.

Anhand dieses Rückgabewertes soll außerhalb der Funktion eine entsprechende Ausgabe erfolgen.



## 5. Luhn-Algorithmus
    
**Beschreibung**

Der Luhn Algorithmus ist eine einfache Formel zur Berechnung von Prüfziffern bzw. Prüfsummen, mithilfe dessen die Integrität einer gewissen Zahl (Information) überprüft werden kann. So kann beispielsweise festgestellt werden, dass die Information bei der Übertragung oder Dekodierung beschädigt wurde.

Stimmen Prüfziffern nicht überein, ist die Nachricht fehlerhaft übertragen worden, bei einer Übereinstimmung kann mit hoher Wahrscheinlichkeit von einer korrekten Übertragung ausgegangen werden.
Prüfziffern werden in der Praxis sehr häufig eingesetzt, beispielsweise bei der Sozialversicherungsnummer, Kontonummern, Wertpapierkennnummern, ...

Der Algorithmus kann folgendermaßen beschrieben werden:

*  Durchlaufe die Nummer ziffernweise von rechts nach links und bilde die Summe der Ziffern, aber: Verdoppele dabei jede zweite Ziffer, und wenn dabei ein Wert größer als 9 herauskommt, subtrahiere 9
    
* Wenn die Summe als letzte Ziffer eine 0 hat, erkenne die Nummer als gültig an und sonst nicht

**Aufgabe**

Schreiben Sie eine Funktion `is_luhn_valid`, die als Parameter eine Zahl entgegennimmt. Innerhalb der Funktion soll nach dem oben beschriebenen Algorithmus geprüft werden, ob die Prüfsumme korrekt ist und als Rückgabewert dementsprechend ein boolescher Wert zurückgegeben werden.

Außerhalb der Funktion soll eine Ausgabe erfolgen, ob die Integrität der Zahl gegeben ist.

**Beispiel**

* Eingabewert: *4556 7375 8689 9855*, Rückgabewert `True`
* Eingabewert: *4024 0071 0902 2143*, Rückgabewert `False`