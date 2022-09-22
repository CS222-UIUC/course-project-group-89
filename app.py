from flask import Flask, render_template, request, jsonify
import os
import requests
from datetime import datetime, timedelta, time

app = Flask(__name__)

# Route for "/" (frontend):
@app.route('/')
def index():
  return render_template("index.html")

def main():
  print("hi")
#backend file
