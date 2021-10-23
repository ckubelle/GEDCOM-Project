# User Story #9: Birth Before Marriage of Parents
from dateutil.relativedelta import relativedelta

def isbirthBeforeFatherDeath(birthday, fatureDeath):
    if fatureDeath == 'NA' or birthday < fatureDeath + relativedelta(months=+9):
        return True

    return False

def isbirthBeforeMotherDeath(birthday, motherDeath):
    if motherDeath == 'NA' or birthday < motherDeath:
        return True
    
    return False
    
def birthBeforeDeathOfParents(indi_list, fam_list):
    errorStatements = []
    fatherDeathDate = 'NA'
    motherDeathDate = 'NA'
    for fam in fam_list:
        # Find death dates of child's parents in family
        for indi in indi_list:
            if indi['id'] == fam['husb_id']:
                fatherDeathDate = indi['death']
            if indi['id'] == fam['wife_id']:
                motherDeathDate = indi['death']
        # For each child in family, check if child is born before death of parents
        for child in fam['children']:
            for indi in indi_list:
                if child == indi['id']:
                    if (isbirthBeforeFatherDeath(indi['birthday'], fatherDeathDate) == False):
                        errorStatements.append(f"Error US09: Birth date of child {indi['name']} ({indi['id']}) occurs after 9 months after death of father {fam['husb_name']} ({fam['husb_id']}) in family ({fam['id']}). The birthday of child is {indi['birthday']}, and the death date of father is ({fatherDeathDate}).")
                    if (isbirthBeforeMotherDeath(indi['birthday'], motherDeathDate) == False):
                        errorStatements.append(f"Error US09: Birth date of child {indi['name']} ({indi['id']}) occurs after death of mother {fam['wife_name']} ({fam['wife_id']}) in family ({fam['id']}). The birthday of child is {indi['birthday']}, and the death date of mother is ({motherDeathDate}).")
    return errorStatements