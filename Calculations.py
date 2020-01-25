# imports
from AppData import *
from os import system, name 
import re

# classes
from Ladder import Ladder
from Pallet import *

# merge EPALhalfpallets to EPALpallets
def pairEPALhalfpallets(palletLst): # e.g. [1600, 1200, 1700, 1700] in mm
    heights = list(pallet.height for pallet in palletLst)
    heights = sorted(heights)
    
    resultPallets = []
    
    def calcDifferenceBetweenpallets(palletLst):
        lst = []
        for i in range(len(palletLst)-1):
            lst.append(abs(palletLst[i]-palletLst[i+1]))            
        return lst
    
    while(len(palletLst)>1):
        diffLst = calcDifferenceBetweenpallets(heights)
        index = diffLst.index(min(diffLst))
        resultPallets.append(EPALpallet(palletLst.pop(index), palletLst.pop(index)))
        heights.pop(index)
        heights.pop(index)
    if(len(palletLst)==1):
        resultPallets.append(palletLst.pop())
    return resultPallets 

def createListOfLadders(order):
    ladderLst = []
    for request in order: 
        ladderLst = ladderLst + createLadders(request[0],request[1],request[2])
    return ladderLst
    
def createLadders(amount, length, lights): 
    ladderLst = []
    for l in range(amount):
        x = Ladder.create(length,lights) 
        ladderLst.append(x) 
    return ladderLst

# check user input
def checkInput(inputStr):
    inputAsList = re.split(',',inputStr)
    if(len(inputAsList) != 3):
        print('Error - Exactly 3 arguments are needed.\n')
        return None
    numberTuple = [0,0,0]
    try:
        for index in range(3):
            numberTuple[index] = int(inputAsList[index])
        if(numberTuple[2] not in (0,1)):
            print('Number of lightUnits is not 0 or 1. Try again.')
            return None
        return numberTuple
    except:
        print('Error - Not all inputs are numbers.\n')
        return None

# clear screen 
def clear(): 
    
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def dimensionsFormatter(pallet):
    if (type(pallet)== EPALhalfpallet):
        dim = [palletWidth/1000, EPALhalfpalletLength/1000, pallet.height/1000] 
    else: 
        dim = [palletWidth/1000, EPALpalletLength/1000, pallet.height/1000] 
    return str(round(dim[0],1))+' X '+str(round(dim[1],1))+' X '+str(round(dim[2],1))
    
