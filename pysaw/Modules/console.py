
from .baseModule import baseEndPoint
from .config import Config

from ..Core.message import Message

class Console(baseEndPoint):
    """
    About:

    """
    def __init__(self, Config: Config ):
        self.Config = Config
        pass

    # Replaceable property that we can load new messages into.
    __msg:Message

    def isValidEndpoint(self, level:str):
        """
        About:
        returns bool that states if the endpoint has a valid configuration to be able to handle messages.

        Parameters:
        level = pass the value that needs to be checked

        Returns: Bool
        """
        
        if level != "":
            # Exctract the allowed levels we will log
            levels = self.Config.ActiveConfig['PySaw']['Console']['Levels']

            # Loop though all of the values we will accept
            for v in levels:

                # Check each level against what was sent
                if level == v:
                    
                    # If we have a match return True
                    return True
        
        return False

    def __FormatMessage(self):
        f:str = self.Config.ActiveConfig['PySaw']['Console']['MessageTemplate']

        if f.__contains__('$$Level$$') == True:
            f = f.replace('$$Level$$', self.__msg.Level)

        if f.__contains__('$$Message$$') == True:
            f = f.replace('$$Message$$', self.__msg.Message)

        if f.__contains__('$$Line$$') == True:
            f = f.replace('$$Line$$', str(self.__msg.LineNumber))

        if f.__contains__('$$File$$') == True:
            f = f.replace('$$File$$', self.__msg.FileName)

        if f.__contains__('$$Method$$') == True:

            if not self.__msg.MethodName.__eq__('<module>'):
                f = f.replace('$$Method$$', self.__msg.MethodName)
            else:
                f = f.replace('$$Method$$', '')

        return f

    def Write(self, msg:Message, passBack:bool = False):
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

        self.__msg = msg
        s:str = self.__FormatMessage()
        
        print(s)

        if(passBack == True):
            return s

        pass

if __name__ == '__main__':
    Console