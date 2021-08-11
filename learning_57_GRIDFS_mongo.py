#configuration
from pymongo import MongoClient
from pprint import pprint

#GridFS사용을 위해서 필요한 모듈.
import gridfs


#1 connect
client = MongoClient("localhost",27017)
db = client.python
fs = gridfs.GridFS(db)


#2 Pickling image(to make it binary)

import pickle
apple = pickle.dumps("some images")


#저장하는 것과 동시에 해당 file에 대한 Objectid를 리턴해준다.
file_id = fs.put(apple,filename="apple")


print(fs.list())

#load
pickle.loads(fs.get(file_id).read())