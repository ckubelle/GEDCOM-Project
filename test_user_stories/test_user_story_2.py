# Jeffrey Lee - User Story 2
# Birth Before Marriage
# I pledge my honor that I have abided by the Stevens Honor System.

import unittest
import datetime

from user_stories import user_story_2

class TestUserStory2(unittest.TestCase):

    def test_birth_before_marriage(self):
        self.assertEqual(user_story_2.birthBeforeMarriage([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}], [

            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            [])

    def test_birth_after_marriage(self):
        self.assertEqual(user_story_2.birthBeforeMarriage([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}], [

            {'id': '@F01@', 'married': datetime.date(1900, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            ["Error US02: Birth date of Joseph Biden (@I01@) occurs after marriage date in Family @F01@",
            "Error US02: Birth date of Jill Jacobs (@I03@) occurs after marriage date in Family @F01@"])

    def test_birth_after_marriage_two_families(self):
        self.assertEqual(user_story_2.birthBeforeMarriage([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}], [

            {'id': '@F01@', 'married': datetime.date(1900, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1901, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            ["Error US02: Birth date of Joseph Biden (@I01@) occurs after marriage date in Family @F01@",
            "Error US02: Birth date of Jill Jacobs (@I03@) occurs after marriage date in Family @F01@",
            "Error US02: Birth date of Joseph Biden (@I01@) occurs after marriage date in Family @F02@",
            "Error US02: Birth date of Neilia Hunter (@I02@) occurs after marriage date in Family @F02@"])
    
    def test_isBirthBeforeMarr_method_true_yr(self):
        self.assertTrue(user_story_2.isBirthBeforeMarr(10, 1, 1970, 1, 20, 2000))

    def test_isBirthBeforeMarr_method_true_month(self):
        self.assertTrue(user_story_2.isBirthBeforeMarr(10, 1, 1970, 11, 1, 1970))
    
    def test_isBirthBeforeMarr_method_true_day(self):
        self.assertTrue(user_story_2.isBirthBeforeMarr(1, 19, 2000, 1, 20, 2000))

    def test_isBirthBeforeMarr_method_false_yr(self):
        self.assertFalse(user_story_2.isBirthBeforeMarr(10, 1, 2000, 1, 20, 1980))

    def test_isBirthBeforeMarr_method_false_month(self):
        self.assertFalse(user_story_2.isBirthBeforeMarr(10, 1, 2000, 1, 20, 2000))
    
    def test_isBirthBeforeMarr_method_false_day(self):
        self.assertFalse(user_story_2.isBirthBeforeMarr(10, 2, 2000, 10, 1, 2000))

