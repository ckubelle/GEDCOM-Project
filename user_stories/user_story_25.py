#User Story 25

def uniqueNameAndBirthInFam(indi_list, fam_list):

    errorStatements = []

    for fam in fam_list:
        dictOfNames = dict()

        for child in fam['children']:

            for indi in indi_list:

                if indi['id'] == child:
                    if indi['name'] in dictOfNames and dictOfNames[indi['name']] == indi['birthday']:
                        errorStatements.append(f"Error US25: Individual {indi['name']} appears more than once in the same family")
                    else:
                        dictOfNames[indi['name']] = indi['birthday']



    return errorStatements