# imports
from AppData import *
# classes
from Ladder import *
from Pallet import *
from Shipment import *

# calc ladder weight
def calcWeight(ladder):
    return (
        ladder.modules * moduleWeight + # modules
        ladder.brackets * bracketWeight + # brackets
        fixedSuppliesWeight + # fixedSupplies
        ladder.lightUnits * lightUnitWeight) # lightUnits

# calc number of brackets to include
def calcBrackets(length):
    index = 0
    for limit in bracketsIncluded:    
        if(limit>=length):
            return index
        index+=1
    return 0

# calc folded height of ladder
def calcFoldHeight(length):
    nrModules = int(length/moduleLength)
    # first iteration of foldHeight (73mm)
    res1 = addedFoldHeight[0] * math.floor((nrModules+1)/4)
    # second iteration of foldHeight (103mm)
    res2 = addedFoldHeight[1] * math.floor((nrModules-1)/4)
    return intitialFoldHeight + res1 + res2

# merge EUR6pallets to EURpallets
def pairEUR6pallets(palletLst): # e.g. [1600, 1200, 1700, 1700] in mm
    heights = list(pallet.height for pallet in palletLst)
    heights = sorted(heights)
    
    resultPallets = []
    
    def calcDifferenceBetweenpallets(palletLst):
        lst = []
        for i in range(len(palletLst)-1):
            lst.append(abs(palletLst[i]-palletLst[i+1]))            
        return lst
    
    while(len(palletLst)>1):
        diffLst = calcDifferenceBetweenpallets(heights)
        index = diffLst.index(min(diffLst))
        resultPallets.append(EURpallet(palletLst.pop(index), palletLst.pop(index)))
        heights.pop(index)
        heights.pop(index)
    if(len(palletLst)==1):
        resultPallets.append(palletLst.pop())
    return resultPallets 

def addListOfLadders(requestList):
    for request in requestList: 
        addLadders(request[0],request[1],request[2])
    
def addLadders(amount, length, lights): 
    for l in range(amount): 
        allLadders.append(Ladder.create(length,lights)) 
