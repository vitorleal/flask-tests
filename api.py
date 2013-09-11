from app       import app, db
from flask     import jsonify
from flask.ext import restful
from models    import Users

#Create the Rest api App
api = restful.Api(app)

#Rest api
class MyUsers(restful.Resource):
    def get(self):
        return { 'teste': 'ok' }

api.add_resource(MyUsers, '/api/users')
