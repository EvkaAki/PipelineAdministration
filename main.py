from flask import Flask, request, Response, abort
import os

app = Flask(__name__)

@app.route('/')
def index_action():
    return "App Running"

@app.route('/list')
def list_action():
    print('hello')

if __name__ == '__main__':
    app.run()