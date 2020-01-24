# imports
from AppData import maxPackingHeight, palletHeight, wrappingHeight
from Calculations import pairEUR6pallets
from Pallet import EUR6pallet
import binpacking

# Shipment object
class Shipment:

    # initialize a shipment
    def __init__(self, ladderLst):
            
        self.ladders = ladderLst
        self.pallets = []
        self.packOnEUR6pallets()
        self.packedPallets = pairEUR6pallets(self.pallets)
        self.totalWeight = sum(pallet.weight for pallet in self.pallets)
        
    def packOnEUR6pallets(cls):
        foldHeights = list(ladder.foldHeight for ladder in cls.ladders)

        # create dictionary
        #laddersWithHeights = []
        #for index in range(len(foldHeights)):
            #laddersWithHeights.append((str(foldHeights[index]),str(cls.ladders[index].id))) 
            
        laddersHeightsInEUR6pallets = binpacking.to_constant_volume(foldHeights, maxPackingHeight-palletHeight-wrappingHeight)
        # e.g. ladderHeightsInEUR6pallets = [[1370, 138], [1370, 138], [666, 666], [666]]
        print(len(laddersHeightsInEUR6pallets),'HALF PALLETS =',laddersHeightsInEUR6pallets)
        cls.fromHeightsToLadders(laddersHeightsInEUR6pallets, cls.ladders)
            
    def fromHeightsToLadders(cls, heightLst, ladderLst):
        for p in heightLst:
            palletN = EUR6pallet()
            for height in p:
            # foldToLad = Ladder(0,0)
                for ladder in ladderLst:
                    if(ladder.foldHeight == height):
                        # print('LADDER IN PALLETN',ladder.id, height)
                        palletN.addLadder(ladder)
                        ladderLst.pop(ladderLst.index(ladder))
                        break
            cls.pallets.append(palletN)   
        
    def balancePallets(cls):
        cls.pallets = cls.pallets
