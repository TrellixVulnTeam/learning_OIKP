from pymongo import MongoClient
import pprint
from bson.code import Code


#Connect
client = MongoClient('localhost',27017)
db = client.test01


def geo():
    #db.pro3.create_index({"location": "2dsphere"})
    pr = db.pro3.aggregate([{"$geoNear": {
        "spherical": True,
        "maxDistance": 500,
        "near": {"type": "Point",
                 "coordinates": [126.78082573200001,37.49944304533334, ]},
        "distanceField": "distance",
        "key": "location"}}])
    for i in pr:
        print(i)


    #Insert new document

def Agg_MR():
    #AGGREGATE
    for i in db.places.aggregate([{"$project":{"manu_price":1,"place":1,"_id":0}},{"$group":{"_id":"$place", "price":{"$avg":"$manu_price.Americano"}}}]):
        print(i)


    #MAP REDUCE
    mr = Code("""function mymap(){
        if (this.manu_price.Americano != null){
        emit(this.place,{manu_price:this.manu_price.Americano})};
    }""")

    red = Code("""function myred(key,values){
        var result = {price :0};
        var cnt = 0;
        values.forEach(function(v){
            result.price += v.manu_price;
            cnt +=1;
        })
        result.price /= cnt;
        return result;
    }""")
    db.places.map_reduce(mr,red,"res5")
    for i in db.res5.find():
        pprint.pprint(i)


def javacode():
    a = db.product.distinct("price")
    for i in a:
        db.product.delete_many({"price":i},{"justOne":True})

    for i in db.product.find():
        print(i)
javacode()
