from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable


def compareDates(date1, date2):
    if min(date1, date2) + relativedelta(days=1) >= max(date1, date2):
        return True
    return False


def makeMultiTable(indi_list, fam_list):
    childrenBirthDates = {}
    multi_table = PrettyTable()
    multi_table.field_names = ["Fam ID", "Multiple Births ID"]

    for fam in fam_list:

        if len(fam['children']) > 1:
            tempchildren = {}
            for indi in indi_list:

                if indi['id'] in fam['children']:
                    tempchildren[indi['id']] = indi['birthday']

            childrenBirthDates[fam['id']] = tempchildren


    for fam in childrenBirthDates:

        #dictionary of individuals with there corresponding bdays
        individuals = childrenBirthDates[fam]

        similar_bdays = set()

        for indi in individuals:

            for indi2 in individuals:
                
                if indi != indi2 and compareDates(individuals[indi], individuals[indi2]):
                    similar_bdays.add(indi)
                    similar_bdays.add(indi2)

        #Only want to add if twins or more...
        if len(similar_bdays) > 1:
            multi_table.add_row([fam, similar_bdays])

    return multi_table