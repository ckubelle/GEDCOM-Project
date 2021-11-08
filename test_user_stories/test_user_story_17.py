# User Story 17: No marriages to descendants

import unittest
import datetime

from user_stories import user_story_17

class TestUserStory17(unittest.TestCase):

    def test_no_marriages_to_descendants(self):
        self.assertEqual(user_story_17.getDescendants(
            "@I09@",
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
                {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
                {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ],
            set()),

            {'@I11@', '@I10@'})

        self.assertEqual(user_story_17.parentsMarriedToDescendants(
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
                {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
                {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]
        ),
        [])

    def test_one_marriage_to_child(self):
        self.assertEqual(user_story_17.getDescendants(
            "@I01@",
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I05@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@'}},
                {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I05@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
                {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ],
            set()),

            {'@I07@','@I05@'})

        self.assertEqual(user_story_17.parentsMarriedToDescendants(
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I05@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@'}},
                {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I05@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
                {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]
        ),
        ["Error US17: Joseph /Biden/ (@I01@) is married to his descendant Jill /Jacobs/ (@I05@) in Family @F01@."])    

        self.assertEqual(user_story_17.parentsMarriedToDescendants(
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I05@', 'husb_name': 'Jill /Jacobs/', 'wife_id': '@I01@', 'wife_name': 'Joseph /Biden/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I02@', 'husb_name': 'Neilla /Hunter/', 'wife_id': '@I01@', 'wife_name': 'Joseph /Biden/', 'children': {'@I05@'}},
                {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I05@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
                {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]
        ),
        ["Error US17: Joseph /Biden/ (@I01@) is married to her descendant Jill /Jacobs/ (@I05@) in Family @F01@."]) 

    def test_marriage_to_grandson(self):
        self.assertEqual(user_story_17.getDescendants(
            "@I01@",
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I11@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
                {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I05@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I08@'}},
                {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ],
            set()),

            {'@I07@','@I05@', '@I06@', '@I04@', '@I08@', '@I11@', '@I10@'})

        self.assertEqual(user_story_17.parentsMarriedToDescendants(
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I11@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
                {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I05@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I08@'}},
                {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]
        ),
        ["Error US17: Joseph /Biden/ (@I01@) is married to his descendant Jill /Jacobs/ (@I11@) in Family @F01@."])

    def test_multiple_marriages_to_descendants(self):
        self.assertEqual(user_story_17.getDescendants(
            "@I01@",
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I41@', '@I04@'}},
                {'id': '@F03@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I10@', 'husb_name': 'Biden /Biden/', 'wife_id': '@I04@', 'wife_name': 'Amanda /Smith/', 'children': {'@I08@'}},
                {'id': '@F04@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I08@', 'husb_name': 'Jeremy /Biden/', 'wife_id': '@I05@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I90@'}},
                {'id': '@F05@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I90@', 'wife_name': 'Rachel /Hunter/', 'children': set()},

                {'id': '@F06@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I30@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I31@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I100@', '@I33@'}},
                {'id': '@F07@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I32@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I33@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I111@', '@I110@'}},
                {'id': '@F08@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I30@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I110@', 'wife_name': 'Haley /Brown/', 'children': set()}
            ],
            set()),

            {'@I07@','@I41@', '@I04@', '@I08@', '@I90@'})

        self.assertEqual(user_story_17.getDescendants(
            "@I30@",
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I41@', '@I04@'}},
                {'id': '@F03@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I10@', 'husb_name': 'Biden /Biden/', 'wife_id': '@I04@', 'wife_name': 'Amanda /Smith/', 'children': {'@I08@'}},
                {'id': '@F04@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I08@', 'husb_name': 'Jeremy /Biden/', 'wife_id': '@I05@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I90@'}},
                {'id': '@F05@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I90@', 'wife_name': 'Rachel /Hunter/', 'children': set()},

                {'id': '@F06@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I30@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I31@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I100@', '@I33@'}},
                {'id': '@F07@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I32@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I33@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I111@', '@I110@'}},
                {'id': '@F08@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I30@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I110@', 'wife_name': 'Haley /Brown/', 'children': set()}
            ],
            set()),

            {'@I100@', '@I33@', '@I111@', '@I110@'})


        self.assertEqual(user_story_17.parentsMarriedToDescendants(
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I41@', '@I04@'}},
                {'id': '@F03@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I10@', 'husb_name': 'Biden /Biden/', 'wife_id': '@I04@', 'wife_name': 'Amanda /Smith/', 'children': {'@I08@'}},
                {'id': '@F04@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I08@', 'husb_name': 'Jeremy /Biden/', 'wife_id': '@I05@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I90@'}},
                {'id': '@F05@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I90@', 'wife_name': 'Rachel /Hunter/', 'children': set()},

                {'id': '@F06@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I30@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I31@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I100@', '@I33@'}},
                {'id': '@F07@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I32@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I33@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I111@', '@I110@'}},
                {'id': '@F08@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I30@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I110@', 'wife_name': 'Haley /Brown/', 'children': set()},
                {'id': '@F09@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I100@', 'husb_name': 'Bob /Brown/', 'wife_id': '@I31@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
                {'id': '@F10@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I30@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I33@', 'wife_name': 'Hallie /Olivere/', 'children': set()},
            ]
        ),
        ["Error US17: Joseph /Biden/ (@I01@) is married to his descendant Rachel /Hunter/ (@I90@) in Family @F05@.",
        "Error US17: Bill /Stevenson/ (@I30@) is married to his descendant Haley /Brown/ (@I110@) in Family @F08@.",
        "Error US17: Jill /Jacobs/ (@I31@) is married to her descendant Bob /Brown/ (@I100@) in Family @F09@.",
        "Error US17: Bill /Stevenson/ (@I30@) is married to his descendant Hallie /Olivere/ (@I33@) in Family @F10@."])

        self.assertNotEqual(user_story_17.parentsMarriedToDescendants(
            [
                {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
                {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I41@', '@I04@'}},
                {'id': '@F03@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I10@', 'husb_name': 'Biden /Biden/', 'wife_id': '@I04@', 'wife_name': 'Amanda /Smith/', 'children': {'@I08@'}},
                {'id': '@F04@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I08@', 'husb_name': 'Jeremy /Biden/', 'wife_id': '@I05@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I90@'}},
                {'id': '@F05@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I90@', 'wife_name': 'Rachel /Hunter/', 'children': set()},

                {'id': '@F06@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I30@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I31@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I100@', '@I33@'}},
                {'id': '@F07@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I32@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I33@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I111@', '@I110@'}},
                {'id': '@F08@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I30@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I110@', 'wife_name': 'Haley /Brown/', 'children': set()},
                {'id': '@F09@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I100@', 'husb_name': 'Bob /Brown/', 'wife_id': '@I31@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
                {'id': '@F10@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I30@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I33@', 'wife_name': 'Hallie /Olivere/', 'children': set()},
            ]
        ),
        ["Error US17: Joseph /Biden/ (@I01@) is married to his descendant Rachel /Hunter/ (@I90@) in Family @F05@.",
        "Error US17: Bill /Stevenson/ (@I30@) is married to his descendant Haley /Brown/ (@I110@) in Family @F08@.",
        "Error US17: Jill /Jacobs/ (@I31@) is married to her descendant Bob /Brown/ (@I100@) in Family @F09@.",
        "Error US17: Bill /Stevenson/ (@I30@) is married to his descendant Hallie /Olivere/ (@I33@) in Family @F10@.",
        "Error US17: Bill /Stevenson/ (@I30@) is married to his descendant Ike /Smith/ (@I01@) in Family @F12@."])