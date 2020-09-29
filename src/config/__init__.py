from os import getenv
from dotenv.main import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = b'\x80\xf2/\xc7\xfb\xf2\xa3E\xb34OCI\xd9~.'
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


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True


app_config = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    testing=TestingConfig
)
