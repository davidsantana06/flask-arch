from flask import Flask, Blueprint
from importlib import import_module
from os import path, listdir
from types import ModuleType
from app.constants import APP_FOLDER_PATH


MODULES_DIRECTORY: str = path.join(APP_FOLDER_PATH, 'modules')
VIEWS_MODULE_PATH: str = 'app.modules.{module_name}.views'


def configure_blueprints(app: Flask) -> None:
    for module_name in listdir(MODULES_DIRECTORY):
        try:
            views: ModuleType = import_module(
                VIEWS_MODULE_PATH.format(module_name=module_name)
            )

            for _, item in views.__dict__.items():
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)
                    break
        except ModuleNotFoundError:
            continue
