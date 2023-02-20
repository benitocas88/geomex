from marshmallow.fields import String, Email
from marshmallow.validate import Length
from commons.models import SQLAlchemySchema
from customers.models import User


class UserSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = User
        fields = SQLAlchemySchema.Meta.fields + (
            User.email.key,
            User.password.key,
        )

    email = Email(required=True)
    password = String(required=True, validate=[Length(min=6)])
