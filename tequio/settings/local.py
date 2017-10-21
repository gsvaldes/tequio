from .base import *  # noqa

DEBUG = True

# Note: This key only used for development and testing.
SECRET_KEY = get_env_variable('TEQUIO_SECRET_KEY')
