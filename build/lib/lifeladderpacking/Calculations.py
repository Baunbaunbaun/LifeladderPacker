# imports
from  lifeladderpacking.AppData import *
from  lifeladderpacking.Ladder import Ladder
from  lifeladderpacking.Pallet import *

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

def dimensionsFormatter(pallet):
    if (type(pallet)== EPALhalfpallet):
        dim = [palletWidth/1000, EPALhalfpalletLength/1000, pallet.height/1000] 
    else: 
        dim = [palletWidth/1000, EPALpalletLength/1000, pallet.height/1000] 
    return str(round(dim[0],1))+' X '+str(round(dim[1],1))+' X '+str(round(dim[2],1))