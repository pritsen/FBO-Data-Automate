from flask import Flask
import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine
import urllib
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BaseBlobService
#from azure.storage.blob import blob_service
from fbodatfunc import chunker
from fbodatfunc import connectdb
import time
from io import StringIO


app = Flask(__name__)

@app.route("/oppdata")
def compdata():
    try:
        STORAGEACCOUNTURL= "https://fbostoracct.blob.core.windows.net/"
        account_name="fbostoracct"
        account_key="qcNEwmBQtcOOQAgDdHLwpC02urawMOxpYNHvkUtK4FKiWcuuAxCiZpLMrD1uE5QQl/etZoxk85cCICGsznlBCA=="
        STORAGEACCOUNTKEY= "qcNEwmBQtcOOQAgDdHLwpC02urawMOxpYNHvkUtK4FKiWcuuAxCiZpLMrD1uE5QQl/etZoxk85cCICGsznlBCA=="
        CONTAINERNAME= "fbo-blob"
        BLOBNAME= "OpportunityData-2.csv"
        LOCALFILENAME = "test.csv"
        t1=time.time()
        blob_service_client_instance = BlobServiceClient(account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)
        blob_client_instance = blob_service_client_instance.get_blob_client(CONTAINERNAME, BLOBNAME, None)
        with open(LOCALFILENAME, "wb") as my_blob:
            blob_data = blob_client_instance.download_blob()
            blob_data.readinto(my_blob)
            t2=time.time()
        print(("It takes %s seconds to download "+BLOBNAME) % (t2 - t1))
        df=pd.read_csv(LOCALFILENAME)
        #print(df)
        return df
    except Exception as e:
        return "Unable to read file" + e


@app.route("/test")
def hello():
    return "API Test Successful!"