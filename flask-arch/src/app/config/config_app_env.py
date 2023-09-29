from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask
from os import environ, path

from app.constants import APP_DIRECTORY, ROOT_DIRECTORY


ENV_FILE_PATH = path.join(ROOT_DIRECTORY, '..', '.env')
load_dotenv(ENV_FILE_PATH)


def configure_app_env(app: Flask) -> None:
    app.static_folder = path.join(APP_DIRECTORY, 'static')
    app.template_folder = path.join(APP_DIRECTORY, 'templates')
    app.config.from_mapping({
        'SECRET_KEY': environ.get('SECRET_KEY'),
        'SQLALCHEMY_DATABASE_URI': environ.get('SQLALCHEMY_DATABASE_URI'),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'PERMANENT_SESSION_LIFETIME': timedelta(days=1)
    })
