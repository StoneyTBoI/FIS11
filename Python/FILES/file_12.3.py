try:
    datei="./Python/FILES/SUBFILES/namen_12.3.txt"
    stream = open(datei, mode="r", encoding="utf-8")
    anzahl_teams = 0
    teams = [[] for _ in range(5)]
    for zeile in stream:
        if anzahl_teams < 5:
            teams[anzahl_teams].append(zeile.strip())
            if len(teams[anzahl_teams]) == 4:
                anzahl_teams += 1
        else:
            break
    stream.close()
    print(teams[:anzahl_teams])
    print("Es wurden", anzahl_teams, "Gruppen gebildet.")
except Exception as e:
    print("Fehler:", e)