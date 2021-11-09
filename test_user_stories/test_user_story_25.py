# Christian Kubelle - User Story 25
# Multiple names with same birthday in the same family

import unittest
import datetime

from user_stories import user_story_25

class TestUserStory25(unittest.TestCase):

    def test_no_errors(self):
        self.assertEqual(
            user_story_25.uniqueNameAndBirthInFam(
                [
                    {'id': '@I05@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                    {'id': '@I07@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
                ],
                [
                    {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I05@', '@I07@'}},
                ]
            ),
            []
        )

    def test_same_person(self):
        self.assertEqual(
            user_story_25.uniqueNameAndBirthInFam(
                [
                    {'id': '@I05@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                    {'id': '@I07@', 'name': 'Joseph /Biden/', 'gender': 'F', 'birthday': datetime.date(1942, 11, 20), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
                ],
                [
                    {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I05@', '@I07@'}},
                ]
            ),
            ["Error US25: Individual Joseph /Biden/ appears more than once in the same family"]
        )

    def test_mul_fam(self):
        self.assertEqual(
            user_story_25.uniqueNameAndBirthInFam(
                [
                    {'id': '@I05@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                    {'id': '@I07@', 'name': 'Joseph /Biden/', 'gender': 'F', 'birthday': datetime.date(1942, 11, 20), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
                    {'id': '@I10@', 'name': 'Hunter /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
                    {'id': '@I11@', 'name': 'Hunter /Biden/', 'gender': 'F', 'birthday': datetime.date(1942, 11, 20), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
                ],
                [
                    {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I05@', '@I07@'}},
                    {'id': '@F02@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I10@', '@I11@'}},
                ]
            ),
            ["Error US25: Individual Joseph /Biden/ appears more than once in the same family", "Error US25: Individual Hunter /Biden/ appears more than once in the same family"]
        )

