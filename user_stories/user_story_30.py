# Jeffrey Lee
# User Story 30 - List living married
# I pledge my honor that I have abided by the Stevens Honor System.

from operator import itemgetter
from prettytable import PrettyTable

def checkIfMarried(indi, fam_list):
    isMarried = False
    for fam in fam_list:
        if indi["id"] == fam["husb_id"] or indi["id"] == fam["wife_id"]:
            if fam["married"] != "NA" and fam["divorced"] == "NA":
                isMarried = True
    return isMarried

def checkIfLiving(indi):
    if indi["alive"] == True and indi["age"] > 0:
        return True
    return False

def makeLivingMarriedList(indi_list, fam_list):
    livingMarriedList = []
    for indi in indi_list:
        isMarried = checkIfMarried(indi, fam_list)
        isLiving = checkIfLiving(indi)
        if isMarried and isLiving:
            livingMarriedList.append(indi)
    return sorted(livingMarriedList, key=itemgetter('id'))

def makeLivingMarriedTable(indi_list, fam_list):
    living_married_list = makeLivingMarriedList(indi_list, fam_list)
    living_married_table = PrettyTable()
    living_married_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for living_married in living_married_list:
        if len(living_married['child']) == 0:
            living_married['child'] = "NA"
        if len(living_married['spouse']) == 0:
            living_married['spouse'] = "NA"
        living_married_table.add_row([living_married['id'], living_married['name'], living_married['gender'], living_married['birthday'], living_married['age'], living_married['alive'], living_married['death'], living_married['child'], living_married['spouse']])
    return living_married_table