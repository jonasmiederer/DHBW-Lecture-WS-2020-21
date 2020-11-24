# Übungsaufgaben: Conditionals

## 1. Teilbarkeit

**Aufgabe:**

Schreiben Sie ein Programm, mit dem der Nutzer 2 Zahlen eingeben kann. Anschließend soll überprüft werden, ob die zweite Zahl durch die erste Zahl (restlos) teilbar ist und eine entsprechende Ausgabe erfolgen.

## 2. Temperaturen

**Aufgabe:**

Schreiben Sie ein Programm, mit dem der Nutzer eine Zahl sowie einen Buchstaben **F** oder **C** eingeben kann. Gibt der Nutzer den Buchstaben ”**F**” ein, soll die eingegebene Zahl von Grad Celsius in Grad Fahrenheit umgewandelt werden, umgekehrt soll mit demBuchstaben ”**C**” in Celsius konvertiert werden.


## 3. Mitternachtsformel

**Aufgabe:**

Schreiben Sie ein Programm, mit dem quadratische Gleichungen der Form ![ax^2 + bx +c = 0](https://latex.codecogs.com/png.latex?ax%5E2%20&plus;%20bx%20&plus;%20c%20%3D%200) gelöst werden können. Der Nutzer kann die entsprechenden Koeffizienten eingeben.

Hierbei soll überprüft werden, ob Lösungen im reellen Zahlenraum existieren. Ist dies nicht der Fall soll eine Fehlermeldung ausgegeben werden.

## 4. Schlatjahr

**Beschreibung:**

Schlatjahre treten auf, wenn

* die Jahreszahl durch 4 teilbar ist
* Ausnahme: Falls die Jahreszahl ebenfalls durch 100 ist, ist es kein Schaltjahr
* Ausnahme: Falls die Jahreszhal ebenfalls durch 400 teilbar ist, ist es ein Schaltjahr

**Aufgabe:**

Der Nutzer kann ein beliebiges Jahr eingeben. Das Programm ermittelt, ob es sich dabei um ein Schaltjahr handelt. Falls eine der oben beschriebenen Regeln greift, soll außerdem die Begründung ausgegeben werden (also warum es sich um (k)ein Schaltjahr handelt).

## 5. Alter & Gesetze 

**Beschreibung:**

In Deutschland, den USA und Großbritannien gelten bezüglich des Wahlalters ähnliche Gesetze: Grundsätzlich wahlberechtigt ist, wer das 18. Lebensjahr erreicht hat.

Anders sieht es dagegen bei der Legalität hinsichtlich des Erwerbs und Konsums von Alkohol aus. Undestillierte Getränke dürfen in Deutschland ab dem Alter von 16 Jahren konsumiert werden, während in Großbritannien ein Mindestalter von 18 und in den USA von 21 gelten.

**Aufgabe:**

Schreiben Sie ein Programm, das den Nutzer nach seinem Alter sowie seinem Herkunftsland (DE/UK/US) fragt.

Entsprechend seiner Eingabe soll eine Ausgabe erfolgen, die den Nutzer darauf hinweist, ob er wählen und legal Alkohol konsumieren darf.

Falls der Nutzer ein ungültiges Herkunfsland eingibt, soll er ebenfalls darauf hingewiesen werden.

## 6. Mathe Trainer

**Aufabe 1:**

Erstellen Sie einen Mathematik-Trainer, der dem Nutzer zufällige Rechenaufgaben stellt. Der Nutzer wird nach der korrekten Lösung gefragt, entsprechend der Eingabe soll zu jeder Aufgabe eine Ausgabe ("Die Lösung ist korrekt" oder "Die Lösung ist nicht korrekt") erfolgen. Falls die Eingabe nicht korrekt ist soll außerdem das korrekte Ergebnis ausgegeben werden.

Wurden alle Aufgaben bearbeitet soll zudem eine Auswertung erfolgen ("X/Y Aufgaben richtig (Z%)").

Stellen Sie dem Nutzer mindestens 5 Fragen.

**Aufgabe 2:**

Anstatt die Aufgaben statisch ("hardgecoded") im Code zu hinterlegen, sollen die Fragen dynamisch und zufällig erzeugt werden. Erzeugen Sie hierfür jeweils 2 Zufallszahlen zwischen 0 und 100 und verbinden diese mit einer zufällig gewählten Rechenoperation ("+" oder "-", wenn Sie möchten auch "*" und "/").

Zur Erzeugung von Zufallszahlen steht in Python die eingebaute Bibliothek `random` zur Verfügung. Diese muss zunächst importiert werden, bevor sie genutzt werden kann: 

```python
import random

# Erzeugung einer ganzzahligen Zufallszahl zwischen 0 und 5
random_integer = random.randint(0,5)

# Erzeugung einer zufälligen Fließkommazhal zwischen 0  und 1
random_float = random.random()
```