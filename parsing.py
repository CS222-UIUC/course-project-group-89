"'this module reades into the courses.csv'"
from queue import Empty
import pandas as pd
import course_requirements

df_ = pd.read_csv('courses.csv')

df_['Subject and Number'] = df_['Subject'] + " " + df_['Number'].map(str)
df_ = df_.drop(columns = ['Subject', 'Number'])

def sort_core_classes(major_):
    '''returns core classes given a major'''
    df_user_information = pd.DataFrame(columns = df_.columns.tolist())
    core_course_list = Empty
    if major_ == "CS + MATH":
        # print("math major over here")
        # print(course_requirements.MATH)
        # print("math major over here")
        core_course_list = course_requirements.df_cs_math.values.tolist()
        # print(core_course_list)
    elif major_ == "STAT & CS":
        core_course_list = course_requirements.df_cs_stats.values.tolist()
    elif major_ == "CS + ASTRO":
        core_course_list = course_requirements.df_cs_astronomy.values.tolist()
    for course in core_course_list:
        entry = df_.loc[df_['Subject and Number'] == course[0]]
        # print("entry: ", entry)
        df_user_information = pd.concat([df_user_information, entry])
    return df_user_information

def get_unique_classes(df_classes):
    '''this function returns a list of the unique core courses given someone's major'''
    # df_classes: dataframe from getting user's major to include all possible major-related courses
    # df_to_return: gets unique major-related courses from inputted dataframe
    df_to_return = df_classes.drop_duplicates(subset=['Subject and Number'])
    # list_to_return: converts all 'Subject and Number' items in column into list to return
    # list_to_return = df_to_return['Subject and Number'].tolist()
    return df_to_return

# df_user_backend = sort_core_classes("CS + MATH")
# print(df_user_backend)
# df_user_frontend = get_unique_classes(df_user_backend)
# print(df_user_frontend)

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
