from flask import Blueprint
from http import HTTPStatus
from typing import Tuple
from app.lib.utils import render_page


home: Blueprint = Blueprint('home', __name__, url_prefix='')


@home.get('/')
def index() -> Tuple[str, HTTPStatus]:
    # data: Dict[str, object] = {
    #     'user': __home_service.find_user_by_username(
    #         'davidsantana06'
    #     )
    # }
    return (render_page('home/index'), HTTPStatus.OK)
