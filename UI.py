from guietta import Gui, _, HSeparator, C, R, ___, III, QMessageBox, Quit
from AppData import maxPackingHeight

def showOutput(myShipment):
    gui = Gui(
                ['ladderStr0', 'ladderStr1', 'ladderStr2'],
                ['ladderStr3', 'ladderStr4', 'ladderStr5'],
                ['ladderStr6', 'ladderStr7', 'ladderStr8']
            )   

    index = len(myShipment.packedPallets)-1
    while index >= 0:
        strIndex = 'ladderStr' + str(index)
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

def inputDialogue():
        
    global maxPackingHeight 

    guiInput = Gui(
        [ 'Max packing height:'   , '__maxHeight__'       , 'm'   , _                 , _             , _               , _    ],
        [ _                       , _                     , _     , _                 , _             , _               , _    ],
        [ _                       , 'Length'              , _     , 'Add LightUnit'   , _             , 'Volume'        , _    ],
        [ 'LifeLadder type 1:'    , '__length1__'         , 'm'   , C('addLightUnit1'), _             , '__volumen1__' , 'Pcs.'],
        [ _                       , _                     , _     , _                 , _             , _               , _    ],
        [ 'light1'                , _                     , _     , _                 , _             , Quit            , _    ]
                )
        
    guiInput.widgets['Quit'].setText('Output packing')
    guiInput.widgets['addLightUnit1'].setText('')
    guiInput.widgets['light1'].setText('')
    guiInput.light = 0
    #guiInput.widgets['pack'].setText('Pack LifeLadders')
    guiInput.maxHeight = maxPackingHeight
    
    with guiInput.addLightUnit1:
        if guiInput.is_running:
            guiInput.light1 = 1

    """
    with guiInput.pack:
        if guiInput.is_running:
            guiPallets = Gui(   ['Volumen:'    , guiInput.volumen1], 
                                ['Length:'     , guiInput.length1],
                                ['LightUnit:'  , guiInput.light1],
                                ['Max packing height:',guiInput.maxHeight] 
                            )

            guiPallets.run()
    """

    guiInput.run()

    ladderOrder1 = [int(guiInput.volumen1), int(float(guiInput.length1)*1000), int(guiInput.light1)]
    orderInNumbers = [ladderOrder1]    
    
    return orderInNumbers


