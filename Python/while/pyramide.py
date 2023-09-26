bloecke = int(input("Geben Sie die Anzahl der Blöcke ein: "))

hoehe = 0

innerer_block = 1

while innerer_block <= bloecke:

    hoehe += 1
    bloecke -= innerer_block
    innerer_block += 1

print("Die höhe der Pyramide: ", hoehe)
