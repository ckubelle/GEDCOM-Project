#Christian  Kubelle - User Story 4
# Divorce before marriage
#I pledge my Honor that I have abided by the Stevens Honor System - Leena Domadia

import unittest
from datetime import date

from user_stories import user_story_4

class TestUserStory3(unittest.TestCase):

    def test_divorced_before_marriageA(self):
        self.assertFalse(user_story_4.divorcedBeforeMarried('NA', date(2000, 10, 10)))

    def test_divorced_before_marriageB(self):
        self.assertTrue(user_story_4.divorcedBeforeMarried(date(1967, 10, 10), date(2000, 10, 10)))

    def test_divorced_before_marriageC(self):
        self.assertFalse(user_story_4.divorcedBeforeMarried(date(2020, 10, 10), date(2000, 10, 10)))

