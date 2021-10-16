# Christian Kubelle - User Story 6 
# Divorce before death

import unittest
import datetime

from user_stories import user_story_6

class TestUserStory6(unittest.TestCase):

    def test_no_errors(self):
        self.assertEqual(user_story_6.divorceBeforeDeath([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I20@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(1947, 10, 7), 'age': 74, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@'}}],
            
            [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()}
            ]),
            
            [])

    def test_divorce_before_death_husband(self):
        self.assertEqual(user_story_6.divorceBeforeDeath([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I20@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(1947, 10, 7), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}}],
            
            [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()}
            ]),
            
            ["Error US06: Divorce of FAM (@F03@) occurs after death of Husband (@I20@)"])


    def test_divorce_before_death_wife(self):
        self.assertEqual(user_story_6.divorceBeforeDeath([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': datetime.date(1979, 8, 5), 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I20@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(1947, 10, 7), 'age': 74, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@'}}],
            
            [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': datetime.date(1980, 8, 5), 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()}
            ]),
            
            ["Error US06: Divorce of FAM (@F01@) occurs after death of Wife (@I03@)"])

    def test_divorce_before_death_of_both(self):
        self.assertEqual(user_story_6.divorceBeforeDeath([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': datetime.date(1979, 8, 5), 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': datetime.date(1979, 8, 5), 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I20@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(1947, 10, 7), 'age': 74, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@'}}],
            
            [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': datetime.date(1980, 8, 5), 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()}
            ]),
            
            ["Error US06: Divorce of FAM (@F01@) occurs after death of Husband (@I01@)", "Error US06: Divorce of FAM (@F01@) occurs after death of Wife (@I03@)"])