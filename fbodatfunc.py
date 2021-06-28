from sqlalchemy import create_engine
import urllib

def chunker(seq, size):
    # from http://stackoverflow.com/a/434328
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def connectdb():
    quoted = urllib.parse.quote_plus(
     "Driver={ODBC Driver 17 for SQL Server};Server=tcp:fbonextdb.database.windows.net,1433;Database=FBONextDB;Uid=fbodbadmin;Pwd={!1BHeN3?rt<q78i2};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30")
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
    return engine