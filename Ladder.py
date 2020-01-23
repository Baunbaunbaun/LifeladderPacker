# imports
from AppData import *
from Calculations import *

class Ladder:

    # initialize a ladder
    def __init__(self, length, lights):
        
        self.id = getLadderID() 
        self.lightUnits = lights
        self.length = length
        self.modules =  int(length/moduleLength)
        self.foldHeight = calcFoldHeight(length)
        self.brackets = calcBrackets(length)   
        self.weight = calcWeight(self)
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
    
    def lengthIsLegal(length):
        if(length<=0 or 
            length>maxLadderLength or 
            length % moduleLength != 0):
            return False
        else: 
            return True
