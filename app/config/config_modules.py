from flask import Blueprint, Flask
from importlib import import_module
from os import listdir

from app.constants import MODULE_FOLDER, MODULES_FOLDER, MODULE_PATH


def configure_modules(app: Flask) -> None:
    for module_name in listdir(MODULES_FOLDER):
        module_folder = MODULE_FOLDER.format(module_name)

        if '__init__.py' in listdir(module_folder):
            module_path = MODULE_PATH.format(module_name)
            module = import_module(module_path)

            for _, item in module.__dict__.items():
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)
                    break
