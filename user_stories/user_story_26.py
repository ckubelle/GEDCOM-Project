# Leena Domadia
# User Story 26 - Corresponding Entries
# I pledge my Honor that I have abided by the Stevens Honor System - Leena Domadia

def isCorrespondingChild(indi_indi_id, indi_fam_id, fam_fam_id, fam_children):
    if indi_fam_id == fam_fam_id:
        if indi_indi_id in fam_children:
            return True
        else:
            return False
    # if id's are not the same, ignore
    return True

def isCorrespondingSpouse(indi_indi_id, indi_fam_id, fam_fam_id, fam_husb_id, fam_wife_id):
    if indi_fam_id == fam_fam_id:
        if indi_indi_id == fam_husb_id or indi_indi_id == fam_wife_id:
            return True
        else:
            return False
    # if id's are not the same, ignore
    return True

def isChildInFamChildren(indi_id, fam_children):
    if indi_id in fam_children:
        return True
    else:
        return False

def isFamInIndiChild(fam_id, indi_child):
    if fam_id in indi_child:
        return True
    else:
        return False

def isSpouseInFam(indi_id, husb_id, wife_id):
    if indi_id == husb_id or indi_id == wife_id:
        return True
    else:
        return False

def isFamInIndiSpouse(fam_id, indi_spouse):
    if fam_id in indi_spouse:
        return True
    else:
        return False

def correspondingEntries(indi_list, fam_list):
    error_statements = []
    # # traversing indi_list for correctness
    # for indi in indi_list:
    #     if indi['child'] != 'NA':
    #         for fam_id in indi['child']:
    #             for fam in fam_list:
    #                 if not isCorrespondingChild(indi['id'], fam_id, fam['id'], fam['children']):
    #                     error_statements.append(f"Error US26: In the Individuals table, {indi['name']} ({indi['id']}) is listed as a child in {fam_id}, but isn't listed as a child in {fam['id']} in the Family table")
    #     if indi['spouse'] != 'NA':
    #         for fam_id in indi['spouse']:
    #             for fam in fam_list:
    #                 if not isCorrespondingSpouse(indi['id'], fam_id, fam['id'], fam['husb_id'], fam['wife_id']):
    #                     error_statements.append(f"Error US26: In the Individuals table, {indi['name']} ({indi['id']}) is listed as a spouse in {fam_id}, but isn't listed as a spouse in {fam['id']} in the Family table")
    # # traversing fam_list for correctness
    # for fam in fam_list:
    #     if fam['children'] != 'NA':
    #         for indi_id in fam['children']:
    #             for indi in indi_list:
    #                 if indi['child'] != 'NA':
    #                     for fam_id in indi['child']:
    #                         if not isCorrespondingChild(indi['id'], )
    # return error_statements

    for indi in indi_list:
        for fam in fam_list:
            indi_id = indi['id']
            indi_child_fam_id = indi['child']
            indi_spouse_fam_id = indi['spouse']
            fam_id = fam['id']
            fam_husb_indi_id = fam['husb_id']
            fam_wife_indi_id = fam['wife_id']
            fam_children_id = fam['children']
            # CHECK CHILDREN
            # check if indi_id is in fam_children (indi -> fam)
            if fam_id in indi_child_fam_id:
                if not isChildInFamChildren(indi_id, fam_children_id):
                    error_statements.append(f"Error US26: In the Individuals table, {indi['name']} ({indi['id']}) is listed as a child in {fam_id}, but isn't listed as a child in {fam['id']} in the Family table")
            # check if indi in fam_children is in indi table (fam -> indi)
            if indi_id in fam_children_id:
                if not isFamInIndiChild(fam_id, indi_child_fam_id):
                    error_statements.append(f"Error US26: In the Family table, {indi['name']} ({indi['id']}) is listed as a child in {fam_id}, but isn't listed as a child in {fam['id']} in the Individuals table")
            # CHECK SPOUSES
            # check if indi_id is in fam husb_id or wife_id (indi -> fam)
            if fam_id in indi_spouse_fam_id:
                if not isSpouseInFam(indi_id, fam_husb_indi_id, fam_wife_indi_id):
                    error_statements.append(f"Error US26: In the Individuals table, {indi['name']} ({indi['id']}) is listed as a spouse in {fam_id}, but isn't listed as a spouse in {fam['id']} in the Family table")
            # check if indi in husb_id or wife_id is in indi table (fam -> indi)
            if indi_id == fam_wife_indi_id or indi_id == fam_husb_indi_id:
                if not isFamInIndiSpouse(fam_id, indi_spouse_fam_id):
                    error_statements.append(f"Error US26: In the Family table, {indi['name']} ({indi['id']}) is listed as a spouse in {fam_id}, but isn't listed as a spouse in {fam['id']} in the Individuals table")
    return error_statements