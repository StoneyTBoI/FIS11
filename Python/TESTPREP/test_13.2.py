import random

try:
    # Datei für Speicherung
    datei = "Python/TESTPREP/13_2_Zahlenraten.csv"
    stream = open(datei, mode="a+", encoding="ANSI")
    ergebnis = int(random.randrange(1,1000)) # Zufällige Zahl für Spiel
    eingabe = 0
    anzahl_geraten = 1
    erraten = False

    while erraten == False:
        eingabe = int(input("Bitte Ganzzahl eingeben "))
        if (eingabe == ergebnis):
            erraten = True
            print("Das war richtig, du hast", anzahl_geraten, "versuche gebraucht!")
        else:
            anzahl_geraten = anzahl_geraten + 1
            print("Leider Falsch!")
            print(ergebnis)
            if (eingabe < ergebnis):
                print("Das Ergebnis ist GRÖßER als ", eingabe)
            elif (eingabe > ergebnis):
                print("Das Ergebnis ist KLEINER als ", eingabe)
    
except Exception as e:
    print("Fehler: ", e)