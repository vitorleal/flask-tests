#Flask, AngularJS and MongoLabs tests
Simple app testing [Flask](http://flask.pocoo.org/) with [AngularJS](http://angularjs.org/) and [MongoLabs](https://mongolab.com/welcome/)

##Config
Update the [config](https://github.com/vitorleal/flask-tests/blob/master/flask_app/config.py) file with the correct mongolabs database info:
```python
#Config
class Configuration(object):
    MONGODB_SETTINGS = {
        'DB'      : <db-name>,
        'HOST'    : <mongolabs-url>,
        'PORT'    : 43338,
        'USERNAME': <username>,
        'PASSWORD': <password>,
    }

```

- userame
- password
- database url
- database name

##Install dependencies
Install [Bower](http://bower.io/) dependencies [Bootstrap, angular, angular-route]
```
bower install
```


###Init a virtualenv
Init a [Virtualenv](http://www.virtualenv.org/) enviroment
```
virtualenv ENV
```
Then activate the enviroment
```
source ENV/bin/activate
```

###Install pip dependencies
Instll the project dependencies usin [pip](http://www.pip-installer.org/en/latest/)
```
pip install -r requirements.txt
```

###Run the server
Then run the server
```
python main.py
```
