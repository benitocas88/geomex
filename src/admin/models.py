from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow.schema import Schema as BaseSchema
from marshmallow.utils import EXCLUDE
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.ext.declarative import declared_attr

db = SQLAlchemy()
ma = Marshmallow()


# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html?highlight=tablename#mixin-and-custom-base-classes
# noinspection PyUnresolvedReferences
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
    # https://marshmallow.readthedocs.io/en/stable/examples.html#inflection-camel-casing-keys
    @staticmethod
    def __camelcase(s):
        parts = iter(s.split("_"))
        return next(parts) + "".join(i.title() for i in parts)

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = self.__camelcase(field_obj.data_key or field_name)

    class Meta:
        unknown = EXCLUDE

class SQLAlchemySchema(Schema, ma.SQLAlchemySchema):
    class Meta(Schema.Meta):
        model = None
        sqla_session = db.Session
        load_instance = True
        fields = ('id', 'created_at', 'updated_at')
        dump_only = ('id', 'created_at', 'updated_at')
