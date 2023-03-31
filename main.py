from flask import Flask, request, Response, abort
import os
import requests


app = Flask(__name__)

@app.route('/')
def index_action():
    return "App Running"

@app.route('/list')
def list_action():
    print('list')


if __name__ == '__main__':
    response = requests.get("http://ml-pipeline:8888/apis/v1beta1/healthz")
    print(response)
    print(response.json())
    app.run()
