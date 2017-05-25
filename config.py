DB_CONFIG = {
    'DRIVER': 'postgresql',
    'USER': 'root',
    'PASSWORD': 'pass',
    'HOST': '127.0.0.1',
    'PORT': 5432,
    'NAME': 'user_db'
}

DEVELOPMENT = True

DEBUG = True

SECRET_KEY = '123456789'

SQLALCHEMY_TRACK_MODIFICATIONS = True

# Settings that shouldn't be overriden.
SQLALCHEMY_DATABASE_URI = '{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(**DB_CONFIG)