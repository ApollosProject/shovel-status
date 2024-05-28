import requests
from flask import Flask

app = Flask(__name__)


@app.route("/status")
def hello_world():
    return "<p>Hello, World!</p>"
