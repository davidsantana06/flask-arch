from sqlalchemy import Column, DateTime, Integer, String
from app.extensions import database


class User(database.Model):
    __tablename__ = 'User'

    id: Column = Column(Integer, primary_key=True)
    name: Column = Column(String(50), nullable=False)
    email: Column = Column(String(50), unique=True, nullable=False)
    username: Column = Column(String(30), unique=True, nullable=False)
    password: Column = Column(String(60), nullable=False)
    created_at: Column = Column(DateTime, nullable=False)
    updated_at: Column = Column(DateTime, nullable=False)
    status: Column = Column(Integer, nullable=False)
