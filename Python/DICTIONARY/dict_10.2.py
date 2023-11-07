lagerbestand = {"Bourbon": 0,
                "Schokolade": 5,
                "Erdbeeren": 3,
                "Hopfenblütentee": 1,
                "Lasagne": 0,
                "Himbeeren": 4,
                "Eis": 7,
                "Litschi": 0}

def bestand_anzeigen():
    for key in lagerbestand:
        if lagerbestand[key] == 0:
            print("Der Bestand von", key, "beträgt:", lagerbestand[key])
            print("Der Artikel ist nicht auf Lager.")
            bestellung = input("Wollen Sie " + key + " bestellen? Bitte geben Sie 'ja' oder 'nein' ein: ")
            if bestellung == "ja":
                menge = int(input("Wie viele " + key + " möchten Sie bestellen? Bitte geben Sie die Menge ein: "))
                lagerbestand[key] += menge
                print("Der neue Bestand von", key, "beträgt:", lagerbestand[key])
        else:
            print("Der Bestand von", key, "beträgt:", lagerbestand[key])

bestand_anzeigen()