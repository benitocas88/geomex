from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import app_config

db = SQLAlchemy()
migrate = Migrate()


def create_app(env: str = "development"):
    app = Flask(__name__)
    app.config.from_object(app_config[env])

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    return app
