#Leena Domadia - Homework 4 - User Story 1
#I pledge my Honor that I have abided by the Stevens Honor System - Leena Domadia

import unittest
from datetime import date

from user_stories.user_story_1 import isValidDate

class TestUserStory1(unittest.TestCase):

    def test_date_before_currentA(self):
        self.assertTrue(isValidDate(date(2020, 3, 20)))

    def test_date_equal_current(self):
        self.assertTrue(isValidDate(date.today()))

    def test_date_after_currentA(self):
        self.assertFalse(isValidDate(date(2021, 12, 25)))

    def test_date_before_currentB(self):
        self.assertTrue(isValidDate(date(2021, 9, 26)))

    def test_date_after_currentB(self):
        self.assertFalse(isValidDate(date(2341, 1, 30)))
