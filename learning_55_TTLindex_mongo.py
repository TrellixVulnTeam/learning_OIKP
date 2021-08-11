#Configuration

from pymongo import MongoClient
from pprint import pprint
import pytz
import datetime

connection = MongoClient("localhost",27017)
db = connection.python


#Creating index
db.login.create_index([("last_updated",1)],expireAfterSeconds =10)
#It will make documents with "last_updated" field disappear in 10 secs.

#Inserting data
#Don't forget to put datetime type data.
KST = pytz.timezone('Asia/Seoul')
times = datetime.datetime.now(KST)

db.login.insert_many([{"ID":"Hey","last_updated":times},
                      {"ID":"I'm","last_updated":times},
                      {"ID":"here","last_updated":times},
                      {"ID":"can","last_updated":times},
                      {"ID":"you","last_updated":times},
                      {"ID":"hear","last_updated":times},
                      {"ID":"me","last_updated":times}])


for i in db.login.find():
    pprint(i)


