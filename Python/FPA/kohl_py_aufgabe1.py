def kennwort():
    versuche = 1
    while (versuche <= 3):
        print("Eingabe Kennwort")
        kennwort = str(input())
        if (kennwort == "2Eofnl"):
            print("Hallo")
            break
        else:
            print(versuche)
        versuche = versuche + 1
    if (versuche > 3):
        print("Login wird gesperrt")
        input()
        
kennwort()