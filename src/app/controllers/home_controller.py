from flask import render_template
from http import HTTPStatus
from typing import Tuple


class HomeController():
    def index(self) -> Tuple[str, int]:
        return (
            render_template('pages/home/index.html.j2'), 
            HTTPStatus.OK
        )
