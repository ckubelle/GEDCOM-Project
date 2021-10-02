
def gedcomData():
    validTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

    indi_list = []
    fam_list = []

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
                if prev_tag == "BIRT":
                    indi_list[indi_i]['birthday'] = arguments
                elif prev_tag == "DEAT":
                    indi_list[indi_i]['death'] = arguments
                    indi_list[indi_i]['alive'] = False
            elif tag == "FAMS":
                indi_list[indi_i]['spouse'].add(arguments)
            elif tag == "FAMC":
                indi_list[indi_i]['child'].add(arguments)
        
        # print the second line
        if hasArgs == True:
            print("<-- %s|%s|%s|%s" % (level, tag, valid, arguments))
        else:
            print("<-- %s|%s|%s" % (level, tag, valid))

        prev_tag = tag
         # print("Current indi_i: %s" % (indi_i))
    print(indi_list)
    gedcom.close()

if __name__ == "__main__":
    gedcomData()
