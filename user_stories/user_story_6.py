

def checkDates(divorced, death):

    if death != 'NA' and divorced > death:
        return False
    else:
        return True

def divorceBeforeDeath(indi_list, fam_list):

    errorStatements = []

    for fam in fam_list:

        if fam['divorced'] != 'NA':
    
            for indi in indi_list:

                if fam['husb_id'] == indi['id']:
                    if checkDates(fam['divorced'], indi['death']):
                        continue
                    else:
                        errorStatements.append(f"Error US06: Divorce of FAM ({fam['id']}) occurs after death of Husband ({indi['id']})")

                if fam['wife_id'] == indi['id']:
                    if checkDates(fam['divorced'], indi['death']):
                       continue
                    else:
                        errorStatements.append(f"Error US06: Divorce of FAM ({fam['id']}) occurs after death of Wife ({indi['id']})")

    return errorStatements


