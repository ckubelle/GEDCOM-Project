# Jeffrey Lee - User Story 9: Birth Before Death of Parents
# I pledge my honor that I have abided by the Stevens Honor System.

import unittest
import datetime

from user_stories import user_story_9

class TestUserStory9(unittest.TestCase):

    def test_child_born_before_mother_death(self):
        self.assertTrue(user_story_9.isbirthBeforeMotherDeath(datetime.date(1990, 5, 20), 'NA'))
        self.assertTrue(user_story_9.isbirthBeforeMotherDeath(datetime.date(1990, 5, 20), datetime.date(1990, 5, 21)))
        self.assertTrue(user_story_9.isbirthBeforeMotherDeath(datetime.date(1990, 5, 20), datetime.date(1990, 6, 10)))
        self.assertTrue(user_story_9.isbirthBeforeMotherDeath(datetime.date(1990, 5, 20), datetime.date(1991, 1, 30)))
        self.assertTrue(user_story_9.isbirthBeforeMotherDeath(datetime.date(1990, 5, 20), datetime.date(2000, 10, 2)))
        self.assertFalse(user_story_9.isbirthBeforeMotherDeath(datetime.date(1990, 5, 20), datetime.date(1990, 5, 19)))
        self.assertFalse(user_story_9.isbirthBeforeMotherDeath(datetime.date(1990, 5, 20), datetime.date(1990, 4, 19)))
        self.assertFalse(user_story_9.isbirthBeforeMotherDeath(datetime.date(1990, 5, 20), datetime.date(1989, 5, 20)))


    def test_child_born_before_father_death(self):
        self.assertTrue(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 5, 20), 'NA'))
        self.assertTrue(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 5, 20), datetime.date(1990, 5, 21)))
        self.assertTrue(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 5, 20), datetime.date(1990, 6, 10)))
        self.assertTrue(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 5, 20), datetime.date(1991, 1, 30)))
        self.assertTrue(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 5, 20), datetime.date(2000, 10, 2)))
        self.assertTrue(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 5, 20), datetime.date(1990, 5, 19)))
        self.assertTrue(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 5, 20), datetime.date(1990, 4, 20)))
        self.assertFalse(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 5, 20), datetime.date(1978, 5, 20)))

    
    def test_child_born_before_nine_months_after_father_death(self):
        self.assertTrue(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 10, 5), datetime.date(1990, 1, 6)))
        self.assertFalse(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 10, 5), datetime.date(1990, 1, 4)))
        self.assertFalse(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 10, 5), datetime.date(1990, 1, 5)))
        self.assertTrue(user_story_9.isbirthBeforeFatherDeath(datetime.date(1800, 10, 20), datetime.date(1800, 10, 20)))
        self.assertTrue(user_story_9.isbirthBeforeFatherDeath(datetime.date(1990, 5, 20), datetime.date(1990, 4, 10)))

    def test_born_after_parents_death(self):
        self.assertEqual(user_story_9.birthBeforeDeathOfParents([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(2018, 11, 28), 'age': 30, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1970, 2, 3), 'age': 46, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': {'@F04@'}}], [

            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I02@', '@I04@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            ["Error US09: Birth date of child Neilia /Hunter/ (@I02@) occurs after 9 months after death of father Joseph /Biden/ (@I01@) in family (@F01@). The birthday of child is 2018-11-28, and the death date of father is 1972-12-18.",
            "Error US09: Birth date of child Neilia /Hunter/ (@I02@) occurs after death of mother Jill /Jacobs/ (@I03@) in family (@F01@). The birthday of child is 2018-11-28, and the death date of mother is 2015-05-30."])