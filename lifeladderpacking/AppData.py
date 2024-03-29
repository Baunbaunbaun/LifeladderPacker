# max ladder length and max packing height in milimeters
maxPackingHeight = 1800 
maxHalfPackingHeight = 1200
maxLadderLength = 9000

# a list of ladders
allLadders = []

# a list of requests - a request is: (amount,length)
requestLadders = []

# list of nr brackets included in a ladder.
# index indicate nr brackets, value indicate max height in millimeters. 
# e.g. ladder with length=3900 is less than 4200, which is index 2.
bracketsIncluded = [0,0,4200,7200,9000] 

# weight table in grams
moduleWeight = 1592
bracketWeight = 6150
fixedSuppliesWeight = 394

repairSetWeight = [4485,5045,5583] # Small, Medium, Large
lightUnitWeight = 2630 # with support
handHoldWeight = [2800,0,6500] # Small, Medium, Large

wrappingWeight = 2500

# pallet data
# weight in grams; length in mm
EPALhalfpalletWeight = 12500    
EPALhalfpalletLength = 600      
EPALpalletLength = 1200
palletWidth = 800
palletHeight = 150

# length and height table in mm
intitialFoldHeight = 138
addedFoldHeight = [73, 103]
moduleLength = 300
wrappingHeight = 50

# indexes
small = 0
medium = 1
large = 2