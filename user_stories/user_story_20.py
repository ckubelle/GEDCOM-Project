# User Story 20 - Aunts and uncles should 
# not marry their nieces or nephews

# return error statements if marriage is between an aunt/uncle and neice/nephew
def isAuntUnc(indi_list, fam_list):
    errorStatements = []
    for fam in fam_list:
        if checkAuntUnc(indi_list, fam_list, fam):
            errorStatements.append("Error US20: Spouse in Family %s is married to their neice or nephew." % (fam["id"]))
    return errorStatements

# return True if given fam contains marriage between aunt/uncle and neice/nephew
def checkAuntUnc(indi_list, fam_list, fam):
    if fam['married'] == 'NA':
        return False
    husb_id = fam['husb_id']
    wife_id = fam['wife_id']
    husb_ext = getAuntUnc(indi_list, fam_list, husb_id)
    wife_ext = getAuntUnc(indi_list, fam_list, wife_id)
    for unc in husb_ext:
        if unc == wife_id:
            return True
    for unc in wife_ext:
        if unc == husb_id:
            return True
    return False

# return given ind's aunts and uncles
def getAuntUnc(indi_list, fam_list, indi_id):
    auntsUncs = set()
    given_fam = ''
    mom_id = ''
    dad_id = ''
    mom_fam = ''
    dad_fam = ''
    # find given ind's family
    for ind in indi_list:
        if ind['id'] == indi_id:
            for fam in ind['child']:
                given_fam = fam
    # find given ind's parents
    for fam in fam_list:
        if fam["id"] == given_fam:
            dad_id = fam['husb_id']
            mom_id = fam['wife_id']
    # find parents' families
    for ind in indi_list:
        if ind['id'] == dad_id:
            for fam in ind['child']:
                dad_fam = fam
        elif ind['id'] == mom_id:
            for fam in ind['child']:
                mom_fam = fam
    # find parents siblings
    for fam in fam_list:
        if fam['id'] == dad_fam:
            for child in fam['children']:
                if child != dad_id:
                    auntsUncs.add(child)
        elif fam['id'] == mom_fam:
            for child in fam['children']:
                if child != mom_id:
                    auntsUncs.add(child)
    return auntsUncs
