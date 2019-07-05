
from .baseModule import baseEndPoint
from ..Core.message import Message

class Console(baseEndPoint):
    """
    About:

    """
    def __init__(self, Config):
        """
        Config contains the json data that was extracted.
        """
        
        # We have data in Config rather then null
        # Try to find the values
        try:
            self.Levels = Config['PySaw']['Console']['Levels']
        except Exception:
            print("Unable to find PySaw.Console.Levels in the configuration file.")
            self.Levels:str = ['']
    
        try:
            self.Template = Config['PySaw']['Console']['Template']
        except Exception:
            print("Unable to find PySaw.Console.Template in the configuration file.")
            self.Template:str = ''

        try:
            self.IsOutputColored = Config['PySaw']['Console']['IsOutputColored']
        except Exception:
            print("Unable to find PySaw.Console.IsOutputColored in the configuration file.")
            self.IsOutputColored:bool = True
        pass

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
            levels = self.Levels

            # Loop though all of the values we will accept
            for v in levels:

                # Check each level against what was sent
                if level == v:
                    
                    # If we have a match return True
                    return True
        
        return False

    def __FormatMessage(self):
        f:str = self.Template
        
        if f.__contains__('$$Level$$') == True:
            f = f.replace('$$Level$$', self.__msg.Level)

        if f.__contains__('$$Message$$') == True:
            f = f.replace('$$Message$$', self.__msg.Message)

        if f.__contains__('$$Line$$') == True:
            f = f.replace('$$Line$$', str(self.__msg.LineNumber))

        if f.__contains__('$$File$$') == True:
            f = f.replace('$$File$$', self.__msg.FileName)

        if f.__contains__('$$Method$$') == True:
            f=f.replace('$$Method$$', self.__msg.MethodName)
            #if self.__msg.MethodName.__eq__('<module>') == False:
             #   f = f.replace('$$Method$$', self.__msg.MethodName)
            #else:
            #    f = f.replace('$$Method$$', '')

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