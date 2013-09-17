from flask.ext.wtf      import Form
from wtforms            import TextField, PasswordField
from wtforms.validators import Required

from models import Advertiser

class LoginForm(Form):
    email    = TextField('Email', [Required()])
    password = PasswordField('Password', [Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        advertiser = Advertiser.objects.filter(email=self.email.data).first()

        if advertiser is None:
            self.email.errors.append('Unknown email')
            return False

        if not advertiser.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = advertiser
        return True