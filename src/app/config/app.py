from datetime import timedelta
from flask import Flask
from typing import Dict


APP_CONFIG_PARAMS: Dict[str, object] = {
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

    'PERMANENT_SESSION_LIFETIME': timedelta(days=7)
}


def configure_app(app: Flask) -> None:
    for name, param in APP_CONFIG_PARAMS.items():
        app.config[name] = param