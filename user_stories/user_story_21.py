# Leena Domadia
# User Story 21 - Correct Gender for Role
# I pledge my Honor that I have abided by the Stevens Honor System - Leena Domadia

def isCorrectGenderHusb(indi_gender):
    if indi_gender == "M":
        return True
    return False

def isCorrectGenderWife(indi_gender):
    if indi_gender == "F":
        return True
    return False

def correctGender(indi_list, fam_list):
    error_statements = []
    husb_list = []
    wife_list = []
    # get all husb and wife ids
    for fam in fam_list:
        husb_list.append(fam['husb_id'])
        wife_list.append(fam['wife_id'])
    # check for errors
    for husb in husb_list:
        for indi in indi_list:
            if indi['id'] == husb:
                if not isCorrectGenderHusb(indi['gender']):
                    error_statements.append(f"Error US21: {indi['name']} ({indi['id']}) is male but is the wife in Family {indi['spouse']}")
    for wife in wife_list:
        for indi in indi_list:
            if indi['id'] == wife:
                if not isCorrectGenderWife(indi['gender']):
                    error_statements.append(f"Error US21: {indi['name']} ({indi['id']}) is female but is the husband in Family {indi['spouse']}")
    return error_statements
    