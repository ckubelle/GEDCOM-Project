# Leena Domadia
# User Story 13 - Sibiling Spacing
# I pledge my Honor that I have abided by the Stevens Honor System

from datetime import datetime
from dateutil.relativedelta import relativedelta

def isCorrectSibilingSpacing(bday_1, bday_2):
    greater_bday = ''
    lesser_bday = ''

    if bday_1 > bday_2:
        greater_bday = bday_1
        lesser_bday = bday_2
    else:
        greater_bday = bday_2
        lesser_bday = bday_1
    
    if lesser_bday + relativedelta(months=8) < greater_bday:
        return True
    else:
        if lesser_bday + relativedelta(days=2) > greater_bday:
            return True
    return False

def sibilingSpacing(indi_list, fam_list):
    error_statements = []
    for fam in fam_list:
        child_list = []
        for child in fam['children']:
            for indi in indi_list:
                if child == indi['id']:
                    child_list.append(indi)
        # COMMENTED CODE PRINTED ERRORS TWICE (child1 & child2, child2 & child1)
        # for child1 in child_list:
        #     for child2 in child_list:
        #         if child1 != child2:
        #             if not isCorrectSibilingSpacing(child1['birthday'], child2['birthday']):
        #                 error_statements.append(f"Error US13: {child1['name']} ({child1['id']}) and {child2['name']} ({child2['id']}) are born within 8 months of each other and are not twins")
        for i in range(len(child_list)):
            for j in range(i + 1, len(child_list)):
                if not isCorrectSibilingSpacing(child_list[i]['birthday'], child_list[j]['birthday']):
                    error_statements.append(f"Error US13: {child_list[i]['name']} ({child_list[i]['id']}) and {child_list[j]['name']} ({child_list[j]['id']}) are born within 8 months of each other and are not twins")
        child_list = []
    return error_statements
