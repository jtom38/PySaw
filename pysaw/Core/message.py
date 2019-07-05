
class Message():
    """
    About:
    Message class contains all the information that can be passed to endpoints.

    Parameters:
    Level:str
    Message:str
    Line:int
    File:str
    Method:str
    """

    def __init__(self, Level:str, Message:str, Line:int, File:str, Method:str = ''):

        self.Level = Level
        self.Message = Message
        self.LineNumber = Line
        self.FileName = File

        if Method.__eq__("<module>") == False:
            self.MethodName = Method
        else:
            self.MethodName = ''
        pass
    
