from typing import List
from .models import User


def find_user_by_username(username: str) -> User:
    return User.find_by_username(username)


def find_all_users_by_name(name: str) -> List[User]:
    return User.find_all_by_name(name)


def find_all_users() -> List[User]:
    return User.find_all()
