'" this module is for the app "'

import os
from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime, timedelta, time

app = Flask(__name__)

# Route for "/" (frontend):
@app.route('/')
def index():
    "'this function is for index.html'"
    return render_template("index.html")

def main():
    "'this function is for main'"
    print("hi")
    #backend file
