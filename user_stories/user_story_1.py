# Leena Domadia - Homework 4
# User Story 1 - Dates Before Current Date
# I pledge my Honor that I have abided by the Stevens Honor System - Leena Domadia

from datetime import date;

def isValidDate(givenDate):
    currentDate = date.today()
    if currentDate < givenDate:
        return False
    else:
        return True

def validDate(indi_list, fam_list):
    error_statements = []
    # check dates in individuals
    for indi in indi_list:
        if not isValidDate(indi['birthday']):
            error_statements.append(f"Error US01: Birthday {indi['birthday']} of {indi['name']} ({indi['id']}) occurs in the future")
        if indi['death'] != "NA" and not isValidDate(indi['death']):
            error_statements.append(f"Error US01: Death {indi['death']} of {indi['name']} ({indi['id']}) occurs in the future")

    # check dates in families
    for fam in fam_list:
        if fam['married'] != "NA" and not isValidDate(fam['married']):
            error_statements.append(f"Error US01: Marriage {fam['married']} of {fam['id']} occurs in the future")
        if fam['divorced'] != "NA" and not isValidDate(fam['divorced']):
            error_statements.append(f"Error US01: Divorce {fam['divorced']} of {fam['id']} occurs in the future")

    return error_statements