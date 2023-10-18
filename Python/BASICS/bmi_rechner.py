gewicht = float(input("Bitte Gewicht eingeben (in kG): \n"))
groesse = float(input("Bitte Körpergröße eingeben (in Meter): \n"))
BMI = gewicht / (groesse ** 2)

if BMI < 18.5:
    print("Untergewicht!\n")
elif BMI < 25:
    print("Normalgewicht!\n")
elif BMI < 30:
    print("Übergewicht!\n")
elif BMI < 35:
    print("Adipositas Grad 1!\n")
else:
    print("Adipositas Grad 2!\n")