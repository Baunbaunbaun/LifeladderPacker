#!/usr/bin/env python
# coding: utf-8

# Code by Christian Baun 
# baunbaun@gmail.com
# Lifeladder packing for PortS
# July 2019 - October 2020

from lifeladderpacking.Calculations import createListOfLadders
from lifeladderpacking.Shipment import Shipment

def ladderLogic(lst):
    orderInLadders = createListOfLadders(lst)
    # create shipment 
    myShipment = Shipment(orderInLadders)
    # pair half pallets
    myShipment.pairEPALhalfpallets()
    return myShipment