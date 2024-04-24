# import user defined methods
from src.smallModel import testSystem
from src.distributionOptimalPowerFlow import opf

opfFlag = False

if __name__ == "__main__":  

  if opfFlag == False:
    testSystem.smallModel()

  else: 
    opf.distributionNetwork(self=None)