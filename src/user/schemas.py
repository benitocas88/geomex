from marshmallow.fields import String, Email
from marshmallow.validate import Length
from admin.models import SQLAlchemySchema
from user.models import User

class UserSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = User
        fields = SQLAlchemySchema.Meta.fields + (
            User.email.key,
            User.password.key,
            User.username.key
        )

    email = Email(required=True)
    username = String(required=True, validate=[Length(min=1)])
    password = String(required=True, validate=[Length(min=6)])
