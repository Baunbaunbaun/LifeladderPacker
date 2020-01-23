# classes
from Ladder import *
from Pallet import *
from Shipment import *
# data
from AppData import *
# calculations
from Calculations import *

def printLadder(ladder):
    if(ladder.length>0):
        print('\n-- LADDER',ladder.id,'--')
        print('LENGTH:\t\t', ladder.length/1000, 'M')
        print('MODULES:\t', ladder.modules)
        print('WEIGTH:\t\t', ladder.weight/1000, 'KG')
        print('FOLD HEIGHT:\t', ladder.foldHeight/1000, 'M')
        print('BRACKETS:\t', ladder.brackets)
        print('LIGHTUNITS:\t', ladder.lightUnits,'\n')
    else: 
        print('Illegal ladder\n')

def printListOfLadders(lst):
    #print('\n----',len(lst),'LADDERS ----n')
    for l in lst: 
        printLadder(l)

def printShipment(shipment):
    print('\n== SHIPMENT ==n')
    print('LADDERS:\t\t', len(shipment.ladders))
    print('PALLETS (ALL):\t\t:',shipment.pallets)
    print('PALLETS (EUR):\t\t', sum(1 for p in shipment.pallets if type(p)== EURpallet))
    print('PALLETS (EUR6):\t\t', sum(1 for p in shipment.pallets if type(p)== EUR6pallet))
    print('TOTAL WEIGHT:\t\t', shipment.totalWeight/1000,'KG\n')

def printShipmentEUR6pallets(shipment):
    for pallet in shipment.pallets:
        printPallet(pallet)

def printShipmentEURpallets(shipment):
    for pallet in shipment.packedPallets:
        printPallet(pallet)
    
def printPallet(pallet):
    print('\n^^ PALLET',pallet.id,'^^')
    print('WEIGTH:\t\t', pallet.weight/1000, 'KG')
    print('HEIGHT:\t\t', pallet.height/1000, 'M\n')
    if(len(pallet.pallets)==2):
        for p in pallet.pallets:
            printPallet(p)
    else:
        printListOfLadders(pallet.ladders)
    
def printList(lst):
    for item in lst:
        print(item)
        