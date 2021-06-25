from flask import Flask
import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine
import urllib
from azure.storage.blob import BlobServiceClient
from fbodatfunc import chunker
from fbodatfunc import connectdb
import time

app = Flask(__name__)


@app.route("/test")
def hello():
    return "Hello, Test!"

@app.route("/test2")
def hello2():
    return "Hello, Test2!"