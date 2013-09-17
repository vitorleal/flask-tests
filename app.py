from flask import Flask
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager

#Create the Flask app
app = Flask(__name__, static_folder='static', static_url_path='', template_folder='static/templates')

#Config
app.config.from_object('config.Configuration')

#Login manager
login_manager = LoginManager()
login_manager.init_app(app)

#Connect to MongoLabs
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
