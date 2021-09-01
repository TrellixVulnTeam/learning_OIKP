from flask import Flask
from flask_restful import reqparse, Api, Resource, marshal_with, fields, abort
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient


app =Flask(__name__)
api = Api(app)



app.config["SQLALCHEMY_DATABASE_URI"] = "oracle+cx_oracle://migo:admin1234@127.0.0.1:1521/?service_name=XE"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False

db = SQLAlchemy(app)

class userlogin(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),nullable=False)
    password = db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return f"id={self.id}, name={self.name}, log={self.log}"

instance_matcher = {
    "id":fields.Integer,
    "name":fields.String,
    "password":fields.Integer
}

#db.create_all()



login_args = reqparse.RequestParser()
login_args.add_argument("id",type=int,help="ID must be given",required=True)
login_args.add_argument("name",type=str,help="Name must be given",required=True)
login_args.add_argument("password",type=int,help="password must be given",required=True)

class page_contoller(Resource):
    @marshal_with(instance_matcher)
    def post(self,id):
        result = userlogin.query.filter_by(id=id).first()
        if not result:
            abort(404,message="존재하지 않는 아이디 입니다.")
        else:
            args = login_args.parse_args()
            if args['password'] != result.password:
                abort(400,message="아이디와 비밀번호가 일치하지 않습니다.")
            else:
                return result,200

    @marshal_with(instance_matcher)
    def put(self,id):
        result = userlogin.query.filter_by(id=id).first()
        if result:
            abort(409,message="Primary key constraint conflicted")

        args = login_args.parse_args()
        instance = userlogin(id=id,name=args['name'],password=args['password'])
        db.session.add(instance)
        db.session.commit()
        return instance,201
api.add_resource(page_contoller,"/<int:id>")


mongo_args = reqparse.RequestParser()
mongo_args.add_argument("location",action='append',help="location must be provided",required=True)
#lesson learned : If you want to accept multiple values for a key as a list, you can pass action='append'


class mongo_controller(Resource):
    client = MongoClient("127.0.0.1", 27017)
    mongodb = client.district

    def get(self,id):
        #유저의 위치를 제공받았다고 가정, 현재 동네 위치를 리턴해준다.
        args = mongo_args.parse_args()
        location = list(map(float,args['location']))
        loc_info = self.mongodb.neiborhood.find_one({"geometry":
                                                         {"$geoIntersects":
                                                              {"$geometry":
                                                                   {"type":"Point",
                                                                    "coordinates":location}}}})['name']
        if not loc_info:
            abort(404,message="어디에 있는지 특정할 수 없습니다.")
        return loc_info


api.add_resource(mongo_controller,"/mongo/<int:id>")







if __name__ == '__main__':
    app.run(debug=True)