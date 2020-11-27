from os import getenv


class Config:
    SECRET_KEY = b'\x80\xf2/\xc7\xfb\xf2\xa3E\xb34OCI\xd9~.'

    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = b'\xb5.\x17W\x103^=\x9d_\t\x9d\x93\xc0\x82\xda'

    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'charset': 'utf8mb4'
        }
    }


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
    STATIC_URL = 'http://127.0.0.1:7070/'


class ProductionConfig(Config):
    STATIC_URL = 'https://guros.cnd.mx/'


class TestingConfig(Config):
    TESTING = True


app_config = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    testing=TestingConfig
)
