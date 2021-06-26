from flask import Flask
import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine
import urllib
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import blob_service
from fbodatfunc import chunker
from fbodatfunc import connectdb
import time
from io import StringIO


app = Flask(__name__)

@app.route("/compdata")
def compdata():
    try:
        STORAGEACCOUNTURL= "https://fbostoracct.blob.core.windows.net/"
        STORAGEACCOUNTKEY= "qcNEwmBQtcOOQAgDdHLwpC02urawMOxpYNHvkUtK4FKiWcuuAxCiZpLMrD1uE5QQl/etZoxk85cCICGsznlBCA=="
        #LOCALFILENAME= "Opportunity-2.csv"
        CONTAINERNAME= "fbo-blob"
        BLOBNAME= "Opportunity-2.csv"
        #download from blob
        #t1=time.time()
        #blob_service_client_instance = BlobServiceClient(account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)
        #blob_client_instance = BlobServiceClient.get_blob_client(CONTAINERNAME, BLOBNAME, snapshot=None)
        #with open(LOCALFILENAME, "wb") as my_blob:
            #blob_data = blob_client_instance.download_blob()
            #blob_data.readinto(my_blob)
        #t2=time.time()
        blobstring = blob_service.get_blob_to_text(CONTAINERNAME,BLOBNAME).content
        df=pd.read_csv(StringIO(blobstring))
        return df
    except Exception as e:
        print("Unable to read file", e)


@app.route("/test")
def hello():
    return "API Test Successful!"