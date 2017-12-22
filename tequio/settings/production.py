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

ADMINS = [('geoff', 'valdesgeoffrey@gmail.com')]
SERVER_EMAIL = env('MAILGUN_USERNAME')


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL')
    )
}

ALLOWED_HOSTS = ['demo-tequio.herokuapp.com']

INSTALLED_APPS += ['gunicorn', ]
