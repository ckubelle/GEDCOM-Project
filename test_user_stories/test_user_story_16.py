# User Story 16 Test Class
# All males in a family should have the same last name

import unittest
import datetime
from user_stories import user_story_16

class TestUserStory16(unittest.TestCase):
  # define objects to interact with during tests
  test_true = [
        {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 11, 28), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I03@', 'name': 'James /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 52, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 52, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()}]
  test_false = [
        {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 11, 28), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F01@'}},
        {'id': '@I03@', 'name': 'James /Jacobs/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 52, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()},
        {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 52, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': set()}]
  test_fam = [
        {'id': '@F01@', 'married': datetime.date(2000, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I03@', '@I04@'}}]
  
  # define test methods
  def test_check_male_last(self):
    self.assertTrue(user_story_16.checkMaleLastNames(self.test_fam, self.test_true))
    self.assertFalse(user_story_16.checkMaleLastNames(self.test_fam, self.test_false))

  def test_is_male(self):
    self.assertTrue(user_story_16.isMale('@I01@', self.test_true))
    self.assertFalse(user_story_16.isMale('@I02@', self.test_true))
  
  def test_find_last(self):
    self.assertEqual(user_story_16.findLastName('@I01@', self.test_true), "/Biden/")
    self.assertNotEqual(user_story_16.findLastName('@I03@', self.test_false), "/Biden/")
