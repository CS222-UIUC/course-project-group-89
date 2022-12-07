"""This module will include testing for various majors for backend"""
import unittest
import pandas as pd
# import course_requirements
from parsing import (df_, check_credit_hours, filter_based_on_time, get_all_classes,
    sort_core_classes, remaining_classes, check_time_conflict)

class TestSortCoreClasses(unittest.TestCase):
    '''this test class is to test that it returns the proper dataframe of all core classes'''
    def test_cs_math(self):
        '''test backend on CS + MATH courses'''
        core_classes = sort_core_classes("CS + MATH")
        ans = [['CS 124'], ['CS 128'], ['CS 173'], ['CS 222'], ['CS 225'], ['CS 233'], ['CS 341'],
               ['CS 340'], ['CS 357'], ['CS 374'], ['CS 421'], ['CS 450'], ['MATH 220'],
               ['MATH 231'], ['MATH 241'], ['MATH 257'], ['MATH 416']]
        self.assertCountEqual(core_classes.values.tolist(), ans)
    def test_cs_astro(self):
        '''test backend STAT & CS courses'''
        core_classes = sort_core_classes("CS + ASTRO")
        ans = [['CS 124'], ['CS 128'], ['CS 173'], ['CS 222'], ['CS 225'], ['CS 233'], ['CS 341'],
               ['CS 340'], ['STAT 200'], ['STAT 212'], ['CS 361'], ['CS 374'], ['CS 421'],
               ['MATH 221'], ['MATH 220'], ['MATH 225'], ['MATH 257'], ['MATH 231'], ['PHYS 211'],
               ['PHYS 212'], ['MATH 241'], ['ASTR 210'], ['ASTR 310'], ['ASTR 404'], ['ASTR4 05'],
               ['ASTR 406'], ['ASTR 414']]
        self.assertCountEqual(core_classes.values.tolist(), ans)
    def test_cs_stat(self):
        '''test backend on STAT & CS courses'''
        core_classes = sort_core_classes("STAT & CS")
        ans = [['CS 124'], ['CS 128'], ['CS 173'], ['CS 222'], ['CS 225'], ['MATH 241'],
               ['MATH 231'], ['CS 233'], ['CS 341'], ['CS 340'], ['CS 357'], ['MATH 257'],
               ['MATH 415'], ['MATH 416'], ['CS 374'], ['CS 421'], ['STAT 107'], ['STAT 200'],
               ['STAT 212'], ['STAT 400'], ['STAT 410'], ['STAT 425'], ['STAT 426']]
        self.assertCountEqual(core_classes.values.tolist(), ans)
class TestGetAllClasses(unittest.TestCase):
    '''this test class is to test that it returns the proper dataframe of all classes
    & their information'''
    def test_cs_math(self):
        '''test backend on CS + MATH courses & getting their information'''
        core_classes = sort_core_classes("CS + MATH")
        all_classes = get_all_classes(core_classes)
        ans = 8008
        self.assertEqual(all_classes.size, ans)
    def test_cs_astro(self):
        '''test backend STAT & CS courses & getting their information'''
        core_classes = sort_core_classes("CS + ASTRO")
        all_classes = get_all_classes(core_classes)
        ans = 11076
        self.assertEqual(all_classes.size, ans)
    def test_cs_stat(self):
        '''test backend on STAT & CS courses & getting their information'''
        core_classes = sort_core_classes("STAT & CS")
        all_classes = get_all_classes(core_classes)
        ans = 8892
        self.assertEqual(all_classes.size, ans)
class TestFilterClassesBasedOnTime(unittest.TestCase):
    '''this test class is to test that it returns the proper dataframe of all classes
    & their information'''
    def test_cs_math(self):
        '''test backend on CS + MATH courses & filtering based on user selected times'''
        core_classes = sort_core_classes("CS + MATH")
        all_classes = get_all_classes(core_classes)
        start_time = '10:30 am'
        end_time = '3:30 pm'
        time_filtered_classes = filter_based_on_time(all_classes, start_time, end_time)
        first_entry = time_filtered_classes.iloc[0]
        self.assertGreaterEqual(pd.to_datetime(first_entry['Start Time']),
            pd.to_datetime(start_time))
        self.assertLessEqual(pd.to_datetime(first_entry['End Time']), pd.to_datetime(end_time))
        last_entry = time_filtered_classes.iloc[-1]
        self.assertGreaterEqual(pd.to_datetime(last_entry['Start Time']),
            pd.to_datetime(start_time))
        self.assertLessEqual(pd.to_datetime(last_entry['End Time']), pd.to_datetime(end_time))
    def test_cs_astro(self):
        '''test backend STAT & CS courses & filtering based on user selected times'''
        core_classes = sort_core_classes("CS + ASTRO")
        all_classes = get_all_classes(core_classes)
        start_time = '8:00 am'
        end_time = '12:00 pm'
        time_filtered_classes = filter_based_on_time(all_classes, start_time, end_time)
        first_entry = time_filtered_classes.iloc[0]
        self.assertGreaterEqual(pd.to_datetime(first_entry['Start Time']),
            pd.to_datetime(start_time))
        self.assertLessEqual(pd.to_datetime(first_entry['End Time']), pd.to_datetime(end_time))
        last_entry = time_filtered_classes.iloc[-1]
        self.assertGreaterEqual(pd.to_datetime(last_entry['Start Time']),
            pd.to_datetime(start_time))
        self.assertLessEqual(pd.to_datetime(last_entry['End Time']), pd.to_datetime(end_time))
    def test_cs_stat(self):
        '''test backend on STAT & CS courses & filtering based on user selected times'''
        core_classes = sort_core_classes("STAT & CS")
        all_classes = get_all_classes(core_classes)
        start_time = '3:00 pm'
        end_time = '8:00 pm'
        time_filtered_classes = filter_based_on_time(all_classes, start_time, end_time)
        first_entry = time_filtered_classes.iloc[0]
        self.assertGreaterEqual(pd.to_datetime(first_entry['Start Time']),
            pd.to_datetime(start_time))
        self.assertLessEqual(pd.to_datetime(first_entry['End Time']), pd.to_datetime(end_time))
        last_entry = time_filtered_classes.iloc[-1]
        self.assertGreaterEqual(pd.to_datetime(last_entry['Start Time']),
            pd.to_datetime(start_time))
        self.assertLessEqual(pd.to_datetime(last_entry['End Time']), pd.to_datetime(end_time))
# class TestMerge(unittest.TestCase):
#     """ this class is is to test certain aspects of the backend"""
#     def test_cs_stats(self):
#         """to test based on ggis + stats courses"""
#         common_courses = course_requirements.merge(
#             course_requirements.df_cs_ggis, course_requirements.df_cs_stats)
#         ans = []
#         self.assertCountEqual(common_courses["technical requirements"].values.tolist(), ans)
#     def test_cs_astr(self):
#         """to test ggis + astro courses"""
#         common_courses = course_requirements.merge(
#             course_requirements.df_cs_ggis, course_requirements.df_cs_astronomy)
#         ans = []
#         self.assertCountEqual(common_courses["technical requirements"].values.tolist(), ans)
#     def test_stat_astr(self):
#         """to test stat & astro merged courses"""
#         common_courses = course_requirements.merge(
#             course_requirements.df_cs_stats, course_requirements.df_cs_astronomy)
#         ans = []
#         self.assertCountEqual(common_courses["technical requirements"].values.tolist(), ans)

class TestCreditHours(unittest.TestCase):
    """ this class is is to test certain aspects of the backend"""
    def test_count_credit_hours(self):
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
    def test_remove_same_requirements_stat(self):
        """gets rid of all STAT200/STAT212 classes after user1 selects STAT107"""
        selected_subjects = ['CS 124', 'CS 128', 'CS 225', 'CS 173', 'CS 222',
        'MATH 231', 'MATH 241', 'MATH 257', 'STAT 107', 'STAT 400', 'STAT 410', 'STAT 425']
        ans = ["CS 233", "CS 341", "CS 340", "CS 357", "MATH 415",
        "MATH 416", "CS 374","CS 421", "STAT 426"]


        calculated = remaining_classes(selected_subjects, 'STAT & CS')
        self.assertCountEqual(calculated, ans)
    def test_remove_same_requirements_cs(self):
        """gets rid of all CS341/CS233 classes after user1 selects CS340"""
        selected_subjects = ['CS 124', 'CS 128', 'CS 225', 'CS 173', 'CS 222',
        'MATH 231', 'MATH 241', 'MATH 257', 'STAT 107', 'STAT 200', 'STAT 212',
        'STAT 400', 'STAT 410', 'STAT 425', 'CS 340']
        ans = ["CS 357", "MATH 415", "MATH 416", "CS 374","CS 421", "STAT 426"]
        calculated = remaining_classes(selected_subjects, 'STAT & CS')
        self.assertCountEqual(calculated, ans)
    def test_time_conflict_beginning(self):
        '''determines if there's a time conflict in the user's selected classes'''
        user1 = pd.DataFrame(columns = df_.columns.tolist())
        user1= pd.concat([user1, df_.loc[df_['CRN']==69781]])
        user1= pd.concat([user1, df_.loc[df_['CRN']==30107]])
        user1= pd.concat([user1, df_.loc[df_['CRN']==46074]])
        user1= pd.concat([user1, df_.loc[df_['CRN']==30855]])
        user1= pd.concat([user1, df_.loc[df_['CRN']==68851]])
        ans = check_time_conflict(user1.values.tolist())
        assert ans is False
    def test_time_conflict_ending(self):
        """determines if there's a time conflict in the user's selected classes"""
        user1 = pd.DataFrame(columns = df_.columns.tolist())
        user1= pd.concat([user1, df_.loc[df_['CRN']==71844]]) # 3:00-3:50
        user1= pd.concat([user1, df_.loc[df_['CRN']==71907]]) # 3:30-4:50
        user1= pd.concat([user1, df_.loc[df_['CRN']==68851]])
        ans = check_time_conflict(user1.values.tolist())
        assert ans is False
    def test_no_time_conflict(self):
        """determines if there's a time conflict in the user's selected classes"""
        user1 = pd.DataFrame(columns = df_.columns.tolist())
        user1= pd.concat([user1, df_.loc[df_['CRN']==71844]]) # 3:00-3:50
        user1= pd.concat([user1, df_.loc[df_['CRN']==69781]]) # 9:00-10:20
        user1= pd.concat([user1, df_.loc[df_['CRN']==43832]]) # 11:00-11:50
        ans = check_time_conflict(user1.values.tolist())
        assert ans is False

if __name__ == '__main__':
    unittest.main()
