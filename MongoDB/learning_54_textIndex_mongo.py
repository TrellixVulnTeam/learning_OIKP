from pymongo import MongoClient
from pprint import pprint

# basic configuration

connection = MongoClient("localhost", 27017)
db = connection.python

# Creating index
# 텍스트 인덱스 생성(특수인덱스임.)
col = db.posts
col.create_index([("title", "text"), ("body", "text")])

# 인덱스 생성 확인
pprint(col.index_information())

# Inserting documents

# 자료 넣어보기

col.insert_many([{"title": "It's such a beatiful day!",
                  "body": "I woke up really early this morning, rubbing my eyes and when I looked my side, there was a beatiful girl as always yet opening her eyes. And yeah, as you can imagine it was my girlfriend."},
                 {"title": "Sombre day",
                  "body": "Stressful but figure no way out. When I first started learning this big data and deep learning stuff, I was really hopeful and energetic but as it has been wrapped out as freaking difficult, I realized this is not my thang. What should I do?"},
                 {"title": "Wanna learn big data?",
                  "body": "No can do. If you haven't studied yet and are older than 35, chances are you getting into a serious trouble GIVEN that you are not related to math, science or stuff."},
                 {"title": "Mongo DB!",
                  "body": "anybody wants to learn Mongo DB together?, if you do, plz let me know."},
                 {"title": "Good morning", "body": "What have you been up to guys?"}])



# 텍스트 인덱스 이용, 원하는 도큐먼트 쿼리하기.
for i in col.find({"$text": {"$search": "want"}}):
    pprint(i)

# Allocating weights

# 인덱스 제거후 웨이트 재분배
col.drop_index([("title", "text"), ("body", "text")])


# 웨이트값을 조정하여 새로 인덱스를 준다.
# 쉘에서와 다르게 weights는 키워드변수로 입력된다.
col.create_index([("title", "text"), ("body", "text")], weights={"title": 5, "body": 2})

for i in col.find({"$text": {"$search": "DB"}}):
    pprint(i)

# 결과는 똑같이 나오는 것 같은데... 연관성을 어떻게 판단하는가?


# Find documents relevant to what you want
# 연관성 판단. projection field에 $meta 파이프라인을 추가해서 textScore를 매겨준다.

what_you_want = "data"
wants_to_find, score = {"$text": {"$search": what_you_want}}, {"LEVEL": {"$meta": "textScore"}}

for i in col.find(wants_to_find, score):
    pprint(i)
