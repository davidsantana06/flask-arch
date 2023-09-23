from flask_sqlalchemy.model import Model
from sqlalchemy import (
    Column, ColumnElement, DateTime, Integer, String, UnaryExpression,
    and_
)
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func
from typing import List

from .extensions import database


class CRUDMixin(Model):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__

    @declared_attr
    def created_at(cls):
        return Column(DateTime, nullable=False, default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, nullable=False, default=func.now())

    @declared_attr
    def status(cls):
        return Column(Integer, nullable=False, default=1)

    @staticmethod
    def add(model: Model) -> None:
        try:
            database.session.add(model)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @staticmethod
    def delete(model: Model) -> None:
        try:
            database.session.delete(model)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @classmethod
    def find_first(cls, filters: List[ColumnElement[bool]]) -> Model:
        return cls.query.filter(
            and_(*filters)
        ).first()

    @classmethod
    def find_all(
        cls, filter_clauses: List[ColumnElement[bool]] = None, order_clauses: List[UnaryExpression] = None
    ) -> List[Model]:
        query = cls.query

        if filter_clauses:
            query = query.filter(and_(*filter_clauses))

        if order_clauses:
            query = query.order_by(*order_clauses)

        return query.all()


class User(database.Model, CRUDMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(60), nullable=False)

    @classmethod
    def find_by_username(cls, username: str) -> 'User':
        return cls.find_first([User.username == username])

    @classmethod
    def find_all_by_name(cls, name: str) -> List['User']:
        return cls.find_all([User.name.icontains(name)])
