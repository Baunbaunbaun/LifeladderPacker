# imports
from AppData import maxPackingHeight, palletHeight, wrappingHeight
from Calculations import pairEPALhalfpallets
from Pallet import EPALhalfpallet
import binpacking

# Shipment object
class Shipment:

    # initialize a shipment
    def __init__(self, ladderLst):
            
        self.ladders = ladderLst
        self.pallets = []
        self.packOnEPALhalfpallets()
        self.packedPallets = pairEPALhalfpallets(self.pallets)
        self.totalWeight = sum(pallet.weight for pallet in self.pallets)
        
    def packOnEPALhalfpallets(cls):
        foldHeights = list(ladder.foldHeight for ladder in cls.ladders)

        # create dictionary
        #laddersWithHeights = []
        #for index in range(len(foldHeights)):
            #laddersWithHeights.append((str(foldHeights[index]),str(cls.ladders[index].id))) 
            
        laddersHeightsInEPALhalfpallets = binpacking.to_constant_volume(foldHeights, maxPackingHeight-palletHeight-wrappingHeight)
        # e.g. ladderHeightsInEPALhalfpallets = [[1370, 138], [1370, 138], [666, 666], [666]]
        print(len(laddersHeightsInEPALhalfpallets),'HALF PALLETS =',laddersHeightsInEPALhalfpallets)
        cls.fromHeightsToLadders(laddersHeightsInEPALhalfpallets, cls.ladders)
            
    def fromHeightsToLadders(cls, heightLst, ladderLst):
        for p in heightLst:
            palletN = EPALhalfpallet()
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

    def getEPALdistribution(cls):
        half = 0
        for pallet in cls.packedPallets:
            if(type(pallet)==EPALhalfpallet):
                half = 1
                break
        return [len(cls.packedPallets),half]
