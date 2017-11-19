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
