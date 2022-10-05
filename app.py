'''this module renders a template and has two functions (testing for emily 10/1/22)'''

# import os
# from datetime import datetime, timedelta, time
from flask import Flask, render_template, request
# request, jsonify
# import requests

app = Flask(__name__)

# Route for "/" (frontend):
@app.route('/')
def index():
    "'this function is for index.html'"
    return render_template("index.html")


@app.route('/class', methods=["POST"])
def main():
    "'this function is for main'"
    course = request.form["course"]
    print("course: ", course)
    print("hi")
    #backend file
