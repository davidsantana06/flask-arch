from flask import Flask
from importlib import import_module
from inspect import isfunction
from os import (
    path,
    listdir
)
from types import FunctionType, ModuleType
from typing import List


def configure_all(app: Flask) -> None:
    configure_functions: List[FunctionType] = []

    package_directory: str = path.dirname(__file__)
    files_in_directory: List[str] = listdir(package_directory)

    modules: List[str] = [
        file_name[:-3] for file_name in files_in_directory
        if (file_name.endswith('.py')) and (not file_name.startswith('__init__'))
    ]

    for module_name in modules:
        module: ModuleType = import_module(f'app.config.{module_name}')

        for name, item in module.__dict__.items():
            if isfunction(item) and name.startswith('configure'):
                configure_functions.append(item)

    for configure_function in configure_functions:
        configure_function(app)
