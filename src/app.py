from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from config import app_config

db = SQLAlchemy()
csrf = CSRFProtect()
migrate = Migrate()


def create_app(env: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(app_config[env])

    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    return app
