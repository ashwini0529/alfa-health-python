import sqlite3
import json
with open('juice.json') as data_file:
	data = json.load(data_file)
print data