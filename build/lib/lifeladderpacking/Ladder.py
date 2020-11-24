# imports
from math import floor
from lifeladderpacking.AppData import *

class Ladder:

    # initialize a ladder
    def __init__(self, length, lights):
        
        self.id = getLadderID() 
        self.lightUnits = lights
        self.length = length
        self.modules =  int(length/moduleLength)
        self.foldHeight = self.calcFoldHeight(length)
        self.brackets = self.calcBrackets(length)   
        self.weight = self.calcWeight(self)
        self.odd = (self.modules%2)==1
        if(self.length==0):
            self.weight = 0
            self.foldHeight = 0
    
    @classmethod
    def create(cls, length, lights):
        if(cls.lengthIsLegal(length)):
            return cls(length, lights)
        else: 
            return cls(0,0)
        
    def __lt__(self, other):
        return (self.foldHeight < other.foldHeight)
    
    @staticmethod
    def lengthIsLegal(length):
        if(length<=0 or 
            length>maxLadderLength or 
            length % moduleLength != 0):
            return False
        else: 
            return True
    
    # calc folded height of ladder
    @staticmethod
    def calcFoldHeight(length):
        nrModules = int(length/moduleLength)
        # first iteration of foldHeight (73mm)
        res1 = addedFoldHeight[0] * floor((nrModules+1)/4)
        # second iteration of foldHeight (103mm)
        res2 = addedFoldHeight[1] * floor((nrModules-1)/4)
        return intitialFoldHeight + res1 + res2

    # calc number of brackets to include
    @staticmethod
    def calcBrackets(length):
        index = 0
        for limit in bracketsIncluded:    
            if(limit>=length):
                return index
            index+=1
        return 0
    
    # calc ladder weight
    @staticmethod
    def calcWeight(ladder):
        print("Modules: ", ladder.modules,
            " LifeLadder only: ", ladder.modules * moduleWeight + fixedSuppliesWeight,
            " With brackets: ", ladder.modules * moduleWeight + fixedSuppliesWeight + ladder.brackets * bracketWeight,
            " Foldheight : ", ladder.foldHeight)
        return (
            ladder.modules * moduleWeight + # modules
            ladder.brackets * bracketWeight + # brackets
            fixedSuppliesWeight + # fixedSupplies
            ladder.lightUnits * lightUnitWeight) # lightUnits
