
from .baseModule import baseEndPoint
from .config import Config

class Console(baseEndPoint):
    def __init__(self, Config: Config ):
        self.Config = Config
        pass

    def isValidEndpoint(self, level: str = ""):
        """
        About:
        returns bool that states if the endpoint has a valid configuration to be able to handle messages.

        Parameters:
        level = pass the value that needs to be checked

        Returns: Bool
        """
        
        if level != "":
            return self.__IsValidLevel(level)
        
        return False

    def __IsValidLevel(self, level: str):
        # Exctract the allowed levels we will log
        levels = self.Config.ActiveConfig['PySaw']['Console']['Levels']

        # Loop though all of the values we will accept
        for v in levels:

            # Check each level against what was sent
            if level == v:
                
                # If we have a match return True
                return True

        # If all of them did not match, return False
        return False

    def __FormatMessage(self):
        f:str = self.Config.ActiveConfig['PySaw']['Console']['MessageTemplate']

        if f.__contains__('$$Level$$') == True:
            f = f.replace('$$Level$$', self.level)

        if f.__contains__('$$Message$$') == True:
            f = f.replace('$$Message$$', self.message)

        return f

    def Write(self, level: str, message: str, passBack:bool = False):
        """
        Writes the message that is sent to the console window

        level: string
            Defines the level that we are using for this message. Debug, Information, Error

        message: string
            Defines the message of the log we wanted to record.

        passBack: bool
            Defines if you want the message that is sent to console to also be returned.
            This was added to help test the function.
        """

        self.level = level
        self.message = message

        msg:str = self.__FormatMessage()

        

        print(msg)

        if(passBack == True):
            return msg

        pass

if __name__ == '__main__':
    Console