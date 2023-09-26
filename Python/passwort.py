passwort_klein = "cringe"
passwort_gross = "Cringe"
pw_eingabe = str(input("Bitte Passwort eingeben\n"))

if(pw_eingabe == passwort_klein or pw_eingabe == passwort_gross):
    print("Korrekt!\n")
else:
    print("Falsch!\n")