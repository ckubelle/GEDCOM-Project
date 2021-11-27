
from operator import itemgetter
from prettytable import PrettyTable


def checkIfLiving(indi):
    if indi["alive"]:
        return True
    return False

def makeDeceasedList(indi_list):
    deceasedList = []

    for indi in indi_list:
        isLiving = checkIfLiving(indi)
        if not isLiving:
            deceasedList.append(indi)
    return sorted(deceasedList, key=itemgetter('id'))


def makeDeceasedTable(indi_list):

    deceased_list = makeDeceasedList(indi_list)

    deceased_table = PrettyTable()
    deceased_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for deceased in deceased_list:
        if len(deceased['child']) == 0:
            deceased['child'] = "NA"
        if len(deceased['spouse']) == 0:
            deceased['spouse'] = "NA"
        deceased_table.add_row([deceased['id'], deceased['name'], deceased['gender'], deceased['birthday'], deceased['age'], deceased['alive'], deceased['death'], deceased['child'], deceased['spouse']])
    return deceased_table
