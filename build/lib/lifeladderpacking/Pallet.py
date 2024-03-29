# imports
from AppData import *
from IdGenerator import getPalletID, getEPALpalletID

# pallet parent object
class Pallet: 
    pass

# so called HALF PALLET
class EPALhalfpallet(Pallet): 

    # initialize a half pallet
    def __init__(self):
        self.id = getPalletID() 
        self.pallets = []
        self.ladders = [] # ladderLst
        self.weight = EPALhalfpalletWeight # sum(ladder.weight for ladder in ladderLst)
        self.height = palletHeight # sum(ladder.foldHeight for ladder in ladderLst)
        self.lights = 0

    def amend(self, itemLst):
        self.weight += sum(item.weight for item in itemLst)
        self.height += sum(item.height for item in itemLst)
    
    def addLadder(self, ladder):
        self.ladders.append(ladder)
        self.weight += ladder.weight
        self.height += ladder.foldHeight
        self.lights += ladder.lightUnits
    
    def __lt__(self, other):
        return (self.height < self.height)
    
    @staticmethod
    def getDimensions(pallet):
        width = str(round(palletWidth/1000,1)) 
        length = str(round(EPALhalfpalletLength/1000,1))
        height = str(round(pallet.height/1000,1))
        return f'{width} X {length} X {height}'

# twice the size of EPALhalfpallet
class EPALpallet(Pallet): 
    
    def __init__(self, pallet1,pallet2):
        self.id = getEPALpalletID()
        self.pallets = [pallet1, pallet2]
        self.ladders = pallet1.ladders + pallet2.ladders
        self.weight = pallet1.weight + pallet2.weight
        self.height = max(pallet1.height,pallet2.height)
        self.lights = pallet1.lights + pallet2.lights
    
    @staticmethod
    def getDimensions(pallet):
        width = palletWidth/1000
        length = EPALpalletLength/1000
        height = pallet.height/1000
        return str(round(width,1)) + ' X ' + str(round(length,1)) + ' X ' + str(round(height,1))
    
    # create class method to balance all ladders on the EPALpallet
    # So we dont have odd ladders in the bottom  

