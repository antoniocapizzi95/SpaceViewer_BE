from flask import Flask, jsonify
import requests, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def key():
    k = '' #insert NASA Open API token
    j = jsonify(key = k)
    return j

@app.route("/rebuildStaging", methods=['POST'])
def rebuildStaging():
    jenkinsServer = '' #insert name:token@serveraddress:port from Jenkins
    project = '' #insert the name of jenkins project
    input_id = '' #insert the input id from jenkins pipeline
    buildToken = '' #insert build token from jenkins pipeline
    r = requests.get(
        'http://'+jenkinsServer+'/job/'+project+'/wfapi/runs')
    c = json.loads(r.content)

    latest = c[0]['id']
    status = c[0]['status']
    if(status == 'PAUSED_PENDING_INPUT'):
        r2 = requests.post(
            'http://'+jenkinsServer+'/job/'+project+'/'+latest+'/input/'+input_id+'/proceedEmpty')
        run = 'http://'+jenkinsServer+'/job/'+project+'/build?token='+buildToken
        r2 = requests.post(run)
    if(status == 'SUCCESS' or status == 'ABORTED' or status == 'FAILED'):
        run = 'http://' + jenkinsServer + '/job/' + project + '/build?token=' + buildToken
        r2 = requests.post(run)
    k = 'ok'
    j = jsonify(status=k)
    return j


if __name__ == '__main__':
    app.run(port=5001)
