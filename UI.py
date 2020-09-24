from guietta import Gui, _

def showOutput(myShipment):
    gui = Gui(
                ['ladderStr0', 'ladderStr1', 'ladderStr2'],
                ['ladderStr3', 'ladderStr4', 'ladderStr5'],
                ['ladderStr6', 'ladderStr7', 'ladderStr8']
            )   

    index = len(myShipment.packedPallets)-1
    while index >= 0:
        strIndex = 'ladderStr' + str(index)
        print(type(gui.widgets[strIndex]))
        gui.widgets[strIndex].setText(stringBuildPallet(myShipment.packedPallets[index]))
        index = index - 1

    gui.run()

def stringBuildPallet(pallet):
    if len(pallet.pallets) == 2:
        stringPallet = 'Pallet ' + str(pallet.id) + ':\n\n'
        
        if len(pallet.pallets[0].ladders) > len(pallet.pallets[1].ladders):
            longLadderList = pallet.pallets[0].ladders
            shortLadderList = pallet.pallets[1].ladders
        else:
            longLadderList = pallet.pallets[1].ladders
            shortLadderList = pallet.pallets[0].ladders
        index = len(longLadderList)-1


        while index >= len(shortLadderList):
            stringPallet = stringPallet + str(longLadderList[index].length/1000) + ' m\n'
            index = index-1

        while index >= 0:
            stringPallet = stringPallet + str(longLadderList[index].length/1000) + ' m  ' + str(shortLadderList[index].length/1000) + ' m\n'
            index = index-1

        return stringPallet + '=========='
    else:
        stringPallet = 'Half Pallet ' + str(pallet.id) + ':\n\n'
        for ladder in reversed(pallet.ladders): 
            stringPallet = stringPallet + str(ladder.length/1000) + ' m' + '\n'
        return stringPallet + '====='