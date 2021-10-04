#Christian  Kubelle - User Story 8
# Birth before marriage of parents
#I pledge my Honor that I have abided by the Stevens Honor System - Christian Kubelle

import unittest
from datetime import date

from user_stories import user_story_8

class TestUserStory8(unittest.TestCase):

    def test_birth_before_marriage_of_parentsA(self):
        self.assertTrue(user_story_8.birthBeforeMarriageCheck(date(1967, 10, 10), 'NA', date(2000, 10, 10)))

    def test_birth_before_marriage_of_parentsB(self):
        self.assertTrue(user_story_8.birthBeforeMarriageCheck(date(1967, 10, 10), date(1980, 10, 10), 'NA'))

    def test_birth_before_marriage_of_parentsC(self):
        self.assertFalse(user_story_8.birthBeforeMarriageCheck(date(1967, 10, 10), date(1950, 10, 10), 'NA'))

    def test_birth_before_marriage_of_parentsD(self):
        self.assertTrue(user_story_8.birthBeforeMarriageCheck(date(1967, 10, 10), date(1950, 10, 10), date(1967, 1, 9)))

    def test_birth_before_marriage_of_parentsE(self):
        self.assertFalse(user_story_8.birthBeforeMarriageCheck(date(1967, 10, 10), date(1950, 10, 10), date(1967, 1, 11)))

    def test_birth_before_marriage_of_parentsF(self):
                self.assertFalse(user_story_8.birthBeforeMarriageCheck(date(1967, 10, 10), date(1950, 10, 10), date(1970,10,10)))