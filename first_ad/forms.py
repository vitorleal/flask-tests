from flask.ext.wtf      import Form
from wtforms            import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

from models import Advertiser

class LoginForm(Form):
    email    = TextField('Email', [Required(), Email()])
    password = PasswordField('Password', [Required()])


class RegisterForm(Form):
    name     = TextField('First',   [Required()])
    last     = TextField('Last',    [Required()])
    cpf      = TextField('Cpf',     [Required(), Email()])
    address  = TextField('Address', [Required(), Email()])
    email    = TextField('Email',   [Required(), Email()])
    password = PasswordField('Password', [Required()])
    confirm  = PasswordField('Repeat Password', [
      Required(),
      EqualTo('password', message='Passwords must match')
    ])
