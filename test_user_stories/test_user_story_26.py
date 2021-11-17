# Leena Domadia - User Story 26
# I pledge my Honor that I have abided by the Stevens Honor System

import unittest

from user_stories.user_story_26 import isCorrespondingChild,  isCorrespondingSpouse

class TestUserStory26(unittest.TestCase):

    def test_not_corresponding_child(self):
        self.assertFalse(isCorrespondingChild('I1', 'F1', 'F1', []))
    
    def test_different_fam_id_corresponding_child(self):
        self.assertTrue(isCorrespondingChild('I1', 'F1', 'F2', ['I1']))

    def test_is_corresponding_child(self):
        self.assertTrue(isCorrespondingChild('I1', 'F1', 'F1', ['I2', 'I1', 'I3']))

    def test_not_corresponding_spouse(self):
        self.assertFalse(isCorrespondingSpouse('I1', 'F1', 'F1', 'I2', 'I3'))
    
    def test_different_fam_id_corresponding_spouse(self):
        self.assertTrue(isCorrespondingSpouse('I1', 'F1', 'F2', 'I2', 'I1'))

    def test_is_corresponding_spouse(self):
        self.assertTrue(isCorrespondingSpouse('I1', 'F1', 'F1', 'I2', 'I1'))