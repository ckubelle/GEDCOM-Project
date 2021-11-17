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

def correspondingEntries(indi_list, fam_list):
    error_statements = []
    # traversing indi_list for correctness
    for indi in indi_list:
        if indi['child'] != 'NA':
            for fam_id in indi['child']:
                for fam in fam_list:
                    if not isCorrespondingChild(indi['id'], fam_id, fam['id'], fam['children']):
                        error_statements.append(f"Error US26: In the Individuals table, {indi['name']} ({indi['id']}) is listed as a child in {fam_id}, but isn't listed as a child in {fam['id']} in the Family table")
        if indi['spouse'] != 'NA':
            for fam_id in indi['spouse']:
                for fam in fam_list:
                    if not isCorrespondingSpouse(indi['id'], fam_id, fam['id'], fam['husb_id'], fam['wife_id']):
                        error_statements.append(f"Error US26: In the Individuals table, {indi['name']} ({indi['id']}) is listed as a spouse in {fam_id}, but isn't listed as a spouse in {fam['id']} in the Family table")
    # traversing fam_list for correctness
    # for fam in fam_list:
    #     if fam['children'] != 'NA':
    #         for indi_id in fam['children']:
    #             for indi in indi_list:
    #                 if not isCorrespondingChild(indi['id'], )
