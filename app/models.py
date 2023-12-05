from flask_login import UserMixin
from flask_sqlalchemy.model import Model
from flask_wtf import FlaskForm
from re import findall
from sqlalchemy import (
    Column, ColumnElement, DateTime, Integer, String, UnaryExpression,
    and_
)
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func
from typing import List

from .extensions import database


# BASES/MIXINS #

class Entity(Model):
    @declared_attr
    def __tablename__(cls):
        cls_name_words = findall(r'[A-Z][a-z]*', cls.__name__)
        table_name = '_'.join(cls_name_words).lower()
        return table_name

    @staticmethod
    def save(entity: 'Entity') -> None:
        try:
            database.session.add(entity)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @classmethod
    def _find_first(cls, filter_clauses: List[ColumnElement[bool]]) -> 'Entity':
        return cls.query.filter(and_(*filter_clauses)).first()

    @classmethod
    def _find_all(cls, filter_clauses: List[ColumnElement[bool]] = [], order_clauses: List[UnaryExpression] = []) -> List['Entity']:
        query = cls.query.filter(and_(*filter_clauses))

        if order_clauses:
            query = query.order_by(*order_clauses)

        return query.all()


class MainEntity(Entity):
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
    def deactivate(entity: 'MainEntity') -> None:
        try:
            entity.status = 0
            database.session.add(entity)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @classmethod
    def _find_first(cls, filter_clauses: List[ColumnElement[bool]]) -> 'MainEntity':
        return super()._find_first([*filter_clauses, cls.status == 1])

    @classmethod
    def _find_all(cls, filter_clauses: List[ColumnElement[bool]] = [], order_clauses: List[UnaryExpression] = []) -> List['MainEntity']:
        return super()._find_all([*filter_clauses, cls.status == 1], order_clauses)


class AssociationEntity(Entity):
    ...


class PopulateMixin:
    def populate_form(self, form: FlaskForm) -> None:
        for field in form:
            if hasattr(self, field.name):
                field.data = getattr(self, field.name)

    def populate_obj(self, obj: object) -> None:
        for attr in obj.__dict__:
            if hasattr(self, attr):
                value = getattr(self, attr)
                setattr(obj, attr, value)


# MODELS #

class User(database.Model, MainEntity, PopulateMixin, UserMixin):
    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(60), nullable=False)

    @classmethod
    def find_by_id(cls, id: int) -> 'User':
        return cls._find_first([cls.id == id])

    @classmethod
    def find_by_username(cls, username: str) -> 'User':
        return cls._find_first([cls.username == username])

    @classmethod
    def find_all_by_name(cls, name: str) -> List['User']:
        return cls._find_all([cls.name.icontains(name)])

    def __init__(self, name: str, email: str, username: str, password: str) -> None:
        self.name = name
        self.email = email
        self.username = username
        self.password = password
