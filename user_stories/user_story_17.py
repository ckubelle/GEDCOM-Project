# User Story #17: No marriage to descendants
# Parents should not marry any of their descendants

def getDescendants(indi_id, fam_list, currDesc):
    for fam in fam_list:
        if (fam['husb_id'] == indi_id or fam['wife_id'] == indi_id) and fam['children'] != 'NA':
            for child in fam['children']:
                currDesc.add(child)
                currDesc.update(getDescendants(child, fam_list, currDesc))
    return currDesc

def parentsMarriedToDescendants(fam_list):
    errorStatements = []
    for fam in fam_list:
        # Check if wife is a descendant of husband
        husb_descendants = getDescendants(fam['husb_id'], fam_list, set())
        if fam['wife_id'] in husb_descendants:
            errorStatements.append(f"Error US17: {fam['husb_name']} ({fam['husb_id']}) is married to his descendant {fam['wife_name']} ({fam['wife_id']}) in Family {fam['id']}.")
        # Check if husband is a descendant of wife
        wife_descendants = getDescendants(fam['wife_id'], fam_list, set())
        if fam['husb_id'] in wife_descendants:
            errorStatements.append(f"Error US17: {fam['wife_name']} ({fam['wife_id']}) is married to her descendant {fam['husb_name']} ({fam['husb_id']}) in Family {fam['id']}.") 
    return errorStatements