class Ampel:
    __zustand = ""

    def getZustand(self):
        return self.__zustand

    def setZustand(self, zustand):
        self.__zustand = zustand

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass