from prettytable import PrettyTable 
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from operator import itemgetter
from user_stories.user_story_1 import validDate
from user_stories.user_story_2 import birthBeforeMarriage
from user_stories.user_story_3 import birthBeforeDeath
from user_stories.user_story_5 import marrBeforeDeath
from user_stories.user_story_4 import marrBeforeDivorce
from user_stories.user_story_22 import uniqueIds
from user_stories.user_story_8 import birthBeforeMarriageOfParents

def gedcomData(indi_list, fam_list):
    validTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

    months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
    indi_i = -1
    fam_i = -1

    prev_tag = ""
    prev_lvl = ""

    gedcom = open("gedcom_files/gedcom_testfile_1.ged")
    for line in gedcom:
        # print the first line
        # print("--> %s" % (line.strip()))
        # start splitting the line
        splitLine = line.split(" ", 2)
        level = splitLine[0].strip()
        tag = splitLine[1].strip()
        # if there are arguments, set argBool to true
        hasArgs = False
        arguments = ""
        if len(splitLine) > 2:
            hasArgs = True
            arguments = splitLine[2].strip()
        # consider the two exceptions
        if arguments == "INDI" or arguments == "FAM":
            tag = splitLine[2].strip()
            arguments = splitLine[1].strip()
        # check if tag is valid
        valid = "N"
        if tag in validTags:
            valid = "Y"
        if (level == "1" and tag == "DATE") or (level == "2" and tag == "NAME"):
            valid = "N"
        # add new individual or individual's data
        if valid == "Y":
            # individual tags
            if tag == "INDI" and level == "0":
                new_indi = {
                    'id': arguments,
                    'name': "NA",
                    'gender': "NA", 
                    'birthday': "NA",
                    'age': "NA",
                    'alive': True, 
                    'death': "NA", 
                    'child': set(), 
                    'spouse': set()
                }
                indi_list.append(new_indi)
                # print("=========ADDED NEW INDI=========")
                indi_i = indi_i + 1
            elif tag == "NAME" and level == "1":
                indi_list[indi_i]['name'] = arguments
            elif tag == "SEX" and level == "1":
                indi_list[indi_i]['gender']= arguments
            elif tag == "DATE" and level == "2":
                # create date object from line
                date_list = arguments.split(" ")
                day = int(date_list[0])
                month = months[date_list[1]]
                year = int (date_list[2])
                given_date = date(year, month, day)
                today = date.today()
                if prev_tag == "BIRT":
                    indi_list[indi_i]['birthday'] = given_date
                    indi_list[indi_i]['age'] = relativedelta(today, given_date).years
                elif prev_tag == "DEAT":
                    b_date = indi_list[indi_i]['birthday']
                    indi_list[indi_i]['death'] = given_date
                    indi_list[indi_i]['alive'] = False
                    indi_list[indi_i]['age'] = relativedelta(given_date, b_date).years
                elif prev_tag == "MARR":
                    fam_list[fam_i]['married'] = given_date
                elif prev_tag == "DIV":
                    fam_list[fam_i]['divorced'] = given_date
            elif tag == "FAMS" and level == "1":
                indi_list[indi_i]['spouse'].add(arguments)
            elif tag == "FAMC" and level == "1":
                indi_list[indi_i]['child'].add(arguments)
            # family tags
            elif tag == "FAM" and level == "0":
                new_fam = {
                    'id': arguments,
                    'married': "NA",
                    'divorced': "NA", 
                    'husb_id': "NA",
                    'husb_name': "NA",
                    'wife_id': "NA",
                    'wife_name': "NA",
                    'children': set()
                }
                fam_list.append(new_fam)
                # print("=========ADDED NEW FAM=========")
                fam_i = fam_i + 1
            elif tag == "HUSB" and level == "1":
                husb_name = ""
                for indi in indi_list:
                    if indi['id'] == arguments:
                        husb_name = indi['name']
                        break
                fam_list[fam_i]['husb_id'] = arguments
                fam_list[fam_i]['husb_name'] = husb_name
            elif tag == "WIFE" and level == "1":
                wife_name = ""
                for indi in indi_list:
                    if indi['id'] == arguments:
                        wife_name = indi['name']
                        break
                fam_list[fam_i]['wife_id'] = arguments
                fam_list[fam_i]['wife_name'] = wife_name
            elif tag == "CHIL" and level == "1":
                fam_list[fam_i]['children'].add(arguments)
        
        # print the second line
        # if hasArgs == True:
        #     print("<-- %s|%s|%s|%s" % (level, tag, valid, arguments))
        # else:
        #     print("<-- %s|%s|%s" % (level, tag, valid))

        prev_tag = tag
        prev_lvl = level
         # print("Current indi_i: %s" % (indi_i))
    gedcom.close()



if __name__ == "__main__":
    indi_list = []
    fam_list = []
    errors = []

    gedcomData(indi_list, fam_list)

    indi_list = sorted(indi_list, key=itemgetter('id'))
    fam_list = sorted(fam_list, key=itemgetter('id'))

    # Call all user stories
    errors1 = validDate(indi_list, fam_list)
    errors2 = birthBeforeMarriage(indi_list, fam_list)
    errors3 = birthBeforeDeath(indi_list)
    errors4 = marrBeforeDivorce(fam_list)
    errors5 = marrBeforeDeath(indi_list, fam_list)
    errors8 = birthBeforeMarriageOfParents(indi_list, fam_list)
    errors22 = uniqueIds(indi_list, fam_list)
    errors = errors1 + errors2 + errors3 + errors4 + errors5  + errors8 + errors22

    indi_table = PrettyTable()
    indi_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]

    fam_table = PrettyTable()
    fam_table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

    for indi in indi_list:
        if len(indi['child']) == 0:
            indi['child'] = "NA"
        if len(indi['spouse']) == 0:
            indi['spouse'] = "NA"
        indi_table.add_row([indi['id'], indi['name'], indi['gender'], indi['birthday'], indi['age'], indi['alive'], indi['death'], indi['child'], indi['spouse']])

    for fam in fam_list:
        if len(fam['children']) == 0:
            fam['children'] = "NA"
        fam_table.add_row([fam['id'], fam['married'], fam['divorced'], fam['husb_id'], fam['husb_name'], fam['wife_id'], fam['wife_name'], fam['children']])

    print("")
    print("Individuals")
    print(indi_table)
    print("Families")
    print(fam_table)
    # print all found errors and anomalies
    if errors is not None:
        for err in errors:
            print(err)
