# Jeffrey Lee - User Story 22
# Unique IDs
# I pledge my honor that I have abided by the Stevens Honor System.

import unittest
import datetime

from user_stories import user_story_22

class TestUserStory22(unittest.TestCase):

    def test_all_unique_ids(self):
        self.assertEqual(user_story_22.uniqueIds([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}], [

            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            [])
    
    def test_duplicate_individual_ids(self):
        self.assertEqual(user_story_22.uniqueIds([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I01@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}], [

            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F04@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            ["Error US22: Joseph Biden, Neilia Hunter all have the same individual ID (@I01@)."])


    def test_duplicate_family_ids(self):
        self.assertEqual(user_story_22.uniqueIds([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}], [

            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F03@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F01@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            ["Error US22: There are duplicates of the family ID @F01@. All family IDs should be unique."])

    def test_duplicate_family_individual_ids(self):
        self.assertEqual(user_story_22.uniqueIds([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I01@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}], [

            {'id': '@F01@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F02@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F03@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            ["Error US22: Joseph Biden, Jill Jacobs all have the same individual ID (@I01@).",
            "Error US22: There are duplicates of the family ID @F02@. All family IDs should be unique."])

    def test_duplicate_ids_many_members(self):
        self.assertEqual(user_story_22.uniqueIds([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I01@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I01@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}], [

            {'id': '@F02@', 'married': datetime.date(1977, 6, 17), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': {'@I07@'}},
            {'id': '@F02@', 'married': datetime.date(1966, 8, 27), 'divorced': 'NA', 'husb_id': '@I01@', 'husb_name': 'Joseph /Biden/', 'wife_id': '@I02@', 'wife_name': 'Neilia /Hunter/', 'children': {'@I05@', '@I06@', '@I04@'}},
            {'id': '@F02@', 'married': datetime.date(1970, 2, 14), 'divorced': datetime.date(1975, 8, 5), 'husb_id': '@I20@', 'husb_name': 'Bill /Stevenson/', 'wife_id': '@I03@', 'wife_name': 'Jill /Jacobs/', 'children': set()},
            {'id': '@F03@', 'married': datetime.date(2002, 11, 30), 'divorced': 'NA', 'husb_id': '@I04@', 'husb_name': 'Beau /Biden/', 'wife_id': '@I09@', 'wife_name': 'Hallie /Olivere/', 'children': {'@I11@', '@I10@'}}
            ]),
            
            ["Error US22: Joseph Biden, Neilia Hunter, Jill Jacobs all have the same individual ID (@I01@).",
            "Error US22: There are duplicates of the family ID @F02@. All family IDs should be unique."])

    def test_findNonUniqueIds_method(self):
        self.assertEqual(user_story_22.findNonUniqueIds([
            {'id': '@I02@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I01@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I02@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}
        ]), 
        
        {"@I02@"})

    def test_findNonUniqueIds_method_all_unique(self):
        self.assertEqual(user_story_22.findNonUniqueIds([
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I03@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}
        ]), 
        
        set())

    def test_findNamesWNonUniqueIds_method(self):
        self.assertEqual(user_story_22.findNamesWNonUniqueIds(
            {"@I02@"}
        ,
        [
            {'id': '@I01@', 'name': 'Joseph /Biden/', 'gender': 'M', 'birthday': datetime.date(1942, 11, 20), 'age': 78, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F02@', '@F01@'}},
            {'id': '@I02@', 'name': 'Neilia /Hunter/', 'gender': 'F', 'birthday': datetime.date(1942, 7, 28), 'age': 30, 'alive': False, 'death': datetime.date(1972, 12, 18), 'child': set(), 'spouse': {'@F02@'}},
            {'id': '@I02@', 'name': 'Jill /Jacobs/', 'gender': 'F', 'birthday': datetime.date(1951, 6, 3), 'age': 70, 'alive': True, 'death': 'NA', 'child': set(), 'spouse': {'@F03@', '@F01@'}},
            {'id': '@I04@', 'name': 'Beau /Biden/', 'gender': 'M', 'birthday': datetime.date(1969, 2, 3), 'age': 46, 'alive': False, 'death': datetime.date(2015, 5, 30), 'child': {'@F02@'}, 'spouse': {'@F04@'}}
        ]), 
        
        {"@I02@": ["Neilia Hunter", "Jill Jacobs"]})
