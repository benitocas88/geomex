from flask_wtf.form import FlaskForm
from wtforms import fields


class ZipcodeForm(FlaskForm):
    zipcode = fields.StringField()
    neighborhoods = fields.SelectField()
