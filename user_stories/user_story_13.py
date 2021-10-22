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

def sibilingSpacing(fam_list, indi_list):
    error_statements = []

    return error_statements
