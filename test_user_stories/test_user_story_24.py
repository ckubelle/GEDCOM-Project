# Leena Domadia - User Story 24
# I pledge my Honor that I have abided by the Stevens Honor System

import unittest

from user_stories.user_story_24 import isSameFamily

class TestUserStory24(unittest.TestCase):

    def test_same_husb(self):
        self.assertFalse(isSameFamily("Bob", "Amy", "11-17-1972", "Bob", "Linda", "11-29-1978"))

    def test_same_wife(self):
        self.assertFalse(isSameFamily("Bob", "Amy", "11-17-1972", "Jeff", "Amy", "11-29-1978"))

    def test_same_husb_and_wife(self):
        self.assertFalse(isSameFamily("Bob", "Amy", "11-17-1972", "Bob", "Amy", "11-29-1978"))

    def test_same_everything(self):
        self.assertTrue(isSameFamily("Bob", "Amy", "11-17-1972", "Bob", "Amy", "11-17-1972"))