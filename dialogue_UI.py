from guietta import _, Gui, Quit, QFileDialog, C, R
from AppData import maxPackingHeight
from Calculations import createListOfLadders
from os import system, name 
import re


def userInterface():


    def input():
        
        """
        def output(ladderHalfPallets):
            guiOutput = Gui(
                            [ladderHalfPallets]
                            )
        """
        
        
        
        global maxPackingHeight 

        guiInput = Gui(
                  [ 'Max packing height:'   , '__maxHeight__'       , 'm'   , _                 , _             , _             ],
                  [ _                       , _                     , _     , _                 , _             , _                     ],
                  [ _                       , 'Length'              , _     , 'LightUnit'       , 'Volume'      , _                     ],
                  [ 'LifeLadder type 1:'    , '__length1__'         , 'm'   , C('lightUnit1')  , '__volumen1__' , 'Pcs.'                 ],
                  [ ['moreLadderTypes']     , _                     , _     , _                 , _             , _                     ],
                  [ ['clear']               , _                     , _     , _                 , _             , ['pack']         ],
                  [ 'Max height is:'        , '__maxHeight__'       , _     , _                 , _             , Quit                  ],
                  [ 'Packing result'        , _                     , _     , _                 , _             , Quit                  ]
                )
        
        subgui = Gui( [C('checkbox'), '__editbox__'] )

        guiInput.widgets['clear'].setText('Clear all input')
        guiInput.widgets['lightUnit1'].setText('')
        guiInput.widgets['pack'].setText('Pack LifeLadders')
        guiInput.maxHeight = maxPackingHeight

        
        #gui.widgets['lightUnit1']

        with guiInput.pack:
            if guiInput.is_running:
                guiInput.Packingresult = 'LADDERS OUTPUT'

        with guiInput.clear:
            guiInput.maxHeight = 1800
            guiInput.length1 = 0
        
        guiInput.run()

        guiOutput.run()

    input()


#inputNewMaxHeightDialogue()

userInterface()
