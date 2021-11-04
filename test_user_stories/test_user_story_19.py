# Leena Domadia - User Story 19
# I pledge my Honor that I have abided by the Stevens Honor System

import unittest

from user_stories.user_story_19 import isFirstCousinsMarry

class TestUserStory19(unittest.TestCase):

    def test_first_cousins_marry(self):
        fam = {
            'husb_id': 1,
            'wife_id': 2
        }
        cousins = [1, 2]
        self.assertTrue(isFirstCousinsMarry(fam, cousins))

    def test_first_cousins_not_marry(self):
        fam = {
            'husb_id': 1,
            'wife_id': 2
        }
        cousins = [1, 3]
        self.assertFalse(isFirstCousinsMarry(fam, cousins))

    