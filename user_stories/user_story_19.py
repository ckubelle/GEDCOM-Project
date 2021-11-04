# Leena Domadia
# User Story 19 - First Cousins should not marry
# I pledge my Honor that I have abided by the Stevens Honor System - Leena Domadia

def isFirstCousinsMarry(family, sib1, sib2):
    if (family['husb_id'] in sib1) and (family['wife_id'] in sib2):
        return True
    elif (family['husb_id'] in sib2) and (family['wife_id'] in sib1):
        return True
    return False

def firstCousinsNotMarry(fam_list):
    error_statements = []
    for fam1 in fam_list:
        children = fam1['children']
        if len(children) > 1 and children != 'NA':
            for child1 in children:
                for child2 in children:
                    if child1 != child2:
                        for fam2 in fam_list:
                            if fam2['husb_id'] == child1 or fam2['wife_id'] == child1:
                                sibling1 = fam2['children']
                                for fam3 in fam_list:
                                    if (fam2 != fam3) and (fam3['husb_id'] == child2 or fam3['wife_id'] == child2):
                                        sibling2 = fam3['children']
                                        print(f'Sibling 1: {sibling1}')
                                        print(f'Sibling 2: {sibling2}')
                                        for fam4 in fam_list:
                                            if isFirstCousinsMarry(fam4, sibling1, sibling2):
                                                error_statements.append(f"Error US19: {fam4['husb_name']} ({fam4['husb_id']}) and {fam4['wife_name']} ({fam4['wife_id']}) in Family {fam4['id']} are first cousins.")
    return error_statements