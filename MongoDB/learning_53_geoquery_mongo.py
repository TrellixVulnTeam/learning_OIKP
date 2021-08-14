from pymongo import MongoClient


class mongo:
    db = MongoClient("localhost",27017).python
    col = db.nei

    def insert(self):
        for i in range(101):
            for j in range(101):
                self.col.insert_one({"xy":[i,j]})

    def query_for_nei(self,query,projection):
        cur = self.col.find(query,projection)
        a = cur.next()

        return a['geometry']

    def query_for_res(self,query,projection):
        cur = self.db.res.find(query,projection)
        lst = []
        for i in cur:
            lst.append(i['name'])

        print(" / ".join(lst))


if __name__ == '__main__':
    mongo_handling = mongo()
    #$near query
    #query = {"xy":{"$near":[5.5,25]}}

    #$box query
    #query = {"xy": {"$within":{"$box": [[5.5, 25],[6.5,6.5]]}}}

    #구형쿼리
    #query = {"xy": {"$within":{"$center": [[25, 25],5]}}}

    #query = {"xy": {"$near": [5.5, 25]}}


    #GEOquery - 구역정보 뽑아오기
    user_pos = [-73.93554,40.6800]
    query,projection = ({"geometry":{"$geoIntersects":{"$geometry":{"type":"Point","coordinates":user_pos}}}},{"_id":0,"geometry":1})
    geometry = mongo_handling.query_for_nei(query, projection)


    #GEOwithin - 해당 구역에 무엇이 얼마나 있는지 알아오기.
    query1, projection1 = (
    {"location": {"$geoWithin": {"$geometry": geometry}}},
    {"_id": 0, "name": 1})


    #범위를 지정하여 찾기 - centerSphere -> 경계를 그려주어야!
    query2 , projection2 = (
        {"location":{"$geoWithin":{"$centerSphere" : [[-73.93414657,40.82302903],5/3963.2]}}},{"_id":0,"name":1}
    )

    #범위 지정하여 찾기
    query3, projection3 = (
        {"location": {"$nearSphere" : {
            "$geometry": {
                "type" : "Point",
                "coordinates":[-73.93414657, 40.82302903]
            },
            "$maxDistance": 300
        }
        }},
        {"_id": 0, "name": 1}
    )

    mongo_handling.query_for_res(query3,projection3)


