from app    import app, login_manager
from flask  import make_response, jsonify, render_template, redirect
from flask.ext.login import login_user, logout_user, current_user, login_required

from models import Advertiser

'''
Routes
'''
#Index
@app.route("/")
def home():
    return render_template('index.html')

'''
Authenticate
'''
#Login
@login_manager.user_loader
def load_user(userid):
    return Advertiser.get(userid)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))

    return render_template("login.html", form=form)

#Error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
