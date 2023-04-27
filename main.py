from flask import Flask, request, Response, abort, render_template
import os
import kfp
import pprint


app = Flask(__name__)

@app.route('/')
def researcher_action():
    credentials = kfp.auth.ServiceAccountTokenVolumeCredentials(path=None)
    client = kfp.Client(host="http://ml-pipeline.kubeflow.svc.cluster.local:8888", credentials=credentials)
    namespace = client.get_user_namespace()
    pipelines = client.list_pipelines(namespace=namespace)
    # return render_template('index.html')
    return str(pipelines)


@app.route('/admin')
def admin_action():
    credentials = kfp.auth.ServiceAccountTokenVolumeCredentials(path=None)
    client = kfp.Client(host="http://ml-pipeline.kubeflow.svc.cluster.local:8888", credentials=credentials)
    namespace = client.get_user_namespace()

    # return render_template('index.html')
    return 'tralo'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3500, debug=True)