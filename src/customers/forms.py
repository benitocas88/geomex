from flask_wtf.form import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired, EqualTo

class SignForm(FlaskForm):
    email = fields.EmailField(
        validators=[DataRequired()],
        render_kw={
            "placeholder": "email@domain.com",
            "autocomplete": "off",
        }
    )
    password = fields.PasswordField(
        validators=[DataRequired()],
        render_kw={"placeholder": "password123"},
    )

class SignupForm(SignForm):
    confirmation = fields.PasswordField(render_kw={"placeholder": "password123"})
