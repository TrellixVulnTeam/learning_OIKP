from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api =Api(app) #this initialize that fact that we are using RESTful api


class HelloWorld(Resource): #get it inherited Resource
    def get(self): #this works only when we request things through "get"
        return {"data":"This is 'get'"}
    def post(self):
        return {"data":"This is 'post'"}

#to register above class as a resource,
api.add_resource(HelloWorld,"/helloworld") #the second parameter is url.


#What does "serializable" mean?
# - json format (dictionary)
# - something else that's seriableable



if __name__ == "__main__":
    app.run(debug=True)
    #Hey! this is in debug mode so we're gonna see all that output and any logging information
    #when running this in production environments, shouldn't use it.
