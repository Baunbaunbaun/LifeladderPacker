from math import ceil
from lifeladderpacking.Pallet import EPALhalfpallet, EPALpallet

def stringBuildPallet(pallet):
    if len(pallet.pallets) == 2:
        stringPallet = '<h3>Pallet ' + str(pallet.id) + ':</h3>'
        
        if len(pallet.pallets[0].ladders) > len(pallet.pallets[1].ladders):
            longLadderList = pallet.pallets[0].ladders
            shortLadderList = pallet.pallets[1].ladders
        else:
            longLadderList = pallet.pallets[1].ladders
            shortLadderList = pallet.pallets[0].ladders
        index = len(longLadderList)-1


        while index >= len(shortLadderList):
            stringPallet = stringPallet + str(longLadderList[index].length/1000) + ' m.\n'
            index = index-1

        while index >= 0:
            stringPallet = stringPallet + str(longLadderList[index].length/1000) + ' m.  ' + str(shortLadderList[index].length/1000) + ' m.\n'
            index = index-1

        return stringPallet + '==========\nWeight:\t' + str(ceil(pallet.weight/1000)) + ' kg.\nHeight:\t' + str(round(pallet.height/1000,2)) + ' m.\nLightUnits:\t' + str(pallet.lights)
    else:
        stringPallet = 'Half Pallet ' + str(pallet.id) + ':\n\n'
        for ladder in reversed(pallet.ladders): 
            stringPallet = stringPallet + str(ladder.length/1000) + ' m.\n'
        return stringPallet + '=====\nWeight:\t' + str(ceil(pallet.weight/1000)) + ' kg.\nHeight:\t' + str(round(pallet.height/1000,2)) + ' m.\nLightUnits:\t' + str(pallet.lights)
    
def palletsInShipmentAsOneString(myShipment):
    EPALs = str(sum(1 for p in myShipment.packedPallets if type(p)== EPALpallet)) + ' x EUR Pallet'
    EPALhalfs = str(sum(1 for p in myShipment.packedPallets if type(p)== EPALhalfpallet)) + ' x EUR Half Pallet'

    out = 'Number of pallets:\n' + EPALs + '\n' + EPALhalfs + '\n\nTotal weight:\t' + str(ceil(myShipment.totalWeight/1000)) + ' kg.\n\n'
    
    for pallet in myShipment.packedPallets:
        out = out + stringBuildPallet(pallet) + '\n\n'
    return out
        

