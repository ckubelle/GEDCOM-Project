# User Story #8: Birth Before Marriage of Parents

def birthBeforeMarriageOfParents(indi_list, fam_list):

    errorStatements = []
    for fam in fam_list:

        for child in fam['children']:

            for indi in indi_list:

                if child == indi['id']:
                    if fam['married'] == 'NA' or indi['birthday'] < fam['married']:
                        errorStatements.append(f"Error US08: Birth date of {indi['name']} ({indi['id']}) occurs before family ({fam['id']}) marriage which is ({fam['married']})) ")

    return errorStatements