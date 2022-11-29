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
        core_course_list = course_requirements.df_cs_math
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
        df_course_information = pd.concat([df_course_information, entry])
    return df_course_information

df_core_classes_ = sort_core_classes("CS + MATH")
df_all_classes_ = get_all_classes(df_core_classes_)
print(df_all_classes_.size)

# def get_unique_classes(df_classes):
#     '''this function returns a list of the unique core courses given someone's major'''
#     df_classes: dataframe from getting user's major to include all possible major-related courses
#     df_to_return: gets unique major-related courses from inputted dataframe
#     df_to_return = df_classes.drop_duplicates(subset=['Subject and Number'])
#     df_to_return = df_to_return["Subject and Number"]
#     list_to_return: converts all 'Subject and Number' items in column into list to return
#     list_to_return = df_to_return['Subject and Number'].tolist()
#     return df_to_return

# df_user_frontend = get_all_classes(sort_core_classes("STAT & CS"))
# print(df_user_frontend.iloc[0].values.tolist())

def sort_common_courses(user_one_courses, user_two_courses):
    '''takes 2 different user's DF of the courses they can take and
    returns courses they can take together'''
    common_courses = user_one_courses.merge(
        user_two_courses, how = 'inner', on='Subject and Number')
    return common_courses

df_user1 = pd.DataFrame(columns = df_.columns.tolist())
user1_selected_subjects = []

def check_credit_hours(selected_classes, major_requirements, credit_limit):
    '''Takes User1's df of selected course sections. Returns a df of course
    sections they can additionally take within credit limit'''
    num_credits = selected_classes['Credit Hours'].dropna().str.extract(r"(\d+)").astype(int).sum()
    credits_left = credit_limit - num_credits[0]
    major_requirements['Num Credits'] = (major_requirements['Credit Hours']
                                        .dropna().str.extract(r"(\d+)").astype(int))
    valid_courses = major_requirements.loc[major_requirements['Num Credits'] <= credits_left]
    # ensures no selected classes get re-added
    selected_subjects = selected_classes['Subject and Number'].tolist()
    for subject in selected_subjects:
        rows_overlap = valid_courses.loc[valid_courses['Subject and Number'] == subject].index
        valid_courses.drop(rows_overlap, inplace=True)
    return valid_courses

def remove_stat_equivalents(selected_subjects, list_differences):
    '''updates list_differences w/o duplicate STAT classes'''
    if 'STAT 107' in selected_subjects:
        if 'STAT 200' in list_differences:
            list_differences.remove('STAT 200')
        if 'STAT 212' in list_differences:
            list_differences.remove('STAT 212')
    elif 'STAT 212' in selected_subjects:
        if 'STAT 200' in list_differences:
            list_differences.remove('STAT 200')
        if 'STAT 107' in list_differences:
            list_differences.remove('STAT 107')
    elif 'STAT 200' in selected_subjects:
        if 'STAT 107' in list_differences:
            list_differences.remove('STAT 107')
        if 'STAT 212' in list_differences:
            list_differences.remove('STAT 212')
    return list_differences

def remove_cs_equivalents(selected_subjects, list_differences):
    '''updates list_differences w/o duplicate CS classes'''
    if 'CS 340' in selected_subjects:
        if 'CS 341' in list_differences:
            list_differences.remove('CS 341')
        if 'CS 233' in list_differences:
            list_differences.remove('CS 233')
    elif 'CS 341' in selected_subjects or 'CS 233' in selected_subjects:
        if 'CS 340' in list_differences:
            list_differences.remove('CS 340')
    return list_differences

def remaining_classes(selected_subjects, major):
    '''selected_subjects => a list of subject names (ex. [CS 124, CS 225])
    returns list of remaining classes from requirements excluding selected_subjects'''
    list_requirements = sort_core_classes(major)["technical requirements"].tolist()
    difference = []

    for element in list_requirements:
        if element not in selected_subjects:
            difference.append(element)

    difference = remove_stat_equivalents(selected_subjects, difference)
    difference = remove_cs_equivalents(selected_subjects, difference)

    return difference

# def sort_in_time_frame(start_time, end_time, df_classes):

def check_time_conflict(selected_sections):
    '''takes in list of selected class sections. returns true if there
    is no time conflict. returns false if there is a time conflict'''
    for section in selected_sections:
        remaining_sections = [x for x in selected_sections if x != section]
        for other_section in remaining_sections:
            if (section[20] >= other_section[20]
                and section[20] <= other_section[20]):
                return False
            if (section[21] >= other_section[21]
            and section[21] >= other_section[21]):
                return False
    return True
