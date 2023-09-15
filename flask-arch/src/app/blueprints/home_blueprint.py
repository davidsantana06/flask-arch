from flask import Blueprint
from http import HTTPStatus
from typing import Tuple
from app.services.home_service import HomeService
from app.utils.jinja import render_page


home_blueprint: Blueprint = Blueprint('home', __name__, url_prefix='')
__home_service: HomeService = HomeService()


@home_blueprint.get('/')
def index() -> Tuple[str, HTTPStatus]:
    # data: Dict[str, object] = {
    #     'user': __home_service.find_user_by_username(
    #         'davidsantana06'
    #     )
    # }
    return (render_page('home/index'), HTTPStatus.OK)
