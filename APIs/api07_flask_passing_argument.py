from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api =Api(app) #this initialize that fact that we are using RESTful api


names = {"Mago" :{"age":31,"gender":"male"},
         "Craig" :{"age":43,"gender":"male"}}

class HelloWorld(Resource):
    def get(self,name):
        return {"name":name}
    def post(self,name):
        return names[name]


#to pass parameter through request URL
api.add_resource(HelloWorld,"/helloworld/<string:name>")
#it can be int, boolean as well.
#it is to ask users to type in some string after "helloworld/" and int after "helloworld/some_string/" and we will pass that into get reqeust


if __name__ == '__main__':
    app.run(debug=True)


