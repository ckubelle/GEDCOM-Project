# User Story 11 - Marriage should not occur 
# during marriage to another spouse

# return error statements if bigamy exists
def isBigamy(indi_list, fam_list):
    for fam in fam_list:
        
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
