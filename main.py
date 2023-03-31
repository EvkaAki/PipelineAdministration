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
#     client = kfp.Client(host="http://ml-pipeline.kubeflow.svc.cluster.local:8888")
#
#     print(client.list_experiments())
#     sleep(90000000000)


if __name__ == '__main__':
#     response = requests.get("http://ml-pipeline:8888/apis/v1beta1/healthz")
#     print(response)
#     print(response.json())
#     params = {'resource_reference_key.type':'NAMESPACE', 'resource_reference_key.id' : 'admin'}
#     response = requests.get("http://ml-pipeline:8888/apis/v1beta1/experiments", params=params)
#     print(response)
#     print(response.json())
#     app.run()
    f = open("/var/run/secrets/kubernetes.io/serviceaccount/token", "r")
    token = f.readline()
    client = kfp.Client(host="http://ml-pipeline.kubeflow.svc.cluster.local:8888", existing_token=token)
    print(client.list_experiments())
    app.run()

