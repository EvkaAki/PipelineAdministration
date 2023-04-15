from flask import Flask, request, Response, abort
import os
import kfp


app = Flask(__name__)

@app.route('/')
def index_action():
    return "App Running"

@app.route('/list')
def list_action():
    print('list')



if __name__ == '__main__':
    credentials = kfp.auth.ServiceAccountTokenVolumeCredentials(path=None)
    client = kfp.Client(host="http://ml-pipeline.kubeflow.svc.cluster.local:8888", credentials=credentials)
    print(client.list_experiments(namespace="admin"))
    app.run()

