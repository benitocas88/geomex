from flask.app import Flask


def make_api(app: Flask):
    from commons.api import api_v1

    app.register_blueprint(api_v1)
