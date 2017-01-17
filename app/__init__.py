from flask import Flask
from config import config
from flask.ext.bootstrap import Bootstrap
#from flask.ext.sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
    #db.init_app(app)