from flask import Flask
from flask_restful import Api,Resource,reqparse
import trans_mongo


app =  Flask(__name__)
api = Api(app)

payment_agrs = reqparse.RequestParser()
payment_agrs.add_argument("interest",type=str,help="Interest is required",required=True)

class payment_info(Resource):
    a = trans_mongo.MongoTrans()
    def post(self,info):
        inventory = self.a.list_items()
        inventory.pop("_id")
        return inventory
    def get(self,info):
        inventory = self.a.list_items()
        inventory.pop("_id")
        return inventory

    def put(self,info):
        args = payment_agrs.parse_args().get("interest")
        self.a.transaction(args)
        return "Transaction succeeded!", 201

api.add_resource(payment_info,"/payment_info/<string:info>")

@app.route('/')
def hi():
    return "Hey!"

@app.route('/list_of_item')
def list():
    a = trans_mongo.MongoTrans()
    inventory = a.list_items()
    inventory.pop("_id")
    return inventory



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)



