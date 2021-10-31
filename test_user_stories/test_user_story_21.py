# Leena Domadia - User Story 21
# I pledge my Honor that I have abided by the Stevens Honor System

import unittest

from user_stories.user_story_21 import isCorrectGenderWife,  isCorrectGenderHusb

class TestUserStory21(unittest.TestCase):

    def test_husb_true(self):
        self.assertTrue(isCorrectGenderHusb("M"))

    def test_husb_false(self):
        self.assertFalse(isCorrectGenderHusb("F"))
    
    def test_wife_true(self):
        self.assertTrue(isCorrectGenderWife("F"))

    def test_wife_false(self):
        self.assertFalse(isCorrectGenderWife("M"))