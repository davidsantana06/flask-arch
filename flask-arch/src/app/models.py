from flask_sqlalchemy.model import Model
from sqlalchemy import (
    Column, ColumnElement, DateTime, Integer, String, UnaryExpression,
    and_
)
from sqlalchemy.orm import Query
from sqlalchemy.sql import func
from typing import List

from .extensions import database


class CRUDMixin(Model):
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
    def find_by(cls, filters: List[ColumnElement[bool]]) -> Model:
        model: Model = cls.query.filter(
            and_(*filters)
        ).first()

        return model

    @classmethod
    def find_all(
        cls, filter_clauses: List[ColumnElement[bool]] = None, order_clauses: List[UnaryExpression] = None
    ) -> List[Model]:
        query: Query = cls.query

        if filter_clauses:
            query = query.filter(and_(*filter_clauses))

        if order_clauses:
            query = query.order_by(*order_clauses)

        models: List[Model] = query.all()
        return models


class User(database.Model, CRUDMixin):
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
        return cls.find_all([User.name.icontains(name)])
