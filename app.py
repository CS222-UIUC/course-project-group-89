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

@app.route('/')
def dropdown():
    """Function printing python version."""
    cs_req = ["CS + GIS", "CS+Astro", "CS + STAT", "CS"]
    return render_template('index.html', cs_req=cs_req)

@app.route('/major', methods=["POST"])
def main():
    "'this function is for main'"
    major = request.form["major"]
    print("major: ", major)
    #Have backend team return the info in this function
    #backend file
    return render_template("index.html")

def index():
    """Function printing python version."""
    return render_template("index.html")