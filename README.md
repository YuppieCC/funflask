
# FlaskFun
## Build
```bash
$ git clone git@github.com:YuppieCC/FlaskFun.git

# Virtualenv is a tool to create isolated Python environments.
$ virtualenv venv 
$ source venv/bin/activate

(venv) $ pip freeze >requirements.txt

# Create the database
(venv) $ python manage.py shell
>>> from app import db
>>> db.create_all()

# Add a migrations folder to your application
(venv) $ python manage.py db init

# Generate an initial migration
(venv) $ python manage.py db migrate

# Running on http://127.0.0.1:5000/
(venv) $ python manage.py runserver
```
## Show
<img src="https://raw.githubusercontent.com/YuppieCC/Django-FreeNote/37bdfcd7bdff2b96831a6f41c425b9ba3a774c9e/show/f1.png" >


