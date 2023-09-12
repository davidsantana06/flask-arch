from sqlalchemy import Column, DateTime, Integer, String
from app.extensions import database


class User(database.Model):
    __tablename__ = 'User'

    id: Column = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    status = Column(Integer, nullable=False)
