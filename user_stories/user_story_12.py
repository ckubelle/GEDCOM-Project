# User Story 12 - Mother should be less than 60 years 
# older than her children and father should be 
# less than 80 years older than his children
from datetime import date, datetime
from dateutil import relativedelta

# return error statements if parents are too old given the requirements
def parentsTooOld(indi_list, fam_list):
    errorStatements = []

# return true if parents in given fam are too old 
def checkParentsTooOld(indi_list, fam):

# return birthday of given fam's youngest child
def getYoungestBday(fam_list, fam_id):
    # initialize default youngest birthday
    youngBday = date(9999, 9, 9)
    for fam in fam_list:
        if fam["id"] == fam_id:
            # loop through all children
            for child in fam["children"]:
                # check if this is first child
                if youngBday == date(9999, 9, 9):
                    youngBday = child["birthday"]
                # if not, compare and find youngest birthday (most recent date is "greater")
                else:
                    if child["birthday"] >= youngBday:
                        youngBday = child["birthday"]
    return youngBday

# return difference in given dates by years
def diffDates(date1, date2):
    # calculate difference in time using relative delta
    diff = relativedelta.relativedelta(date1, date2)
    # return absolute value of difference, in years
    return abs(diff.years)

# return given ind's birthday
def getBirthday(indi_list, ind_id):
    for ind in indi_list:
      if ind["id"] == ind_id:
          birthday = ind["birthday"]
    return birthday
