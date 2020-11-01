#!/usr/bin/env python
# coding: utf-8

# Code by Christian Baun 
# baunbaun@gmail.com
# Lifeladder packing for PortS
# July 2019 - October 2020

from lifeladderpacking.Calculations import createListOfLadders
from lifeladderpacking.Shipment import Shipment
from lifeladderpacking.AppData import maxPackingHeight

def ladderLogic(lst, maxHeight=maxPackingHeight):
    
    # is lst empty?
    try: 
        assert(lst)
    except: 
        return ValueError

    # from order to ladders
    orderInLadders = createListOfLadders(lst)

    # create shipment 
    myShipment = Shipment(orderInLadders, maxHeight)

    # pair half pallets
    myShipment.pairEPALhalfpallets()

    return myShipment