# Jeffrey Lee - User Story 15
# Fewer than 15 siblings
# I pledge my honor that I have abided by the Stevens Honor System.

import unittest
import datetime

from user_stories import user_story_15

class TestUserStory15(unittest.TestCase):

    def test_all_fewer_than_fifteen_siblings(self):
        self.assertEqual(user_story_15.fewerThanFifteenSiblings(
        [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
        ]),
            
        [])

    def test_one_family_each_child_have_fourteen_siblings(self):
        self.assertEqual(user_story_15.fewerThanFifteenSiblings(
        [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@', '@I03@', '@I15@', '@I12@', '@I20@', '@I21@', '@I22@', '@I23@', '@I24@', '@I25@', '@I26@', '@I27@', '@I28@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
        ]),

        [])

    def test_one_family_each_child_have_fifteen_siblings(self):
        self.assertEqual(user_story_15.fewerThanFifteenSiblings(
        [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@', '@I03@', '@I15@', '@I12@', '@I20@', '@I21@', '@I22@', '@I23@', '@I24@', '@I25@', '@I26@', '@I27@', '@I28@', '@I29@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
        ]),
            
        ["Error US15: There are 15 or more siblings in Family @F02@. There should be fewer than 15 siblings in a family."])

    def test_two_families_each_child_have_fifteen_siblings(self):
        self.assertEqual(user_story_15.fewerThanFifteenSiblings(
        [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@', '@I03@', '@I15@', '@I12@', '@I20@', '@I21@', '@I22@', '@I23@', '@I24@', '@I25@', '@I26@', '@I27@', '@I28@', '@I29@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I30@', '@I31@', '@I32@', '@I33@', '@I34@', '@I35@', '@I36@', '@I37@', '@I38@', '@I39@', '@I40@', '@I41@', '@I42@', '@I43@', '@I44@', '@I45@'}}
        ]),
            
        ["Error US15: There are 15 or more siblings in Family @F02@. There should be fewer than 15 siblings in a family.",
        "Error US15: There are 15 or more siblings in Family @F04@. There should be fewer than 15 siblings in a family."])

    def test_families_each_child_have_more_than_fifteen_siblings(self):
        self.assertEqual(user_story_15.fewerThanFifteenSiblings(
        [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I30@', '@I31@', '@I32@', '@I33@', '@I34@', '@I35@', '@I36@', '@I37@', '@I38@', '@I39@', '@I40@', '@I41@', '@I42@', '@I43@', '@I44@', '@I45@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@', '@I03@', '@I15@', '@I12@', '@I20@', '@I21@', '@I22@', '@I23@', '@I24@', '@I25@', '@I26@', '@I27@', '@I28@', '@I29@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I46@', '@I47@', '@I48@', '@I49@', '@I50@', '@I51@', '@I52@', '@I53@', '@I54@', '@I55@', '@I56@', '@I57@', '@I58@', '@I59@', '@I60@', '@I61@', '@I62@'}},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I63@', '@I64@', '@I65@', '@I66@', '@I67@', '@I68@', '@I69@', '@I70@', '@I71@', '@I72@', '@I73@', '@I74@', '@I75@', '@I76@', '@I77@', '@I78@', '@I79@', '@I80@'}}
        ]),
            
        ["Error US15: There are 15 or more siblings in Family @F01@. There should be fewer than 15 siblings in a family.",
        "Error US15: There are 15 or more siblings in Family @F02@. There should be fewer than 15 siblings in a family.",
        "Error US15: There are 15 or more siblings in Family @F03@. There should be fewer than 15 siblings in a family.",
        "Error US15: There are 15 or more siblings in Family @F04@. There should be fewer than 15 siblings in a family."])