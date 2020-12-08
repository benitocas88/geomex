from os.path import join
from flask.app import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from urllib.parse import urljoin

from admin.models import db, ma


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(join('admin', 'settings.py'))

    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db, compare_type=True)
    CSRFProtect(app)

    from admin.api import api_v1
    app.register_blueprint(api_v1)

    from geomex.views import home
    app.register_blueprint(home)

    @app.template_global()
    def static_url(prefix, filename) -> str:
        return urljoin(app.config['STATIC_URL'], f'/{prefix}/{filename}')

    return app
