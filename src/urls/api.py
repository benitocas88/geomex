from flask.app import Flask
from flask_wtf.csrf import CSRFProtect


def make_api(app: Flask, csrf: CSRFProtect):
    from commons.api import api_v1

    csrf.exempt(api_v1)
    app.register_blueprint(api_v1)
