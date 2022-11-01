"'this module reades into the courses.csv'"
from queue import Empty
import pandas as pd
import course_requirements

df_ = pd.read_csv('courses.csv')

df_['Subject and Number'] = df_['Subject'] + " " + df_['Number'].map(str)
df_ = df_.drop(columns = ['Subject', 'Number'])

def sort_core_classes(major_):
    '''returns core classes given a major'''

    core_course_list = Empty #has list of all core courses  & their info
    if major_ == "CS + MATH":
        # print("math major over here")
        # print(course_requirements.MATH)
        # print("math major over here")
        core_course_list = course_requirements.df_cs_math
        # print(core_course_list)
    elif major_ == "STAT & CS":
        core_course_list = course_requirements.df_cs_stats
    elif major_ == "CS + ASTRO":
        core_course_list = course_requirements.df_cs_astronomy

    return core_course_list

def get_all_classes(df_course_list):
    ''''pulls all classes & their course information and puts it into a Pandas dataframe'''
    # goes into dataframe and pulls information about matched courses from core course list
    df_course_information = pd.DataFrame(columns = df_.columns.tolist())
    for course in df_course_list.values.tolist():
        entry = df_.loc[df_['Subject and Number'] == course[0]]
        # print("entry: ", entry)
        df_course_information = pd.concat([df_course_information, entry])
    return df_course_information


# def get_unique_classes(df_classes):
#     '''this function returns a list of the unique core courses given someone's major'''
#     df_classes: dataframe from getting user's major to include all possible major-related courses
#     df_to_return: gets unique major-related courses from inputted dataframe
#     df_to_return = df_classes.drop_duplicates(subset=['Subject and Number'])
#     df_to_return = df_to_return["Subject and Number"]
#     list_to_return: converts all 'Subject and Number' items in column into list to return
#     list_to_return = df_to_return['Subject and Number'].tolist()
#     return df_to_return

df_user_backend = sort_core_classes("CS + MATH")
# print(df_user_backend)
df_user_frontend = get_all_classes(df_user_backend)
# print(df_user_frontend)

def sort_common_courses(user_one_courses, user_two_courses):
    '''takes 2 different user's DF of the courses they can take and
    returns courses they can take together'''
    common_courses = user_one_courses.merge(
        user_two_courses, how = 'inner', on='Subject and Number')
    return common_courses

df_user1 = pd.DataFrame(columns = df_.columns.tolist())
user1_selected_subjects = []

def check_credit_hours(selected_classes, major_requirements, credit_limit):
    '''Takes User1's df of selected courses. Returns names of
    additional courses within credit limit'''
    num_credits = selected_classes['Credit Hours'].dropna().str.extract(r"(\d+)").astype(int).sum()
    credits_left = credit_limit - num_credits[0]
    major_requirements['Num Credits'] = (major_requirements['Credit Hours']
                                        .dropna().str.extract(r"(\d+)").astype(int))
    valid_courses = major_requirements.loc[major_requirements['Num Credits'] <= credits_left]
    return valid_courses

def remaining_classes(selected_subjects, major):
    '''selected_subjects => user1_selected_subjects or user2_selected_subjects,
    returns list of remaining classes from requirements excluding selected_subjects'''
    list_requirements = sort_core_classes(major)["technical requirements"].tolist()
    difference = []

    for element in list_requirements:
        if element not in selected_subjects:
            difference.append(element)
    if 'CS 340' in selected_subjects:
        if 'CS 341' in difference:
            difference.remove('CS 341')
        if 'CS 233' in difference:
            difference.remove('CS 233')
    if 'CS 341' in selected_subjects or 'CS 233' in selected_subjects:
        if 'CS 340' in difference:
            difference.remove('CS 340')
    if 'STAT 107' in selected_subjects:
        if 'STAT 200' in difference:
            difference.remove('STAT 200')
        if 'STAT 212' in difference:
            difference.remove('STAT 212')
    if 'STAT 212' in selected_subjects:
        if 'STAT 200' in difference:
            difference.remove('STAT 200')
        if 'STAT 107' in difference:
            difference.remove('STAT 107')
    if 'STAT 200' in selected_subjects:
        if 'STAT 107' in difference:
            difference.remove('STAT 107')
        if 'STAT 212' in difference:
            difference.remove('STAT 212')
    return difference
