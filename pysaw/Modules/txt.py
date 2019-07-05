
from .baseModule import baseEndPoint
from ..Core.config import Config

# PySaw modules to handle txt files
 
class Txt(baseEndPoint):
    def __init__(self, Config: Config):
        self.Config = Config
        pass 

    def isValidEndpoint(self, level: str = ""):

        if level != "":
            return self.__IsValidLevel(level)
        
        return False

    def __IsValidLevel(self, level:str):
        levels = self.Config.ActiveConfig['PySaw']['txt']['Levels']

        for v in levels:
            if level == v:
                return True
        
        return False

    def __FormatMesage(self):
        f:str = self.Config.ActiveConfig['PySaw']['txt']['MessageTemplate']

        if f.__contains__('$$Level$$') == True:
            f = f.replace('$$Level$$', self.level)

        if f.__contains__('$$Message$$' == True):
            f = f.replace('$$Message$$', self.message)

        return f

    def Write(self, level:str, message:str):
        self.level = level
        self.message = message

        msg:str = self.__FormatMesage()
        pass

if __name__ == '__main__':
    Txt        