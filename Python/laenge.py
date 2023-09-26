eingabe_eins = str(input("Bitte Wort 1 eingeben: \n"))
eingabe_zwei = str(input("Bitte Wort 2 eingeben: \n"))

eins_length = len(eingabe_eins)
zwei_length = len(eingabe_zwei)

if(eins_length > zwei_length):
    print("Wort 1 ist länger! \n")
elif(eins_length < zwei_length):
    print("Wort 2 ist länger! \n")
else:
    print("Beide Worte sind gleich lang!\n")