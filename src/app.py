from os.path import join

from flask.app import Flask
from flask_migrate import Migrate
from urllib.parse import urljoin
from commons.models import db, ma

migrate = Migrate()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(join('settings', 'base.py'))

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    from commons.api import api_v1
    app.register_blueprint(api_v1)

    from settings.views import home
    from user.views import user
    from geomex.views import geomex

    app.register_blueprint(home)
    app.register_blueprint(user)
    app.register_blueprint(geomex)

    @app.template_global()
    def static_url(prefix, filename) -> str:
        return urljoin(app.config["STATIC_URL"], f"/{prefix}/{filename}")

    return app
