# Leena Domadia - Use Story 3
# Birth before death
# I pledge my Honor that I have abided by the Stevens Honor System - Leena Domadia

def isBirthBeforeDeath(bdate, ddate):
    if ddate == "NA":
        return True
    elif bdate < ddate:
        return True
    return False

def birthBeforeDeath(indi_list):
    errorStatements = []
    for indi in indi_list:
        if not isBirthBeforeDeath(indi['birthday'], indi['death']):
            errorStatements.append(f"Error US03: Birth date of {indi['name']} ({indi['id']}) occurs after his/her death date")

    return errorStatements