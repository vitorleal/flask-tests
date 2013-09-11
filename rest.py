from app import app
from flask.ext import restful

#Create the Rest api App
api = restful.Api(app)

#Rest api
class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api')
