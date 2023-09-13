from http import HTTPStatus
from typing import Dict, Tuple
from app.common.utils import render_page
from app.services.home_service import HomeService


class HomeController():
    __home_service: HomeService

    def __init__(self):
        self.__home_service = HomeService()

    def index(self) -> Tuple[str, int]:
        # data: Dict[str, object] = {
        #     'user': self.__home_service.find_user_by_username(
        #         'davidsantana06'
        #     )
        # }
        return (render_page('home/index'), HTTPStatus.OK)
