from first_ad  import app, db
from flask.ext import restful
from models    import Advertiser
from flask.ext.login import current_user, login_required
import json

#Create the Rest api App
api = restful.Api(app)

'''
Rest api
'''
#Users
class CurentUser(restful.Resource):
    def get(self):
        if current_user.is_anonymous():
            return { 'error': 'no_user' }
        else:
            return json.loads(current_user.to_json())

api.add_resource(CurentUser, '/api/user')
