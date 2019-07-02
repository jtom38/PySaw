
from pysaw.pysaw import pysaw

logger = pysaw(".//demo.json")
#cfg = "demo.json"

#logger.ExportActiveConfig(".\\Export.json", True)
#logger.Emergency("Emergency msg")
#logger.Alert("Alert msg")
logger.Debug("This is a debug msg.")