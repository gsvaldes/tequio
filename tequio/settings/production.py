"""
settings used for deployed app
"""
from .base import *  # noqa

import logging

import dj_database_url

DEBUG = False

SECRET_KEY = env('DJANGO_SECRET_KEY')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = env('MAILGUN_USERNAME')
EMAIL_HOST_PASSWORD = env('MAILGUN_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

ADMINS = [('geoff', 'valdesgeoffrey@gmail.com')]  # TODO move to env variable
SERVER_EMAIL = env('MAILGUN_USERNAME')


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL')
    )
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

ALLOWED_HOSTS = ['demo-tequio.herokuapp.com']  # TODO move to env variable

INSTALLED_APPS += ['gunicorn', ]

# see https://devcenter.heroku.com/articles/postgis#geodjango-setup
GDAL_LIBRARY_PATH = "/app/.heroku/vendor/lib/libgdal.so"
GEOS_LIBRARY_PATH = "/app/.heroku/vendor/lib/libgeos_c.so"

# Django-webpack
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',  # must end with slash
        'STATS_FILE': str(ROOT_DIR('webpack-stats-prod.json')),
    }
}
