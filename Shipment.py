# imports
from AppData import maxPackingHeight, palletHeight, wrappingHeight
#from Calculations import pairEPALhalfpallets
from Pallet import EPALhalfpallet
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
        return [len(cls.packedPallets)-half,half]
    
    # merge EPALhalfpallets to EPALpallets
    def pairEPALhalfpallets(cls): # e.g. [1600, 1200, 1700, 1700] in mm
        palletLstCopy = cls.palletLst
        heights = list(pallet.height for pallet in cls.palletLst)
        heights = sorted(heights)
        
        resultPallets = []
        
        def calcDifferenceBetweenpallets(palletLst):
            lst = []
            for i in range(len(palletLst)-1):
                lst.append(abs(palletLst[i]-palletLst[i+1]))            
            return lst
        
        while(len(cls.palletLst)>1):
            diffLst = calcDifferenceBetweenpallets(heights)
            index = diffLst.index(min(diffLst))
            resultPallets.append(EPALpallet(palletLst.pop(index), palletLst.pop(index)))
            heights.pop(index)
            heights.pop(index)
        if(len(cls.palletLst)==1):
            resultPallets.append(cls.palletLst.pop())
        cls.packedPalletc = resultPallets 
    
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
