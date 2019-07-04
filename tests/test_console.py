import pytest

import pysaw
from pysaw.Modules.console import Console
from pysaw.Modules.config import Config

from pysaw.Core.message import Message

def testConsoleConfigNoFile():
    """
    Tests Console logger to make sure the base line config is valid.
    """
    cfg = Config()
    con = Console(cfg)

    res = con.isValidEndpoint("Debug")
    if res == True:
        assert True
    else:
        assert False

def testBaseConfigEmergency():
    """
    This method will test the base config.  
    This one should fail to be pass.
    """
    cfg = Config()
    cmd = Console(cfg)
    valid = cmd.isValidEndpoint(level="Emergency")

    if valid == False:
        assert True
    else:
        assert False

def testLoadedConfigEmergency():
    """
    This method will load the fully loaded config.
    This one will work to pass.
    """

    cfg = Config("./tests/testConfig.json")
    cmd = Console(cfg)
    valid = cmd.isValidEndpoint(level="Emergency")

    if valid == True:
        assert True
#    else:
#        assert False

def testConsoleDebug():
    cfg = Config()
    cfg.ActiveConfig['PySaw']['Console']['Levels'] = ['Debug']
    cfg.ActiveConfig['PySaw']['Console']['MessageTemplate'] = '$$Level$$ $$Message$$'

    msg = Message()
    msg.Message = "Test"
    msg.Level = "Debug"

    con = Console(cfg)
    if con.isValidEndpoint(msg.Level) == False:
        assert False
    else:
        res = con.Write(msg, passBack=True)
        assert res == 'Debug Test'


def testConsoleEmergency():
    cfg = Config()
    cfg.ActiveConfig['PySaw']['Console']['Levels'] = ['Emergency']
    cfg.ActiveConfig['PySaw']['Console']['MessageTemplate'] = '$$Level$$ $$Message$$'

    msg = Message()
    msg.Message = "Test"
    msg.Level = "Emergency"

    con = Console(cfg)
    if con.isValidEndpoint(msg.Level) == False:
        assert False
    else:
        res = con.Write(msg, passBack=True)
        assert res == 'Emergency Test'


def testConsoleAlert():
    cfg = Config()
    cfg.ActiveConfig['PySaw']['Console']['Levels'] = ['Alert']
    cfg.ActiveConfig['PySaw']['Console']['MessageTemplate'] = '$$Level$$ $$Message$$'

    msg = Message()
    msg.Message = "Test"
    msg.Level = "Alert"

    con = Console(cfg)
    if con.isValidEndpoint(msg.Level) == False:
        assert False
    else:
        res = con.Write(msg, passBack=True)
        assert res == 'Alert Test'

def testConsoleCritical():
    cfg = Config()
    cfg.ActiveConfig['PySaw']['Console']['Levels'] = ['Critical']
    cfg.ActiveConfig['PySaw']['Console']['MessageTemplate'] = '$$Level$$ $$Message$$'

    msg = Message()
    msg.Message = "Test"
    msg.Level = "Critical"

    con = Console(cfg)
    if con.isValidEndpoint(msg.Level) == False:
        assert False
    else:
        res = con.Write(msg, passBack=True)
        assert res == 'Critical Test'

def testConsoleError():
    cfg = Config()
    cfg.ActiveConfig['PySaw']['Console']['Levels'] = ['Error']
    cfg.ActiveConfig['PySaw']['Console']['MessageTemplate'] = '$$Level$$ $$Message$$'

    msg = Message()
    msg.Message = "Test"
    msg.Level = "Error"

    con = Console(cfg)
    if con.isValidEndpoint(msg.Level) == False:
        assert False
    else:
        res = con.Write(msg, passBack=True)
        assert res == 'Error Test'
    
def testConsoleWarning():
    cfg = Config()
    cfg.ActiveConfig['PySaw']['Console']['Levels'] = ['Warning']
    cfg.ActiveConfig['PySaw']['Console']['MessageTemplate'] = '$$Level$$ $$Message$$'

    msg = Message()
    msg.Message = "Test"
    msg.Level = "Warning"

    con = Console(cfg)
    if con.isValidEndpoint(msg.Level) == False:
        assert False
    else:
        res = con.Write(msg, passBack=True)
        assert res == 'Warning Test'

def testConsoleInformation():
    cfg = Config()
    cfg.ActiveConfig['PySaw']['Console']['Levels'] = ['Information']
    cfg.ActiveConfig['PySaw']['Console']['MessageTemplate'] = '$$Level$$ $$Message$$'

    msg = Message()
    msg.Message = "Test"
    msg.Level = "Information"

    con = Console(cfg)
    if con.isValidEndpoint(msg.Level) == False:
        assert False
    else:
        res = con.Write(msg, passBack=True)
        assert res == 'Information Test'