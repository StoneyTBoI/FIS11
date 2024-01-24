class Tier:
    __name = ""
    __art = ""
    __farbe = ""
    __futter = ""
    __hungrig = False

    def GetName(self):
        return self.__name
    
    def SetName(self, name):
        self.__name = name

    def GetArt(self):
        return self.__art
    
    def SetArt(self, art):
        self.__art = art

    def GetFarbe(self):
        return self.__farbe
    
    def SetFarbe(self, farbe):
        self.__farbe = farbe

    def GetFutter(self):
        return self.__futter
    
    def SetFutter(self, futter):
        self.__futter = futter

    def GetHungrig(self):
        return self.__hungrig
    
    def SetHungrig(self, hungrig):
        if hungrig == True:
            self.__hungrig = True
        elif hungrig == False:
            self.__hungrig = False

    def __init__(self) -> None:
        pass

    def __str__(self):
        return f"{self.__name} ({self.__art})"