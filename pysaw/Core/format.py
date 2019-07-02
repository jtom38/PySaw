
from ..Modules.config import Config

class FormatMessage:
    """
    About:
    FormatMessage is the class that works to convet the common message flags into real messages.

    Properties:
    Stores the information from the config file.
    Config: Config

    Methods:

    """
    def __init__(self, Config: Config):
        self.Config = Config
        pass

    # Properties
    Config: Config

    # Methods
    def ConvertToString(self, level:str, message:str):
        """
        About: ConvertToString takes in all the args passed and will work to match the values to the template
        """
        pass

if __name__ == "__main__":
    FormatMessage