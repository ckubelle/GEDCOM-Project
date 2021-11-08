

def uniqueNameAndBirth(indi_list):

    errorStatements = []
    dictOfNames = dict()
    
    for indi in indi_list:
        if indi['name'] in dictOfNames and dictOfNames[indi['name']] == indi['birthday']:
            errorStatements.append(f"Error US23: Individual {indi['name']} appears more than once in the GEDCOM file")
        else:
            dictOfNames[indi['name']] = indi['birthday']

    return errorStatements