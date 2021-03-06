#!/usr/bin/python
#THis script creates a Flask server, and serves the index.html out of the templates folder.#It also creates an app route to be called via ajax from javascript in the index.html to query
#the database that is being written to by tempReader.py, and return the data as a json object.

#This was written for Joshua Simons's Embedded Linux Class at SUNY New Paltz 2020
#And is licenses under the MIT Software License

#Import libraries as needed
from flask import Flask, render_template, jsonify, Response
import sqlite3 as sql
import json
import os

#Globals
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('/index.html')

@app.route("/SQLData_A")
def chartData_A():
#	os.system('clear')
	con = sql.connect('log/accelLog.db')
	cur = con.cursor()
	con.row_factory = sql.Row
	cur.execute("SELECT * FROM accelLog")
	dataset = cur.fetchall()
#	print (dataset)
	chartData = []
	for row in dataset:
		chartData.append({"Date": row[0], "X_Axis": float(row[1]), "Y_Axis": float(row[2]), "Z_Axis": float(row[3])})
	return Response(json.dumps(chartData), mimetype='application/json')

@app.route("/SQLData_M")
def chartData_M():
#       os.system('clear')
	con = sql.connect('log/mtLog.db')
	cur = con.cursor()
	con.row_factory = sql.Row
	cur.execute("SELECT * FROM mtLog")
	dataset = cur.fetchall()
#       print (dataset)
	chartData = []
	for row in dataset:
		chartData.append({"Date": row[0], "Motor_1": float(row[1]), "Motor_2": float(row[2]), "Motor_3": float(row[3])})
	return Response(json.dumps(chartData), mimetype='application/json')

@app.route("/button")
def button():
	os.system('python3 ../iot/blink.py')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=2020, debug=True)

