import sqlite3
import json
with open('workout.json') as data_file:
	data = json.load(data_file)
conn = sqlite3.connect('content.db')
count=1
id= str(data[0]['id'])
print id
conn.execute('update workout set ids = "skdfajkfadfafd" where id = 1')
#conn.execute('INSERT into  workout (ids) values (?)',[id])
#for row in y:
#   print "ID = ", row[16]
conn.commit()
print 'done'