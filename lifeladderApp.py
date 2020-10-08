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
import UI

# # APPLICATION # #
#orderInNumbers = UI.inputDialogue()
#orderInNumbers = Dialogue.run()

def ladderLogic(lst):
    orderInLadders = createListOfLadders(lst)

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

    UI.showOutput(myShipment)

#ladderLogic()
