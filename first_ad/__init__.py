from flask import Flask
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager

#Create the Flask app
app = Flask(__name__, static_folder='../static', template_folder='../templates')

#Config
app.config.from_object('first_ad.config.Configuration')

#secret key
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#Login manager
login_manager = LoginManager()
login_manager.init_app(app)

#Connect to MongoLabs
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
