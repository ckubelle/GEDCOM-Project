# Leena Domadia
# User Story 07 - Less than 150 years
# I pledge my Honor that I have abided by the Stevens Honor System

from datetime import datetime
from dateutil.relativedelta import relativedelta

def isTooOld(birthdate):
    now = datetime.now()
    birthdate = datetime.combine(birthdate, datetime.min.time())
    if birthdate + relativedelta(years=150) > now:
        return False
    return True

def tooOld(indi_list):
    error_statements = []
    for indi in indi_list:
        if indi['death'] == "NA":
            if isTooOld(indi['birthday']):
                error_statements.append(f"Error US07: {indi['name']} ({indi['id']}) is more than 150 years old")
    return error_statements