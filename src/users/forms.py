from flask_wtf.form import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()
