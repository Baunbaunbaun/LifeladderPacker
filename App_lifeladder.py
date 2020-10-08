#!/usr/bin/env python
# coding: utf-8

# Code by Christian Baun 
# baunbaun@gmail.com
# LifeLadder packing for PortSafety
# July 2019 - September 2020

from sys import exit
from  Calculations import createListOfLadders
from LifeLadderPacking import Printer 
from  Shipment import Shipment
from LifeLadderPacking import UI

# # APPLICATION # #
orderInNumbers = UI.inputDialogue()
orderInLadders = createListOfLadders(orderInNumbers)

# print ordered ladders
Printer.printListOfLadders(sorted(orderInLadders))

# create shipment 
myShipment = Shipment(orderInLadders)
# pair half pallets
myShipment.pairEPALhalfpallets()

# print meta data
Printer.printShipment(myShipment)

Printer.printShipmentEPALhalfpallets(myShipment)

Printer.printShipmentEPALpallets(myShipment)

UI.showOutput(myShipment)
