import random

def spiel():
    zufallszahl = random.randint(1, 100)
    spielerzahl = -1
    while spielerzahl != zufallszahl:
        spielerzahl = int(input("Bitte geben Sie eine Zahl zwischen 1 und 100 ein: "))
        if spielerzahl > zufallszahl:
            print("Die Zahl ist zu groß.")
        elif spielerzahl < zufallszahl:
            print("Die Zahl ist zu klein.")
        else:
            print("Sie haben die Zahl erraten!")

spiel()