# classes
from Pallet import EUR6pallet, EURpallet
from Calculations import dimensionsFormatter

def printLadder(ladder):
    if(ladder.length>0):
        print('\n** LADDER',ladder.id,'**\n')
        print('LENGTH:\t\t', ladder.length/1000, 'M')
        print('MODULES:\t', ladder.modules)
        print('WEIGHT:\t\t', ladder.weight/1000, 'KG')
        print('FOLD HEIGHT:\t', ladder.foldHeight/1000, 'M')
        print('BRACKETS:\t', ladder.brackets)
        print('LIGHTUNITS:\t', ladder.lightUnits,'\n')
    else: 
        print('Illegal ladder\n')

def printListOfLadders(lst):
    print('\n**********************************')
    print('************ LADDERS *************')
    print('**********************************\n')
    for l in lst: 
        printLadder(l)

def printShipment(shipment):
    print('\n== SHIPMENT ==')
    # print('LADDERS:\t\t', len(shipment.ladders))
    print('PALLETS (ALL):\t\t:',shipment.pallets)
    print('PALLETS (EUR):\t\t', sum(1 for p in shipment.pallets if type(p)== EURpallet))
    print('PALLETS (EUR6):\t\t', sum(1 for p in shipment.pallets if type(p)== EUR6pallet))
    print('TOTAL WEIGHT:\t\t', round(shipment.totalWeight/1000),'KG\n')

def printShipmentEUR6pallets(shipment):
    for pallet in shipment.pallets:
        printPallet(pallet)

def printShipmentEURpallets(shipment):
    print('\n**********************************')
    print('*********** SHIPMENT *************')
    print('**********************************\n')
    print('\n', len(shipment.packedPallets),'pcs. pallets\n')
    for pallet in shipment.packedPallets:
        printPallet(pallet)
    print('\nTotal weight:', round(sum(pallet.weight for pallet in shipment.packedPallets)/1000,1) ,'KG\n')
    
def printPallet(pallet):
    print('\n== PALLET',pallet.id,'==')
    print('DIMENSIONS:\t', dimensionsFormatter(pallet), 'M   (W x L x H)')
    print('WEIGHT:\t\t', round(pallet.weight/1000), 'KG')
    #if(len(pallet.pallets)==2):
      #  for p in pallet.pallets:
            # printPallet(p)
    # else:
        # printListOfLadders(pallet.ladders)
    
def printList(lst):
    for item in lst:
        print(item)
        
