import pytest

#import pysaw
from pysaw.Modules.config import Config

def testInitNoFile():
    # Generate a Config without a file...
    cfg = Config()

    if cfg.ActiveConfig != "":
        assert True
    else:
        assert False

    #assert cfg.ActiveConfig

#if __name__ == "__main__":
 #   Test_Init_NoFile
  #  pass