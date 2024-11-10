from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME_DEV", default="apapesc_db_desenvolvimento"),
        'USER': env("DB_USER_DEV", default="postgres"),
        'PASSWORD': env("DB_PASSWORD_DEV", default="mr1703"),
        'HOST': env("DB_HOST_DEV", default="localhost"),
        'PORT': '5432',
    }
}
