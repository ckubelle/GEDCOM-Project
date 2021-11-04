# Leena Domadia
# User Story 19 - First Cousins should not marry
# I pledge my Honor that I have abided by the Stevens Honor System - Leena Domadia

def isFirstCousinsMarry(family, cousins):
    if (family['husb_id'] in cousins) and (family['wife_id'] in cousins):
        return True
    return False

def firstCousinsNotMarry(fam_list):
    error_statements = []
    for fam1 in fam_list:
        children = fam1['children']
        cousins = []
        for child in children:
            for fam2 in fam_list:
                if child == fam2['husb_id'] or child == fam2['wife_id']:
                    cousins.append(child)
                    for fam3 in fam_list:
                        if isFirstCousinsMarry(fam3, cousins):
                            error_statements.append(f"ERROR US19: Husband {fam3['husb_id']} and Wife {fam3['wife_id']} in Family {fam3['id']} are first cousins.")
    return error_statements