# User Story 27 Test Class
# Include person's current age when listing individuals

import unittest
from datetime import date
from user_stories import user_story_27

class TestUserStory27(unittest.TestCase):
    # create test objects to interact with
    test_indi = [
        {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': {'@F03@'}},
        {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': date(1962, 2, 28), 'age': 59, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': {'@F03@'}},
        {'id': '@I03@', 'name': 'James /Biden/', 'gender': 'M', 'birthday': date(1999, 2, 3), 'age': 22, 'alive': True, 'death': 'NA', 'child': {'@F03@'}, 'spouse': set()},
        {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': date(2014, 2, 3), 'age': 7, 'alive': True, 'death': 'NA', 'child': {'@F03@'}, 'spouse': set()},
        {'id': '@I05@', 'name': 'Jim /Biden/', 'gender': 'M', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I06@', 'name': 'Kim /Hunter/', 'gender': 'F', 'birthday': date(1962, 2, 28), 'age': 59, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I07@', 'name': 'Tim /Biden/', 'gender': 'M', 'birthday': date(1999, 2, 3), 'age': 22, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': set()},
        {'id': '@I08@', 'name': 'Sim /Biden/', 'gender': 'M', 'birthday': date(2014, 2, 3), 'age': 7, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': set()}]
    test_false = {'id': '@F01@', 'married': date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I20@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I21@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I01@', '@I05@', '@I06@'}}
    test_true = {'id': '@F04@', 'married': date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I03@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I07@', 'wife_name': 'Neilia /Hunter/', 'children': set()}
   
    # define test methods
    def test_is_Include_Age(self):

    def test_check_Include_Age(self):
