from os import environ
from flask.app import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from urllib.parse import urljoin

from admin.models import db, ma
from admin.settings import app_config

env = environ.get('FLASK_ENV', 'development')


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(app_config[env])

    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db, compare_type=True)
    CSRFProtect(app)

    from admin.urls import api_v1
    app.register_blueprint(api_v1)

    @app.template_global()
    def static_url(prefix, filename) -> str:
        return urljoin(app.config['STATIC_URL'], f'/{prefix}/{filename}')

    return app
