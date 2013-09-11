from app import app
from flask.ext import restful

api = restful.Api(app)


'''
RESTfull API
'''
class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api')
