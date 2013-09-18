from first_ad import db
import datetime

#Advertiser
class Advertiser(db.Document):
    isActive     = db.BooleanField(default=True, required=True)
    first_name   = db.StringField(max_length=255, required=True)
    last_name    = db.StringField(max_length=255, required=True)
    email        = db.EmailField(max_length=255, required=True, unique=True)
    cpf          = db.StringField(max_length=255, required=True, unique=True)
    address      = db.StringField(max_length=255, required=True)
    country      = db.StringField(max_length=255, required=True)
    created_at   = db.DateTimeField(default=datetime.datetime.now, required=True)
    last_sign_in = db.DateTimeField(default=datetime.datetime.now, required=True)
    password     = db.StringField(max_length=255, required=True)

    def __unicode__(self):
        return self.email

    """Wraps User object for Flask-Login"""
    def get_id(self):
        print(self)
        return unicode(self.id)

    def is_active(self):
        return self.isActive

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    meta = {
        'allow_inheritance': True,
        'indexes' : ['-created_at'],
        'ordering': ['-created_at']
    }


#Categories
class Categories(db.Document):
    name = db.StringField(max_length=255, required=True)


#Ads
class Ads(db.Document):
    name        = db.StringField(max_length=255, required=True)
    advertizer  = db.ReferenceField('Advertiser')
    start_date  = db.DateTimeField(required=True)
    end_date    = db.DateTimeField(required=True)
    created_at  = db.DateTimeField(default=datetime.datetime.now, required=True)
    cpc         = db.StringField(max_length=255, required=True)
    cpa         = db.StringField(max_length=255, required=True)
    impressions = db.LongField(required=True)
    taps        = db.LongField(required=True)
    budget      = db.DecimalField(required=True)

