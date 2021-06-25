from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route("/test")
def hello():
    return "Hello, Test!"

@app.route("/test2")
def hello2():
    return "Hello, Test2!"