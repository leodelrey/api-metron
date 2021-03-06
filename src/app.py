# src/app.py

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from .config import app_config
from .models import db
from .views.CharacterView import character_api as character_blueprint
from .views.HatView import hat_api as hat_blueprint
from .views.DataView import data_api as data_blueprint


def create_app(config_name):
    """
        The function to create the Flask application
        Parameters:
            config_name (str): The environment to execute on
        Returns:
            Flask: The application
    """
    # Create the app
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    # Add the endpoints from views files
    app.register_blueprint(character_blueprint, url_prefix='/character')
    app.register_blueprint(hat_blueprint, url_prefix='/hat')
    app.register_blueprint(data_blueprint, url_prefix='/data')

    return app


def create_db(DB_URL):
    """
        The function to create the database if doesn't exist
        Parameters:
            DB_URL (str): The URL of the database (postgres)
    """
    engine = create_engine(DB_URL)
    if not database_exists(engine.url):
        print('Creating database.')
        create_database(engine.url)
