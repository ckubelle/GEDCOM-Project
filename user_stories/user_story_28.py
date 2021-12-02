# User Story 28
# List siblings in families by decreasing age, i.e. oldest siblings first

# returns ordered list of siblings by decreasing age
def orderedSibs(indi_list, fam):
    # if only 1 or 0 siblings, return children set as list
    if len(fam['children']) <= 1:
        return list(fam['children'])
    else:
        age_dict = {}
        ret_list = []
        # add children to new dictionary as key = birthday: value = id
        for sibling in fam['children']:
            for ind in indi_list:
                if sibling == ind['id']:
                    age_dict[ind['birthday']] = sibling
        # sort dictionary by key from oldest child to youngest
        age_dict = dict(sorted(age_dict.items()))
        # add just the ordered values (IDs) to list
        for val in age_dict.values():
            ret_list.append(val)
        return ret_list
