from flask import Flask, request, Response, abort
import os
import kfp
import time


app = Flask(__name__)

@app.route('/')
def index_action():
    return "App Running"

@app.route('/list')
def list_action():
    print('list')
#     client = kfp.Client(host="http://ml-pipeline-ui-artifact:80")
#
#     print(client.list_experiments())
#     sleep(90000000000)


if __name__ == '__main__':
#     client = kfp.Client(host="http://ml-pipeline:8888")
#     print(client.list_experiments())
    time.sleep(90000000000)
    app.run()
