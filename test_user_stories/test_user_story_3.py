#Leena Domadia - User Story 3
# Birth before death
#I pledge my Honor that I have abided by the Stevens Honor System - Leena Domadia

import unittest
from datetime import date

from user_stories import user_story_3

class TestUserStory3(unittest.TestCase):

    def test_birth_before_deathA(self):
        self.assertTrue(user_story_3.isBirthBeforeDeath(date(2000, 1, 16), "NA"))

    def test_birth_before_deathB(self):
        self.assertTrue(user_story_3.isBirthBeforeDeath(date(2000, 1, 16), date(2021, 3, 10)))

    def test_birth_before_deathC(self):
        self.assertFalse(user_story_3.isBirthBeforeDeath(date(2021, 1, 16), date(2000, 1, 3)))

    def test_string_sort(self):
        self.assertGreater("I10", "I1")
