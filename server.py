from flask import Flask, session, render_template
import requests
import json
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/<reg>')
def dump(reg):
    error = None
    url = 'http://apius.faceplusplus.com/v2/detection/detect?api_key=e2707513a30c55f950583457e8845ec1&api_secret=9cWd6oDOtFMmqhGT7mwPKphefakx52tI&url=https%3A%2F%2Facademics.vit.ac.in%2Fstudent%2Fview_photo_2.asp%3Frgno%3D'+str(reg)+'&attribute=age%2Cgender%2Crace%2Csmiling%2Cpose%2Cglass'
    r = requests.get(url)
    return json.dumps(r.json(), indent = 4)

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port= port)
