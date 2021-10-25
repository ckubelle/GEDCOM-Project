# Name: Jeffrey Lee
# User Story #15: Fewer than 15 siblings
# There should be fewer than 15 sublings in a family

def fewerThanFifteenSiblings(fam_list):
    errorStatements = []

    for fam in fam_list:
        if len(fam['children']) > 15:
            errorStatements.append(f"Error US15: There are 15 or more siblings in Family {fam['id']}. There should be fewer than 15 siblings in a family.")

    return errorStatements