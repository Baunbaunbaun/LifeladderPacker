#!/usr/bin/env python
# coding: utf-8

# Code by Christian Baun 
# baunbaun@gmail.com
# Lifeladder packing for PortS
# July 2019 - Feb 2020
'''
# pip imports
from ipywidgets import widgets
from IPython import get_ipython
from IPython.display import display
import math
#from functools import reduce
import itertools
import uuid 

# data
from AppData import *
# calculations
from Calculations import *
'''
from Calculations import createListOfLadders, checkInput, clear

# printer
from Printer import *
# classes
from Shipment import Shipment

# # APPLICATION # #

# get user input
clear()
print('Please input all the lifeladders for this shipment.')
userInput = ''
orderInNumbers = []
while(userInput != 'done'):
    userInput = input('The format is "amount_of_ladders, length_in_mm, number_of_lightUnits" e.g. 2, 3600, 1.\n\nWhen you are done write "done"\nInput next ladders:\n')
    if(userInput == 'done'):
        break
    if(userInput == 'delete'):
        del(orderInNumbers[-1])
        print('\nPresent order list:\t\t',orderInNumbers,'\n')
        continue
    ladderOrder = checkInput(userInput)
    if(ladderOrder == None):
        print('\nTry to input those ladders again\n')
        continue
    orderInNumbers.append(ladderOrder)
    print('\nPresent order list:\t\t',orderInNumbers,'\n')

print('\nThank you!\nYour shipment contains',(sum(order[0] for order in orderInNumbers)),'ladders.\n')

orderInLadders = createListOfLadders(orderInNumbers)

printListOfLadders(sorted(orderInLadders))

myShipment = Shipment(orderInLadders)

printShipmentEUR6pallets(myShipment)

print('\nPAIRING pallets ====>>>\n')

printShipmentEURpallets(myShipment)

printShipment(myShipment)