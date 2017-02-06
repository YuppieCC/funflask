from flask import Blueprint
from . import authentication, posts, users, comments, errors

api = Blueprint('api', __name__)

def create_app(config_name):
	from .api_1_0 import api as api_1_0_blueprint
	app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')