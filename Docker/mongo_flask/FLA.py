from flask import Flask
import pymongo

app = Flask(__name__)


@app.route('/mongo',methods=['POST'])
def mongo():
    connection = pymongo.MongoClient("mongo-server",27017)
    db = connection.prac
    col = db.visits
    col.update_one({"visits":{"$exists":1}},{"$inc":{"visits":1}},upsert=True)
    result = col.find_one({"visits":{"$exists":True}})['visits']
    return result




@app.route("/")
def hello(): 
    return f"Hey! this site has been visited {mongo()}times!"


if __name__ == "__main__":
    app.run(host="web-app",debug=True)

