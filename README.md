#Flask, AngularJS and MongoLabs tests
Simple app testing [Flask](http://flask.pocoo.org/) with [AngularJS](http://angularjs.org/) and [MongoLabs](https://mongolab.com/welcome/)

##Config
Update the [config](https://github.com/vitorleal/flask-tests/blob/master/flask_app/config.py) file with the correct mongolabs database info:
```python
#Config
class Configuration(object):
    MONGODB_SETTINGS = {
        'DB'      : '<db-name>',
        'HOST'    : '<mongolabs-url>',
        'PORT'    : 43338,
        'USERNAME': '<username>',
        'PASSWORD': '<password>',
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

##License (Unlicense)
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
