
import json
import os

class Config:
    """
    Config class manages the configuration files for the module.

    Attributes:
        PathConfig : str
            Defines the location of where the configuration file will be adjusted
    
    Methods
        NewConfig(PathConfig: str)
            Generates a new blank configuration file
    """

    def __init__(self, PathConfig: str = ""):
        # On load, start off with basic config
        self.ActiveConfig = self.__baseJson()

        # Confirm we can find the file
        if os.path.exists(PathConfig):

            # Open the file, read it and store in memory
            with open(PathConfig) as jsonFile:
                self.ActiveConfig = json.load(jsonFile)
                
    pass

    def __baseJson(self):
        obj = {
            'PySaw':{ 
                'Core':{ 

                }, 
                'Console':{
                    'Levels': [
                        "Debug",
                        "information"
                    ],
                    "MessageTemplate": "[$$Level$$] $$Message$$"

                }, 
                'Txt':{
                    'Levels': [
                        "Debug",
                        "Information"
                    ],
                    'MessageTemplate': "[$$Level$$] - $$Message$$ - $$File$$ - $$Method$$ - $$Line$$"
                },
                'CSV':{
                    'Levels': [
                        "Debug",
                        "Information"
                    ]
                },
                "Template": '$$Level$$, $$Message$$, $$File$$, $$Method$$, $$Line$$'
            }
        }
        return obj

    def NewConfig(self, PathConfig: str, OverWrite: bool = False):
        """
        About:
        This will generate a base configuration file when requested.

        How to use:
        NewConfig(PathConfig: str, OverWrite:bool)

        Returns:
        void
        """

        baseconfig: str = self.__baseJson()

        PathValid = os.path.exists(PathConfig)

        if PathValid == False:
            with open(PathConfig, 'w') as f:
                json.dump(baseconfig, f, indent=4)
            return

        if PathValid == True and OverWrite == True:
            # Write over the existing file and start is a new
            os.remove(PathConfig)
            with open(PathConfig, 'w') as f:
                json.dump(baseconfig, f, indent=4)

            return

    def ExportActiveConfig(self, PathConfig: str, Replace: bool):
        """
        About:
        This will take the currently active config and export it to a file to load at a later time.

        Parameters:
        PathConfig: String
        Defines where the config file will be placed.

        Replace: Bool
        True  - If a existing file is found, it will be replaced.
        False - If a existing file is found, it will not be replaced and a error will be throw.
        
        Returns: Bool
        """
        if os.path.exists(PathConfig) == True and Replace == True:
            try:
                os.remove(PathConfig)
                pass
            except FileExistsError:
                print(f"Unable to remove {PathConfig} from disk.  Is the file open?")
                pass

            try:
                with open(PathConfig, 'w') as f:
                    json.dump(self.ActiveConfig, f, indent=4)
            except FileExistsError:
                print(f"Tried to export the active config but was unable to lock the file.")            

if __name__ == '__main__':
    Config