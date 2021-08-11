#1configuration

import numpy as np
import pandas as pd
from pymongo import MongoClient
from pprint import pprint

connection = MongoClient("localhost",27017)
db = connection.python


#2 Creating capped-collection


# 실제 몽고디비에서 해야하는 방식 db.createCollection("limited",{"capped":True,"size":100000})
#파이몽고로 해야하는 방식
db.create_collection("limited",capped=True,size=100000,max=3)


#3 Inserting data
db.limited.insert_one({"name":"Oracle","age":19})
db.limited.insert_one({"name":"Json","age":20})
db.limited.insert_one({"name":"Mongo","age":50})
db.limited.insert_one({"name":"Python","age":13})

#check
for i in db.limited.find():
    print(i)
