from prettytable import PrettyTable 
from datetime import date
from dateutil.relativedelta import relativedelta

def gedcomData(indi_list, fam_list):
    validTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

    months = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
    indi_i = -1
    fam_i = -1

    prev_tag = ""

    gedcom = open("gedcom_testfile_1.ged")
    for line in gedcom:
        # print the first line
        print("--> %s" % (line.strip()))
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
            if tag == "INDI":
                new_indi = {
                    'ID': arguments,
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
                print("=========ADDED NEW INDI=========")
                indi_i = indi_i + 1
            elif tag == "NAME":
                indi_list[indi_i]['name'] = arguments
            elif tag == "SEX":
                indi_list[indi_i]['gender']= arguments
            elif tag == "DATE":
                date_list = arguments.split(" ")
                day = int(date_list[0])
                month = months[date_list[1]]
                year = int (date_list[2])
                given_date = date(year, month, day)
                today = date.today()
                if prev_tag == "BIRT":
                    indi_list[indi_i]['birthday'] = arguments
                    indi_list[indi_i]['age'] = relativedelta(today, given_date).years
                elif prev_tag == "DEAT":
                    bdate_list = indi_list[indi_i]['birthday'].split(" ")
                    b_day = int(bdate_list[0])
                    b_month = months[bdate_list[1]]
                    b_year = int (bdate_list[2])
                    b_date = date(b_year, b_month, b_day)
                    indi_list[indi_i]['death'] = arguments
                    indi_list[indi_i]['alive'] = False
                    indi_list[indi_i]['age'] = relativedelta(given_date, b_date).years
            elif tag == "FAMS":
                indi_list[indi_i]['spouse'].add(arguments)
            elif tag == "FAMC":
                indi_list[indi_i]['child'].add(arguments)
        
        # print the second line
        # if hasArgs == True:
        #     print("<-- %s|%s|%s|%s" % (level, tag, valid, arguments))
        # else:
        #     print("<-- %s|%s|%s" % (level, tag, valid))

        prev_tag = tag
         # print("Current indi_i: %s" % (indi_i))
    gedcom.close()

if __name__ == "__main__":
    indi_list = []
    fam_list = []

    gedcomData(indi_list, fam_list)

    # print(indi_list)

    indi_table = PrettyTable()
    indi_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]

    for indi in indi_list:
        if len(indi['child']) == 0:
            indi['child'] = "NA"
        if len(indi['spouse']) == 0:
            indi['spouse'] = "NA"
        indi_table.add_row([indi['ID'], indi['name'], indi['gender'], indi['birthday'], indi['age'], indi['alive'], indi['death'], indi['child'], indi['spouse']])

    print(indi_table)
