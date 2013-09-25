from flask.ext.wtf      import Form
from wtforms            import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

from models import Advertiser

class LoginForm(Form):
    email    = TextField('Email', [Required(), Email()])
    password = PasswordField('Password', [Required()])


class RegisterForm(Form):
    first    = TextField('First',        [Required()])
    last     = TextField('Last',         [Required()])
    cpf      = TextField('Cpf',          [Required()])
    address  = TextField('Address',      [Required()])
    email    = TextField('Email',        [Required(), Email()])
    password = PasswordField('Password', [Required()])
    repeat   = PasswordField('Repeat', [
      Required(),
      EqualTo('password', message='Passwords must match')
    ])
