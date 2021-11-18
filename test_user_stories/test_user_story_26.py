# Leena Domadia - User Story 26
# I pledge my Honor that I have abided by the Stevens Honor System

import unittest

from user_stories.user_story_26 import isChildInFamChildren, isFamInIndiChild, isSpouseInFam, isFamInIndiSpouse

class TestUserStory26(unittest.TestCase):

    def test_is_child_in_fam_children(self):
        self.assertTrue(isChildInFamChildren('I1', ['I2', 'I1', 'I3']))

    def test_is_not_child_in_fam_children(self):
        self.assertFalse(isChildInFamChildren('I4', ['I2', 'I1', 'I3']))

    def test_is_fam_in_indi_child(self):
        self.assertTrue(isFamInIndiChild('F1', {'F1'}))

    def test_is_not_fam_in_indi_child(self):
        self.assertFalse(isFamInIndiChild('F1', {'F2'}))

    def test_is_spouse_in_fam(self):
        self.assertTrue(isSpouseInFam('I1', 'I1', 'I2'))

    def test_is_not_spouse_in_fam(self):
        self.assertFalse(isSpouseInFam('I1', 'I3', 'I2'))

    def test_is_fam_in_indi_spouse(self):
        self.assertTrue(isFamInIndiChild('F1', {'F1', 'F2', 'F3'}))

    def test_is_not_fam_in_indi_spouse(self):
        self.assertFalse(isFamInIndiChild('F1', {'F2', 'F3', 'F4'}))