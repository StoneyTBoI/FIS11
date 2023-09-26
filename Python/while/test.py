blöcke = int(input("Geben Sie die Anzahl der Blöcke ein: "))

höhe = 0

innerer_block = 1

while innerer_block <= blöcke:

    höhe += 1
    blöcke -= innerer_block
    innerer_block += 1

print("Die Höhe der Pyramide: ", höhe)
