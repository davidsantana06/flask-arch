from flask import Flask
from importlib import import_module
from inspect import isfunction
from os import (
    path,
    listdir
)
from types import FunctionType
from typing import List

from app.constants import APP_FOLDER_PATH


CONFIG_DIRECTORY = path.join(APP_FOLDER_PATH, 'config')
CONFIG_MODULE_PATH = 'app.config.{module_name}'


def load_configure_functions() -> List[FunctionType]:
    configure_functions = []
    modules = [
        file_name[:-3] for file_name in listdir(CONFIG_DIRECTORY)
        if (file_name.endswith('.py')) and (not file_name.startswith('__'))
    ]

    for module_name in modules:
        module = import_module(
            CONFIG_MODULE_PATH.format(module_name=module_name)
        )

        for name, item in module.__dict__.items():
            if (name.startswith('configure')) and (isfunction(item)):
                configure_functions.append(item)

    return configure_functions


def configure_all(app: Flask) -> None:
    configure_functions = load_configure_functions()

    for configure_function in configure_functions:
        configure_function(app)
