from flask import Flask
app = Flask(__name__)

@app.route("/test")
def hello():
    return "Hello, Test!"

@app.route("/test2")
def hello():
    return "Hello, Test2!"