# Jeffrey Lee - User Story 30
# I pledge my honor that I have abided by the Stevens Honor System.

import unittest
import datetime

from user_stories.user_story_30 import makeLivingMarriedList, checkIfLiving, checkIfMarried

class TestUserStory30(unittest.TestCase):

    def test_no_living_married(self):
        self.assertEqual(makeLivingMarriedList(
            [
                {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 79, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
                {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
                {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F12@', '@F04@'}}
            ],
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': datetime.date(1979, 6, 17), 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1975, 8, 27), 'divorced': "NA", 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I06@', '@I04@', '@I05@'}},
            ]
        ),

            []
        )
    
    def test_living_married(self):
        self.assertEqual(makeLivingMarriedList(
        [
                {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 79, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@'}},
                {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
                {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': {'@F12@', '@F04@'}}
            ],
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': "NA", 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1975, 8, 27), 'divorced': "NA", 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I06@', '@I04@', '@I05@'}},
            ]
        ),

            [
                {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 79, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@'}},
                {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
                {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': {'@F12@', '@F04@'}}
            ]
        )   

    def test_if_living(self):
        self.assertTrue(checkIfLiving({'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 79, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}}))
        self.assertTrue(checkIfLiving({'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@'}}))
        self.assertFalse(checkIfLiving({'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}}))

    def test_if_not_living(self):
        self.assertFalse(checkIfLiving({'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}}))
        self.assertTrue(checkIfLiving({'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 79, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}}))

    def test_if_married(self):
        self.assertFalse(checkIfMarried(
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 79, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': datetime.date(1979, 6, 17), 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1975, 8, 27), 'divorced': "NA", 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I06@', '@I04@', '@I05@'}},
            ]
        ))

        self.assertTrue(checkIfMarried(
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@'}},

            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': "NA", 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1975, 8, 27), 'divorced': "NA", 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I06@', '@I04@', '@I05@'}},
            ]
        ))