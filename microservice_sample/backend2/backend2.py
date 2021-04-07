from random import randint
from time import sleep

from flask import request
from flask import Flask
app = Flask(__name__)


def get_response():
    return "from backend2"

def another_response():
    return "another response from backend2"

@app.route('/api/response', methods=['GET', 'POST'])
def counter():
    if request.method == 'GET':
        return get_response()
    elif request.method == 'POST':
        return another_response()
