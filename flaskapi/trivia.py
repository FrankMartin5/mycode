#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
# @app.route("/home")
def index():
    return render_template("trivia.html")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)