from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask
from os import (
    environ, path, 
    mkdir
)
from typing import List

from app.constants import DATABASE_FILE, DATABASE_FOLDER, ENV_FILE, OUTPUT_FOLDER, UPLOADS_FOLDER
from app.lib.misc import create_folder


def create_necessary_folders() -> None:
    for folder in (DATABASE_FOLDER, OUTPUT_FOLDER, UPLOADS_FOLDER):
        create_folder(folder)


def configure_app_env(app: Flask) -> None:
    load_dotenv(ENV_FILE)
    create_necessary_folders()

    app.config.update(
        SECRET_KEY=environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=f'sqlite:///{DATABASE_FILE}',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        PERMANENT_SESSION_LIFETIME=timedelta(days=1)
    )
