# imports
from  AppData import maxPackingHeight, palletHeight, wrappingHeight
#from Calculations import pairEPALhalfpallets
from  Pallet import EPALhalfpallet, EPALpallet
import binpacking

# Shipment object
class Shipment:

    # initialize a shipment
    def __init__(self, ladderLst):
            
        self.ladders = ladderLst
        self.pallets = []
        self.packOnEPALhalfpallets()
        self.packedPallets = []
        self.totalWeight = sum(pallet.weight for pallet in self.pallets)
        #self.maxHeightForOneLessPallet = None
        #self.maxHeightForBestStability = None
        #self.packedStabil = []
        
    def packOnEPALhalfpallets(cls):
        foldHeights = list(ladder.foldHeight for ladder in cls.ladders)
        # use binpacking library
        laddersHeightsInEPALhalfpallets = binpacking.to_constant_volume(foldHeights, maxPackingHeight-palletHeight-wrappingHeight)
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
        half = len(cls.pallets)%2
        return [len(cls.packedPallets)-half, half]
    
    # merge EPALhalfpallets to EPALpallets
    def pairEPALhalfpallets(cls):
        palletsCopy = cls.pallets
        heights = list(pallet.height for pallet in palletsCopy)
        heights = sorted(heights)
        palletsCopy = sorted(palletsCopy)
        resultPallets = []
        
        def calcDifferenceBetweenpallets(pallets):
            lst = []
            for i in range(len(pallets)-1):
                lst.append(abs(pallets[i]-pallets[i+1]))            
            return lst
        
        while(len(palletsCopy)>1):
            diffLst = calcDifferenceBetweenpallets(heights)
            index = diffLst.index(min(diffLst))
            resultPallets.append(EPALpallet(palletsCopy.pop(index), palletsCopy.pop(index)))
            heights.pop(index)
            heights.pop(index)
        if(len(palletsCopy)==1):
            resultPallets.append(palletsCopy.pop())
        cls.packedPallets = resultPallets 
    
    def calcNewPackingWithBestEvenOddDistribution(cls):
        '''
        use ladderLst and len(pallets) to create a new improved packing. 
        where ODD ladders are distributed evenly on all pallets.
        this improves stabling stability.

        use a stability index. 
        GOOD = <= 1 odd ladder on the pallet
        BAD = > 1 odd

        IF you cannot avoid more than 1 odd on a pallet, then make the max height smaller. 


        if(oddLadders>numberPallets):

        
        '''
        pass
