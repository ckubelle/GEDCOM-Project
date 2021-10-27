# Leena Domadia - User Story 7 TEST
# I pledge my Honor that I have abided by the Stevens Honor System

import unittest
from datetime import date
from dateutil.relativedelta import relativedelta

from user_stories.user_story_7 import isTooOld

class TestUserStory7(unittest.TestCase):

    def test_is_too_old(self):
        self.assertTrue(isTooOld(date(1850, 1, 1)))

    def test_is_not_too_old(self):
        self.assertFalse(isTooOld(date(1980, 1, 1)))