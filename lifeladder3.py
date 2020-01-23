#!/usr/bin/env python
# coding: utf-8

# Code by Christian Baun
# Lifeladder packing for PortS
# July 2019 - Feb 2020

# pip imports here
from ipywidgets import widgets
from IPython import get_ipython
from IPython.display import display
import math
from functools import reduce
import binpacking
import itertools
import uuid 

# # Data and settings

# max ladder length and max packing height in milimeters
maxPackingHeight = 1800 
maxLadderLength = 9000

# a list of ladders
allLadders = []

# a list of requests - a request is: (amount,length)
requestLadders = []

# list of nr brackets included in a ladder.
# index indicate nr brackets, value indicate max height in millimeters. 
# e.g. ladder with length=3900 is less than 4200, which is index 2.
bracketsIncluded = [0,0,4200,7200,9000] 

# weight table in grams
moduleWeight = 1592
bracketWeight = 6150
fixedSuppliesWeight = 394

repairSetWeight = [4233,4569,4905] # Small, Medium, Large
lightUnitWeight = 2600 # with support
handHoldWeight = [2800,0,6500] # Small, Medium, Large

wrappingWeight = 2500
#EURpalletWeight = 25000
EUR6palletWeight = 12500

# length and height table in mm
intitialFoldHeight = 138
addedFoldHeight = [73, 103]
moduleLength = 300
palletHeight = 150
wrappingHeight = 50

# indexes
small = 0
medium = 1
large = 2

# ladder ID generator
ladderID = 0
def getLadderID():
    global ladderID
    newID = ladderID
    ladderID += 1
    return newID

# pallet ID generator
palletID = 0
def getPalletID():
    global palletID
    newID = palletID
    palletID += 1
    return newID

# Ladder object
class Ladder:

    # initialize a ladder
    def __init__(self, length, lights):
        
        self.id = getLadderID() 
        self.lightUnits = lights
        self.length = length
        self.modules =  int(length/moduleLength)
        self.foldHeight = calcFoldHeight(length)
        self.brackets = calcBrackets(length)   
        self.weight = calcWeight(self)
        if(self.length==0):
            self.weight = 0
            self.foldHeight = 0
        
    @classmethod
    def create(cls, length, lights):
        if(cls.lengthIsLegal(length)):
            return cls(length, lights)
        else: 
            return cls(0,0)
        
    def __lt__(self, other):
        return (self.foldHeight < other.foldHeight)
    
    def lengthIsLegal(length):
        if(length<=0 or 
            length>maxLadderLength or 
            length % moduleLength != 0):
            return False
        else: 
            return True

# pallet parent object
class Pallet: 
    pass

# so called HALF PALLET
class EUR6pallet(Pallet): 

    # initialize a half pallet
    def __init__(self):
        self.id = getPalletID() 
        self.pallets = []
        self.ladders = [] # ladderLst
        self.weight = EUR6palletWeight # sum(ladder.weight for ladder in ladderLst)
        self.height = palletHeight # sum(ladder.foldHeight for ladder in ladderLst)

    def amend(cls, itemLst):
        cls.weight += sum(item.weight for item in itemLst)
        cls.height += sum(item.height for item in itemLst)
    
    def addLadder(cls, ladder):
        cls.ladders.append(ladder)
        cls.weight += ladder.weight
        cls.height += ladder.foldHeight

# twice the size of EUR6pallet
class EURpallet(Pallet): 
    
    def __init__(self, pallet1,pallet2):
        self.id = str(pallet1.id)+'_'+str(pallet2.id)
        self.pallets = [pallet1, pallet2]
        self.ladders = pallet1.ladders + pallet2.ladders
        self.weight = pallet1.weight + pallet2.weight
        self.height = max(pallet1.height,pallet2.height)
    
    # create class method to balance all ladders on the EURpallet
    # So we dont have odd ladders in the bottom  
        
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
        laddersWithHeights = []
        for index in range(len(foldHeights)):
            laddersWithHeights.append((str(foldHeights[index]),str(cls.ladders[index].id))) 
            
        laddersHeightsInEUR6pallets = binpacking.to_constant_volume(foldHeights, maxPackingHeight-palletHeight-wrappingHeight)
        # e.g. ladderHeightsInEUR6pallets = [[1370, 138], [1370, 138], [666, 666], [666]]
        print('HALF PALLETS =',laddersHeightsInEUR6pallets)
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

# Item objects for amendment
class Item:
    
    # initialize an item
    def __init__(self, weight, addedHeightToPallet):
        self.weight = weight
        self.height = addedHeightToPallet
    

# # Calculate

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


# # Print functions


def printLadder(ladder):
    if(ladder.length>0):
        print('\n-- LADDER',ladder.id,'--')
        print('LENGTH:\t\t', ladder.length/1000, 'M')
        print('MODULES:\t', ladder.modules)
        print('WEIGTH:\t\t', ladder.weight/1000, 'KG')
        print('FOLD HEIGHT:\t', ladder.foldHeight/1000, 'M')
        print('BRACKETS:\t', ladder.brackets)
        print('LIGHTUNITS:\t', ladder.lightUnits,'\n')
    else: 
        print('Illegal ladder\n')

def printListOfLadders(lst):
    #print('\n----',len(lst),'LADDERS ----n')
    for l in lst: 
        printLadder(l)

def printShipment(shipment):
    print('\n== SHIPMENT ==n')
    print('LADDERS:\t\t', len(shipment.ladders))
    print('PALLETS (ALL):\t\t:',shipment.pallets)
    print('PALLETS (EUR):\t\t', sum(1 for p in shipment.pallets if type(p)== EURpallet))
    print('PALLETS (EUR6):\t\t', sum(1 for p in shipment.pallets if type(p)== EUR6pallet))
    print('TOTAL WEIGHT:\t\t', shipment.totalWeight/1000,'KG\n')

def printShipmentEUR6pallets(shipment):
    for pallet in shipment.pallets:
        printPallet(pallet)

def printShipmentEURpallets(shipment):
    for pallet in shipment.packedPallets:
        printPallet(pallet)
    
def printPallet(pallet):
    print('\n^^ PALLET',pallet.id,'^^')
    print('WEIGTH:\t\t', pallet.weight/1000, 'KG')
    print('HEIGHT:\t\t', pallet.height/1000, 'M\n')
    if(len(pallet.pallets)==2):
        for p in pallet.pallets:
            printPallet(p)
    else:
        printListOfLadders(pallet.ladders)
    
def printList(lst):
    for item in lst:
        print(item)
        
 
# # Test area


# empty list
allLadders = []

# A) Add some ladders to an order
orderLadders = [(5,3000,1) ,(5,900,0),(6,600,0), (2, 8400,0) ,(1,1500,0),(1,8100,0),(5,5100,0)]

# B) create ladders and add them to the list 'allLadders'
addListOfLadders(orderLadders)

moreLadders = input('Want to add more ladders?')

# C) print the list of ladders
printListOfLadders(allLadders)
# printListOfLadders(sorted(allLadders))

# D) gather data of shipment
myShipment = Shipment(allLadders)

#printShipmentEUR6pallets(myShipment)

print('PAIRING pallets ====>>>\n')

printShipmentEURpallets(myShipment)


#x = pairEUR6pallets(myShipment.pallets)

#for p in x:
 #   printPallet(p)

# E) print shipment data
#printShipment(myShipment)


'''
printPacking(myShipment)


printPacking(myShipment)

# F) pack shipment on pallets
#packShipment(myShipment)

'''

