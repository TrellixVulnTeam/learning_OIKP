from flask import Flask
from flask_restful import Resource , abort,Api,reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type=str,help="Name of the video is required",required=True)
video_put_args.add_argument("views",type=int,help="Views of the video is required",required=True)
video_put_args.add_argument("likes",type=int,help="Likes on the video is required",required=True)


#just use memory for practice purposes
videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Couldn't find ID")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="video already exists with that ID")

class Video(Resource):
    def get(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    def put(self,video_id):
        #if video already exists, abort it.
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id] , 201

    def delete(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        #in case you get a request for deleting stuff,
        del videos[video_id]
        return "",204




api.add_resource(Video,"/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)