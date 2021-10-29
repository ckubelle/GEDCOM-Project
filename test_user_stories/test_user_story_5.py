# User Story 5 Test Class
# Marriage Before Death

import unittest
import datetime
from user_stories import user_story_5

class TestUserStory5(unittest.TestCase):
    # create test objects to interact with
    test_indi = [
        {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 11, 28), 'age': 50, 'alive': False, 'death': datetime.date(1992, 11, 28), 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I03@', 'name': 'James /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 52, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 52, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()}]
    test_true = [{'id': '@F01@', 'married': datetime.date(1997, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I03@', '@I04@'}}]
    test_false = [{'id': '@F01@', 'married': datetime.date(1950, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I03@', '@I04@'}}]
    death_date = datetime.date(1992, 11, 28)
    marr_date_before = datetime.date(1950, 6, 17)
    marr_date_after = datetime.date(1997, 6, 17)

    # define test methods
    def test_marr_before_death(self):
        self.assertEqual(user_story_5.marrBeforeDeath(self.test_indi, self.test_false), [])
        self.assertEqual(user_story_5.marrBeforeDeath(self.test_indi, self.test_true), ["Error US05: Marriage date in Family @F01@ occurs after death date of Neilia Hunter (@I02@)"])
    
    def test_is_marr_before_death(self):
        self.assertTrue(user_story_5.isMarrBeforeDeath(self.marr_date_before.month, self.marr_date_before.day, self.marr_date_before.year, 
                            self.death_date.month, self.death_date.day, self.death_date.year))
        self.assertFalse(user_story_5.isMarrBeforeDeath(self.marr_date_after.month, self.marr_date_after.day, self.marr_date_after.year, 
                            self.death_date.month, self.death_date.day, self.death_date.year))
