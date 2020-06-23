from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config:
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args": {
            "charset": "utf8mb4"
        }
    }


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True


app_config = dict(
    development=DevelopmentConfig,
)
