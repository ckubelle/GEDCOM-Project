# User Story 27
# Include person's current age when listing individuals
from datetime import date, datetime
from dateutil import relativedelta


# return error statements if individual is missing current age
def isIncludeAge(indi_list):
    errorStatements = []
    for ind in indi_list:
        if not checkIncludeAge(ind):
            errorStatements.append("Error US27: Individual %s does not have their current age listed" % (ind["id"]))
    return errorStatements

# return false if ind is missing current age 
def checkIncludeAge(indi):
    if indi['birthday'] == "NA" or indi['age'] == "NA":
        return False
    else:
        # check if age is current or correct
        today = date.today()
        if indi["death"] == "NA":
            diff = relativedelta.relativedelta(today, indi['birthday']).years
        else:
            diff = relativedelta.relativedelta(indi['death'], indi['birthday']).years
        if (diff != indi['age']):
            return False
        else:
            return True
