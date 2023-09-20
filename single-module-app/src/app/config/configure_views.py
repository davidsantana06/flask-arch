from flask import Flask, Blueprint
from importlib import import_module
from os import path, listdir
from types import ModuleType

from app.constants import APP_FOLDER_PATH


VIEWS_MODULE_PATH: str = 'app.views'


def configure_views(app: Flask) -> None:
    if 'views.py' in listdir(APP_FOLDER_PATH):
        views: ModuleType = import_module(VIEWS_MODULE_PATH)

        for _, item in views.__dict__.items():
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
                break
