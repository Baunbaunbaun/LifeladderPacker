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
import Dialogue
from UI import showOutput

# # APPLICATION # #
orderInNumbers = Dialogue.run()
orderInLadders = createListOfLadders(orderInNumbers)

# print ordered ladders
printListOfLadders(sorted(orderInLadders))

# create shipment 
myShipment = Shipment(orderInLadders)
# pair half pallets
myShipment.pairEPALhalfpallets()

# print meta data
printShipment(myShipment)

printShipmentEPALhalfpallets(myShipment)

printShipmentEPALpallets(myShipment)

showOutput(myShipment)
