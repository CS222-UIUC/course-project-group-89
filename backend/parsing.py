"'this module reades into the courses.csv'"
from queue import Empty
import pandas as pd
import course_requirements
df_ = pd.read_csv('courses.csv')
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

def check_credit_hours(selected_classes, major_requirements, credit_limit):
    '''Takes User1's DF of selected courses. Returns additional courses within credit limit'''
    num_credits = selected_classes['Credit Hours'].dropna().str.extract('(\d+)').astype(int).sum()
    credits_left = credit_limit - num_credits[0]
    major_requirements['Num Credits'] = (major_requirements['Credit Hours']
                                        .dropna().str.extract('(\d+)').astype(int))
    valid_courses = major_requirements.loc[major_requirements['Num Credits'] <= credits_left]
    return valid_courses
    