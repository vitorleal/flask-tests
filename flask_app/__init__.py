from flask import Flask
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager
from flask.ext.gravatar import Gravatar

#Create the Flask app
app = Flask(__name__, static_folder='../static', template_folder='../templates')

#Config
app.config.from_object('flask_app.config.Configuration')

#secret key
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#Login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

#gravatar
gravatar = Gravatar(app, size=40, rating='g',
                    default='retro', force_default=False,
                    use_ssl=False, base_url=None,
                  )

#Connect to MongoLabs
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
