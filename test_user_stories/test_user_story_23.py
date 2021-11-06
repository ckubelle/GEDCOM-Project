# Christian Kubelle - User Story 23
# Multiple names with same birthday

import unittest
import datetime

from user_stories import user_story_23

class TestUserStory23(unittest.TestCase):

    def test_no_errors(self):
        self.assertEqual(
            user_story_23.uniqueNameAndBirth(
                [
                    {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                    {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
                ]
            ),
            []
        )

    def test_same_person(self):
        self.assertEqual(
            user_story_23.uniqueNameAndBirth(
                [
                    {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                    {'id': '@I02@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                ]
            ),
            ["Error US23: Individual Joseph /Biden/ appears more than once in the GEDCOM file"]
        )

    def test_different_bday(self):
        self.assertEqual(
            user_story_23.uniqueNameAndBirth(
                [
                    {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                    {'id': '@I02@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1957, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                ]
            ),
            []
        )

    def test_multiple_people(self):
        self.assertEqual(
            user_story_23.uniqueNameAndBirth(
                [
                    {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                    {'id': '@I02@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                    {'id': '@I01@', 'name': 'Hunter /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                    {'id': '@I02@', 'name': 'Hunter /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                ]
            ),
            ["Error US23: Individual Joseph /Biden/ appears more than once in the GEDCOM file", "Error US23: Individual Hunter /Biden/ appears more than once in the GEDCOM file"]
        )
 