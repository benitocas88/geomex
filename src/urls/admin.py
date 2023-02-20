from flask.app import Flask


def make_admin(app: Flask):
    from settings.views import home
    from customers.views import user
    from geomex.views import geomex

    app.register_blueprint(home)
    app.register_blueprint(user)
    app.register_blueprint(geomex)
