# User Story #18: Siblings should not marry
# Siblings should not marry one another

def siblingsNotMarried(indi_list, fam_list):
    errorStatements = []
    for fam in fam_list:
        if fam['children'] != 'NA':
            for child in fam['children']:
                for family in fam_list:
                    if (family['husb_id'] == child and family['wife_id'] in fam['children']):
                        errorStatements.append(f"Error US18: {family['husb_name']} ({family['husb_id']}) should not be married to his sibling {family['wife_name']} ({family['wife_id']}) in Family {family['id']}. These two people are siblings in Family {fam['id']}.")
                    if (family['wife_id'] == child and family['husb_id'] in fam['children']):
                        errorStatements.append(f"Error US18: {family['wife_name']} ({family['wife_id']}) should not be married to her sibling {family['husb_name']} ({family['husb_id']}) in Family {family['id']}. These two people are siblings in Family {fam['id']}.")
    errorStatements.sort()
    return errorStatements