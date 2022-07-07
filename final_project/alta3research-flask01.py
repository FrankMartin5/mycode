#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info", methods = ["POST", "GET"])
def info():
    if request.method == "POST":
        try:
            nm = request.form['nm']
            hob = request.form['hob']

            with sql.connect("database.db") as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO students (name,hob) VALUES (?,?)",(nm,hob))
                conn.commit()
                msg = "Added Successfully"
        except:
            conn.rollback()
            msg = "Error during INSERT"
        finally:
            return render_template("results.html", msg = msg)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)