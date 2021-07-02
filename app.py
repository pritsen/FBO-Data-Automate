from flask import Flask
import pandas as pd
from tqdm import tqdm
from azure.storage.blob import BlobServiceClient
from fbodatfunc import chunker
from fbodatfunc import connectdb
import time
import sys
import logging
import io
import requests

app = Flask(__name__)

@app.route("/oppdata")
def oppdata():
    try:
        url="https://drive.google.com/uc?export=download&confirm=Sc8m&id=1a0w7rQhuib8jGSf7g2ovd-sDmUnXPMhX"
        s=requests.get(url).content
        c=pd.read_csv(io.StringIO(s.decode('1252')))
        return "Dataframe Creation Successful"
    except:
        return "Dataframe Creation Unsuccessful"


@app.route("/test")
def hello():
    print("Test", file=sys.stderr)
    return "API Test Successful!"