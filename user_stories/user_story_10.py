# User Story 10 - Marriage should be at least 14 years after 
# birth of both spouses

import datetime

# return error statements if marriage occurs before age 14
def checkMarrAfter14(indi_list, fam_list):

# return true if marriage in given fam occurred after spouses were age 14
def isMarrAfter14(indi_list, fam):
    # if no marriage, return false
    if fam["married"] == "NA":
        return false;
    # else, find the marriage date
    else:
        marrMonth = fam["married"].strftime("%m")
        marrDay = fam["married"].strftime("%d")
        marrYear = fam["married"].strftime("%Y")

# return given ind's birthday month, day, and year in that order
def getIndBirthday(indi_list, ind_id):
    for ind in indi_list:
      if ind["id"] == ind_id:
          month = ind["birthday"].strftime("%m")
          day = ind["birthday"].strftime("%d")
          year = ind["birthday"].strftime("%Y")
    return month, day, year
