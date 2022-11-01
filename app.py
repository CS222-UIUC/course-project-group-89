'''this module renders a template and has two functions (testing for emily 10/1/22)'''
import os
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from parsing import sort_core_classes

app = Flask(__name__)
class_cs =  ["CS 124", "CS 128", "CS 173", "MATH 241", "MATH 257",
    "CS 210", "CS 211", "CS 222", "CS 225", "CS 233", "CS 341", "CS 357", "CS 361", "CS 374", "CS 421"]
    
class_cs_stats =  ["CS 124", "CS 128", "CS 173", "CS 222", "CS 225",
    "MATH 241", "CS 233", "CS 341", "CS 340",  "CS 357", "MATH 257", "MATH 415", "MATH 416", "CS 374",
    "CS 421", "STAT 107", "STAT 200", "STAT 212", "STAT 400", "STAT 410", "STAT 425", "STAT 426"]
    
class_cs_astro =  ["CS 124", "CS 128", "CS 173", "CS 222",
    "CS 225",  "CS 233", "CS 341", "CS 340", "STAT 200", "STAT 212", "CS 361", "CS 374", "CS 421", "MATH 221",
    "MATH 220", "MATH 225", "MATH 257", "MATH 231", "PHYS 211", "PHYS 212", "MATH 241",
    "ASTR 210", "ASTR 310", "ASTR 404", "ASTR 405", "ASTR 406", "ASTR 414"]

class_cs_ggis = ["Needs to be Removed"]
# Route for "/" (frontend):
@app.route('/')
def dropdown():
    """Function printing python version."""
    print(os.getcwd())
    cs_req = ["CS + GGIS", "CS + ASTRO", "Stats & CS", "CS"]
    return render_template('index.html', cs_req=cs_req)

@app.route('/major', methods=["POST"])
def main():
    "'this function is for main'"
    major = request.form["major"]
    print("in main(), major: ", major)
    with open("store_user_input.txt", "w+", encoding="utf8") as curr_file:
        curr_file.write(major)
        curr_file.write("\n")
    curr_file.close()
    return render_template("index.html")
'''
"CS + GGIS", "CS + ASTRO", "Stats & CS", "CS"
'''
@app.route('/class', methods=["GET"])
def checkboxes():
    "'checboxes for class.html'"
    major = ""
    with open("store_user_input.txt", "r", encoding="utf8") as curr_file:
        major = curr_file.readline().rstrip()
    print("in checkboxes(): ", major)
    cs_req = []
    if major == "CS + ASTRO":
        cs_req = class_cs_astro
    elif major == "CS + GGIS":
        cs_req = class_cs_ggis
    elif major == "Stats & CS":
        cs_req = class_cs_stats
    else:
        cs_req = class_cs
    curr_file.close()
    return render_template("class.html", cs_req= cs_req)

@app.route('/class', methods=["POST"])
def store_classes():
    "'checboxes for class.html'"
    courses = request.form["courses"]
    print("in main(), major: ", courses)
    with open("store_user_input.txt", "w+", encoding="utf8") as curr_file:
        curr_file.write(courses)
        curr_file.write("\n")
    curr_file.close()
    return render_template("class.html")

'''
NOW GET FRIEND'S CLASS
'''
# Getting major of second user for "/friendmajor" (frontend):
@app.route('/friendmajor', methods=["POST", "GET"])
def friendmajor():
    #Have backend team return the info in this function
    #backend file
    """Function printing python version."""
    cs_req = ["CS + GIS", "CS + ASTRO", "CS + STAT", "CS"]
    return render_template('friendmajor.html', cs_req=cs_req)

@app.route('/friendclass', methods=["POST", "GET"])
def friendclasses():
    """Function printing python version."""
    major = ""
    with open("store_user_input.txt", "r", encoding="utf8") as curr_file:
        major = curr_file.readline().rstrip()
    print("in checkboxes(): ", major)
    cs_req = []
    if major == "CS + ASTRO":
        cs_req = class_cs_astro
    elif major == "CS + GGIS":
        cs_req = class_cs_ggis
    elif major == "Stats & CS":
        cs_req = class_cs_stats
    else:
        cs_req = class_cs
    curr_file.close()
    return render_template("friendclass.html", cs_req = cs_req)





