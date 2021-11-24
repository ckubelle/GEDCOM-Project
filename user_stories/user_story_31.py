# Jeffrey Lee
# User Story 31 - List living single
# List all living people over 30 who have never been married in a GEDCOM file
# I pledge my honor that I have abided by the Stevens Honor System.

from operator import itemgetter
from prettytable import PrettyTable

def checkIfNeverMarried(indi, fam_list):
    neverMarried = True
    for fam in fam_list:
        if indi["id"] == fam["husb_id"] or indi["id"] == fam["wife_id"]:
            #if fam["married"] != "NA":
            neverMarried = False
    return neverMarried

def checkIfLivingOver30(indi):
    if indi["alive"] == True and indi["age"] > 30:
        return True
    return False

def makeLivingSingleList(indi_list, fam_list):
    livingSingleList = []
    for indi in indi_list:
        isNeverMarried = checkIfNeverMarried(indi, fam_list)
        isLivingOver30 = checkIfLivingOver30(indi)
        if isNeverMarried and isLivingOver30:
            livingSingleList.append(indi)
    return sorted(livingSingleList, key=itemgetter('id'))

def makeLivingSingleTable(indi_list, fam_list):
    living_single_list = makeLivingSingleList(indi_list, fam_list)
    living_single_table = PrettyTable()
    living_single_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for living_single in living_single_list:
        if len(living_single['child']) == 0:
            living_single['child'] = "NA"
        if len(living_single['spouse']) == 0:
            living_single['spouse'] = "NA"
        living_single_table.add_row([living_single['id'], living_single['name'], living_single['gender'], living_single['birthday'], living_single['age'], living_single['alive'], living_single['death'], living_single['child'], living_single['spouse']])
    return living_single_table