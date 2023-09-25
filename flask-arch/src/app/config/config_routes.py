from flask import Flask, Blueprint
from importlib import import_module
from os import path, listdir

from app.constants import APP_FOLDER_PATH


MODULES_DIRECTORY = path.join(APP_FOLDER_PATH, 'modules')
MODULE_DIRECTORY = MODULES_DIRECTORY + '\\{module_name}'
ROUTES_MODULE_PATH = 'app.modules.{module_name}.routes'


def configure_routes(app: Flask) -> None:
    for module_name in listdir(MODULES_DIRECTORY):
        module_directory = MODULE_DIRECTORY.format(
            module_name=module_name
        )

        if 'routes.py' in listdir(module_directory):
            routes = import_module(
                ROUTES_MODULE_PATH.format(module_name=module_name)
            )

            for _, item in routes.__dict__.items():
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)
                    break
