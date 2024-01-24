try:
    datei = open("Python/TESTPREP/13_1_Produkte.csv", "r")
    produkte = {}
    for zeile in datei:
        teil = zeile.strip().split(";")
        produkt_name = teil[0]
        produkt_anzahl = int(teil[1])
        produkte[produkt_name] = produkt_anzahl
    datei.close()
    print(produkte)
except Exception as e:
    print("Fehler: ", e)