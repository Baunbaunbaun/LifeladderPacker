# classes
from Pallet import EPALhalfpallet, EPALpallet
from Calculations import dimensionsFormatter
from math import ceil

def printLadder(ladder):
    if(ladder.length>0):
        if(ladder.odd): 
            oddEven = 'ODD'
        else:
            oddEven = 'EVEN'
        print('\n**',oddEven,'LADDER',ladder.id,'**\n')
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
    print('\n== PRELIMINARY SHIPMENT DETAILS ==')
    # print('LADDERS:\t\t', len(shipment.ladders))
    print('PALLETS (EPAL):\t\t', sum(1 for p in shipment.pallets if type(p)== EPALpallet))
    print('PALLETS (EPALhalf):\t', sum(1 for p in shipment.pallets if type(p)== EPALhalfpallet))
    print('TOTAL WEIGHT:\t\t', round(shipment.totalWeight/1000),'KG\n')

def printShipmentEPALhalfpallets(shipment):
    for pallet in shipment.pallets:
        printPallet(pallet)

def printShipmentEPALpallets(shipment):
    print('\n**********************************')
    print('*********** SHIPMENT *************')
    print('**********************************\n')  
    distributionOfPallets = shipment.getEPALdistribution()
    print(distributionOfPallets[0],'pcs. EPAL Pallet')
    if(distributionOfPallets[1]==1):
        print(distributionOfPallets[1],'pcs. EPAL Half Pallet')
    print('\nDimensions and weight per pallet:')
    for pallet in shipment.packedPallets:
        printPallet(pallet)
    print('\nTotal weight:', ceil(sum(pallet.weight for pallet in shipment.packedPallets)/1000) ,'KG\n')
    
def printPallet(pallet):
    if type(pallet)== EPALhalfpallet:
        palletType = 'EPAL HALF PALLET'
    else: 
        palletType = 'EPAL PALLET'
    print('==',palletType,pallet.id,'==')
    print('DIMENSIONS:\t', dimensionsFormatter(pallet), 'M   (W x L x H)')
    print('WEIGHT:\t\t', round(pallet.weight/1000), 'KG\n')
    
def printList(lst):
    for item in lst:
        print(item)

def printTheLastHalfPallet(shipment):
    count = 0
    for pallet in reversed(shipment.packedPallets):
        print(count)
        count = count+1
        if type(pallet) == EPALhalfpallet:
            print('This is the single half pallet in shipment:')
            printPallet(pallet)
            break
    print('No halfpallets in this shipment')


        
