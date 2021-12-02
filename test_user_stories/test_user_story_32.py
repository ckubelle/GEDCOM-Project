import unittest
import datetime

from user_stories.user_story_32 import compareDates

class TestUserStory29(unittest.TestCase):

    def test_same_day(self):
        self.assertTrue(compareDates(datetime.date(1942, 11, 20), datetime.date(1942, 11, 20)))

    def test_diff_day(self):
        self.assertFalse(compareDates(datetime.date(1945, 11, 20), datetime.date(1942, 11, 20)))

    def test_diff_day2(self):
        self.assertFalse(compareDates(datetime.date(1940, 11, 20), datetime.date(1942, 11, 20)))

    def test_diff_day4(self):
        self.assertFalse(compareDates(datetime.date(1942, 11, 22), datetime.date(1942, 11, 20)))

    def test_sim_day(self):
        self.assertTrue(compareDates(datetime.date(1942, 11, 20), datetime.date(1942, 11, 21)))

    def test_sim_day2(self):
        self.assertTrue(compareDates(datetime.date(1942, 11, 21), datetime.date(1942, 11, 20)))

        