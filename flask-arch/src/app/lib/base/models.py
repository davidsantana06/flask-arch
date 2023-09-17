from flask_sqlalchemy.model import Model
from sqlalchemy import (
    ColumnElement, UnaryExpression,
    and_
)
from sqlalchemy.orm import Query
from typing import List

from app.extensions import database


class BaseModel(Model):
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
    def find_all_by(
        cls, filter_clauses: List[ColumnElement[bool]] = None, order_clauses: List[UnaryExpression] = None
    ) -> List[Model]:
        query: Query = cls.query

        if filter_clauses:
            query = query.filter(and_(*filter_clauses))

        if order_clauses:
            query = query.order_by(*order_clauses)

        models: List[Model] = query.all()
        return models

    @classmethod
    def find_all(cls) -> List[Model]:
        models: List[Model] = cls.query.all()
        return models
