import sqlite3
import json
with open('workout.json') as data_file:
	data = json.load(data_file)
conn = sqlite3.connect('content.db')
count=1
for i in data:
	if(count<874):
		ids = str(i['id'])
		conn.execute("update workout set rating = 1") 
		conn.commit()
		count=count+1
print 'done'