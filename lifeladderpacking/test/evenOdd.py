from typing import List
import binpacking
from ../AppData import maxPackingHeight
from ../lifeladderApp import ladderLogic
import UI

"""
from  Calculations import createListOfLadders
from  Shipment import Shipment
from  Printer import printListOfLadders
"""

maxHeight = 1500

# (len, foldHeight)
odd300 = (300, 138)
odd2100 = (2100, 387)
odd6300 = (6300, 1018)

even600 = (600, 138)
even1800 = (1800, 314)
even6000 = (6000, 915) 

ladders = [odd300, odd300, odd2100, odd2100, odd6300, odd6300, even600, even600, even1800, even1800, even6000, even6000]

"""
def ladderLogic(lst, maxHeight=maxPackingHeight):
    
    # is lst empty?
    try: 
        assert(lst)
    except: 
        return ValueError

    # from order to ladders
    orderInLadders = createListOfLadders(lst)

    Printer.printListOfLadders(orderInLadders)

    # create shipment 
    myShipment = Shipment(orderInLadders, maxHeight)

    Printer.printShipment(myShipment)

    # pair half pallets
    myShipment.pairEPALhalfpallets()

    return myShipment
"""
ship = ladderLogic([[11,1500,0]])

# ship = Shipment([[5,4200,0]], )
"""
for p in ship.packedPallets:
    if len(p.pallets) == 0:
        Printer.printPallet(p)
"""
print(UI.palletsInShipmentAsOneString(ship))

"""
def evenOddLadders(lst: list):
    even: List[int] = []
    odd: List[int] = []
    for l in lst:
        if (l[0]/300)%2 == 0:
            even.append(l)
        else: 
            odd.append(l)
    return even, odd

def fromLaddersToFoldHeights(lst: list):
    foldHeights = []
    for l in lst: 
        foldHeights.append(l[1])
    return foldHeights

def packOddOnEven(even: list, odd: list):
    oddThatdoesNotFit = []
    for o in odd: 
        oHeight = o[1]
        #print(o)
        index = 99
        bestFit = 10000000
        for i in range(len(even)): 
            eHeight = sum(even[i])
            #print('Max height: ', maxHeight, 'Even height: ', eHeight, ' Odd height: ', oHeight, ' Potential: ', maxHeight-eHeight, ' Fit: ', maxHeight-eHeight-oHeight)
            fit = maxHeight-eHeight-oHeight
            goodFit: bool = fit < bestFit
            fitAtAll: bool = fit > 0
            if goodFit and fitAtAll:
                bestFit = goodFit
                index = i
                #print('Best fit: ', bestFit, ' Pallet ', index, ' add ', o[1])
        try:
            even[index].append(o[1])
        except:
            oddThatdoesNotFit.append(o)
    return even

def pack(ladders: list):
    allPacked = binpacking.to_constant_volume(fromLaddersToFoldHeights(ladders), maxHeight)
    print('ALL: \t\t', allPacked)
    n = len(allPacked)
    even, odd = evenOddLadders(ladders)
    evenPackedOnNpallets = binpacking.to_constant_bin_number(fromLaddersToFoldHeights(even), n)
    print('EVEN: \t\t', evenPackedOnNpallets)
    oddPackedOnEven = packOddOnEven(evenPackedOnNpallets, odd)
    print('EVEN+ODD: \t', oddPackedOnEven)
    m = 0
    for l in oddPackedOnEven: 
        m = m + len(l)
        print(sum(l))
    print(m)

pack(ladders)


"""
