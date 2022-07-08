#!/usr/bin/python3

import sqlite3 as sql
import json
import pprint

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/addpoke", methods = ["POST"])
def addpoke():
    try:
        nm = request.form['nm']
        typ = request.form['typ']
        lvl = request.form['lvl']

        with sql.connect("database.db") as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO pokedex (name,type,level) VALUES (?,?,?)",(nm,typ,lvl))
            conn.commit()
        msg = "Pokemon Added Successfully"
    except:
        conn.rollback()
        msg = "Error adding Pokemon"
    finally:
        conn.close()
        return render_template("results.html", msg = msg)

@app.route("/showpoke")
def show_pokemon():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row

    cur = conn.cursor()
    cur.execute("SELECT * from pokedex")

    rows = cur.fetchall()

    return render_template("showpoke.html", rows = rows)

@app.route("/showjson")
def show_json():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row

    cur = conn.cursor()
    cur.execute("SELECT * from pokedex")
    row_headers=[x[0] for x in cur.description]

    data = cur.fetchall()
    json_data=[]
    for result in data:
        json_data.append(dict(zip(row_headers,result)))

    return jsonify(json_data)

if __name__ == "__main__":
    try:
        conn = sql.connect("database.db")
        print("Opened db successfully")

        conn.execute('CREATE TABLE IF NOT EXISTS pokedex (name TEXT, type TEXT, level INT)')
        print("Table created successfully")
        conn.close()
        app.run(host="0.0.0.0", port=2224, debug = True)
    except:
        print("App failed on boot")