pin_code = [1, 2, 3, 4]

print("Bitte geben Sie die PIN ein:")
eingabe = input()

eingabe_liste = [int(eingabe_tmp) for eingabe_tmp in eingabe]

if eingabe_liste == pin_code:
    print("Die PIN ist korrekt.")
else:
    print("Die PIN ist falsch.")