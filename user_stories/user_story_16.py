# User Story #16: Male Last Names
# All male members of a family should have the same last name

# return true if all males in the fam have the same last name, false if they do not
def checkMaleLastNames(indi_list, fam_list):
    for fam in fam_list:
        # set family name as husband's last name
        husbId = fam['husb_id']
        famName = findLastName(husbId, indi_list)
        # check last name of all male children
        for child in fam['children']:
            if (isMale(child, indi_list)):
                childLast = findLastName(child, indi_list)
                if (childLast != famName):
                    return False
    return True
        

# return true if given ind is male
def isMale(indi_id, indi_list):
    for indi in indi_list:
        if indi['id'] == indi_id:
            check = indi['gender'] == 'M'
    return check

# return given indi's last name
def findLastName(indi_id, indi_list):
    for indi in indi_list:
        if indi['id'] == indi_id:
            fullName = indi['name'].split()
            last = fullName[1].strip()
    return last

