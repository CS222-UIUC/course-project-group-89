# Courses Microservice /waf

import os
import requests
import pandas as pd

def fetchIfNotExists(url, fileName):
  if not os.path.exists(fileName):
    r = requests.get(url, stream=True)
    with open(fileName, 'wb') as fd:
      for chunk in r.iter_content(chunk_size=4096):
        fd.write(chunk)

# Ensure we have a GPA dataset and a courses dataset
fetchIfNotExists("https://raw.githubusercontent.com/illinois/courses-dataset/master/course-schedule/2021-fall.csv", "courses.csv")

# Open both as a pandas
df_courses = pd.read_csv("courses.csv")


from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/<subject>/<number>/')
def GET_subject_number(subject, number):
  # Prep result:
  result = { "course": f"{subject} {number}" }

  # Cast `number` as an int and ensure `subject` is all caps:
  try:
    number = int(number)
  except:
    result["error"] = f"Course number `{number}` is not a number"
    status_code = 404
    return jsonify(result), status_code
  subject = subject.upper()

  # Fetch data:
  courses = df_courses[ (df_courses["Subject"] == subject) & (df_courses["Number"] == number) & (df_courses["Start Time"] != "") & (df_courses["Start Time"] != "ARRANGED") ] 

  if len(courses) == 0:
    # Provide an error:
    result["error"] = f"No course data available for {subject} {number}"
    status_code = 404
  else:
    # Prefer LEC sections (for courses with discussions/labs)
    course_lec = courses[ courses["Type Code"] == "LEC" ]
    if len(course_lec) > 0:
      courses = course_lec

    # Get the first result's data:
    c = courses.iloc[0]
    result["Start Time"] = c["Start Time"]
    result["Days of Week"] = c["Days of Week"]
    status_code = 200

  return jsonify(result), status_code
