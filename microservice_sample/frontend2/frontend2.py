import os
import requests
from flask import Flask
app = Flask(__name__)

def get_counter(counter_endpoint):
    counter_response = requests.get(counter_endpoint)
    return counter_response.text

def increase_counter(counter_endpoint):
    counter_response = requests.post(counter_endpoint)
    return counter_response.text

def get_response(response_endpoint):
    response_backend2 = requests.get(response_endpoint)
    return response_backend2.text

def get_another_response(response_endpoint):
    response_backend2 = requests.post(response_endpoint)
    return response_backend2.text


@app.route('/')
def hello_world():
    counter_service = os.environ.get('COUNTER_ENDPOINT', default="https://localhost:5000")
    counter_endpoint = f'{counter_service}/api/counter'

    response_service = os.environ.get('RESPONSE_ENDPOINT', default="https://localhost:5100")
    response_endpoint = f'{response_service}/api/response'

    counter = get_counter(counter_endpoint)

    increase_counter(counter_endpoint)

    response = get_response(response_endpoint)

    return f"""Hello, World!

You're visitor number {counter} in here! message from: {response}  \n\n"""
