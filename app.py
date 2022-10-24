'''this module renders a template and has two functions (testing for emily 10/1/22)'''

# import os
# from datetime import datetime, timedelta, time
from flask import Flask, render_template, request
# request, jsonify
# import requests

app = Flask(__name__)

# MAJOR_GLOBAL = ""
@app.route('/')
def dropdown():
    """Function printing python version."""
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
    # MAJOR_GLOBAL = major
    # print("MAJOR_GLOBAL: ", MAJOR_GLOBAL)
    #Have backend team return the info in this function
    #backend file
    return render_template("index.html")


@app.route('/class', methods=["GET"])
def checkboxes():
    "'checboxes for class.html'"
    df_cs =  ["CS 124", "CS 128", "CS 173", "MATH 241", "MATH 257",
    "CS 210", "CS 211", "CS 222", "CS 225", "CS 233",
    "CS 341", "CS 357", "CS 361", "CS 374", "CS 421"]

    df_cs_stats =  ["CS 124", "CS 128", "CS 173", "CS 222", "CS 225",
    "MATH241", "CS 233", "CS 341", "CS 340",  "CS 357",
    "MATH 257", "MATH 415", "MATH 416", "CS 374", "CS 421",
    "STAT 107", "STAT 200", "STAT 212", "STAT 400",
    "STAT 410", "STAT 425", "STAT 426"]

    df_cs_astronomy =  ["CS 124", "CS 128", "CS 173", "CS 222",
    "CS 225",  "CS 233", "CS 341", "CS 340", "STAT 200",
    "STAT 212", "CS 361", "CS 374", "CS 421", "MATH 221",
    "MATH 220", "MATH 225", "MATH 257", "MATH 231",
    "PHYS 211", "PHYS 212", "MATH 241","ASTR 210", "ASTR 310",
    "ASTR 404", "ASTR 405", "ASTR 406", "ASTR 414"]

    df_cs_ggis = ["CS 124", "CS 128", "CS 173", "CS 222",
    "CS 225", "CS 211", "CS 233", "CS 341", "CS 340",
    "CS 374", "CS 421", "MATH 231", "MATH 257", "STAT 200",
    "STAT 212", "CS 361", "GGIS 371", "GGIS 379", "GGIS 380"]

    major = ""
    with open("store_user_input.txt", "r", encoding="utf8") as curr_file:
        major = curr_file.readline().rstrip()
    print("in checkboxes(): ", major)
    cs_req = []
    if major == "CS":
        cs_req = df_cs
    elif major == "Stats & CS":
        cs_req = df_cs_stats
        # return render_template("class.html", cs_req= df_cs_stats)
    elif major == "CS + GGIS":
        cs_req = df_cs_ggis
    elif major == "CS + ASTRO":
        cs_req = df_cs_astronomy
    curr_file.close()
    return render_template("class.html", cs_req= cs_req)

@app.route('/class', methods=["POST"])
def classes():
    "'Handle return of checkboxes'"
    classes_taken = request.form["class"]
    print("classes_taken: ", classes_taken)

    with open("store_user_input.txt", "a", encoding="utf8") as curr_file:
        curr_file.write(classes_taken)
        curr_file.write("\n")
    curr_file.close()
    return render_template("class.html")
