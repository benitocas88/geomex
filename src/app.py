from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import app_config

db = SQLAlchemy()
mg = Migrate()


def create_app(env: str):
    app = Flask(__name__)
    app.config.from_object(app_config[env])

    db.init_app(app)
    mg.init_app(app, db, compare_type=True)

    return app
