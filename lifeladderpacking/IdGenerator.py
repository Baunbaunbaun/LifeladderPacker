def resetIDs():
    global ladderID
    ladderID = 1
    
    global palletID
    palletID = 1

    global EPALpalletID
    EPALpalletID = 1

# ladder ID generator
ladderID = 1
def getLadderID():
    global ladderID
    newID = ladderID
    ladderID += 1
    return newID

# pallet ID generator for half pallets
palletID = 1
def getPalletID():
    global palletID
    newID = palletID
    palletID += 1
    return newID

# pallet ID generators for EPAL pallets
EPALpalletID = 1
def getEPALpalletID():
    global EPALpalletID
    newID = EPALpalletID
    EPALpalletID += 1
    return newID