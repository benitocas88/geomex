from os.path import join
from flask.app import Flask
from flask_migrate import Migrate
from flask_seasurf import SeaSurf
from urllib.parse import urljoin
from admin.models import db, ma

sea = SeaSurf()
migrate = Migrate()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(join('admin', 'settings.py'))

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    sea.init_app(app)

    from admin.api import api_v1
    app.register_blueprint(api_v1)

    from admin.views import home
    from user.views import user

    app.register_blueprint(home)
    app.register_blueprint(user)

    @app.template_global()
    def static_url(prefix, filename) -> str:
        return urljoin(app.config['STATIC_URL'], f'/{prefix}/{filename}')

    return app
