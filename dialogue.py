from AppData import maxPackingHeight
from os import system, name 
import re


def run():


    def inputNewMaxHeightDialogue():
        print('\n************ new max height? *************\n')    
        global maxPackingHeight
        while(True):
            print('Max packing height is',maxPackingHeight,'mm\nIf you want to set another max height then input now. Else press ENTER')
            maxH = input('>')
            if(len(maxH)==0):
                break
            elif(not maxH.isdigit()):
                print('\nERROR - Your input is not a number.\n')
            elif(not (1000 <= int(maxH) <= 3000)):
                print('\nERROR - Your input is too high or low. Valid heights are 1000-3000\n')
            else:
                print('\nNew max height is',int(maxH),'mm\n')
                maxPackingHeight = int(maxH)
                break
         
    def inputLaddersDialogue():
        print('\n************ input ladders *************\n')    
        print('Please input all the lifeladders for this shipment.')
        userInput = ''
        orderInNumbers = []
        print('The format is "amount_of_ladders, length_in_mm, number_of_lightUnits_0_or_1" e.g. 2, 3600, 1.\n\n· If you want to delete the last order write "delete" or "D"\n· If you want to restart write "restart" or "R"\n· When you are done write "done" or press ENTER\n\nInput next ladders:\n')
        while(userInput != 'done'):
            userInput = input('>')
            
            if(userInput in ['done','']):
                break
            elif(userInput in ['delete','D']):
                del(orderInNumbers[-1])
                print('\nPresent order list:\t\t',orderInNumbers,'\n')
                continue
            elif(userInput in ['restart','R']):                
                return run()
            else: 
                ladderOrder = checkAndCastInput(userInput)
            
            if(ladderOrder == None):
                print('\nTry to input those ladders again\n')
                continue
            
            orderInNumbers.append(ladderOrder)
            print('\nPresent order list:\t\t',orderInNumbers,'\n')

        if(len(orderInNumbers)==0):
            print('\nYou have ordered 0 ladders. EXITING')
            exit()
        else:
            print('\nThank you!\nYour shipment contains',(sum(order[0] for order in orderInNumbers)),'ladders.\n')

        return orderInNumbers

    # clear screen 
    def clear(): 
        
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear')

    # check users ladder input
    def checkAndCastInput(inputStr):
        inputAsList = re.split(',',inputStr)
        if(len(inputAsList) != 3):
            print('Error - Exactly 3 numbers are needed.\n')
            return None
        numberTuple = [0,0,0]
        try:
            for index in range(3):
                numberTuple[index] = int(inputAsList[index])
            if(numberTuple[2] not in (0,1)):
                print('ERROR - Number of lightUnits is not 0 or 1. Try again.')
                return None
            return numberTuple
        except:
            print('Error - Not all inputs are numbers.\n')
            return None
    
    clear()

    print('\n\n********************************')
    print('****** LIFELADDER PACKING ******')
    print('********************************\n')

    inputNewMaxHeightDialogue()
    output = inputLaddersDialogue()
    return output
