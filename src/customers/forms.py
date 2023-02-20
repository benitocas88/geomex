from flask_wtf.form import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired, EqualTo


class SignupForm(FlaskForm):
    email = fields.EmailField(
        validators=[
            DataRequired(),
            EqualTo("confirmation")
        ]
    )
    password = fields.PasswordField(
        validators=[DataRequired()]
    )
    confirmation = fields.PasswordField()
