try:
    datei = "./Python/FILES/SUBFILES/alphabet_12_2.txt"
    stream = open(datei, mode="r", encoding="utf-8")
    zeichen = stream.read(1)
    zaehler = 1
    while zeichen != "":
        print(str(zeichen), "->", ord(zeichen), end=":")
        zeichen = zeichen.upper()
        print(str(zeichen), "->", ord(zeichen))
        zeichen = stream.read(1)
        zaehler += 1
    stream.close()
except Exception as e:
    print("Fehler:", e)
    