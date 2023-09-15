from typing import List
from app.repositories.base import BaseRepository
from app.models.user import User


class UserRepository(BaseRepository):
    def find_by_username(self, username: str) -> User:
        return self._find_by(
            User, [User.username == username]
        )

    def find_all_by_name(self, name: str) -> List[User]:
        return self._find_all_by(
            User, [User.name.icontains(name)]
        )
