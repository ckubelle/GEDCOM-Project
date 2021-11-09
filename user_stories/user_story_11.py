# User Story 11 - Marriage should not occur 
# during marriage to another spouse

from datetime import date, datetime

# return error statements if bigamy exists
def isBigamy(indi_list, fam_list):
    errorStatements = []
    for fam in fam_list:
        if checkBigamy(indi_list, fam_list, fam):
            errorStatements.append("Error US11: Marriage in Family %s occurred during marriage to another spouse." % (fam["id"]))
    return errorStatements

# return true if bigamy exists in given family
def checkBigamy(indi_list, fam_list, fam):
    # check if they are married
    if fam["married"] == "NA":
        return False
    else:
        # get marriage start date
        currentMarr = fam["married"]
        # check if spouses are in other marriages
        for fam2 in fam_list:
            if fam2 != fam:
                if fam2["husb_id"] == fam["husb_id"] or fam2["wife_id"] == fam["wife_id"]:
                    # if start of current marriage occured before end of other, return true
                    if (currentMarr < getEndMarr(indi_list, fam2)):
                        return True
                    else:
                        return False 
                    
# return end of marriage date or date(3000, 1, 1) if none
def getEndMarr(indi_list, fam):
    # if no divorce, endOfMarr is whichever spouse died first, or date(3000, 1, 1) for default
    if fam["divorced"] == "NA":
        husbDeath = date(3000, 1, 1)
        wifeDeath = date(3000, 1, 1)
        # check if husb or wife are dead
        for ind in indi_list:
            if ind["id"] == fam["husb_id"]:
                if ind["death"] != "NA":
                    husbDeath = ind["death"]
            elif ind["id"] == fam["wife_id"]:
                if ind["death"] != "NA":
                    wifeDeath = ind["death"]
        # least recent date = smaller value. End of Marr is whichever spouse died first
        endOfMarr = min(husbDeath, wifeDeath)
    # if divorced, endOfMarr is just divorce date
    else:
        endOfMarr = fam["divorced"]
    return endOfMarr
