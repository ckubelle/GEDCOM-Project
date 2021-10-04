

def divorcedBeforeMarried(divorced, married):
    if divorced == 'NA':
        return False

    if divorced < married:
        return True

    return False

    



def marrBeforeDivorce(fam_list):

    errorStatements = []
    for fam in fam_list:

        if divorcedBeforeMarried(fam['divorced'], fam['married']):
            errorStatements.append(f"Error US04: Marriage Date of {fam['id']} occurs after divorce.")
    
    return errorStatements
