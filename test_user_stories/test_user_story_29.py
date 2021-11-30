import unittest
import datetime

from user_stories.user_story_29 import makeDeceasedList

class TestUserStory29(unittest.TestCase):

    def test_no_deceased(self):
        self.assertEqual(makeDeceasedList(
            [
                {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 79, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': True, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
                {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
                {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': True, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F12@', '@F04@'}}
            ]

        ),

            []
        )

    def test_deceased(self):
        self.assertEqual(makeDeceasedList(
            [
                {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 79, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': True, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
                {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': False, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
                {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F12@', '@F04@'}}
            ]

        ),

            [   
                {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': False, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
                {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F12@', '@F04@'}}
            ]
        )