from CLASS.tier import Tier


def Ausgabe():
    print("Ausgabe")
    print("Name: " + str(maunzi.GetName()))
    print("Art: " + str(maunzi.GetArt()))

    if maunzi.GetHungrig() == True:
        print("Ist Hungrig")
    elif maunzi.GetHungrig() == False:
        print("Ist nicht Hungrig")
    else:
        print("Maunzi ist v̶̨̧̛̪̮̞̲͍͈̜̩̬͚̞̼̳̊̾͗̑͂͑́̔͘͝ȍ̸̡̥͓̩͍͕͉̗͓̯̣̟͙̤̝͈̆͊̋̄̊̒̇̅̈́̓́̑̀̑͛͗̽̂̿̂̀̈́̕̚̕͘͘ĩ̶̡̡̺̯̟͔̣̙͙̼̣̻͎̺̪̽͋̐̋̎̇̀̓͌̆͘͜͠d̵̤͔͓͚̅̾ ")


maunzi = Tier()
maunzi.SetName("Maunzi")
maunzi.SetArt("Scottish Fold")
maunzi.SetHungrig(True)

Ausgabe()