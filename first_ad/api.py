from first_ad  import app, db
from flask     import jsonify
from flask.ext import restful
from models    import Advertiser
from flask.ext.login import current_user, login_required


#Create the Rest api App
api = restful.Api(app)

'''
Rest api
'''

#Users
class AllUsers(restful.Resource):
    def get(self):
        user = Advertiser.objects(email='vitorleal1@gmail.com').first()
        return { "a": "b" }

api.add_resource(AllUsers, '/api/users')


#Ads
class MyAds(restful.Resource):
    def get(self):
        return { 'ads': 'ok' }

api.add_resource(MyAds, '/api/ads')

