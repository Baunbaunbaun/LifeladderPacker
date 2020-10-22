#!/usr/bin/env python
# coding: utf-8

# Code by Christian Baun 
# baunbaun@gmail.com
# Lifeladder packing for PortS
# July 2019 - October 2020

from lifeladderpacking.Calculations import createListOfLadders
from lifeladderpacking.Shipment import Shipment
#from Printer import *

def ladderLogic(lst):
    orderInLadders = createListOfLadders(lst)

    # print ordered ladders
    #printListOfLadders(sorted(orderInLadders))

    # create shipment 
    myShipment = Shipment(orderInLadders)
    # pair half pallets
    myShipment.pairEPALhalfpallets()

    # print meta data
    #printShipment(myShipment)

    #printShipmentEPALhalfpallets(myShipment)

    #printShipmentEPALpallets(myShipment)

    return myShipment