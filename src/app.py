from os import environ
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from urllib.parse import urljoin, urlparse

from config import app_config

db = SQLAlchemy()
csrf = CSRFProtect()
migrate = Migrate()


def create_app() -> Flask:
    env = environ['FLASK_ENV']

    app = Flask(__name__)
    app.config.from_object(app_config[env])

    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    @app.template_global()
    def static_url(prefix, filename) -> str:
        return urljoin(app.config['STATIC_URL'], f'/{prefix}/{filename}')

    return app
