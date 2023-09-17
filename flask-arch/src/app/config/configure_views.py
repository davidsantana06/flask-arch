from flask import Flask, Blueprint
from importlib import import_module
from os import path, listdir
from types import ModuleType

from app.constants import APP_FOLDER_PATH


MODULES_DIRECTORY: str = path.join(APP_FOLDER_PATH, 'modules')
MODULE_DIRECTORY: str = MODULES_DIRECTORY + '\\{module_name}'
VIEWS_MODULE_PATH: str = 'app.modules.{module_name}.views'


def configure_views(app: Flask) -> None:
    for module_name in listdir(MODULES_DIRECTORY):
        module_directory: str = MODULE_DIRECTORY.format(
            module_name=module_name
        )

        print(listdir(module_directory))

        if 'views.py' in listdir(module_directory):
            views: ModuleType = import_module(
                VIEWS_MODULE_PATH.format(module_name=module_name)
            )

            for _, item in views.__dict__.items():
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)
                    break
