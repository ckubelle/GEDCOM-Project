# Name: Jeffrey Lee
# Homework 6
# I pledge my honor that I have abided by the Stevens Honor System.

# User Story 22: Unique IDs

import unittest

# Return set of non-unique IDs based on given list (For Code Smell of Duplicated Code)
def findNonUniqueIds(lst):
    nonUniqueIds = set()
    # Store all ids into its own list
    allIds = []
    for elem in lst:
        allIds.append(elem["id"])
    # Store all non-unique Ids
    for singleId in allIds:
        if(allIds.count(singleId) > 1):
            nonUniqueIds.add(singleId)
    return nonUniqueIds

# Find names of the individuals with non-unique Ids (For Code Smell of Long Method w/ Too Much Code)
def findNamesWNonUniqueIds(nonUniqueIndiIds, indi_list):
    # Find the names of individuals with non-unique Ids
    idWithNames = {}
    if len(nonUniqueIndiIds) > 0:
        for nonUniqueIndiId in nonUniqueIndiIds:
            tmp_list = []
            for indi in indi_list:
                if indi["id"] == nonUniqueIndiId:
                    tmp_list.append(indi["name"].replace("/", ""))
            idWithNames[nonUniqueIndiId] = tmp_list
    return idWithNames


# Refactored the two code smells in this method which were the following:
# - Duplicated code (very similar code for individual and family functionality)
# - Long method with too much code (should extract method)
def uniqueIds(indi_list, fam_list):
    errorStatements = []
    # Refactored code smell of duplicated code / very similar code for individual and family functionality
    nonUniqueIndiIds = findNonUniqueIds(indi_list)
    nonUniqueFamIds = findNonUniqueIds(fam_list)
    # Refactored code smell of long method with too much code
    namesForNonUniqueIds = findNamesWNonUniqueIds(nonUniqueIndiIds, indi_list)
    # Add error statements
    for key, value in namesForNonUniqueIds.items():
        errorStatements.append("Error US22: %s all have the same individual ID (%s)." % (", ".join(value), key))
    for nonUniqueFamId in nonUniqueFamIds:
        errorStatements.append("Error US22: There are duplicates of the family ID %s. All family IDs should be unique." % (nonUniqueFamId))
    return errorStatements