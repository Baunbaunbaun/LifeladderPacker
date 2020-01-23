#!/usr/bin/env python
# coding: utf-8

# Code by Christian Baun 
# baunbaun@gmail.com
# Lifeladder packing for PortS
# July 2019 - Feb 2020

# pip imports
from ipywidgets import widgets
from IPython import get_ipython
from IPython.display import display
import math
from functools import reduce
import binpacking
import itertools
import uuid 
# classes
from Ladder import *
from Pallet import *
from Shipment import *
# data
from AppData import *
# calculations
from Calculations import *

# Item objects for amendment
class Item:
    
    # initialize an item
    def __init__(self, weight, addedHeightToPallet):
        self.weight = weight
        self.height = addedHeightToPallet

# # APPLICATION # #

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

