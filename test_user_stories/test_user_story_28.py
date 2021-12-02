# User Story 28 Test Class
# List siblings in families by decreasing age, i.e. oldest siblings first

import unittest
from datetime import date
from user_stories import user_story_28

class TestUserStory28(unittest.TestCase):
    # create test objects to interact with
    test_indi = [
        {'id': '@I01@', 'name': 'Jim /Biden/', 'gender': 'M', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I02@', 'name': 'Kim /Hunter/', 'gender': 'F', 'birthday': date(1999, 2, 3), 'age': 22, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I03@', 'name': 'Tim /Biden/', 'gender': 'M', 'birthday': date(1962, 2, 28), 'age': 59, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()}]
    test_indi2 = [
        {'id': '@I01@', 'name': 'Jim /Biden/', 'gender': 'M', 'birthday': date(1980, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I02@', 'name': 'Kim /Hunter/', 'gender': 'F', 'birthday': date(1969, 2, 3), 'age': 22, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I03@', 'name': 'Tim /Biden/', 'gender': 'M', 'birthday': date(2000, 2, 28), 'age': 59, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': set()}]
    test_fam1 = {'id': '@F01@', 'married': date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I20@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I21@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I01@', '@I02@', '@I03@'}}
    test_fam2 = {'id': '@F01@', 'married': date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I20@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I21@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I01@'}}
    test_fam3 = {'id': '@F01@', 'married': date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I20@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I21@', 'wife_name': 'Neilia /Hunter/', 'children': set()}
    test_fam4 = {'id': '@F01@', 'married': date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I20@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I21@', 'wife_name': 'Neilia /Hunter/', 'children': "NA"}
    # define test methods
    def test_ordered_sibs(self):
        self.assertEqual(user_story_28.orderedSibs(self.test_indi, self.test_fam1), ['@I01@', '@I03@', '@I02@'])
        self.assertEqual(user_story_28.orderedSibs(self.test_indi2, self.test_fam1), ['@I02@', '@I01@', '@I03@'])
        self.assertEqual(user_story_28.orderedSibs(self.test_indi, self.test_fam2), ['@I01@'])
        self.assertEqual(user_story_28.orderedSibs(self.test_indi, self.test_fam3), [])
        self.assertEqual(user_story_28.orderedSibs(self.test_indi, self.test_fam4), [])
