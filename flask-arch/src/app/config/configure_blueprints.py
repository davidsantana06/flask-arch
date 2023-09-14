from flask import Flask, Blueprint
from importlib import import_module
from os import path, listdir
from types import ModuleType
from typing import List
from app.constants import APP_FOLDER_PATH


__BLUEPRINTS_DIRECTORY: str = path.join(APP_FOLDER_PATH, 'blueprints')
__BLUEPRINT_MODULE_PATH: str = 'app.blueprints.{module_name}'


def configure_blueprints(app: Flask) -> None:
    modules: List[str] = [
        file_name[:-3] for file_name in listdir(__BLUEPRINTS_DIRECTORY)
        if (file_name.endswith('.py')) and (not file_name.startswith('__'))
    ]

    for module_name in modules:
        module: ModuleType = import_module(
            __BLUEPRINT_MODULE_PATH.format(module_name=module_name)
        )

        for _, item in module.__dict__.items():
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
                break
