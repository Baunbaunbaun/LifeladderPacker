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
# calculations
from Calculations import *
'''
from AppData import maxPackingHeight
from Calculations import createListOfLadders, checkInput, clear
from sys import exit

# printer
from Printer import *
# classes
from Shipment import Shipment

# # APPLICATION # #

# get user input
clear()
print('\n\n********************************')
print('****** LIFELADDER PACKING ******')
print('********************************\n\n')

print('Max packing height is',maxPackingHeight,'mm\nIf you want to set another max height then input now. Else press ENTER')
maxH = input()
if(len(maxH)>1):
    try:
        print('\nNew max height is',int(maxH),'mm\n')
        maxPackingHeight = int(maxH)
    except:
        print('Your input is not a number! EXITING')
        exit()
print('\n********************************\n')
print('Please input all the lifeladders for this shipment.')
userInput = ''
orderInNumbers = []
while(userInput != 'done'):
    userInput = input('The format is "amount_of_ladders, length_in_mm, number_of_lightUnits_0_or_1" e.g. 2, 3600, 1.\n\nWhen you are done write "done"\nInput next ladders:\n')
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

if(len(orderInNumbers)==0):
    print('You have ordered 0 ladders. EXITING')
    exit()
else:
    print('\nThank you!\nYour shipment contains',(sum(order[0] for order in orderInNumbers)),'ladders.\n')

print('\n********************************\n')

orderInLadders = createListOfLadders(orderInNumbers)

printListOfLadders(sorted(orderInLadders))

myShipment = Shipment(orderInLadders)

printShipmentEURpallets(myShipment)




'''
#printShipmentEUR6pallets(myShipment)
print('\n**********************************')
print('* PAIRING pallets on EUR pallets *')
print('**********************************\n')

printShipmentEURpallets(myShipment)

printShipment(myShipment)
'''

