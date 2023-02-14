from environs import Env

env = Env()

SECRET_KEY = env.str("SECRET_KEY", default="ytW6KzluuzsUtuP3WcbAhSZbfVUeibi0L2E5HtvB7MY")

PROPAGATE_EXCEPTIONS = True
# SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = env.str(
    "SQLALCHEMY_DATABASE_URI",
    default="mariadb+mariadbconnector://root:secret@mariadb:3306/geomex"
)
# SQLALCHEMY_ENGINE_OPTIONS = {"connect_args": {"charset": "utf8mb4"}}

DEBUG = True
TEMPLATES_AUTO_RELOAD = True
SEND_FILE_MAX_AGE_DEFAULT = 0
STATIC_URL = env.str("STATIC_URL", default="http://127.0.0.1:7070/")

JWT_SECRET_KEY = env.str("JWT_SECRET_KEY", default="4Qcf4zDsjk4yHHSziqiVXf0o1HD3Lgk2UG1piLYi0co")
