from flask import Flask, jsonify, session, render_template, g
## you did not import "request"
from flask import request
import requests
import json
import os
import sqlite3

DATABASE = 'content.db'
app = Flask(__name__)
DEBUG = True

app.secret_key = os.urandom(24)
app.config.from_object(__name__)
app.config.from_envvar('TRAVELSAFE_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def dump():
    error = None
    url = 'https://api.myjson.com/bins/4f6yu'
    r = requests.get(url)
    return json.dumps(r.json(), indent = 4)

@app.route('/profile')
def profile():
	error = None
	url = 'https://api.myjson.com/bins/59mna'
	r = requests.get(url)
	return json.dumps(r.json(), indent = 4)

@app.route('/exerciseList')
def exerciseList():
	error = None
	url = 'https://api.myjson.com/bins/ot06'
	r = requests.get(url)
	return json.dumps(r.json(), indent = 4)
@app.route('/diet')
def diet():
	error = None
	url = 'https://api.myjson.com/bins/4hz9y'
	r = requests.get(url)
	return json.dumps(r.json(), indent = 4)
@app.route('/calculate', methods=['GET'])
def foo():
	## the get request should be "/calculate?age=23&wight=99"
	return str(request.args.get("age",type=int)) + str(request.args.get("weight",type=int))
@app.route('/try', methods=['GET'])
def variable():
	## the get request should be "/calculate?age=23&wight=99"
	height = request.args.get('height', 0, type=float)
    	weight = request.args.get('weight', 0, type=float)
    	age = request.args.get('age', 0, type=int)
    	gender = request.args.get('gender', 0, type=str)
    	if(gender=='male'):
            bmr=((10*weight)+(6.25*height)-(5*age)+5)
        elif(gender=='female'):
            bmr=((10*weight)+(6.25*height)-(5*age)-161)
        height=height/100
        ht=height*height
        bmi=(weight/(ht))
    	return jsonify(bmi= bmi,bmr=bmr)

@app.route('/workout')
def work():
    sel = g.db.execute('select * from workout limit 5')
    lis = ''
    for row in sel.fetchall():
        lis = lis + row[1] + ' ' + row[2] + ' ' + row[3] + ' ' + row[5] + ' ' + row[8] + ' ' + row[11]
        lis = lis+'<br />'
    return lis

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    ## keep the debug mode on in flask - it helps
    app.run(host='0.0.0.0', port= port, debug=True)
