try:
    datei = "./Python/FILES/SUBFILES/namen_12_4.txt"
    stream = open(datei, mode="r", encoding="utf-8")
    alphabet = {
        buchstabe: {"Buchstabe": buchstabe, "anzahl": 0} for buchstabe in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    }
    zeichen = stream.read(1)
    while zeichen != "":
        zeichen = zeichen.upper()
        if zeichen in alphabet:
            alphabet[zeichen]["anzahl"] += 1
        zeichen = stream.read(1)
    for buchstabe in alphabet:
        print(alphabet[buchstabe]["Buchstabe"], "Anzahl:", alphabet[buchstabe]["anzahl"])
except Exception as e:
    print("Fehler:", e)