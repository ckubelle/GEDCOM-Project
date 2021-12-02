# User Story 27
# Include person's current age when listing individuals

# return error statements if individual is missing current age
def isIncludeAge(indi_list):
    errorStatements = []
    for ind in indi_list:
        if checkIncludeAge(indi_list, ind):
            errorStatements.append("Error US27: Individual %s does not have a current age" % (ind["id"]))
    return errorStatements

# return true if given individual's age is included
def checkIncludeAge(indi_list, fam_list, indi):
    for ind in indi_list:
        if ind['id'] == indi['id']:
            # if ind has no birthday, return false
            if ind['birthday'] == "NA":
                return False
            # else, if ind still has no age, return false
            elif ind['age'] == "NA":
                return False
    return True
