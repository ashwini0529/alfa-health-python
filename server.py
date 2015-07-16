from flask import Flask, session, render_template
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

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port= port)
