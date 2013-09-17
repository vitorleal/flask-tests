from first_ad        import app, login_manager
from flask           import make_response, jsonify, render_template, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required

from models import Advertiser
from forms  import LoginForm


'''
Authenticate
'''
#LogUser
@login_manager.user_loader
def load_user(userid):
    return Advertiser.get(userid)

#Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        login_user(user)
        flash('Logged in successfully.')
        return redirect(request.args.get('next') or url_for('index'))

    return render_template('login.html', form=form)


'''
Routes
'''
#Index
@app.route('/')
@login_required
def home():
    return render_template('index.html')


#Error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.errorhandler(401)
def not_found(error):
    return redirect(url_for('login'))
