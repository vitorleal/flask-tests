from app import app
from flask import make_response, jsonify
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


#Error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
