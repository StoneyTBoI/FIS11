try:
    datei = "Python/FPA/kostueme.txt"
    # Dioctionaries anlegen
    dic = {}
    dic_kostueme = {}
    # Datei öffnen und auslesen
    with open("Python/FPA/kostueme.txt", "r", encoding="utf-8") as datei:
        for zeile in datei:
            key, value = zeile.strip().split(";")
            dic[key] = value
    # print(dic) # Ausgabe Testen
    # Nachkömmlinge in Datei eintragen
    with open("Python/FPA/kostueme.txt", "+a", encoding="utf-8") as datei:
        datei.write("\nSven;Vampir\n")
        datei.write("Anja;Gespenst")

    # Herrausfinden wie oft ein Kostüm vorkommt
    with open("Python/FPA/kostueme.txt", "r", encoding="utf-8") as datei:
        for key, value in dic.items():
            if value in dic_kostueme:
                dic_kostueme[value] += 1
            else:
                dic_kostueme[value] = 1
        print(dic_kostueme) # Ausgabe Testen
    # Kostüme Dictionary in CSV datei abspeichern
    with open("Python/FPA/kostuemeverteilung.csv", "w", encoding="utf-8") as datei:
        for key, value in dic_kostueme.items():
            datei.write(key + ";" + str(value) + "\n")
    print("Datei erfolgreich abgespeichert")
    # Prozentverteilung der Kostüme ausrechnen
    anzahl_kostueme = 0
    for key, value in dic_kostueme.items():
        anzahl_kostueme += value
    # print(anzahl_kostueme) # Ausgabe Testen
    # Prozentverteilung ausgeben
    for key, value in dic_kostueme.items():
        print(key, "==>", value, "==>", round((value / anzahl_kostueme) * 100, 2), "%")

# Falls Fehler auftritt
except Exception as e:
    print("Fehler: ", e)
