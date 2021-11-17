# Leena Domadia
# User Story 24 - Unique Families by Spouses
# I pledge my Honor that I have abided by the Stevens Honor System - Leena Domadia

def isSameFamily(husb1, wife1, date1, husb2, wife2, date2):
    if husb1 == husb2 and wife1 == wife2 and date1 == date2:
        return True
    return False

def uniqueFamily(fam_list):
    error_statements = []
    for i in range(len(fam_list)):
        for j in range(i + 1, len(fam_list)):
            if fam_list[i]['id'] != fam_list[j]['id']:
                if isSameFamily(fam_list[i]['husb_name'], fam_list[i]['wife_name'], fam_list[i]['married'], fam_list[j]['husb_name'], fam_list[j]['wife_name'], fam_list[j]['married']):
                    error_statements.append(f"Error US24: Family {fam_list[i]['id']} and Family {fam_list[j]['id']} has the same husband name, wife name, and marriage date")
    return error_statements
