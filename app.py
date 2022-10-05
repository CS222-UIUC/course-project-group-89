'''this module renders a template and has two functions (testing for emily 10/1/22)'''

# import os
# from datetime import datetime, timedelta, time
from flask import Flask, render_template
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
    cs_req = ["CS124", "CS128", "CS173", "MATH241", "MATH257",
    "CS210", "CS211", "CS222", "CS225", "CS233", "CS341",
    "CS357", "CS361", "CS374", "CS421"]
    return render_template('index.html', cs_req=cs_req)

def main():
    """Function printing python version."""
    app.run()
    return render_template('index.html')
#backend file

def index():
    """Function printing python version."""
    return render_template("index.html")
