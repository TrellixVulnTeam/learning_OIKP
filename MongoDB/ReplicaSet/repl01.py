from pymongo import MongoClient
from pymongo import ReadPreference



seed = "mongodb://localhost:27018,localhost:27018,localhost:27018"
client = MongoClient(seed,read_preference=ReadPreference.PRIMARY_PREFERRED)

db = client.prac

def write_with_concern(col,query):
    db[col].insert_one(query,{"writeConcern":{"w":"majority","wtimeout":100}})

def read_with_concern(col):
    for i in db[col].find():
        print(i)




if __name__ == '__main__':
    write_with_concern("python",{"id":1,"name":"chan"})
    read_with_concern("python")
