import datetime
from app import db

class Advertiser(db.Document):
    isActive     = db.BooleanField(default=False, required=True)
    first_name   = db.StringField(max_length=255, required=True)
    last_name    = db.StringField(max_length=255, required=True)
    email        = db.EmailField(max_length=255, required=True, unique=True)
    cpf          = db.StringField(max_length=255, required=True, unique=True)
    address      = db.StringField(max_length=255, required=True, unique=True)
    country      = db.StringField(max_length=255, required=True, unique=True)
    created_at   = db.DateTimeField(default=datetime.datetime.now, required=True)
    last_sign_in = db.DateTimeField(default=datetime.datetime.now, required=True)
    password     = db.StringField(max_length=255, required=True)

    def __unicode__(self):
        return self.email

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }
