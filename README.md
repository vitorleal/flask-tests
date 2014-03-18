#Flask and MongoLabs tests
Simple app testing [Flask](http://flask.pocoo.org/) with [AngularJS](http://angularjs.org/) and [MongoLabs](https://mongolab.com/welcome/)

##Config
Update the [config](https://github.com/vitorleal/flask-tests/blob/master/flask_app/config.py) file with the correct mongolabs database info:
- userame
- password
- database url
- database name

##Install dependencies
Install the [Bower](http://bower.io/)
```
bower install
```

Init a [Virtualenv](http://www.virtualenv.org/) enviroment
```
virtualenv ENV
```
then activate the enviroment
```
source ENV/bin/activate
```

Instll the project dependencies usin [pip](http://www.pip-installer.org/en/latest/)
```
pip install -r requirements.txt
```

Then run the server
```
python main.py
```
