# User Story #5: Marriage Before Death
def isMarrBeforeDeath(marrMonth, marrDay, marrYear, deathMonth, deathDay, deathYear):
    # If marriage date is after death date, return False. Otherwise, return True
    if deathYear < marrYear:
        return False
    elif deathYear == marrYear and deathMonth < marrMonth:
        return False
    elif deathYear == marrYear and deathMonth == marrMonth and deathDay < marrDay:
        return False
    else:
        return True

def marrBeforeDeath(indi_list, fam_list):
    errorStatements = []
    for fam in fam_list:
        wifeId = fam["wife_id"]
        husbId = fam["husb_id"]
        if fam["married"] != "NA":
            marrMonth = fam["married"].strftime("%m")
            marrDay = fam["married"].strftime("%d")
            marrYear = fam["married"].strftime("%Y")
        for indi in indi_list:
            if indi["id"] == wifeId and indi["death"] != "NA":
                #check if marriage date is before death date
                deathMonth = indi["death"].strftime("%m")
                deathDay = indi["death"].strftime("%d")
                deathYear = indi["death"].strftime("%Y")
                check = isMarrBeforeDeath(int(marrMonth), int(marrDay), int(marrYear), int(deathMonth), int(deathDay), int(deathYear))
                if check == False:
                    errorStatements.append("Error US05: Marriage date in Family %s occurs after death date of %s (%s)" % ( fam["id"], indi["name"].replace("/", ""), indi["id"]))
    return errorStatements
                