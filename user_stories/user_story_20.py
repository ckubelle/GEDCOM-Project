# User Story 20 - Aunts and uncles should 
# not marry their nieces or nephews


# return error statements if marriage is between an aunt/uncle and neice/nephew
def isAuntOrUnc(indi_list, fam_list):
    errorStatements = []
    for fam in fam_list:
        if checkAuntorUnc(indi_list, fam):
            errorStatements.append("Error US20: Spouse in Family %s is married to their neice or nephew." % (fam["id"]))
    return errorStatements
