from os import environ

SECRET_KEY = b'\x80\xf2/\xc7\xfb\xf2\xa3E\xb34OCI\xd9~.'

PROPAGATE_EXCEPTIONS = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = environ['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_ENGINE_OPTIONS = {
    'connect_args': {
        'charset': 'utf8mb4'
    }
}

DEBUG = True
TEMPLATES_AUTO_RELOAD = True
SEND_FILE_MAX_AGE_DEFAULT = 0
STATIC_URL = 'http://127.0.0.1:7070/'

JWT_SECRET_KEY = b'%\xc3o\xec\\\xcc\x80\xcd\xcd\x96\xfc\x8d\nS\xd11'
