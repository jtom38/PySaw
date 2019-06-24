import pytest

import pysaw
from pysaw.Modules.console import Console
from pysaw.Modules.config import Config

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
    else:
        assert False

def testConsole():
    # Generate a basic Config class
    cfg = Config()

    # Pass the config class into console so it knows about the active config
    cmd = Console(cfg)

    # Generate a message
    msg = cmd.Write("Test", "test", True)
    
    # Test the message
    assert msg == "[Test] test"
