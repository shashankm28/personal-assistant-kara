# MongoDB connection

import pymongo

db_client = pymongo.MongoClient('localhost', 27017)

db_list = db_client.list_database_names()
if "mydatabase" in db_list:
    print ("DB exists.")
else:
    print ("DB does not exist.")