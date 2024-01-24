from CLASS.pkw import PKW

# Menu
def menu():
    print("")

def fahren():
    print("KM-Stand vor der Fahrt: ")

impreza_wrx = PKW()
impreza_wrx.SetAktuelleFuellung(50)
impreza_wrx.SetBaujahr(2005)
impreza_wrx.SetFarbe("Blau")
impreza_wrx.SetKmStand(200000)
impreza_wrx.SetMarke("Subaru")
impreza_wrx.SetMaxFuellmenge(60)
impreza_wrx.SetSitze(5)
impreza_wrx.SetVerbrauch(12.5)