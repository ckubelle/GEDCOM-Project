# User Story #2: Birth before marriage
# Birth should occur before marriage of an individual
def isBirthBeforeMarr(birthMonth, birthDay, birthYear, marrMonth, marrDay, marrYear):
    # If birthday is after marriage date, return False. Otherwise, return True
    if marrYear < birthYear:
        return False
    elif marrYear == birthYear and marrMonth < birthMonth:
        return False
    elif marrYear == birthYear and marrMonth == birthMonth and marrDay < birthDay:
        return False
    else:
        return True

def birthBeforeMarriage(indi_list, fam_list):
    errorStatements = []
    for fam in fam_list:
        husbID = fam["husb_id"]
        wifeID = fam["wife_id"]
        for indi in indi_list:
            if indi["id"] == husbID or indi["id"] == wifeID:
                if indi["birthday"] != "NA" and fam["married"] != "NA":
                    birthMonth = indi["birthday"].strftime("%m")
                    birthDay = indi["birthday"].strftime("%d")
                    birthYear = indi["birthday"].strftime("%Y")
                    marrMonth = fam["married"].strftime("%m")
                    marrDay = fam["married"].strftime("%d")
                    marrYear = fam["married"].strftime("%Y")
                    check = isBirthBeforeMarr(int(birthMonth), int(birthDay), int(birthYear), int(marrMonth), int(marrDay), int(marrYear))
                if check == False:
                    errorStatements.append("Error US02: Birth date of %s (%s) occurs after marriage date in Family %s" % (indi["name"].replace("/", ""), indi["id"], fam["id"]))
    return errorStatements