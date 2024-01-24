class PKW:
    __AktuelleFuellung = 0
    __Baujahr = 0
    __Farbe = ""
    __KmStand = 0
    __Marke = ""
    __maxFuellmenge = 0
    __sitze = 0
    __verbrauch = 0.0

#Getter und Setter
    def GetAktuelleFuellung(self):
        return self.__AktuelleFuellung
    def SetAktuelleFuellung(self, AktuelleFuellung):
        self.__AktuelleFuellung = AktuelleFuellung
    def GetBaujahr(self):
        return self.__Baujahr
    def SetBaujahr(self, Baujahr):
        self.__Baujahr = Baujahr
    def GetFarbe(self):
        return self.__Farbe
    def SetFarbe(self, Farbe):
        self.__Farbe = Farbe
    def GetKmStand(self):
        return self.__KmStand
    def SetKmStand(self, KmStand):
        self.__KmStand = KmStand
    def GetMarke(self):
        return self.__Marke
    def SetMarke(self, Marke):
        self.__Marke = Marke
    def GetMaxFuellmenge(self):
        return self.__maxFuellmenge
    def SetMaxFuellmenge(self, maxFuellmenge):
        self.__maxFuellmenge = maxFuellmenge
    def GetSitze(self):
        return self.__sitze
    def SetSitze(self, sitze):
        self.__sitze = sitze
    def GetVerbrauch(self):
        return self.__verbrauch
    def SetVerbrauch(self, verbrauch):
        self.__verbrauch = verbrauch

# Konstruktor
    # def __init__(self, AktuelleFuellung, Baujahr, Farbe, KmStand, Marke, maxFuellmenge, sitze, verbrauch) -> None:
        # self.__AktuelleFuellung = AktuelleFuellung
        # self.__Baujahr = Baujahr
        # self.__Farbe = Farbe
        # self.__KmStand = KmStand
        # self.__Marke = Marke
        # self.__maxFuellmenge = maxFuellmenge
        # self.__sitze = sitze
        # self.__verbrauch = verbrauch
    def __init__(self) -> None:
        pass
