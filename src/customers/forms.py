from flask_wtf.form import FlaskForm
from wtforms import fields


class SignupForm(FlaskForm):
    email = fields.EmailField()
    password = fields.PasswordField()
    confirmation = fields.PasswordField()
