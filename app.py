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

@app.route("/oppdata")
def oppdata():
    #df = [['Test1',1,'x'],['Test2',2,'y']]
    return 'Dataframe Created successfully'


@app.route("/test")
def hello():
    return "API Test Successful!"