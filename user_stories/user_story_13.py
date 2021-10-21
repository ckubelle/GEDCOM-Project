# Leena Domadia
# User Story 13 - Sibiling Spacing
# I pledge my Honor that I have abided by the Stevens Honor System

from datetime import datetime
from dateutil.relativedelta import relativedelta

def isCorrectSibilingSpacing(bday_1, bday_2):
    if bday_1 > bday_2:
        if bday_2 + relativedelta(months=8) < bday_1:
            return True

def sibilingSpacing(fam_list, indi_list):
    error_statements = []
    for fam in fam_list:
        child_list = fam['child']
        child_id_list = []
        for child_id in child_list:
            child_id_list.append(child_id)


    return error_statements
