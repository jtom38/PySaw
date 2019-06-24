
from pysaw.pysaw import pysaw

logger = pysaw(".//demo.json")
#cfg = "demo.json"

#logger.ExportActiveConfig(".\\Export.json", True)
logger.Debug("This is a debug msg.")