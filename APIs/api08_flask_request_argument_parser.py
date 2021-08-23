from flask import Flask, request
#request is request object that can be used inside of "Resource"
#and it gives us any of the information
#if you want to look at the data that we sent,
    # -> request.form
    # HOWEVER, it's still a little hard to remember.
    #better way? -> reqparse

from flask_restful import Api, Resource ,reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
#this will automatically parse through the request that's being sent and
#make sure it fits the guideline we're going to define soon.
video_put_args.add_argument("name",type=str,help="Name of the video is required",required=True)
video_put_args.add_argument("views",type=int,help="Views of the video is required",required=True)
video_put_args.add_argument("likes",type=int,help="Likes on the video is required",required=True)
#with "required = True" if we don't send that argument, it will show up and tell us the requirements.


videos={}

class Video(Resource):
    def get(self,video_id):
        return videos[video_id]

    #way to create a video
    def put(self,video_id):
        #one way to do
        #print(request.form['likes'])

        #better way to do
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201 #status code. 201 stands for "created"

        #200 - OK


api.add_resource(Video,"/video/<int:video_id>")




if __name__ == '__main__':
    app.run(debug=True)
