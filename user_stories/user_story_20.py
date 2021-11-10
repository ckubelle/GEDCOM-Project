# User Story 20 - Aunts and uncles should 
# not marry their nieces or nephews

# return error statements if marriage is between an aunt/uncle and neice/nephew
def isAuntOrUnc(indi_list, fam_list):
    errorStatements = []
    for fam in fam_list:
        if checkAuntorUnc(indi_list, fam_list, fam):
            errorStatements.append("Error US20: Spouse in Family %s is married to their neice or nephew." % (fam["id"]))
    return errorStatements

# return true if the given family marriage is between an aunt/uncle and neice/nephew
def checkAuntorUnc(indi_list, fam_list, fam):
    husbId = fam["husb_id"]
    wifeId = fam["wife_id"]
    # if a spouse's neice or nephew ID matches their spouse's ID, return true
    for neice in getNeiceNeph(indi_list, fam_list, husbId):
        if neice[id] == wifeId:
            return True
    for nephew in getNeiceNeph(indi_list, fam_list, wifeId):
        if nephew[id] == husbId:
            return True
    return False


# return given indi's neices and nephews
def getNeiceNeph(indi_list, fam_list, indi):
    neph = set()
    for ind in indi_list:
        # find given indi
        if ind["id"] == indi:
            family = ind["child"]
            # find indi's family
            for fam in fam_list:
                if fam["id"] == family:
                    for sibling in fam["children"]:
                        # find all siblings except given indi
                        if sibling["id"] != ind["id"]:
                            # append sibling's children to neph
                            for child in sibling["children"]:
                                neph.append(child)
    return neph
