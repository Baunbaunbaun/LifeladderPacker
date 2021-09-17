# content of test_sample.py
from Ladder import Ladder
from math import ceil
from lifeladderpacking import Printer
from lifeladderApp import ladderLogic
import csv
from pathlib import Path
from lifeladderpacking import AppData
import numpy

def test_LadderInitAgainstCsv_Max20gOr20mmError():
    path = Path(__file__).parent / "test/LifeLadderTest.csv"
    with path.open() as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'{" –– ".join(row)}')
                line_count += 1
            else:
                testLadder = initLadderModulesWeightFoldHeight(line_count*300)
                validLadder = (int(row[0]),int(row[1]),int(int(row[2])/10))
                #print(testLadder,' vs ', (int(row[0]),int(row[1]),int(int(row[2])/10)), ' RESULT = ', numpy.subtract(testLadder,validLadder), sum(list(numpy.subtract(testLadder,validLadder))) )
                assert sum(list(numpy.subtract(testLadder,validLadder))) > -20 
                line_count += 1
        #print(f'Processed {line_count} lines.')

def initLadderModulesWeightFoldHeight(length):
    l = Ladder(length,0)
    return l.modules * AppData.moduleWeight + AppData.fixedSuppliesWeight, l.weight, l.foldHeight
    #w = amount * l.weight / 1000
    #h = amount * l.foldHeight / 1000
    #Printer.printLadder(l)

def lifeLadderPacker_tester(order:list, pallets:int, height:int, totalWeight:int):
    orderLst = []
    orderLst.append(order)
    testShipment = ladderLogic(orderLst)

    try:
        assert len(testShipment.packedPallets) == pallets
    except: 
        raise AssertionError('PALLET TEST: ', len(testShipment.packedPallets), ' VS ', pallets)

    maxHeight = 0
    for p in testShipment.packedPallets: 
        maxHeight = max(p.height, maxHeight)
    try: 
        maxHeight = maxHeight/10 # from mm to cm
        assert maxHeight == height
    except: 
        raise AssertionError('HEIGHT TEST: ', maxHeight, ' VS ', height)
       
    try: 
        assert ceil(testShipment.totalWeight/1000) == totalWeight
    except: 
        raise AssertionError('WEIGHT TEST: ', ceil(testShipment.totalWeight/1000), ' VS ', totalWeight) 
    
# orders
buckeye = ([4,3900,1], 1, 153, 196) # [amount, length, lights], true num of pallets, true max height, true total weight

if __name__ == "__main__":
    test_LadderInitAgainstCsv_Max20gOr20mmError()
