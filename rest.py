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


'''
Error handler 404
'''
@app.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
