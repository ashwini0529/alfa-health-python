import sqlite3
import json
with open('workout.json') as data_file:
	data = json.load(data_file)
conn = sqlite3.connect('content.db')
count=1
for i in data:
	while(count<874):
		ids = str(data[count-1]['id'])
		conn.execute("update workout set ids = ? where id = ?",[ids,count]) 
		conn.commit()
		count=count+1
print 'done'