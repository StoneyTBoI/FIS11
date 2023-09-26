eingabe = int(input("Bitte Zahl eingeben: "))
ausgabe = 1

while eingabe > 0:
    ausgabe = ausgabe * eingabe
    eingabe = eingabe - 1

print("\nErgebnis: ", ausgabe)
