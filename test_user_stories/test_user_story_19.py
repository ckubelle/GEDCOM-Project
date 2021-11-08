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
        sib1 = [1, 3]
        sib2 = [2, 4]
        self.assertTrue(isFirstCousinsMarry(fam, sib1, sib2))

    def test_first_cousins_not_marry(self):
        fam = {
            'husb_id': 1,
            'wife_id': 2
        }
        sib1 = [1, 3]
        sib2 = [4, 5]
        self.assertFalse(isFirstCousinsMarry(fam, sib1, sib2))

    