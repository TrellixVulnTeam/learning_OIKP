from flask import Flask
from flask_restful import Api,Resource,reqparse
from MongoDB.Transaction import _05_Transaction_local



app =  Flask(__name__)
api = Api(app)

payment_agrs = reqparse.RequestParser()
payment_agrs.add_argument("interest",type=str,help="Interest is required",required=True)

class payment_info(Resource):
    a = _05_Transaction_local.MongoTrans()
    def post(self,info):
        inventory = self.a.list_items()
        inventory.pop("_id")
        return inventory

    def put(self,info):
        args = payment_agrs.parse_args().get("interest")
        self.a.transaction(args)
        return "Transaction succeeded!"

api.add_resource(payment_info,"/payment_info/<string:info>")


if __name__ == '__main__':
    app.run(debug=True)




