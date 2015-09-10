import json
import urllib2
import sqlite3
from flask import g, Flask
import os

DATABASE = 'content.db'

with open('exercise.json') as data_file:
    data = json.load(data_file)

with open('workout.json') as data_file:
    work_json = json.load(data_file)

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
# code to render json
@app.route('/workout')
def work():
    lis = []
    for i in work_json:
        name = i.keys()[0]
        muscle_worked = i[name]['Main Muscle Worked']
        id = i[name]['id']
        force = i[name]['Force']
        level = i[name]['Level']
        rating = i[name]['Your Rating']
        pic_right = i[name]['pic_right']
        guide = '\n'.join(i[name]['guide'])
        equipment = i[name]['Equipment']
        link = i[name]['link']
        pic_left = i[name]['pic_left']
        sport = i[name]['Sport']
        type_ = i[name]['Type']
        mech_type = i[name]['Mechanics Type']
        dic = json.loads(json.dumps({'name':name,'muscles_worked':muscle_worked,'force':force,'rating':rating,'level':level,'pic_right':pic_right,'mech_type':mech_type,'equipment':equipment,'link':link,'pic_left':pic_left,'Sport':sport,'type':type_,'guide':guide},indent=4))
        # if(type_==" Stretching"):
        #     s_t = i[name]['Stretch Type']
        #     g.db.execute('insert into workout (stretch_type) values (?)',[s_t])
        #     g.db.commit()
        lis.append(dic)
    with open('workout2.json','w') as outfile:
        json.dump(lis, outfile)

    return 'ha'

@app.route('/exercise')
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
# to check if the data went right
@app.route('/see')
def see():
    sel = g.db.execute('select * from workout where id = 1')
    for i in sel.fetchall():
        return "<img src='%s'/>" % i[6]
    return 'hey'

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5001))
    ## keep the debug mode on in flask - it helps
    app.run(host='0.0.0.1', port= port, debug=True)