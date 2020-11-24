# Übungsaufgaben: Eingabe & Ausgabe

## 1. Altersberechnung

**Aufgabe**

Schreiben Sie ein Programm, bei dem der Nutzer sein Geburtsjahr eingeben kann.
Berechnen Sie das Alter des Nutzers und geben Sie dieses entsprechend aus.

**Erweiterung**

Beziehen Sie auch den Monat und den Tag des Geburtstags in die Berechnung mit ein, um stes ein korrektes Ergebnis zu liefern.

**Erweiterung**

Wenn das aktuelle Jahr statisch im Code hinterlegt wird ("hardcoding"), würde das Programm falsche Ergebnisse liefern, sobald das Jahr vorüber ist. Daher ist es die bessere Lösung, das aktuelle Jahr dynamisch zu ermitteln und dieses als Basis für die Altersberechnung zu nutzen. Hierzu steht in Python die eingebaute `datetime`-Bibliothek zur Verfügung, mit der mittels `datetime.datetime.now()` das aktuelle Datum abgefragt werden kann. Dieses liefert über das Attribut `year` das aktuelle Jahr: 
```python
import datetime

current_date = datetime.datetime.now()
current_year = current_date.year
print(f"Aktuelles Jahr: {current_year}")
```