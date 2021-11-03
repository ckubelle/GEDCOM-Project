# Jeffrey Lee - User Story 18
# Siblings should not marry

import unittest
import datetime

from user_stories import user_story_18

class TestUserStory18(unittest.TestCase):

    def test_siblings_not_married(self):
        self.assertEqual(user_story_18.siblingsNotMarried([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}, 
            {'id': '@I05@', 'name': 'Hunter /Biden/', 'gender': 'M', 'birthday': datetime.date(1939, 2, 4), 'age': 82, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': {'@F05@', '@F06@', '@F07@'}}, 
            {'id': '@I06@', 'name': 'Naomi /Biden/', 'gender': 'F', 'birthday': datetime.date(1973, 11, 8), 'age': 0, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': {'@F02@'}, 'spouse': set()}, 
            {'id': '@I07@', 'name': 'Ashley /Biden/', 'gender': 'F', 'birthday': datetime.date(1981, 6, 8), 'age': 40, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': {'@F08@'}}, 
            {'id': '@I10@', 'name': 'Natalie /Biden/', 'gender': 'F', 'birthday': datetime.date(2015, 10, 4), 'age': 6, 'alive': True, 'death': 'NA', 'child': {'@F04@'}, 'spouse': set()}, 
            {'id': '@I11@', 'name': 'Robert /Biden/', 'gender': 'M', 'birthday': datetime.date(2016, 3, 10), 'age': 5, 'alive': True, 'death': 'NA', 'child': {'@F04@'}, 'spouse': set()}
            ],
            [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            [])

    def test_siblings_married(self):
        self.assertEqual(user_story_18.siblingsNotMarried([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}, 
            {'id': '@I05@', 'name': 'Hunter /Biden/', 'gender': 'M', 'birthday': datetime.date(1939, 2, 4), 'age': 82, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': {'@F05@', '@F06@', '@F07@'}}, 
            {'id': '@I06@', 'name': 'Naomi /Biden/', 'gender': 'F', 'birthday': datetime.date(1973, 11, 8), 'age': 0, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': {'@F02@'}, 'spouse': set()}, 
            {'id': '@I07@', 'name': 'Ashley /Biden/', 'gender': 'F', 'birthday': datetime.date(1981, 6, 8), 'age': 40, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': {'@F08@'}}, 
            {'id': '@I10@', 'name': 'Natalie /Biden/', 'gender': 'F', 'birthday': datetime.date(2015, 10, 4), 'age': 6, 'alive': True, 'death': 'NA', 'child': {'@F04@'}, 'spouse': set()}, 
            {'id': '@I11@', 'name': 'Robert /Biden/', 'gender': 'M', 'birthday': datetime.date(2016, 3, 10), 'age': 5, 'alive': True, 'death': 'NA', 'child': {'@F04@'}, 'spouse': set()}
            ],
            [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F05@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I11@', 'husb_name': 'Robert /Biden/', 'wife_id': '@I10@', 'wife_name': 'Natalie /Biden/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            [
                "Error US18: Natalie /Biden/ (@I10@) should not be married to her sibling Robert /Biden/ (@I11@) in Family @F05@. These two people are siblings in Family @F04@.",
                "Error US18: Robert /Biden/ (@I11@) should not be married to his sibling Natalie /Biden/ (@I10@) in Family @F05@. These two people are siblings in Family @F04@."
            ])

    def test_siblings_married_second(self):
        self.assertEqual(user_story_18.siblingsNotMarried([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}, 
            {'id': '@I05@', 'name': 'Hunter /Biden/', 'gender': 'M', 'birthday': datetime.date(1939, 2, 4), 'age': 82, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': {'@F05@', '@F06@', '@F07@'}}, 
            {'id': '@I06@', 'name': 'Naomi /Biden/', 'gender': 'F', 'birthday': datetime.date(1973, 11, 8), 'age': 0, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': {'@F02@'}, 'spouse': set()}, 
            {'id': '@I07@', 'name': 'Ashley /Biden/', 'gender': 'F', 'birthday': datetime.date(1981, 6, 8), 'age': 40, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': {'@F08@'}}, 
            {'id': '@I10@', 'name': 'Natalie /Biden/', 'gender': 'F', 'birthday': datetime.date(2015, 10, 4), 'age': 6, 'alive': True, 'death': 'NA', 'child': {'@F04@'}, 'spouse': set()}, 
            {'id': '@I11@', 'name': 'Robert /Biden/', 'gender': 'M', 'birthday': datetime.date(2016, 3, 10), 'age': 5, 'alive': True, 'death': 'NA', 'child': {'@F04@'}, 'spouse': set()}
            ],
            [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F05@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I10@', 'husb_name': 'Natalie /Biden/', 'wife_id': '@I11@', 'wife_name': 'Robert /Biden/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            [
                "Error US18: Natalie /Biden/ (@I10@) should not be married to his sibling Robert /Biden/ (@I11@) in Family @F05@. These two people are siblings in Family @F04@.",
                "Error US18: Robert /Biden/ (@I11@) should not be married to her sibling Natalie /Biden/ (@I10@) in Family @F05@. These two people are siblings in Family @F04@."
            ])

    def test_siblings_married_from_different_families(self):
        self.assertEqual(user_story_18.siblingsNotMarried([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}, 
            {'id': '@I05@', 'name': 'Hunter /Biden/', 'gender': 'M', 'birthday': datetime.date(1939, 2, 4), 'age': 82, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': {'@F05@', '@F06@', '@F07@'}}, 
            {'id': '@I06@', 'name': 'Naomi /Biden/', 'gender': 'F', 'birthday': datetime.date(1973, 11, 8), 'age': 0, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': {'@F02@'}, 'spouse': set()}, 
            {'id': '@I07@', 'name': 'Ashley /Biden/', 'gender': 'F', 'birthday': datetime.date(1981, 6, 8), 'age': 40, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': {'@F08@'}}, 
            {'id': '@I10@', 'name': 'Natalie /Biden/', 'gender': 'F', 'birthday': datetime.date(2015, 10, 4), 'age': 6, 'alive': True, 'death': 'NA', 'child': {'@F04@'}, 'spouse': set()}, 
            {'id': '@I11@', 'name': 'Robert /Biden/', 'gender': 'M', 'birthday': datetime.date(2016, 3, 10), 'age': 5, 'alive': True, 'death': 'NA', 'child': {'@F04@'}, 'spouse': set()}
            ],
            [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F05@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I11@', 'husb_name': 'Robert /Biden/', 'wife_id': '@I10@', 'wife_name': 'Natalie /Biden/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}},
            {'id': '@F06@', 'married': datetime.date(2002, 10, 23), 'divorced': 'NA', 'husb_id': '@I05@', 'husb_name': 'Hunter /Biden/', 'wife_id': '@I06@', 'wife_name': 'Naomi /Biden/', 'children': {'@I20@', '@I21@'}},
            ]),
            
            [
                "Error US18: Hunter /Biden/ (@I05@) should not be married to his sibling Naomi /Biden/ (@I06@) in Family @F06@. These two people are siblings in Family @F02@.",
                "Error US18: Naomi /Biden/ (@I06@) should not be married to her sibling Hunter /Biden/ (@I05@) in Family @F06@. These two people are siblings in Family @F02@.",
                "Error US18: Natalie /Biden/ (@I10@) should not be married to her sibling Robert /Biden/ (@I11@) in Family @F05@. These two people are siblings in Family @F04@.",
                "Error US18: Robert /Biden/ (@I11@) should not be married to his sibling Natalie /Biden/ (@I10@) in Family @F05@. These two people are siblings in Family @F04@."
            ])

    def test_mutliple_siblings_married_from_same_family(self):
        self.assertEqual(user_story_18.siblingsNotMarried([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}, 
            {'id': '@I05@', 'name': 'Hunter /Biden/', 'gender': 'M', 'birthday': datetime.date(1939, 2, 4), 'age': 82, 'alive': True, 'death': 'NA', 'child': {'@F02@'}, 'spouse': {'@F05@', '@F06@', '@F07@'}}, 
            {'id': '@I06@', 'name': 'Naomi /Biden/', 'gender': 'F', 'birthday': datetime.date(1973, 11, 8), 'age': 0, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': {'@F02@'}, 'spouse': set()}, 
            {'id': '@I07@', 'name': 'Ashley /Biden/', 'gender': 'F', 'birthday': datetime.date(1981, 6, 8), 'age': 40, 'alive': True, 'death': 'NA', 'child': {'@F01@'}, 'spouse': {'@F08@'}}, 
            {'id': '@I10@', 'name': 'Natalie /Biden/', 'gender': 'F', 'birthday': datetime.date(2015, 10, 4), 'age': 6, 'alive': True, 'death': 'NA', 'child': {'@F04@'}, 'spouse': set()}, 
            {'id': '@I11@', 'name': 'Robert /Biden/', 'gender': 'M', 'birthday': datetime.date(2016, 3, 10), 'age': 5, 'alive': True, 'death': 'NA', 'child': {'@F04@'}, 'spouse': set()}
            ],
            [
            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F05@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I11@', 'husb_name': 'Robert /Biden/', 'wife_id': '@I10@', 'wife_name': 'Natalie /Biden/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}},
            {'id': '@F06@', 'married': datetime.date(2002, 10, 23), 'divorced': 'NA', 'husb_id': '@I05@', 'husb_name': 'Hunter /Biden/', 'wife_id': '@I06@', 'wife_name': 'Naomi /Biden/', 'children': {'@I20@', '@I21@'}},
            {'id': '@F07@', 'married': datetime.date(2002, 10, 23), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I06@', 'wife_name': 'Naomi /Biden/', 'children': {'@I22@', '@I21@'}},
            ]),
            
            [
                "Error US18: Beau /Biden/ (@I04@) should not be married to his sibling Naomi /Biden/ (@I06@) in Family @F07@. These two people are siblings in Family @F02@.",
                "Error US18: Hunter /Biden/ (@I05@) should not be married to his sibling Naomi /Biden/ (@I06@) in Family @F06@. These two people are siblings in Family @F02@.",
                "Error US18: Naomi /Biden/ (@I06@) should not be married to her sibling Beau /Biden/ (@I04@) in Family @F07@. These two people are siblings in Family @F02@.",
                "Error US18: Naomi /Biden/ (@I06@) should not be married to her sibling Hunter /Biden/ (@I05@) in Family @F06@. These two people are siblings in Family @F02@.",
                "Error US18: Natalie /Biden/ (@I10@) should not be married to her sibling Robert /Biden/ (@I11@) in Family @F05@. These two people are siblings in Family @F04@.",
                "Error US18: Robert /Biden/ (@I11@) should not be married to his sibling Natalie /Biden/ (@I10@) in Family @F05@. These two people are siblings in Family @F04@."
            ])