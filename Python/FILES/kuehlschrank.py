schnitzel_vom_vortag = True

def kuehlschrank():
    if schnitzel_vom_vortag == True:
        kuehlen(schnitzel_vom_vortag)
    else:
        print()

def kuehlen(schnitzel_vom_vortag):
    ranzig = True
    if schnitzel_vom_vortag == ranzig:
        print("Das Schnitzel ist ranzig!")
