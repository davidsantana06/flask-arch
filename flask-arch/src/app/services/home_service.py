from app.models.user import User
from app.repositories.user_repository import UserRepository


class HomeService:
    __user_repository: UserRepository

    def __init__(self):
        self.__user_repository = UserRepository()

    def find_user_by_username(self, username: str) -> User:
        return self.__user_repository.find_by_username(username)

    def find_users_by_name(self, name: str):
        return self.__user_repository.find_all_by_name(name)
