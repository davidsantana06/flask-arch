from flask import Flask, Blueprint
from importlib import import_module
from os import listdir

from app.constants import MODULES_DIRECTORY

MODULE_DIRECTORY = MODULES_DIRECTORY + '\\{module_name}'
MODULE_PATH = 'app.modules.{module_name}'


def configure_modules(app: Flask) -> None:
    for module_name in listdir(MODULES_DIRECTORY):
        module_directory = MODULE_DIRECTORY.format(
            module_name=module_name
        )

        if '__init__.py' in listdir(module_directory):
            module = import_module(
                MODULE_PATH.format(module_name=module_name)
            )

            for _, item in module.__dict__.items():
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)
                    break
