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
        {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': False, 'death': date(1980, 2, 20), 'child': {'@F03@'}, 'spouse': set()},
        {'id': '@I05@', 'name': 'Kim /Biden/', 'gender': 'F', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': False, 'death': date(1980, 2, 20), 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I06@', 'name': 'Joe /Biden/', 'gender': 'M', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I07@', 'name': 'Moe /Biden/', 'gender': 'M', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I08@', 'name': 'Doe /Biden/', 'gender': 'F', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()}]
    test_none = {'id': '@F01@', 'married': date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': set()}
    test_div = {'id': '@F02@', 'married': date(1950, 6, 17), 'divorced': date(1980, 6, 17), 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': set()}
    test_husb = {'id': '@F03@', 'married': date(1970, 6, 17), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': set()}
    test_wife = {'id': '@F04@', 'married': date(1970, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I05@', 'wife_name': 'Neilia /Hunter/', 'children': set()}
    test_famlist = [test_none, test_husb, test_wife]
    # define test methods
    def test_check_Bigamy(self):
        self.assertFalse(user_story_11.checkBigamy(self.test_indi, self.test_famlist, self.test_none))
    
    def test_get_End_Marr(self):
        self.assertEqual(user_story_11.getEndMarr(self.test_indi, self.test_none), date(3000, 1, 1))
        self.assertEqual(user_story_11.getEndMarr(self.test_indi, self.test_div), date(1980, 6, 17))
        self.assertEqual(user_story_11.getEndMarr(self.test_indi, self.test_husb), date(1980, 2, 20))
        self.assertEqual(user_story_11.getEndMarr(self.test_indi, self.test_wife), date(1980, 2, 20))
