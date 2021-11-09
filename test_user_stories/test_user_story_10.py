# User Story 10 Test Class
# Marriage should be at least 14 years after birth of both spouses

import unittest
import datetime
from user_stories import user_story_10

class TestUserStory10(unittest.TestCase):
    # create test objects to interact with
    test_indi = [
        {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 11, 28), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I03@', 'name': 'James /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 52, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 52, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()}]
    test_true = {'id': '@F01@', 'married': datetime.date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I03@', '@I04@'}}
    test_false = {'id': '@F01@', 'married': datetime.date(2000, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I03@', '@I04@'}}
    
    # define test methods
    def test_is_marr_before_14(self):
        self.assertTrue(user_story_10.isMarrBefore14(self.test_indi, self.test_true))
        self.assertFalse(user_story_10.isMarrBefore14(self.test_indi, self.test_false))

    def test_diff_dates(self):
        self.assertEqual(user_story_10.diffDates(datetime.date(2000, 1, 1), datetime.date(2014, 1, 1)), 14)
        self.assertEqual(user_story_10.diffDates(datetime.date(2014, 1, 1), datetime.date(2000, 1, 1)), 14)

    def test_get_birthday(self):
        self.assertEqual(user_story_10.getBirthday(self.test_indi, '@I01@'), datetime.date(1942, 11, 20))
        self.assertEqual(user_story_10.getBirthday(self.test_indi, '@I03@'), datetime.date(1969, 2, 3))
