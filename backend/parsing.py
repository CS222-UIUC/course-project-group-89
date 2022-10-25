"'this module reades into the courses.csv'"
from queue import Empty
import sys
import pandas as pd
sys.path.insert(1, './backend')
# pylint: disable-next=global-statement
import course_requirements


df_ = pd.read_csv('backend/courses.csv')

df_['Subject and Number'] = df_['Subject'] + df_['Number'].map(str)
df_ = df_.drop(columns = ['Subject', 'Number'])

def sort_core_classes(major_):
    '''returns core classes given a major'''
    df_user_information = pd.DataFrame(columns = df_.columns.tolist())
    core_course_list = Empty
    if major_ == "cs + ggis":
        core_course_list = course_requirements.df_cs_ggis.values.tolist()
    elif major_ == "cs + stat":
        core_course_list = course_requirements.df_cs_stats.values.tolist()
    elif major_ == "cs + astronomy":
        core_course_list = course_requirements.df_cs_astronomy.values.tolist()
    for course in core_course_list:
        entry = df_.loc[df_['Subject and Number'] == course[0]]
        df_user_information = pd.concat([df_user_information, entry])
    return df_user_information

df_core_classes = sort_core_classes("cs + astronomy")

def sort_common_courses(user_one_courses, user_two_courses):
    '''takes 2 different user's DF of the courses they can take and
    returns courses they can take together'''
    common_courses = user_one_courses.merge(
        user_two_courses, how = 'inner', on='Subject and Number')
    return common_courses

df_user1 = pd.DataFrame(columns = df_.columns.tolist())

def check_credit_hours(selected_classes, major_requirements, credit_limit):
    '''Takes User1's DF of selected courses. Returns additional courses within credit limit'''
    num_credits = selected_classes['Credit Hours'].dropna().str.extract(r"(\d+)").astype(int).sum()
    credits_left = credit_limit - num_credits[0]
    major_requirements['Num Credits'] = (major_requirements['Credit Hours']
                                        .dropna().str.extract(r"(\d+)").astype(int))
    valid_courses = major_requirements.loc[major_requirements['Num Credits'] <= credits_left]
    return valid_courses

def remove(course, df_tmp):
    '''removes all courses with selected subject from list of requirements'''
    df_tmp.drop(df_tmp.loc[df_tmp['Subject and Number'] == course].index, inplace=True)
