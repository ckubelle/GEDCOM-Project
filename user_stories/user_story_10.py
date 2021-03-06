# User Story 10 - Marriage should be at least 14 years after 
# birth of both spouses

from datetime import date, datetime
from dateutil import relativedelta

# return error statements if marriage occurs before age 14
def marrBefore14(indi_list, fam_list):
    errorStatements = []
    for fam in fam_list:
        if (isMarrBefore14(indi_list, fam)):
            errorStatements.append("Error US10: Marriage date in Family %s occured before both spouses were over 14 years of age." % (fam["id"]))
    return errorStatements

# return true if marriage in given fam occurred before spouses were age 14
def isMarrBefore14(indi_list, fam):
    # if no marriage, return false
    if fam["married"] == "NA":
        return False
    # else, find the marriage date
    else:
        marrDate = fam["married"]
        # get the spouses birthdays
        husbDate = getBirthday(indi_list, fam["husb_id"])
        wifeDate = getBirthday(indi_list, fam["wife_id"])
        # if marriage date occurred before birth date, return true
        if marrDate.year < husbDate.year or marrDate.year < husbDate.year:
            return True
        # if difference between birthday and marriage date is less than 14, return true
        if diffDates(marrDate, husbDate) < 14.00 or diffDates(marrDate, wifeDate) < 14.00:
            return True
        else:
            return False
        
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
