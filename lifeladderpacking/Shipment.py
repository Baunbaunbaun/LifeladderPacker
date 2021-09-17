# imports
from IdGenerator import resetIDs
from Pallet import EPALhalfpallet, EPALpallet
from AppData import *
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

    def packOnEPALhalfpallets(self, extraHalfPallet = 0):
        resetIDs()
        foldHeights = list(ladder.foldHeight for ladder in self.ladders)
        # use binpacking library to pack on min num of pallets
        ladderHeightsInEPALhalfpallets = binpacking.to_constant_volume(foldHeights, self.maxHeight-palletHeight-wrappingHeight)
        # use binpacking library to even out the ladders on min num of pallets
        ladderHeightsInEPALhalfpallets = binpacking.to_constant_bin_number(foldHeights, len(ladderHeightsInEPALhalfpallets)+extraHalfPallet)
        self.__fromHeightsToLadders(ladderHeightsInEPALhalfpallets, self.ladders)
    
    def __fromHeightsToLadders(self, heightLst, ladderLst):
        laddersCopy = ladderLst.copy()
        pallets = []
        for p in heightLst:
            palletN = EPALhalfpallet()
            for height in p:
                for ladder in laddersCopy:
                    if(ladder.foldHeight == height):
                        palletN.addLadder(ladder)
                        laddersCopy.pop(laddersCopy.index(ladder))
                        break
            pallets.append(palletN)
        self.pallets = pallets           
        self.packedPallets = self.pairEPALhalfpallets()

    # merge EPALhalfpallets to EPALpallets
    def pairEPALhalfpallets(self):
        palletsCopy = self.pallets.copy()
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

        # odd pallets
        if len(self.pallets)%2 == 1:
            for p in self.pallets:
                if (type(p) == EPALhalfpallet) and (p.height > maxHalfPackingHeight):
                    self.packOnEPALhalfpallets(1)

        self.packedPallets = resultPallets 
    
    def getEPALdistribution(self):
        half = len(self.pallets)%2
        return [len(self.packedPallets)-half, half]
    
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
