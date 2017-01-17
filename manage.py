#!/usr/bin/env python
import os
from flask import Flask
from app import create_app
from flask.ext.script import Manager
from flask import render_template
from app.main.forms import NameForm

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()