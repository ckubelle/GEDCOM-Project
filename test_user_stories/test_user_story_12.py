# User Story 12 Test Class
# Mother should be less than 60 years 
# older than her children and father should be 
# less than 80 years older than his children

import unittest
import datetime
from user_stories import user_story_12

class TestUserStory12(unittest.TestCase):
    # create test objects to interact with
    test_dad_true = [
        {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1962, 2, 28), 'age': 59, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I03@', 'name': 'James /Biden/', 'gender': 'M', 'birthday': datetime.date(1999, 2, 3), 'age': 22, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(2014, 2, 3), 'age': 7, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()}]
    test_mom_true = [
        {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 2, 20), 'age': 89, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 2, 28), 'age': 89, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I03@', 'name': 'James /Biden/', 'gender': 'M', 'birthday': datetime.date(2012, 2, 3), 'age': 9, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(2000, 2, 3), 'age': 21, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()}]
    test_false = [
        {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1962, 2, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1962, 2, 28), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I03@', 'name': 'James /Biden/', 'gender': 'M', 'birthday': datetime.date(2012, 2, 3), 'age': 52, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(2012, 2, 3), 'age': 52, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()}]
    test_famlist = []
    test_fam = {'id': '@F01@', 'married': datetime.date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I03@', '@I04@'}}
    
    # define test methods
    def test_check_parents_too_old(self):
        self.assertTrue(user_story_12.checkParentsTooOld(self.test_dad_true, self.test_fam))
        self.assertTrue(user_story_12.checkParentsTooOld(self.test_dad_true, self.test_fam))
        self.assertFalse(user_story_12.checkParentsTooOld(self.test_false, self.test_fam))
      
    def test_get_youngest_bday(self):
        self.assertEqual(user_story_12.getYoungestBday(self.test_dad_true, self.test_fam), datetime.date(2014, 2, 3))
        self.assertEqual(user_story_12.getYoungestBday(self.test_mom_true, self.test_fam), datetime.date(2012, 2, 3))

    def test_diff_dates(self):
        self.assertEqual(user_story_12.diffDates(datetime.date(2000, 1, 1), datetime.date(2014, 1, 1)), 14)
        self.assertEqual(user_story_12.diffDates(datetime.date(2014, 1, 1), datetime.date(2000, 1, 1)), 14)

    def test_get_birthday(self):
        self.assertEqual(user_story_12.getBirthday(self.test_false, '@I01@'), datetime.date(1962, 2, 20))
        self.assertEqual(user_story_12.getBirthday(self.test_false, '@I03@'), datetime.date(2012, 2, 3))
