from datetime import timedelta
from flask import Flask
from typing import Dict
from app.constants import RESOURCES_FOLDER_PATH


STATIC_FOLDER: str = f'{RESOURCES_FOLDER_PATH}/static'
TEMPLATE_FOLDER: str = f'{RESOURCES_FOLDER_PATH}/templates'
CONFIG: Dict[str, object] = {
    'SECRET_KEY': '' + \
        '| ------------------------------- |\n' + \
        '|  Flask Definitive Architecture  |\n' + \
        '|    github.com/davidsantana06    |\n' + \
        '| ------------------------------- |',
    'SQLALCHEMY_DATABASE_URI': '{dbms}://{username}:{password}@{server}/{database}'.format(
        dbms='mysql+mysqlconnector',
        username='',
        password='',
        server='',
        database=''
    ),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'PERMANENT_SESSION_LIFETIME': timedelta(days=1)
}


def configure_app(app: Flask) -> None:
    app.static_folder = STATIC_FOLDER
    app.template_folder = TEMPLATE_FOLDER
    
    for name, param in CONFIG.items():
        app.config[name] = param
        