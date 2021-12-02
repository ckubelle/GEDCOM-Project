# User Story 28
# List siblings in families by decreasing age, i.e. oldest siblings first

from operator import itemgetter

# returns ordered list of siblings by decreasing age
def orderedSibs(indi_list, fam):
    # if only 1 or 0 siblings, return children set as list
    if len(fam['children']) <= 1:
        return list(fam['children'])
    else:
        age_dict = []
        ret_list = []
        # add children to new list
        for sibling in fam['children']:
            for ind in indi_list:
                if sibling == ind['id']:
                    age_dict.append(ind)
        # sort dictionary by value from oldest child to youngest
        age_dict = sorted(age_dict, key=itemgetter('birthday'))
        # add just the ordered IDs to return list
        for child in age_dict:
            ret_list.append(child['id'])
        return ret_list
