from dateutil.relativedelta import relativedelta


def multipleBirths(indi_list, fam_list):
    errorStatements = []

    # a nested array that contains the birthdays of each child within that family
    childrenBirthDates = {}

    for fam in fam_list:

        if len(fam['children']) > 4:
            tempchildren = []
            for indi in indi_list:

                if indi['id'] in fam['children']:
                    tempchildren.append(indi['birthday'])

            childrenBirthDates[fam['id']] = tempchildren


    

    for id in childrenBirthDates:
        childrenBirthDates[id].sort()

        counter = 1
        for i in range(len(childrenBirthDates[id]) - 1):

            if childrenBirthDates[id][i] + relativedelta(days=1) >= childrenBirthDates[id][i+1]:
                counter += 1 
            else:
                counter = 1

            if counter > 5:
                errorStatements.append(f"Error US14: Family ({id}) has more than five siblings born at the same time")
                break

    return errorStatements