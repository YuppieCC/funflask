
# FlaskFun

## Introduction

这是自己学习 Flask 框架时实现[《Flask Web开发：基于Python的Web应用开发实战》](https://book.douban.com/subject/26274202/)的案例。



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
<img src="https://i.loli.net/2017/12/10/5a2d416db2aba.png" title="flaskfun" />

