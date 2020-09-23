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

