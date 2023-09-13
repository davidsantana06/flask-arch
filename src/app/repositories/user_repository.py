from typing import List
from app.core.base.repository import Repository
from app.models.user import User


class UserRepository(Repository):
    def find_by_username(self, username: str) -> User:
        return self._find_by(
            User, (User.username == username)
        )

    def find_all_by_name(self, name: str) -> List[User]:
        return self._find_all_by(
            User, (User.name == name)
        )
