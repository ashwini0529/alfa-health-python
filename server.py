from flask import Flask, session, render_template
## you did not import "request"
from flask import request
import requests
import json
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

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
	
@app.route('/exerciseSample', methods=['GET'])
def exercise():
	num=request.args.get("id", type=int)
	if(num==1):
		url = "https://api.myjson.com/bins/4xk34"
		r=requests.get(url)
		return json.dumps(r.json(), indent=4)
	if(num==2):
		url = "http://api.myjson.com/bins/3su1c"
		r=requests.get(url)
		return json.dumps(r.json(), indent=4)
	if(num==3):
		url = "https://api.myjson.com/bins/vt68"
		r=requests.get(url)
		return json.dumps(r.json(), indent=4)
	if(num==4):
		url = "https://api.myjson.com/bins/24tjk"
		r=requests.get(url)
		return json.dumps(r.json(), indent=4)
	if(num==5):
		url = "https://api.myjson.com/bins/103hs"
		r=requests.get(url)
		return json.dumps(r.json(), indent=4)
	if(num==6):
		url = "https://api.myjson.com/bins/4mua8"
		r=requests.get(url)
		return json.dumps(r.json(), indent=4)
if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    ## keep the debug mode on in flask - it helps
    app.run(host='0.0.0.0', port= port, debug=True)
