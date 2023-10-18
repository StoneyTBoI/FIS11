sitze = [["x" for j in range(15)] for i in range(5)]

for reihe_print in sitze:
    print(" ".join(reihe_print))


weiter = 1


while weiter == 1:
    reihe = int(input("Bitte geben Sie eine Reihe ein: "))
    spalte = int(input("Bitte geben Sie eine Spalte ein: "))
    if reihe > 5 or spalte > 15:
        print("Der Sitz existiert nicht!")
    else:
        if sitze[reihe - 1][spalte - 1] == "x":
            sitze[reihe - 1][spalte - 1] = "o"
            print("Der Sitz wurde reserviert.")
        else:
            print("Der Sitz ist bereits reserviert.")

    for reihe_print in sitze:
        print(" ".join(reihe_print))

    print("Möchten Sie einen weiteren Sitz reservieren? (1/0)")
    weiter = int(input())
