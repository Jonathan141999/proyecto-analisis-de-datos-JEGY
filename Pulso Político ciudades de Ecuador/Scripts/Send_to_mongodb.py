from pymongo.errors import ConnectionFailure
import pymongo 
from argparse import ArgumentParser
import requests
from bson import json_util, ObjectId
import json
import couchdb
import dns

CLIENT = pymongo.MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as e:
    print('MongoDB connection: failed', e)
    
client = pymongo.MongoClient("mongodb+srv://esfot_prueba:esfotesfot@cluster0.tddsj.mongodb.net/ciudades?retryWrites=true&w=majority")
DBm = client.get_database('loja')
DBma = DBm.scifi


try:
    client.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as e:
    print('MongoDB Atlas connection: failed', e)
    

DBS = ['ciudades']

for db in DBS:
    if db not in ('admin', 'local','config'):  
        cols = CLIENT[db].list_collection_names()  
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    documents = json.loads(json_util.dumps(x))
                    DBma.insert_one(documents)
                    print("saved in mongo atlas")

                except TypeError as t:

                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  
                    continue  
                except Exception as e:
                    raise e