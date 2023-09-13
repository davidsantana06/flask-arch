from http import HTTPStatus
from typing import Tuple
from app.common.utils import render_page


class HomeController():
    def index(self) -> Tuple[str, int]:
        return (
            render_page('home/index'),
            HTTPStatus.OK
        )
