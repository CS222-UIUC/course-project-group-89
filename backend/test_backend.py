import course_requirements
import unittest
import pandas as pd

class TestMerge(unittest.TestCase):
    def test_cs_stats(self):
        common_courses = course_requirements.Merge(course_requirements.df_cs, course_requirements.df_cs_stats)
        ans = ["CS124", "CS128", "CS173", "MATH241", "MATH257", "CS222", "CS225", "CS233", "CS341", "CS357", "CS374", "CS421"]
        self.assertCountEqual(common_courses["technical requirements"].values.tolist(), ans)
    def test_cs_astr(self):
        common_courses = course_requirements.Merge(course_requirements.df_cs, course_requirements.df_cs_astronomy)
        ans = ["CS124", "CS128", "CS173", "MATH241", "MATH257", "CS222", "CS225", "CS233", "CS341", "CS361", "CS374", "CS421"]
        self.assertCountEqual(common_courses["technical requirements"].values.tolist(), ans)
    def test_stat_astr(self):
        common_courses = course_requirements.Merge(course_requirements.df_cs_stats, course_requirements.df_cs_astronomy)
        ans = ["CS124", "CS128", "CS173", "MATH241", "MATH257", "CS222", "CS225", "CS233", "CS341", "CS340", "CS374", "CS421", "STAT200", "STAT212"]
        self.assertCountEqual(common_courses["technical requirements"].values.tolist(), ans)
    # self.MergeCS_CSSTATS()

if __name__ == '__main__':
    unittest.main()