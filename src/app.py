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

    from urls import admin, api

    api.make_api(app)
    admin.make_admin(app)

    @app.template_global()
    def static_url(prefix, filename) -> str:
        return urljoin(app.config["STATIC_URL"], f"/{prefix}/{filename}")

    @app.cli.command("test")
    def test():
        from geomex.commands.geomap import Sepomex
        sepomex = Sepomex()
        sepomex.geo()

    return app
