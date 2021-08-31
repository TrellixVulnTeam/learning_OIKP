from flask import Flask
from flask_restful import Resource , Api ,abort,reqparse,marshal_with,fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

#configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "oracle+cx_oracle://migo:admin1234@127.0.0.1:1521/?service_name=XE"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#CREATE Table
class orapratice(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32),nullable=True)

    def __repr__(self):
        return f"id={self.id}, name={self.name}"

db.create_all()


resource_fields = {
    "id":fields.Integer,
    "name":fields.String
}

user_agrs = reqparse.RequestParser()
user_agrs.add_argument("id",type=int,help="id must be given",required=True)
user_agrs.add_argument("name",type=str,help="name must be given",required=True)


class controller(Resource):
    @marshal_with(resource_fields)
    def get(self,id):
        result = orapratice.query.filter_by(id=id).first()
        if not result:
            abort(404,message="No data available with the given ID")
        return result

    @marshal_with(resource_fields)
    def put(self,id):

        result=orapratice.query.filter_by(id=id).first()
        if result:
            abort(409,message="Violating primary_key constraint")
        args = user_agrs.parse_args()
        instance = orapratice(id=id,name=args['name'])
        db.session.add(instance)
        db.session.commit()
        return instance, 201

api.add_resource(controller,"/registration/<int:id>")



if __name__ == '__main__':
    app.run(debug=True)
