from flask import Flask, request, Response, abort
import os
import kfp
import pprint


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
    app.run(host="localhost", port=3500, debug=True)


class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, env, resp):
        errorlog = env['wsgi.errors']
        pprint.pprint(('REQUEST', env), stream=errorlog)

        def log_response(status, headers, *args):
            pprint.pprint(('RESPONSE', status, headers), stream=errorlog)
            return resp(status, headers, *args)

        return self._app(env, log_response)

