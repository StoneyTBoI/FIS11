try:
    print("Bitte Wählen sie ein Gedicht aus:")
    gedicht = input(str("erlkoenig | ribbeck | zauberlehrling: "))
    datei = ""
    if gedicht == "erlkoenig":
        datei = "./Python/FILES/SUBFILES/erlkoenig_12_1.txt"
    elif gedicht == "ribbeck":
        datei = "./Python/FILES/SUBFILES/ribbeck_12_1.txt"
    elif gedicht == "zauberlehrling":
        datei = "./Python/FILES/SUBFILES/zauberlehrling_12_1.txt"
    else:
        print("Falsche Eingabe!")
    stream = open(datei, mode="r", encoding="utf-8")
    text = stream.read()
    print(text)
    words = text.split()
    gesamtlaenge = sum(len(word) for word in words)
    durchschnittslaenge = gesamtlaenge / len(words)
    print("Durchschnittliche Wortlänge:", durchschnittslaenge)
    stream.close()
except Exception as e:
    print("Fehler beim Öffnen der Datei: ", e)
