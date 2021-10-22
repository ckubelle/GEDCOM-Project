# Leena Domadia - User Story 13 TEST
# I pledge my Honor that I have abided by the Stevens Honor System

import unittest
from datetime import date

from user_stories.user_story_13 import isCorrectSibilingSpacing

class TestUserStory13(unittest.TestCase):
    
    def test_if_twins(self):
        self.assertTrue(isCorrectSibilingSpacing(date(2021, 1, 1), date(2021, 1, 2)))

    def test_if_twins_reverse(self):
        self.assertTrue(isCorrectSibilingSpacing(date(2021, 1, 2), date(2021, 1, 1)))

    def test_not_enough_space(self):
        self.assertFalse(isCorrectSibilingSpacing(date(2021, 1, 1), date(2021, 8, 2)))

    def test_not_enough_space_reverse(self):
        self.assertFalse(isCorrectSibilingSpacing(date(2021, 8, 2), date(2021, 1, 1)))

    def test_not_enough_space2(self):
        self.assertFalse(isCorrectSibilingSpacing(date(2021, 1, 1), date(2021, 9, 1)))

    def test_not_enough_space_reverse2(self):
        self.assertFalse(isCorrectSibilingSpacing(date(2021, 9, 1), date(2021, 1, 1)))

    def test_enough_space(self):
        self.assertTrue(isCorrectSibilingSpacing(date(2021, 1, 1), date(2021, 9, 2)))

    def test_enough_space_reverse(self):
        self.assertTrue(isCorrectSibilingSpacing(date(2021, 9, 2), date(2021, 1, 1)))