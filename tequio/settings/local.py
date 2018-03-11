"""
settings used for local development
"""
from .base import *  # noqa

DEBUG = True

# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='CHANGEME!!!')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = env('MAILGUN_USERNAME')
EMAIL_HOST_PASSWORD = env('MAILGUN_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env('TEQUIO_DB_NAME'),
        'USER': env('TEQUIO_DB_USER'),
        'PASSWORD': env('TEQUIO_DB_PASSWORD'),
        # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'HOST': '',
        'PORT': '',  # Set to empty string for default.
    }
}

# Django-webpack
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',  # must end with slash
        'STATS_FILE': str(ROOT_DIR('webpack-stats.json')),
    }
}
