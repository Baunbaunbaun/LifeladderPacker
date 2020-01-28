# imports
from AppData import *
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

    def amend(cls, itemLst):
        cls.weight += sum(item.weight for item in itemLst)
        cls.height += sum(item.height for item in itemLst)
    
    def addLadder(cls, ladder):
        cls.ladders.append(ladder)
        cls.weight += ladder.weight
        cls.height += ladder.foldHeight

# twice the size of EPALhalfpallet
class EPALpallet(Pallet): 
    
    def __init__(self, pallet1,pallet2):
        self.id = getEPALpalletID()
        self.pallets = [pallet1, pallet2]
        self.ladders = pallet1.ladders + pallet2.ladders
        self.weight = pallet1.weight + pallet2.weight
        self.height = max(pallet1.height,pallet2.height)
    
    # create class method to balance all ladders on the EPALpallet
    # So we dont have odd ladders in the bottom  

