# User Story 27
# Include person's current age when listing individuals
from datetime import date, datetime
from dateutil import relativedelta


# return error statements if individual is missing current age
def isIncludeAge(indi_list):
    errorStatements = []
    for ind in indi_list:
        if checkIncludeAge(indi_list, ind):
            errorStatements.append("Error US27: Individual %s does not have their current age" % (ind["id"]))
    return errorStatements

def checkIncludeAge(indi):
    if indi['birthday'] == "NA" or indi['age'] == "NA":
        return False
    else:
        # check if age is current or correct
        today = date.today()
        diff = relativedelta.relativedelta(today, indi['birthday']).years
        if (diff != indi['age']):
            return False
        else:
            return True
