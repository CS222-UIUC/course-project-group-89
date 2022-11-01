"""This module will include testing for various majors for backend"""
import unittest
import pandas as pd
import course_requirements
from parsing import df_, check_credit_hours, get_all_classes, sort_core_classes, remaining_classes

class TestMerge(unittest.TestCase):
    """ this class is is to test certain aspects of the backend"""
    def test_cs_stats(self):
        """to test based on ggis + stats courses"""
        common_courses = course_requirements.merge(
            course_requirements.df_cs_ggis, course_requirements.df_cs_stats)
        ans = ["CS 124", "CS 128", "CS 173", "MATH 257", "MATH 231", "CS 222",
               "CS 225", "CS 233", "CS 340", "CS 341", "CS 374", "CS 421", "STAT 200", "STAT 212"]
        self.assertCountEqual(common_courses["technical requirements"].values.tolist(), ans)
    def test_cs_astr(self):
        """to test ggis + astro courses"""
        common_courses = course_requirements.merge(
            course_requirements.df_cs_ggis, course_requirements.df_cs_astronomy)
        ans = ["CS 124", "CS 128", "CS 173", "MATH 231", "MATH 257", "CS 222",
               "CS 225", "CS 233", "CS 340", "CS 341", "CS 361", "CS 374", "CS 421", "STAT 200",
              "STAT 212"]
        self.assertCountEqual(common_courses["technical requirements"].values.tolist(), ans)
    def test_stat_astr(self):
        """to test stat & astro merged courses"""
        common_courses = course_requirements.merge(
            course_requirements.df_cs_stats, course_requirements.df_cs_astronomy)
        ans = ["CS 124", "CS 128", "CS 173", "MATH 241", "MATH 231", "MATH 257", "CS 222",
               "CS 225", "CS 233", "CS 341", "CS 340", "CS 374", "CS 421", "STAT 200", "STAT 212"]
        self.assertCountEqual(common_courses["technical requirements"].values.tolist(), ans)

class TestCreditHours(unittest.TestCase):
    """ this class is is to test certain aspects of the backend"""
    def test1(self):
        """should return 2 remaining courses within 18 credit hours"""
        user1 = pd.DataFrame(columns = df_.columns.tolist())
        user1= pd.concat([user1, df_.loc[df_['CRN']==69781]])
        user1= pd.concat([user1, df_.loc[df_['CRN']==71571]])
        user1= pd.concat([user1, df_.loc[df_['CRN']==46074]])
        user1= pd.concat([user1, df_.loc[df_['CRN']==30855]])
        user1= pd.concat([user1, df_.loc[df_['CRN']==68851]])
        df_core_classes = get_all_classes(sort_core_classes("STAT & CS"))
        available_classes = check_credit_hours(user1, df_core_classes, 18)
        assert available_classes['CRN'].count() == 2
    def test2(self):
        """gets rid of all CS124 classes after user1 selects it"""
        selected_subjects = ['CS 124', 'CS 128', 'CS 225', 'CS 173', 'CS 222',
        'MATH 231', 'MATH 241', 'MATH 257', 'STAT 107', 'STAT 400', 'STAT 410', 'STAT 425']
        ans = ["CS 233", "CS 341", "CS 340", "CS 357", "MATH 415",
        "MATH 416", "CS 374","CS 421", "STAT 426"]
        calculated = remaining_classes(selected_subjects, 'STAT & CS')
        print(calculated)
        self.assertCountEqual(calculated, ans)
    def test3(self):
        """gets rid of all CS124 classes after user1 selects it"""
        selected_subjects = ['CS 124', 'CS 128', 'CS 225', 'CS 173', 'CS 222',
        'MATH 231', 'MATH 241', 'MATH 257', 'STAT 107', 'STAT 200', 'STAT 212',
        'STAT 400', 'STAT 410', 'STAT 425', 'CS 340']
        ans = ["CS 357", "MATH 415", "MATH 416", "CS 374","CS 421", "STAT 426"]
        calculated = remaining_classes(selected_subjects, 'STAT & CS')
        self.assertCountEqual(calculated, ans)

if __name__ == '__main__':
    unittest.main()
