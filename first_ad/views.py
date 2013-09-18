from first_ad        import app, login_manager
from flask           import make_response, jsonify, render_template, redirect, url_for, flash, request
from flask.ext.login import login_user, logout_user, current_user, login_required

from models import Advertiser
from forms  import LoginForm


'''
Authenticate
'''
#LogUser
@login_manager.user_loader
def load_user(user_id):
    return Advertiser.objects(id=user_id).first()


#Login
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('index'))

    form = LoginForm()

    print(form.validate_on_submit())
    if form.validate_on_submit():
        user = Advertiser.objects(email=form.email.data).first()
        login_user(user)
        flash('Logged in successfully.')

        return redirect(url_for('index'))

    return render_template('login.html', form=form)


#Logout
@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


'''
Routes
'''
#Index
@app.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)


#Error pages 404, 401
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
