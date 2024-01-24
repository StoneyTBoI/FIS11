from CLASS.tier_b import Tier


def menu():
    print("Was möchtest du tun?")
    print("1. Füttern")
    print("2. Spielen")
    print("3. Status anzeigen")
    print("4. Beenden")
    eingabe = input("Eingabe: ")
    if eingabe == "1":
        fuettern()
    elif eingabe == "2":
        spielen()
    elif eingabe == "3":
        print("Status anzeigen")
        status()
    elif eingabe == "4":
        print("Beenden")
    else:
        print("Falsche Eingabe")
        menu()


# def Ausgabe():
#     print("Ausgabe")
#     print("Name: " + str(maunzi.GetName()))
#     print("Art: " + str(maunzi.GetArt()))

#     if maunzi.GetHungrig() == True:
#         print("Ist Hungrig")
#     elif maunzi.GetHungrig() == False:
#         print("Ist nicht Hungrig")
#     else:
#         print("Maunzi ist v̶̨̧̛̪̮̞̲͍͈̜̩̬͚̞̼̳̊̾͗̑͂͑́̔͘͝ȍ̸̡̥͓̩͍͕͉̗͓̯̣̟͙̤̝͈̆͊̋̄̊̒̇̅̈́̓́̑̀̑͛͗̽̂̿̂̀̈́̕̚̕͘͘ĩ̶̡̡̺̯̟͔̣̙͙̼̣̻͎̺̪̽͋̐̋̎̇̀̓͌̆͘͜͠d̵̤͔͓͚̅̾ ")


def status():
    print("Status")
    print(maunzi)
    if maunzi.GetHungrig() == True:
        print("Ist Hungrig")
    elif maunzi.GetHungrig() == False:
        print("Ist nicht Hungrig")
    else:
        print("What the fuck happened")

    menu()


def fuettern():
    print("Füttern")
    maunzi.SetHungrig(False)
    menu()


def spielen():
    print("MauWauPiepFiep")
    maunzi.SetHungrig(True)
    menu()


maunzi = Tier()
maunzi.SetName("Maunzi")
maunzi.SetArt("Scottish Fold")
maunzi.SetHungrig(True)

menu()