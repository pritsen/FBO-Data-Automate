from flask import Flask
import pandas as pd
from pandas.core.frame import DataFrame
from tqdm import tqdm
from sqlalchemy import create_engine
import urllib
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
    #url="https://drive.google.com/uc?export=download&confirm=mrxU&id=1a0w7rQhuib8jGSf7g2ovd-sDmUnXPMhX"
    #s=requests.get(url).content
    df=pd.read_csv("OpportunityData-3.csv", encoding="1252")
    quoted = urllib.parse.quote_plus(
        "Driver={ODBC Driver 17 for SQL Server};Server=tcp:fbonextdb.database.windows.net,1433;Database=FBONextDB;Uid=fbodbadmin;Pwd={!1BHeN3?rt<q78i2};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=3000")
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
    df.to_sql("OPPORTUNITY_TEST", con=engine, schema="FBO", if_exists="append", index=False)
    return "Data Insert Successful"


@app.route("/test")
def hello():
    print("Test", file=sys.stderr)
    return "API Test Successful!"