# Name: Jeffrey Lee
# I pledge my honor that I have abided by the Stevens Honor System.

def gedcomData():
    validTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]
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
        # print the second line
        if hasArgs == True:
            print("<-- %s|%s|%s|%s" % (level, tag, valid, arguments))
        else:
            print("<-- %s|%s|%s" % (level, tag, valid))
    gedcom.close()

if __name__ == "__main__":
    gedcomData()
