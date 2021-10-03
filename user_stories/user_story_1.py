# Leena Domadia - Homework 4
# User Story 1 - Dates Before Current Date
# I pledge my Honor that I have abided by the Stevens Honor System - Leena Domadia

from datetime import date;

def valid_date(givenDate):
    currentDate = date.today()
    if currentDate < givenDate:
        return False
    else:
        return True
