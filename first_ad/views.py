from first_ad        import app, login_manager
from flask           import make_response, jsonify, render_template, redirect, url_for, flash, request
from flask.ext.login import login_url, login_user, logout_user, current_user, login_required

from models import Advertiser
from forms  import LoginForm, RegisterForm


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

    if form.validate_on_submit():
        user = Advertiser.objects(email=form.email.data).first()

        print(user.password)
        print(form.password.data)
        if user.password != form.password.data:
          return render_template('login.html', form=form, error="Usuario ou Senha incorreta")

        else:
          login_user(user)
          return redirect(url_for('index'))

    return render_template('login.html', form=form)

login_url('/login')


#Logout
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


'''
Routes
'''
#Index
@app.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)


#Signup
@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated():
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        newUser = Advertiser(
            first_name = form.first.data,
            last_name  = form.last.data,
            cpf        = form.cpf.data,
            address    = form.address.data,
            country    = 'Brazil',
            email      = form.email.data,
            password   = form.password.data,
        ).save()

        return redirect(url_for('index'))

    return render_template('signup.html', form=form)


#Error pages 404, 401
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
