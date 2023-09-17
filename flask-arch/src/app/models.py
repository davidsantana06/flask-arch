from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from typing import List
from app.extensions import database
from app.lib.base import BaseModel


class User(BaseModel, database.Model):
    __tablename__: str = 'User'

    id: Column = Column(Integer, primary_key=True)
    name: Column = Column(String(50), nullable=False)
    email: Column = Column(String(50), unique=True, nullable=False)
    username: Column = Column(String(30), unique=True, nullable=False)
    password: Column = Column(String(60), nullable=False)
    created_at: Column = Column(DateTime, nullable=False, default=func.now())
    updated_at: Column = Column(DateTime, nullable=False, default=func.now())
    status: Column = Column(Integer, nullable=False, default=1)

    @classmethod
    def find_by_username(cls, username: str) -> 'User':
        return cls.find_by([User.username == username])

    @classmethod
    def find_all_by_name(cls, name: str) -> List['User']:
        return cls.find_all_by([User.name.icontains(name)])
