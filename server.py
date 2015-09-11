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
        height=height*height
        bmi=(weight/(height))
    	return jsonify(bmi= bmi,bmr=bmr)

@app.route('/workout', methods=['GET','POST'])
def work():
    typ = ' '+request.args.get('type','%')
    mech_type = ' '+request.args.get('mech_type','%')
    muscles_worked = ' '+request.args.get('muscles','%')
    instrument = ' '+request.args.get('instrument','%')
    lis = []
    if(typ==' %' and mech_type==' %' and muscles_worked==' %' and instrument==' %'):
        return jsonify(workout=lis)
    sel = g.db.execute("select * from workout where type LIKE ? AND muscle_worked LIKE ? AND mech_type LIKE ? AND equipment LIKE ?",[typ,muscles_worked,mech_type,instrument])

    for row in sel.fetchall():
        dic = json.loads(json.dumps({'id':row[16],'name':row[1],'muscles_worked':row[2],'max_reps': 8,'min_reps':2,'tags':[{"be_healthy":1,"tone_up":1,"loose_weight":1,"get_filter":1,"stamming":1}] ,'force':row[3],'rating':int(row[4]),'level':row[5],'pic_right':row[6],'mech_type':row[7],'equipment':row[8],'link':row[9],'pic_left':row[10],'Sport':row[11],'type':row[12],'guide':row[14],'global_rating':1400,'strech_type': row[13],"exercise_rating":1},indent=4))
        lis.append(dic)
    return jsonify(workout=lis)

#########################ADD ID#########################

with open('workout.json') as data_file:
    data = json.load(data_file)

@app.route('/add')
def exer():
    for i in data:
        if(len(i['mechanics'])>0):
            ids=''.join(i['id'])
            mechanics = ''.join(i['mechanics'])
            difficulty = i['difficulty'][1]
            detailed_muscle = ''.join(i['detailed_muscle'])
            name = ''.join(i['exerciseName'])
            equipments = ''.join(i['equipments'])
            group = ''.join(i['other_muscle_group'])
            muscle = ''.join(i['muscle'])
            type = ''.join(i['type'])
            procedure = ''.join(i['procedure'])
            g.db.execute('update workout set (mechanics,difficulty,detailed_muscle,exercise_name,equipments,other_muscle_group,muscle,type,procedure,ids) values (?,?,?,?,?,?,?,?,?,?)',[mechanics,difficulty,detailed_muscle,name,equipments,group,muscle,type,procedure,ids])
            g.db.commit()
    return 'yo'
########################################################
if __name__ == '__main__':
    port = int(os.environ.get('PORT',5003))
    port = int(os.environ.get('PORT',5000))
    ## keep the debug mode on in flask - it helps
    app.run(host='0.0.0.0', port= port, debug=True)
