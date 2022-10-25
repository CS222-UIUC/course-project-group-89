"""This module will include testing for various majors for backend"""
import unittest
import course_requirements
import pandas as pd
from parsing import df_, df_core_classes, check_credit_hours
class TestMerge(unittest.TestCase):
    """ this class is is to test certain aspects of the backend"""
    def test_cs_stats(self):
        """to test based on ggis + stats courses"""
        common_courses = course_requirements.merge(
            course_requirements.df_cs_ggis, course_requirements.df_cs_stats)
        ans = ["CS124", "CS128", "CS173", "MATH257", "MATH231", "CS222",
               "CS225", "CS233", "CS340", "CS341", "CS374", "CS421", "STAT200", "STAT212"]
        self.assertCountEqual(common_courses["technical requirements"].values.tolist(), ans)
    def test_cs_astr(self):
        """to test ggis + astro courses"""
        common_courses = course_requirements.merge(
            course_requirements.df_cs_ggis, course_requirements.df_cs_astronomy)
        ans = ["CS124", "CS128", "CS173", "MATH231", "MATH257", "CS222",
               "CS225", "CS233", "CS340", "CS341", "CS361", "CS374", "CS421", "STAT200",
              "STAT212"]
        self.assertCountEqual(common_courses["technical requirements"].values.tolist(), ans)
    def test_stat_astr(self):
        """to test stat & astro merged courses"""
        common_courses = course_requirements.merge(
            course_requirements.df_cs_stats, course_requirements.df_cs_astronomy)
        ans = ["CS124", "CS128", "CS173", "MATH241", "MATH231", "MATH257", "CS222",
               "CS225", "CS233", "CS341", "CS340", "CS374", "CS421", "STAT200", "STAT212"]
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

        available_classes = check_credit_hours(user1, df_core_classes, 18)
        assert available_classes['CRN'].count() == 2

if __name__ == '__main__':
    unittest.main()
    