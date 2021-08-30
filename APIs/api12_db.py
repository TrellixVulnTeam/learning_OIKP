from flask import Flask
from flask_restful import Api, Resource,reqparse,abort , fields,marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)


#configuration setting for db
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db' #relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class VideoModel(db.Model): #this is to craete instance of record that will be eventually inserted into a table.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False) #maximum is 100
    views = db.Column(db.Integer,nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name)={self.name}, views={self.views},likes={self.likes}"

#to actually create DB
"""db.create_all()
"""
#we only create db once. So after creating db, you should comment this out. Otherwise, you will overwrite things





video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type=str,help="Name of the video is required",required=True)
video_put_args.add_argument("views",type=int,help="Views of the video is required",required=True)
video_put_args.add_argument("likes",type=int,help="Likes on the video is required",required=True)



resource_fields = {
    "id" : fields.Integer,
    "name" : fields.String,
    "views" : fields.Integer,
    "likes" : fields.Integer
}
#what I'm doing here is ... making dictionary that defines the fields
#from the VideoModel class




class Video(Resource):
    #with marshal_with , when we return, take this return value and
    #serialize it using fields from resource_fields
    @marshal_with(resource_fields)
    def get(self,video_id):
        #gonna query database and return something that fits the query that we have.
        result = VideoModel.query.filter_by(id=video_id).first() #it can be all() as well.

        if not result:
            abort(404, message="Couldn't find video with that id")

        return result
        #this will be the result of __repr__


    @marshal_with(resource_fields)
    def put(self,video_id):
        args = video_put_args.parse_args()

        #check validity of the query(because we are not going to put in instance of which the key has been already inserted in db)
        query = VideoModel.query.filter_by(id=video_id).first()
        if query:
            abort(409,message ="Video_id(Primary key) has been already taken")

        #to create instance that will be put in the db
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])

        #to insert the instance to db
        db.session.add(video)

        #commit()
        db.session.commit()

        #to check if the data has been inserted into db,
        return video,201


    # def delete(self,video_id):
    #     abort_if_video_id_doesnt_exist(video_id)
    #     #in case you get a request for deleting stuff,
    #     del videos[video_id]
    #     return "",204




api.add_resource(Video,"/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)