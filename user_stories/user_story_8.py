# User Story #8: Birth Before Marriage of Parents
from dateutil.relativedelta import relativedelta

def birthBeforeMarriageCheck(birthday, marriage, divorced):
    if marriage == 'NA':
        return True

    if birthday < marriage:
        return True

    if divorced != 'NA' and divorced + relativedelta(months=+9) < birthday:
        return True
    
    return False

def birthBeforeMarriageOfParents(indi_list, fam_list):

    errorStatements = []
    for fam in fam_list:

        for child in fam['children']:

            for indi in indi_list:

                if child == indi['id']:
                    if birthBeforeMarriageCheck(indi['birthday'], fam['married'], fam['divorced']):
                        errorStatements.append(f"Error US08: Birth date of {indi['name']} ({indi['id']}) occurs before family ({fam['id']}) marriage which is ({fam['married']})) ")

    return errorStatements