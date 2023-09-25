from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask
from os import environ, path

from app.constants import ROOT_FOLDER_PATH
from app.constants import RESOURCES_FOLDER_PATH


ENV_FILE_PATH = path.join(ROOT_FOLDER_PATH, '..', '.env')
load_dotenv(ENV_FILE_PATH)


def configure_app_env(app: Flask) -> None:
    app.static_folder = path.join(RESOURCES_FOLDER_PATH, 'static')
    app.template_folder = path.join(RESOURCES_FOLDER_PATH, 'templates')
    app.config.from_mapping({
        'SECRET_KEY': environ.get('SECRET_KEY'),
        'SQLALCHEMY_DATABASE_URI': environ.get('SQLALCHEMY_DATABASE_URI'),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'PERMANENT_SESSION_LIFETIME': timedelta(days=1)
    })
