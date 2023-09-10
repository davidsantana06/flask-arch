from flask import render_template
from typing import Tuple


class HomeController():
    PAGE: str = 'pages/home/%s.html.j2'

    def index(self) -> Tuple[str, int]:
        return (render_template(self.PAGE % 'index'), 200)
