from flask import Flask, render_template, request, jsonify
import os
import requests
from datetime import datetime, timedelta, time

app = Flask(__name__)

# Route for "/" (frontend):
#@app.route('/')
# def index():
#   return render_template("index.html")

@app.route('/')
def dropdown():
    cs_req = ["CS124", "CS128", "CS173", "MATH241", "MATH257", "CS210", "CS211", "CS222", "CS225", "CS233", "CS341", "CS357", "CS361", "CS374", "CS421"]
    return render_template('index.html', cs_req=cs_req)

def main():
  app.run()
#backend file

