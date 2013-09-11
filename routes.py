from app import app, api

'''
Routes
'''
#Index
@app.route("/")
def home():
    return "Hello World!"

#Login
@app.route("/login")
def login():
    return "Login"

#Logout
@app.route("/logout")
def logout():
    return "Logout"



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
