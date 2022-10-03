'''this module renders a template and has two functions (testing for emily 10/1/22)'''
# import os
# from typing import Type
# import requests
import pandas as pd
from flask import Flask, jsonify

# def fetch_if_not_exists(url, file_name):
#     '''function to retrieve UIUC GPA dataset and Courses dataset'''
#     if not os.path.exists(file_name):
#         req = requests.get(url, stream=True)
#         with open(file_name, 'wb') as fd:
#             for chunk in req.iter_content(chunk_size=4096):
#                 fd.write(chunk)


# Open both as a pandas
df_courses = pd.read_csv("courses.csv")

app = Flask(__name__)

#Check to see if class exists --> Needs modifiying for our needs

@app.route('/<subject>/<number>/')
def get_subject_number(subject, number):
    '''Grabs course #'''
    # Prep result:
    result = { "course": f"{subject} {number}" }

    # Cast `number` as an int and ensure `subject` is all caps:
    try:
        number = int(number)
    except TypeError:
        result["error"] = f"Course number `{number}` is not a number, try again"
        status_code = 404
        return jsonify(result), status_code
    subject = subject.upper()

    # Fetch data:
    courses = df_courses[ (df_courses["Subject"] == subject)
                        & (df_courses["Number"] == number)
                        & (df_courses["Start Time"] != "")
                        & (df_courses["Start Time"] != "ARRANGED") ]

    if len(courses) == 0:
        # Provide an error:
        result["error"] = f"No course data for {subject} {number}"
        status_code = 404
    else:
        # Prefer LEC sections (for courses with discussions/labs)
        course_lec = courses[ courses["Type Code"] == "LEC" ]
        if len(course_lec) > 0:
            courses = course_lec

        # # Get the first result's data:
        # selected_course = courses.iloc[0]
        # result["Start Time"] = selected_course["Start Time"]
        # result["Days of Week"] = selected_course["Days of Week"]
        status_code = 200

    return jsonify(result), status_code
