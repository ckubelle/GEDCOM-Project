# Name: Jeffrey Lee
# I pledge my honor that I have abided by the Stevens Honor System.

# User Story 22: Unique IDs

import unittest

# Code for User Story
def isIndividualIDUnique(gedcom_filename):
    gedcom = open(gedcom_filename)
    individualList = []
    for line in gedcom:
        splitLine = line.split(" ", 2)
        level = splitLine[0].strip()
        tag = splitLine[1].strip()
        if len(splitLine) > 2:
            arguments = splitLine[2].strip()
        if arguments == "INDI" and level == "0":
            individualList.append(tag)
    gedcom.close()
    for indiID in individualList:
        if(individualList.count(indiID) != 1):
            return False
    return True

def isFamilyIDUnique(gedcom_filename):
    gedcom = open(gedcom_filename)
    familyList = []
    for line in gedcom:
        splitLine = line.split(" ", 2)
        level = splitLine[0].strip()
        tag = splitLine[1].strip()
        if len(splitLine) > 2:
            arguments = splitLine[2].strip()
        if arguments == "FAM" and level == "0":
            familyList.append(tag)
    gedcom.close()
    for famID in familyList:
        if(familyList.count(famID) != 1):
            return False
    return True

def isAllUnique(gedcom_filename):
    indi = isIndividualIDUnique(gedcom_filename)
    fam = isFamilyIDUnique(gedcom_filename)
    if indi == True and fam == True:
        return True
    return False

# Test Code
class testCode(unittest.TestCase):
    def test_1(self):
        # gedcom file contains all unique individual IDs and family IDs
        self.assertTrue(isAllUnique("gedcom_files_for_tests/GEDCOM_Test1.ged"))
    def test_2(self):
        # gedcom file contains all unique individual IDs but all family IDs are not unique
        self.assertFalse(isAllUnique("gedcom_files_for_tests/GEDCOM_Test2.ged"))
    def test_3(self):
        # gedcom file contains all unique family IDs but all individual IDs are not unique
        self.assertFalse(isAllUnique("gedcom_files_for_tests/GEDCOM_Test3.ged"))
    def test_4(self):
        # gedcom file contains both individual and family IDs that are NOT unique
        self.assertFalse(isAllUnique("gedcom_files_for_tests/GEDCOM_Test4.ged"))
    def test_5(self):
        # gedcom file contains more than one individual ID that are NOT unique (duplicate of @I1@ ID and duplicate of @I2@ ID)
        self.assertFalse(isAllUnique("gedcom_files_for_tests/GEDCOM_Test5.ged"))

if __name__ == "__main__":
    unittest.main()