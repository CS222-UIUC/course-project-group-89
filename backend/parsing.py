"'this module reades into the courses.csv'"
from queue import Empty
import pandas as pd
import course_requirements
df_ = pd.read_csv('./microservice/courses.csv')
df_['Subject and Number'] = df_['Subject'] + df_['Number'].map(str)
df_ = df_.drop(columns = ['Subject', 'Number'])


# print(df_.loc[df_['Subject and Number']=='CS124'])
def sort_core_classes(major_):
    '''returns core classes given a major'''
    df_user_information = pd.DataFrame(columns = df_.columns.tolist())
    core_course_list = Empty
    if major_ == "cs + ggis":
        # change to cs + ggis later on
        core_course_list = course_requirements.df_cs.values.tolist()
    elif major_ == "cs + stat":
        core_course_list = course_requirements.df_cs_stats.values.tolist()
    elif major_ == "cs + astronomy":
        core_course_list = course_requirements.df_cs_astronomy.values.tolist()
    for course in core_course_list:
        entry = df_.loc[df_['Subject and Number'] == course[0]]
        df_user_information = pd.concat([df_user_information, entry])
    return df_user_information

df_core_classes = sort_core_classes("cs + astronomy")
print(df_core_classes)
