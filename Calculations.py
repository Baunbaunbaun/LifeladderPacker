# imports
from AppData import *
# classes
from Ladder import Ladder
from Pallet import *
from Shipment import *

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

def createListOfLadders(order):
    ladderLst = []
    for request in order: 
        ladderLst.append(createLadders(request[0],request[1],request[2]))
    return ladderLst
    
def createLadders(amount, length, lights): 
    ladderLst = []
    for l in range(amount):
        x = Ladder.create(length,lights) 
        ladderLst.append(x) 
    return ladderLst
