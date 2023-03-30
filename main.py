from flask import Flask, request, Response, abort
import os

app = Flask(__name__)

@app.route('/')
def index_action():
    return "App Running"

@app.route('/list')
def list_action():
    import kfp

    # the namespace in which you deployed Kubeflow Pipelines

    # the KF_PIPELINES_SA_TOKEN_PATH environment variable is used when no `path` is set
    # the default KF_PIPELINES_SA_TOKEN_PATH is /var/run/secrets/kubeflow/pipelines/token
#     credentials = kfp.auth.ServiceAccountTokenVolumeCredentials(path=None)

    client = kfp.Client(host="http://ml-pipeline-ui-artifact:80")

    print(client.list_experiments())
    sleep(90000000000)

if __name__ == '__main__':
    app.run()