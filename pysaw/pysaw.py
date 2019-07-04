import typing
import os
import inspect
import sys

from .Modules.config import Config
from .Modules.console import Console
from .Core.message import Message
#from txt import Txt

class pysaw:
    """
    PySaw is the gateway class to your logging needs

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

        configExists = os.path.exists(PathConfig)

        if PathConfig != "" and configExists == True:
            # Generate a new instace of our Config with the path we have been given
            self.__config = Config(PathConfig=PathConfig)
        else:
            self.__config = Config(PathConfig="")

        # Now that we have the config in memory, pass the config class to the Console EndPoint so it knows about its config. 
        self.__console = Console(self.__config)
        
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
        method = inspect.stack()[1].function

        fileName = os.path.basename(filePath)

        msg = Message()
        msg.Level = "Debug"
        msg.Message = message
        msg.FileName = fileName
        msg.LineNumber = lineNum
        msg.MethodName = method

        self.__LogMessage(msg)

    
    def __LogMessage(self, msg:Message):
        """
        Hidden method that will check all endpoints to see if they will accept the current message.

        """
        if self.__console.isValidEndpoint(msg.Level) == True:
            self.__console.Write(msg)
    
if __name__ == '__main__':
    pysaw