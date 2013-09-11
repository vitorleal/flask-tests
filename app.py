from flask import Flask
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface

#Create the Flask app
app = Flask(__name__)

#config
app.config.from_object('config.Configuration')

#connect to MongoLabs
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
