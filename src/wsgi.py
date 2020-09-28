from os import getenv

workers = 1
bind = '0.0.0.0:5000'
reload = getenv('FLASK_ENV') == 'development'
