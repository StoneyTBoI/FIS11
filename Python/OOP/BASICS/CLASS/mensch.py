class Mensch:
    __alter = 0
    __vorname = ""
    __nachname = ""
    __familienstand = ""

    def get_Alter(self):
        return self.__alter

    def set_Alter(self, alter):
        self.__alter = alter

    def get_Vorname(self):
        return self.__vorname

    def set_Vorname(self, vorname):
        self.__vorname = vorname

    def get_Nachname(self):
        return self.__nachname

    def set_Nachname(self, nachname):
        self.__nachname = nachname

    def get_Familienstand(self):
        return self.__familienstand

    def set_Familienstand(self, familienstand):
        self.__familienstand = familienstand

    def geburtstag(self):
        self.__alter += 1
        
    def __init__(self):
        self.__familienstand = "ledig"
