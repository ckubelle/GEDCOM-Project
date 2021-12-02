# User Story 27 Test Class
# Include person's current age when listing individuals

import unittest
from datetime import date
from user_stories import user_story_27

class TestUserStory27(unittest.TestCase):
    # create test objects to interact with
    test_indi = [
        {'id': '@I01@', 'name': 'Jim /Biden/', 'gender': 'M', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I02@', 'name': 'Kim /Hunter/', 'gender': 'F', 'birthday': "NA", 'age': 59, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I03@', 'name': 'Tim /Biden/', 'gender': 'M', 'birthday': date(1999, 2, 3), 'age': "NA", 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': set()}]
    test_true = {'id': '@I01@', 'name': 'Jim /Biden/', 'gender': 'M', 'birthday': date(1930, 2, 20), 'age': 91, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()}
    test_date = {'id': '@I02@', 'name': 'Kim /Hunter/', 'gender': 'F', 'birthday': "NA", 'age': 59, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()}
    test_age = {'id': '@I03@', 'name': 'Tim /Biden/', 'gender': 'M', 'birthday': date(1999, 2, 3), 'age': "NA", 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': set()}
 
    def test_check_Include_Age(self):
        self.assertTrue(user_story_27.checkIncludeAge(self.test_indi, self.test_true))
        self.assertFalse(user_story_27.checkIncludeAge(self.test_indi, self.test_date))
        self.assertFalse(user_story_27.checkIncludeAge(self.test_indi, self.test_age))
        
