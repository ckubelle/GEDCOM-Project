# User Story 11 Test Class
# No Bigamy
import unittest
from datetime import date
from user_stories import user_story_11

class TestUserStory11(unittest.TestCase):
    # create test objects to interact with
    test_indi = [
        {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': {'@F03@'}},
        {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': {'@F03@'}},
        {'id': '@I03@', 'name': 'James /Biden/', 'gender': 'M', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F03@'}, 'spouse': set()},
        {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': False, 'death': date(1960, 2, 20), 'child': {'@F03@'}, 'spouse': set()},
        {'id': '@I05@', 'name': 'Kim /Biden/', 'gender': 'F', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': False, 'death': date(1960, 2, 20), 'child': {'@F01@'}, 'spouse': set()}]
    test_none = {'id': '@F01@', 'married': date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': set()}
    test_div = {'id': '@F02@', 'married': date(1950, 6, 17), 'divorced': date(1970, 6, 17), 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': set()}
    test_husb = {'id': '@F03@', 'married': date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': set()}
    test_wife = {'id': '@F03@', 'married': date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I05@', 'wife_name': 'Neilia /Hunter/', 'children': set()}
