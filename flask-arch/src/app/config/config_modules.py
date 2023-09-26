from flask import Flask, Blueprint
from importlib import import_module
from os import path, listdir

from app.constants import APP_FOLDER_PATH


MODULES_DIRECTORY = path.join(APP_FOLDER_PATH, 'modules')
MODULE_DIRECTORY = MODULES_DIRECTORY + '\\{module_name}'
VIEWS_MODULE_PATH = 'app.modules.{module_name}.views'


def configure_modules(app: Flask) -> None:
    for module_name in listdir(MODULES_DIRECTORY):
        module_directory = MODULE_DIRECTORY.format(
            module_name=module_name
        )

        if 'views.py' in listdir(module_directory):
            routes = import_module(
                VIEWS_MODULE_PATH.format(module_name=module_name)
            )

            for _, item in routes.__dict__.items():
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)
                    break
