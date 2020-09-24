#!/usr/bin/env python
# coding: utf-8

# Code by Christian Baun 
# baunbaun@gmail.com
# Lifeladder packing for PortS
# July 2019 - September 2020

from Calculations import createListOfLadders
from sys import exit
from Printer import *
from Shipment import Shipment
import dialogue
from guietta import Gui, _

# # APPLICATION # #
orderInNumbers = dialogue.run()
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

gui = Gui(
            ['ladderStr0', 'ladderStr1', 'ladderStr2'],
            ['ladderStr3', 'ladderStr4', 'ladderStr5']
         )   

#gui.widgets[1]  = stringBuildPallet(myShipment.packedPallets[0])
#gui.ladderStr2  = stringBuildPallet(myShipment.packedPallets[1])
#gui.ladderStr3  = stringBuildPallet(myShipment.packedPallets[2])

index = len(myShipment.packedPallets)-1
while index >= 0:
    strIndex = 'ladderStr' + str(index)
    print(type(gui.widgets[strIndex]))
    gui.widgets[strIndex].setText(stringBuildPallet(myShipment.packedPallets[index]))
    index = index - 1

gui.run()

