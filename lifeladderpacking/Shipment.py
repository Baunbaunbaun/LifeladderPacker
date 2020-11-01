# imports
from  lifeladderpacking.AppData import maxPackingHeight, palletHeight, wrappingHeight
#from Calculations import pairEPALhalfpallets
from  lifeladderpacking.Pallet import EPALhalfpallet, EPALpallet
import binpacking

# Shipment object
class Shipment:

    # initialize a shipment
    def __init__(self, ladderLst, maxHeight = maxPackingHeight):
        
        try:
            assert(ladderLst)
        except: 
            raise ValueError

        self.ladders = ladderLst
        self.maxHeight = maxHeight
        self.pallets = []
        self.packOnEPALhalfpallets()
        self.packedPallets = []
        self.totalWeight = sum(pallet.weight for pallet in self.pallets)
        #self.maxHeightForOneLessPallet = None
        #self.maxHeightForBestStability = None
        #self.packedStabil = []
    
    def packOnEPALhalfpallets(self):
        foldHeights = list(ladder.foldHeight for ladder in self.ladders)
        # use binpacking library
        laddersHeightsInEPALhalfpallets = binpacking.to_constant_volume(foldHeights, self.maxHeight-palletHeight-wrappingHeight)
        self.fromHeightsToLadders(laddersHeightsInEPALhalfpallets, self.ladders)
    
    def fromHeightsToLadders(self, heightLst, ladderLst):
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
            self.pallets.append(palletN)   

    #def balancePallets(self):
     #   pallets = pallets
    
    def getEPALdistribution(self):
        half = len(pallets)%2
        return [len(packedPallets)-half, half]
    
    # merge EPALhalfpallets to EPALpallets
    def pairEPALhalfpallets(self):
        palletsCopy = self.pallets
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
        self.packedPallets = resultPallets 
    
    @staticmethod
    def calcNewPackingWithBestEvenOddDistribution(self):
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
