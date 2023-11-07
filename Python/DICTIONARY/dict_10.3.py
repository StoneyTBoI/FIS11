waehrung = {"2 Euro": 200,
            "1 Euro": 100,
            "50 Cent": 50,
            "20 Cent": 20,
            "10 Cent": 10,
            "5 Cent": 5,
            "2 Cent": 2,
            "1 Cent": 1}

rechnungsbetrag = float(input("Bitte geben Sie den Rechnungsbetrag ein: "))
bezahlbetrag = float(input("Bitte geben Sie den Betrag ein, mit dem bezahlt wurde: "))
rueckgeld = bezahlbetrag - rechnungsbetrag
print("Das Rückgeld beträgt:", rueckgeld, "€")

kohle = {w: 0 for w in waehrung}

print("Rückgeld in Münzen:")
for w, count in kohle.items():
    if count > 0:
        print(count, "x", w)
