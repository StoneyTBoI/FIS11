user_eingabe = int(input("Bitte geben Sie eine Postleitzahl ein: "))
plz_ort_dict = {"63740": "Aschaffenburg", "97070": "Würzburg", "97072": "Würzburg", "97084": "Würzburg", "89231": "Neu-Ulm", "97424": "Schweinfurt", "91413": "Neustadt/Aisch"}
for plz, ort in plz_ort_dict.items():
    if int(plz) == user_eingabe:
        print("PLZ:", plz, "Ort:", ort)
