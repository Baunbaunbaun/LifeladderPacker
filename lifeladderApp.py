#!/usr/bin/env python
# coding: utf-8

# Code by Christian Baun 
# baunbaun@gmail.com
# Lifeladder packing for PortS
# July 2019 - Feb 2020

from Calculations import createListOfLadders
from sys import exit
from Printer import *
from Shipment import Shipment
import dialogue

# # APPLICATION # #

# clear screen
dialogue.clear()

print('\n\n********************************')
print('****** LIFELADDER PACKING ******')
print('********************************\n')

# ask for new height
dialogue.inputNewMaxHeightDialogue()
    
# ask for ladders
orderInNumbers = dialogue.inputLaddersDialogue()
orderInLadders = createListOfLadders(orderInNumbers)

# print ordered ladders
printListOfLadders(sorted(orderInLadders))

# create shipment 
myShipment = Shipment(orderInLadders)
# pair half pallets
myShipment.pairEPALhalfpallets()

printShipment(myShipment)

printShipmentEPALhalfpallets(myShipment)

printShipmentEPALpallets(myShipment)

