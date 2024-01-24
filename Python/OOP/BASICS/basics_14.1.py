from CLASS.mensch import Mensch


def Ausgabe():
    print("Ausgabe")
    print("Alter: " + str(ich.get_Alter()))
    print("Vorname: " + ich.get_Vorname())
    print("Nachname: " + ich.get_Nachname())
    print("Familienstand: " + ich.get_Familienstand())
    print("")


ich = Mensch()
print(Mensch)
print(ich)

ich.set_Alter(22)
ich.set_Vorname("Max")
ich.set_Nachname("Mustermann")

Ausgabe()

ich.geburtstag()

Ausgabe()
