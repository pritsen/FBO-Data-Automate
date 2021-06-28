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
    try:
        STORAGEACCOUNTURL= "https://fbostoracct.blob.core.windows.net/"
        STORAGEACCOUNTKEY= "qcNEwmBQtcOOQAgDdHLwpC02urawMOxpYNHvkUtK4FKiWcuuAxCiZpLMrD1uE5QQl/etZoxk85cCICGsznlBCA=="
        CONTAINERNAME= "fbo-blob"
        BLOBNAME= "Opportunity.csv"
        LOCALFILENAME = "opptest.csv"
        t1=time.time()
        blob_service_client_instance = BlobServiceClient(account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)
        blob_client_instance = blob_service_client_instance.get_blob_client(CONTAINERNAME, BLOBNAME, None)
        with open(LOCALFILENAME, "wb") as my_blob:
            blob_data = blob_client_instance.download_blob()
            blob_data.readinto(my_blob)
        t2=time.time()
        #print(("It takes %s seconds to download "+BLOBNAME) % (t2 - t1))
        df=pd.read_csv(LOCALFILENAME, encoding='1252')
        return "Dataframe Created Successfully"
    except:
        return "Dataframe Creation Unsuccessful"


@app.route("/test")
def hello():
    return "API Test Successful!"