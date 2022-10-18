'''this module renders a template and has two functions (testing for emily 10/1/22)'''

# import os
# from datetime import datetime, timedelta, time
from flask import Flask, render_template, request
# request, jsonify
# import requests

app = Flask(__name__)

# Route for "/" (frontend):
#@app.route('/')
# def index():
#   return render_template("index.html")

# Comment
#comment


@app.route('/')
def dropdown():
    """Function printing python version."""
    cs_req = ["CS + GIS", "CS + ASTRO", "CS + STAT", "CS"]
    return render_template('index.html', cs_req=cs_req)

@app.route('/major', methods=["POST"])
def main():
    """Function printing python version."""
    app.run()
    return render_template('index.html')
#backend file

def index():
    """Function printing python version."""
    return render_template("index.html")
    "'this function is for main'"
    major = request.form["major"]
    print("major: ", major)
    #Have backend team return the info in this function
    #backend file
    return render_template("index.html")

@app.route('/class', methods=["POST", "GET"])
def classes():
    df_cs =  ["CS124", "CS128", "CS173", "MATH241", "MATH257",
    "CS210", "CS211", "CS222", "CS225", "CS233", "CS341", "CS357", "CS361", "CS374", "CS421"]
    df_cs_stats =  ["CS124", "CS128", "CS173", "CS222", "CS225",
    "MATH241", "CS233", "CS341", "CS340",  "CS357", "MATH257", "MATH415", "MATH416", "CS374",
    "CS421", "STAT107", "STAT200", "STAT212", "STAT400", "STAT410", "STAT425", "STAT426"]
    df_cs_astronomy =  ["CS124", "CS128", "CS173", "CS222",
    "CS225",  "CS233", "CS341", "CS340", "STAT200", "STAT212", "CS361", "CS374", "CS421", "MATH221",
    "MATH220", "MATH225", "MATH257", "MATH231", "PHYS211", "PHYS212", "MATH241",
    "ASTR210", "ASTR310", "ASTR404", "ASTR405", "ASTR406", "ASTR414"]
    place_holder = ""
    if (place_holder == "CS"):
        return render_template("class.html", cs_req= df_cs)
    elif (place_holder == "CS + STATS"):
        return render_template("class.html", cs_req= df_cs_stats)
    else:
        return render_template("class.html", cs_req= df_cs_astronomy)





