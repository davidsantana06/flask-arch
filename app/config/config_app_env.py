from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask
from os import environ, path

from app.constants import APP_FOLDER, DATABASE_FILE, ENV_FILE


def configure_app_env(app: Flask) -> None:
    load_dotenv(ENV_FILE)

    app.static_folder = path.join(APP_FOLDER, 'static')
    app.template_folder = path.join(APP_FOLDER, 'templates')
    app.config.from_mapping({
        'SECRET_KEY': environ.get('SECRET_KEY'),
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{DATABASE_FILE}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'PERMANENT_SESSION_LIFETIME': timedelta(days=1)
    })
