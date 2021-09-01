from sqlalchemy_utils.types.password import PasswordType
from sqlalchemy_utils.types.email import EmailType
from commons.models import Model, db


class User(Model):
    __tablename__ = 'user'

    email = db.Column(EmailType(length=30), nullable=False, unique=True)
    username = db.Column(db.String(length=16), unique=True, nullable=False)
    password = db.Column(PasswordType(max_length=90, schemes=['bcrypt']), nullable=False)
    # addresses = db.Column('Address', uselist=True, lazy=True)

"""
class Address(db.Model):
    __tablename__ = 'address'

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', name='fk_address__user'),
        nullable=False
    )
    neighborhood_id = db.Column(
        db.Integer,
        db.ForeignKey('neighborhood.id', name='fk_address__neighborhood'),
        nullable=False
    )
    street_name = db.Column(db.String(length=90))
    street_number = db.Column(db.String(length=20))
    floor = db.Column(db.String(length=20))
    is_primary = db.Column(db.Boolean, nullable=False)
"""
