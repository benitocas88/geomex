from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow.schema import Schema as BaseSchema
from marshmallow.utils import EXCLUDE
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.ext.declarative import declared_attr

db = SQLAlchemy()
ma = Marshmallow()


# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html?highlight=tablename#mixin-and-custom-base-classes
class Model(db.Model):
    __abstract__ = True

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except (IntegrityError, OperationalError) as error:
            db.session.rollback()
            raise error

    @classmethod
    def by_username(cls, username: str):
        return cls.query.filter_by(username=username).first()


class Schema(BaseSchema):
    class Meta:
        unknown = EXCLUDE


class SQLAlchemySchema(Schema, ma.SQLAlchemySchema):
    class Meta(Schema.Meta):
        model = None
        sqla_session = db.session
        load_instance = True
        fields = ('id', 'created_at', 'updated_at')
        dump_only = ('id', 'created_at', 'updated_at')
