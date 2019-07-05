import typing
import json
import os
import inspect
import sys

from .Modules.console import Console
from .Core.message import Message
#from txt import Txt

class pysaw:
    """
    PySaw is the gateway class to your logging needs.

    Attributes:
        PathConfig: str
            Defines where the configuration file is.

    Methods:
        ExportActiveConfig()
        Emergency()
        Alert()
        Critical()
        Error()
        Warning()
        Notice()
        Information()
        Debug()
    """

    def __init__(self, PathConfig: str):

        # Check to see if we can find the config file
        if os.path.exists(PathConfig):

            # Open the file, read it and store in memory
            with open(PathConfig) as jsonFile:
                try:
                    self.__ActiveConfig = json.load(jsonFile)
                except Exception:
                    print(f"Failed to read {PathConfig}")


        #if PathConfig != "" and configExists == True:
            # Generate a new instace of our Config with the path we have been given
         #   self.Config = Config(PathConfig=PathConfig)
        #else:
        #    self.Config = Config(PathConfig="")

        # Generate the endpoint classes 
        self.Console = Console(self.__ActiveConfig)
        
        pass

    def __LoadConfig(self, PathConfig: str):
        """
        Been replaced by init handling the config
        """
      
        result = os.path.exists(PathConfig)
        if result == True:
            # Take in the config and load values
            cfg = Config(PathConfig=PathConfig)
            
            print(PathConfig)

    def ExportActiveConfig(self, PathConfig: str, OverWrite: bool=False):
        """
        This generates a new configuration file to be used.
        NewConfig(PathConfig)
        NewConfig(PathConfig, True)    
        """
        self.__config.ExportActiveConfig(PathConfig, OverWrite)
        cfg = Config()
        if OverWrite == True:
            cfg.NewConfig(PathConfig, True)
            pass

        else:
            cfg.NewConfig(PathConfig, False)
            pass

        pass

    def Emergency(self, message: str):
        """
        Logs a message about events that relate to unusable actions.
        """
        #self.__LogMessage("Emergency", message)

    def Alert(self, message: str):
        """
        Logs a message about events that require immediate action.
        """
        #self.__LogMessage("Alert", message)

    def Critical(self, message: str):
        """
        Logs a message about events that refer to critical actions.
        """
        #self.__LogMessage("Critical", message)

    def Error(self, message: str):
        """
        Logs a message about events that need to be reviewed.
        Use to monitor Try/Except messages.       
        """
        #self.__LogMessage("Error", message)

    def Warning(self, message: str):
        """
        Logs a message about events that could still work but not expected results.
        """
        #self.__LogMessage("Warning", message)

    def Notice(self, message: str):
        """
        Logs a message about events that are not errors but not expected results.        
        """
        #self.__LogMessage("Notice", message)

    def Information(self, message: str):
        """
        Logs a message about events that contain information.
        """
        #self.__LogMessage("Information", message)

    def Debug(self, message: str):
        """
        Logs a message that contains debugging information

        Debug("This is a test")
        """
        ins = inspect.stack()[1]
        lineNum: int = inspect.stack()[1].lineno
        filePath: str = inspect.stack()[1].filename
        method:str = inspect.stack()[1].function
        fileName:str = os.path.basename(filePath)

        __msg = Message("Debug",message,lineNum,fileName,method)
        self.__LogMessage(__msg)
    
    def __LogMessage(self, msg:Message):
        """
        Hidden method that will check all endpoints to see if they will accept the current message.

        """
        
        if self.Console.isValidEndpoint(msg.Level) == True:
            self.Console.Write(msg)
   
if __name__ == '__main__':
    pysaw