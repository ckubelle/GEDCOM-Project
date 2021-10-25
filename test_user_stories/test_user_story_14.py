# Christian Kubelle - User Story 14
# Multiple births

import unittest
import datetime

from user_stories import user_story_14

class TestUserStory14(unittest.TestCase):

    def test_not_enough_siblings(self):
        self.assertEqual(user_story_14.multipleBirths([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I20@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(1947, 10, 7), 'age': 74, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@'}}],
            
            [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()}
            ]),
            
            [])

    def test_enough_siblings_nothing_wrong(self):
        self.assertEqual(user_story_14.multipleBirths([
            {'id': '@I23@', 'name': 'Chris /Biden/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I20@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(2003, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I27@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2004, 10, 7), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I22@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2005, 10, 7), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I26@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2006, 10, 7), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I32@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2007, 10, 7), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}}],
            [
            {'id': '@F05@', 'married': datetime.date(2019, 5, 16), 'divorced':'NA', 'husb_id': '@I05@', 'husb_name': 'Hunter /Biden/', 'wife_id': '@I18@', 'wife_name': 'Melissa /Cohen/', 'children': {'@I23@', '@I20@', '@I27@', '@I22@', '@I26@', '@I32@'}}
            ]),
            
            [])


    def test_not_enough_siblings_but_born_at_same_time(self):
        self.assertEqual(user_story_14.multipleBirths([
            {'id': '@I23@', 'name': 'Chris /Biden/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I20@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(2003, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I26@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2006, 10, 7), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I32@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2007, 10, 7), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}}],
            [
            {'id': '@F05@', 'married': datetime.date(2019, 5, 16), 'divorced':'NA', 'husb_id': '@I05@', 'husb_name': 'Hunter /Biden/', 'wife_id': '@I18@', 'wife_name': 'Melissa /Cohen/', 'children': {'@I23@', '@I20@', '@I27@', '@I22@', '@I26@', '@I32@'}}
            ]),
            
            [])

    def test_enough_siblings_born_at_same_time(self):
        self.assertEqual(user_story_14.multipleBirths(
            [
            {'id': '@I23@', 'name': 'Chris /Biden/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 2), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I20@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(2002, 11, 2), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I27@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 2), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I22@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 2), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I26@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 2), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I32@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 2), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}}],
            [
            {'id': '@F05@', 'married': datetime.date(2019, 5, 16), 'divorced':'NA', 'husb_id': '@I05@', 'husb_name': 'Hunter /Biden/', 'wife_id': '@I18@', 'wife_name': 'Melissa /Cohen/', 'children': {'@I23@', '@I20@', '@I27@', '@I22@', '@I26@', '@I32@'}}
            ]),
            
            ["Error US14: Family (@F05@) has more than five siblings born at the same time"])

    def test_enough_siblings_born_at_same_time2(self):
        self.assertEqual(user_story_14.multipleBirths(
            [
            {'id': '@I23@', 'name': 'Chris /Biden/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 2), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I20@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(2002, 11, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I27@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 4), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I22@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 5), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I26@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 6), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I32@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 7), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}}],
            [
            {'id': '@F05@', 'married': datetime.date(2019, 5, 16), 'divorced':'NA', 'husb_id': '@I05@', 'husb_name': 'Hunter /Biden/', 'wife_id': '@I18@', 'wife_name': 'Melissa /Cohen/', 'children': {'@I23@', '@I20@', '@I27@', '@I22@', '@I26@', '@I32@'}}
            ]),
            
            ["Error US14: Family (@F05@) has more than five siblings born at the same time"])

    def test_enough_siblings_born_at_same_time(self):
        self.assertEqual(user_story_14.multipleBirths(
            [
            {'id': '@I23@', 'name': 'Chris /Biden/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 2), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I20@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(2002, 11, 2), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I27@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 2), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I22@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 2), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I26@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 2), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}},
            {'id': '@I32@', 'name': 'Bill /Stevenson/', 'gender': 'M', 'birthday': datetime.date(2002, 11, 2), 'age': 74, 'alive': True, 'death': datetime.date(1970, 11, 20), 'child': set(), 'spouse': {'@F03@'}}],
            [
            {'id': '@F05@', 'married': datetime.date(2019, 5, 16), 'divorced':'NA', 'husb_id': '@I05@', 'husb_name': 'Hunter /Biden/', 'wife_id': '@I18@', 'wife_name': 'Melissa /Cohen/', 'children': {'@I23@', '@I20@', '@I27@', '@I22@', '@I26@', '@I32@'}},
            {'id': '@F06@', 'married': datetime.date(2019, 5, 16), 'divorced':'NA', 'husb_id': '@I05@', 'husb_name': 'Hunter /Biden/', 'wife_id': '@I18@', 'wife_name': 'Melissa /Cohen/', 'children': {'@I23@', '@I20@', '@I27@', '@I22@', '@I26@', '@I32@'}}
            ]),
            
            ["Error US14: Family (@F05@) has more than five siblings born at the same time", "Error US14: Family (@F06@) has more than five siblings born at the same time"])